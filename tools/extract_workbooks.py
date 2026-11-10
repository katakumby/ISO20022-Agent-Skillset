#!/usr/bin/env python3
"""Extract supplied XLSX cells/drawings and external-code JSON into focused references.

Reads catalog/sources.json. Never modifies raw inputs. Byte identities are checked before
reading. XML formulas and cached values remain distinct; no recalculation is performed.
Use --root PATH --source src-NNNNN to resume a bounded source, or omit --source for all.
Outputs extraction evidence to work/workbooks and a result manifest for catalog rebuilding.
"""
from __future__ import annotations
import argparse, collections, datetime, hashlib, io, json, os, posixpath, re, zipfile
from pathlib import Path
import xml.etree.ElementTree as ET
from openpyxl.styles.numbers import BUILTIN_FORMATS, is_date_format
from openpyxl.utils.datetime import from_excel, CALENDAR_MAC_1904, CALENDAR_WINDOWS_1900
from openpyxl.utils.cell import get_column_letter, coordinate_to_tuple
NS = {'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main',
      'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
      'p':'http://schemas.openxmlformats.org/package/2006/relationships',
      'd':'http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing',
      'a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
import kb, refresh
DATE = kb.DATE
PRESERVE_EXISTING=False
TICK=chr(96)

def slug(v):
    return re.sub(r'[^a-z0-9]+','-',v.lower()).strip('-') or 'unnamed'

def dump(v): return json.dumps(v,ensure_ascii=False,indent=2)
def esc(v):
    if v is None: return '∅'
    return str(v).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('|','\\|').replace('\r\n','\n').replace('\r','\n').replace('\n','<br>')

def fm(**kw):
    return '---\n'+'\n'.join(k+': '+json.dumps(v,ensure_ascii=False) for k,v in {'template':False,'review_status':'needs-review',**kw}.items())+'\n---\n\n'

def relative(start, target):
    return os.path.relpath(target,Path(start).parent).replace('\\','/').replace(' ','%20')

def write(root,path,data,job):
    path=Path(path)
    if not path.is_absolute(): path=root/path
    path=path.resolve()
    if not path.is_relative_to(root.resolve()) or path.is_relative_to((root/'raw-input').resolve()):
        raise ValueError('Refusing output outside repository output area: '+str(path))
    if path.exists() and path.suffix.lower()=='.md':
        current,_=kb.metadata(path)
        if PRESERVE_EXISTING or current.get('manual_curated') or current.get('review_status')=='reviewed':return
    data=data.encode('utf-8') if isinstance(data,str) else data
    kb.write_bytes(path,data)


def source_id(s): return s.get('source_id',s.get('id'))
def occurrences(s):
    oo=s.get('occurrences') or [s]
    return [o if isinstance(o,dict) else {'path':o} for o in oo]
def source_bytes(root,s):
    return kb.read_source(root,s)


def original_links(root,s,page):
    lines=[]
    for o in occurrences(s):
        path=o.get('archive_path') or o.get('path') or o.get('raw_path') or o.get('source_path')
        member=o.get('member_path',o.get('archive_member'))
        if path:
            lines.append('['+Path(path).name+']('+relative(page,root/path)+')'+(' → archive member '+TICK+member+TICK if member else ''))
    return '; '.join(lines)

def names(s):
    return ' '.join(str(o.get('member_path') or o.get('archive_member') or o.get('path') or o.get('raw_path') or '') for o in occurrences(s))

def area(s):
    d=s.get('domain') or s.get('output_area')
    if d in ['shared','payments','securities','cards','fx','trade-finance']:return d
    n=names(s).lower()
    return 'shared' if 'externalcodesets' in n or 'business_application_header' in n else 'payments' if any(x in n for x in ['payments_','cash_management']) else 'securities'

def outbase(root,s):
    if s.get('workbook_output'):return root/s['workbook_output']
    if s.get('set_path') and '/code-sets/' in s['set_path']:return root/s['set_path']
    domain=area(s); prefix=Path('shared') if domain=='shared' else Path('domains')/domain
    sid=source_id(s)
    if 'BTC_Codification' in names(s):return root/'shared/reference/code-sets/bank-transaction-code-combinations'/('edition-unknown-'+sid)
    if 'externalcodesets' in names(s).lower() and (s.get('format','').lower().lstrip('.')=='json' or names(s).lower().endswith('.json')):
        return root/'shared/reference/code-sets/external-code-sets'/('edition-unknown-'+sid)
    if s.get('set_path'): return root/s['set_path']/'workbooks'/sid
    if s.get('output_base'): return root/s['output_base']/('workbook-'+sid)
    collection=s.get('collection') or s.get('message_set') or occurrences(s)[0].get('collection')
    if not collection:
        p=occurrences(s)[0].get('path') or ''
        collection=Path(p).parts[1] if len(Path(p).parts)>1 else 'supplied-workbooks'
    return root/prefix/'reference/message-sets'/slug(str(collection))/('edition-unknown-'+sid)/('workbook-'+sid)

def rels(z,base):
    rp=posixpath.join(posixpath.dirname(base),'_rels',posixpath.basename(base)+'.rels')
    if rp not in z.namelist(): return {}
    return {e.get('Id'):{**e.attrib,'resolved':posixpath.normpath(posixpath.join(posixpath.dirname(base),e.get('Target',''))).lstrip('/')} for e in ET.fromstring(z.read(rp))}

def cell_text(c,strings):
    typ=c.get('t');v=c.find('m:v',NS);raw=None if v is None else v.text
    if typ=='s':return strings[int(raw)] if raw is not None else None
    if typ=='inlineStr':return ''.join(c.itertext()) if c.find('m:is',NS) is not None else None
    if typ=='b':return None if raw is None else raw=='1'
    return raw

def display(value,typ,fmt,date1904):
    if value is None:return None
    if isinstance(value,bool):return 'TRUE' if value else 'FALSE'
    if typ not in ['s','inlineStr','str','e'] and is_date_format(fmt):
        try:
            dt=from_excel(float(value),CALENDAR_MAC_1904 if date1904 else CALENDAR_WINDOWS_1900)
            if fmt=='mm-dd-yy':return dt.strftime('%m-%d-%y')
            if fmt=='d-mmm-yy':return str(dt.day)+'-'+dt.strftime('%b-%y')
            if fmt=='d-mmm':return str(dt.day)+'-'+dt.strftime('%b')
            if fmt=='mmm-yy':return dt.strftime('%b-%y')
            if fmt in ['h:mm','h:mm:ss','mm:ss']:return dt.strftime({'h:mm':'%H:%M','h:mm:ss':'%H:%M:%S','mm:ss':'%M:%S'}[fmt])
            return dt.isoformat()
        except (ValueError,TypeError):pass
    return value

def extract_xlsx(root,s,args):
    sid=source_id(s); data=source_bytes(root,s);base=outbase(root,s); domain=area(s)
    asset=root/('shared' if domain=='shared' else 'domains/'+domain)/'assets'/sid
    prior_result_path=root/'work/workbook-results.json'
    prior_results=json.loads(prior_result_path.read_text('utf-8')) if prior_result_path.exists() else []
    prior_diagrams={d['page']:d for r in prior_results if r.get('source_id')==sid for d in r.get('diagrams',[])}
    z=zipfile.ZipFile(io.BytesIO(data))
    wb=ET.fromstring(z.read('xl/workbook.xml'));wbrel=rels(z,'xl/workbook.xml')
    ss=ET.fromstring(z.read('xl/sharedStrings.xml')) if 'xl/sharedStrings.xml' in z.namelist() else []
    strings=[''.join(e.itertext()) for e in ss]
    styles=ET.fromstring(z.read('xl/styles.xml'))
    formats=dict(BUILTIN_FORMATS);formats.update({int(e.get('numFmtId')):e.get('formatCode') for e in styles.findall('m:numFmts/m:numFmt',NS)})
    xfs=[dict(e.attrib) for e in styles.findall('m:cellXfs/m:xf',NS)]
    wbp=wb.find('m:workbookPr',NS);date1904=wbp is not None and wbp.get('date1904') in ['true','1']
    metadata={'source_id':sid,'sha256':s['sha256'],'occurrences':occurrences(s),'sheets':[],'styles_xml':ET.tostring(styles,encoding='unicode'),'workbook_xml':ET.tostring(wb,encoding='unicode'),'review_status':'needs-review','limitations':['Visual workbook review remains pending.','Native workbook recalculation was intentionally not performed; cached formula results are source evidence.']}
    allpages=[];diagrams=[];table_count=0;formula_count=0;cache_missing=0;total_rows=0;fig_count=0
    for sheet_i,se in enumerate(wb.findall('m:sheets/m:sheet',NS),1):
        shname=se.get('name');shpath=wbrel[se.get('{'+NS['r']+'}id')]['resolved']
        if shpath.startswith('xl/xl/'):shpath=shpath[3:]
        xml=ET.fromstring(z.read(shpath));shrels=rels(z,shpath)
        sm={'name':shname,'state':se.get('state','visible'),'path':shpath,'dimension':xml.find('m:dimension',NS).get('ref') if xml.find('m:dimension',NS) is not None else None,'merged_ranges':[m.get('ref') for m in xml.findall('m:mergeCells/m:mergeCell',NS)],'cells':[],'row_attributes':[],'column_attributes':[e.attrib for e in xml.findall('m:cols/m:col',NS)],'drawings':[],'comments':[],'hyperlinks':[e.attrib for e in xml.findall('m:hyperlinks/m:hyperlink',NS)],'conditional_formatting':[ET.tostring(e,encoding='unicode') for e in xml.findall('m:conditionalFormatting',NS)]}
        rows={};maxcol=0;maxrow=0; styleused=collections.Counter()
        for relem in xml.findall('m:sheetData/m:row',NS):
            rn=int(relem.get('r'));sm['row_attributes'].append(dict(relem.attrib));rv={}
            for c in relem.findall('m:c',NS):
                coord=c.get('r');ri,ci=coordinate_to_tuple(coord);val=cell_text(c,strings);style=int(c.get('s','0'));fmt=formats.get(int(xfs[style].get('numFmtId','0')),'General');f=c.find('m:f',NS)
                rec={'cell':coord,'value':val,'storage_type':c.get('t','n'),'style_id':style,'number_format':fmt}
                if f is not None:
                    rec.update(formula=f.text or '',formula_attributes=dict(f.attrib),cached_value=val);formula_count+=1
                    if val is None:cache_missing+=1
                shown=display(val,c.get('t','n'),fmt,date1904);rec['displayed_or_typed_value']=shown
                sm['cells'].append(rec);styleused[str(style)]+=1
                if val is not None or f is not None:
                    rv[ci]=('Formula: '+(f.text or '(shared formula)')+'; cached: '+('MISSING' if shown is None else str(shown))) if f is not None else shown
                    maxcol=max(maxcol,ci);maxrow=max(maxrow,ri)
            rows[rn]=rv
        sm['styles_used']=dict(styleused)
        for rr in shrels.values():
            if rr.get('Type','').endswith('/comments') and rr['resolved'] in z.namelist():
                cm=ET.fromstring(z.read(rr['resolved']));authors=[e.text for e in cm.findall('m:authors/m:author',NS)]
                sm['comments']=[{'cell':e.get('ref'),'author':authors[int(e.get('authorId'))],'text':''.join(e.find('m:text',NS).itertext())} for e in cm.findall('m:commentList/m:comment',NS)]
        sheetdir=base/'sheets'/('%02d-'%sheet_i+slug(shname));sheetindex=sheetdir/'index.md'
        headerrow=3 if shname=='BTC_Codification' else 1 if shname in ['FullBusinessModel','Traces','History Log'] else 0
        cols=list(range(1,maxcol+1));headers=[rows.get(headerrow,{}).get(ci) or get_column_letter(ci) for ci in cols] if headerrow else [get_column_letter(ci) for ci in cols]
        chunks=list(range(headerrow+1,maxrow+1,args.rows_per_part)) if maxrow else []
        sheetpages=[]
        for part,start in enumerate(chunks,1):
            end=min(start+args.rows_per_part-1,maxrow);table_count+=1;tid='tbl-%04d'%table_count
            page=sheetdir/(tid+'.md');loc=shname+'!A'+str(start)+':'+get_column_letter(maxcol)+str(end)
            title=shname+' — rows '+str(start)+'–'+str(end)
            content=fm(document_kind='extracted-table',domain=domain,table_id=tid,source_ids=[sid],source_locations=[loc],source_editions=[s.get('source_edition')],message_ids=[])
            content+='# '+title+'\n\nSource: '+sid+', '+TICK+loc+TICK+'. '+original_links(root,s,page)+'.\n\n'
            content+='This is part '+str(part)+' of '+str(len(chunks))+'. Column headings repeat source row '+str(headerrow)+'.\n\n' if headerrow else 'Source column letters identify cells; each original row is retained.\n\n'
            content+='Blank source values are shown as ∅; zero and FALSE retain their distinct values. Line breaks are preserved. Merged cells are not silently filled down; merged ranges and style evidence are on the worksheet index. Dates use the recorded cell number format when supported; other numeric values retain source storage. Formula text and source caches are labelled separately.\n\n'
            content+='| Source row | '+' | '.join(esc(v) for v in headers)+' |\n| --- | '+' | '.join('---' for _ in cols)+' |\n'
            for rn in range(start,end+1):content+='| '+str(rn)+' | '+' | '.join(esc(rows.get(rn,{}).get(ci)) for ci in cols)+' |\n'
            content+='\n[Worksheet context and complete parts](index.md).\n\n## Review evidence\n\nSource XML row coverage and split continuity reconciled by extraction helper on '+DATE+'. Visual comparison, formatting semantics, and substantive diagram review remain pending. This page is not reviewed.\n'
            write(root,page,content,args.job);sheetpages.append({'path':page.relative_to(root).as_posix(),'range':loc,'row_start':start,'row_end':end,'table_id':tid});allpages.append(sheetpages[-1]);total_rows+=end-start+1
        for draw in xml.findall('m:drawing',NS):
            dp=shrels[draw.get('{'+NS['r']+'}id')]['resolved'];dr=ET.fromstring(z.read(dp));drrels=rels(z,dp)
            write(root,asset/'drawing-xml'/Path(dp).name,z.read(dp),args.job)
            for ai,an in enumerate(dr,1):
                anchor={'drawing_part':dp,'anchor_id':ai,'anchor_type':an.tag.split('}')[-1],'attributes':dict(an.attrib),'xml':ET.tostring(an,encoding='unicode')}
                for tag in ['from','to']:
                    pos=an.find('d:'+tag,NS)
                    if pos is not None:
                        vals={e.tag.split('}')[-1]:int(e.text) for e in pos};anchor[tag]=vals;anchor[tag+'_cell']=get_column_letter(vals.get('col',0)+1)+str(vals.get('row',0)+1)
                for bl in an.findall('.//a:blip',NS):
                    rid=bl.get('{'+NS['r']+'}embed')
                    if rid not in drrels:continue
                    media=drrels[rid]['resolved'];raw=z.read(media);out=asset/'media'/Path(media).name;write(root,out,raw,args.job)
                    fig_count+=1;fid='fig-%04d'%fig_count;pg=base/'diagrams'/(fid+'.md')
                    entry={**anchor,'figure_id':fid,'sheet':shname,'media_part':media,'asset':out.relative_to(root).as_posix(),'sha256':hashlib.sha256(raw).hexdigest(),'page':pg.relative_to(root).as_posix(),'disposition':'unresolved','review_status':'needs-review'}
                    previous=prior_diagrams.get(entry['page'],{})
                    if previous.get('sha256')==entry['sha256']:
                        entry.update({k:previous[k] for k in ['disposition','review_status','canonical_output','render_evidence','visual_review'] if k in previous})
                    sm['drawings'].append(entry);diagrams.append(entry)
                    loc=shname+'; '+dp+' anchor '+str(ai)+'; '+anchor.get('from_cell','absolute')+':'+anchor.get('to_cell','extent')
                    content=fm(document_kind='diagram',domain=domain,diagram_id=fid,origin='source-reconstruction',diagram_kind='unclassified-source-drawing',source_ids=[sid],source_locations=[loc],original_image=entry['asset'],limitations=['Mermaid reconstruction and visual comparison are pending.'])
                    content+='# '+shname+' — '+fid+'\n\nSource: '+sid+', '+loc+'. '+original_links(root,s,pg)+'.\n\n![Original supplied drawing]('+relative(pg,out)+')\n\nThe supplied embedded image is retained byte-for-byte. Drawing anchors and offsets are preserved in the [worksheet metadata]('+relative(pg,root/'work/workbooks'/sid/'workbook.json')+'). This image has not yet been classified as substantive or decorative. No relationship, cardinality, or actor is inferred from its file name.\n\n## Reconstruction and review\n\nMermaid reconstruction, textual relationship transcription, flow/participant links, parsing, rendering, and source comparison remain pending. No visual review or render success is claimed.\n'
                    existing=pg.read_text('utf-8-sig') if pg.exists() else ''
                    if 'curated: true' not in existing and chr(96)*3+'mermaid' not in existing:
                        write(root,pg,content,args.job)
        sm['table_pages']=sheetpages;metadata['sheets'].append(sm)
        body=fm(document_kind='worksheet-index',domain=domain,source_ids=[sid],worksheet=shname,source_locations=[shname])
        body+='# '+shname+'\n\nSource: '+sid+'. '+original_links(root,s,sheetindex)+'.\n\n'
        body+='Sheet state: '+sm['state']+'. Source dimension: '+str(sm['dimension'])+'. Populated extent: '+('A1:'+get_column_letter(maxcol)+str(maxrow) if maxcol else 'no cell values')+'.\n\n'
        body+='Merged ranges: '+(', '.join(sm['merged_ranges']) or 'none recorded')+'. Only anchor cells contain stored values; blanks in merged areas are not zeros.\n\n'
        if headerrow>1:
            body+='## Title and context rows\n\n'
            for rn in range(1,headerrow):body+=str(rn)+'. '+ ' / '.join(str(v) for v in rows.get(rn,{}).values())+'\n\n'
        body+='## Complete table parts\n\n| Part | Source range |\n| --- | --- |\n'
        for p in sheetpages:body+='| ['+p['table_id']+']('+relative(sheetindex,root/p['path'])+') | '+esc(p['range'])+' |\n'
        body+='\n## Drawings\n\n'
        body+='\n'.join('- ['+v['figure_id']+']('+relative(sheetindex,root/v['page'])+'): '+v.get('from_cell','absolute')+':'+v.get('to_cell','extent')+'; reconstruction and visual review pending.' for v in sm['drawings']) or 'No picture anchors recorded.'
        body+='\n\n## Source formats and notes\n\n'
        body+='| Style ID | Cell count | Number format | Original style |\n| --- | --- | --- | --- |\n'
        for st,n in styleused.items():body+='| '+st+' | '+str(n)+' | '+esc(formats.get(int(xfs[int(st)].get('numFmtId','0')),'General'))+' | '+esc(json.dumps(xfs[int(st)]))+' |\n'
        for c in sm['comments']:body+='\n'+TICK+c['cell']+TICK+' note by '+c['author']+': '+c['text']+'\n'
        body+='\nExact cells, style definitions (including font and fill colors), merged ranges, hidden row/column state, hyperlinks, comments, formulas/caches, and drawing anchors are preserved in [extraction metadata]('+relative(sheetindex,root/'work/workbooks'/sid/'workbook.json')+'). Visual formatting semantics have not yet been verified.\n'
        write(root,sheetindex,body,args.job)
    metadata['counts']={'sheets':len(metadata['sheets']),'table_parts':table_count,'data_rows':total_rows,'picture_occurrences':fig_count,'formula_cells':formula_count,'missing_formula_caches':cache_missing}
    metadata['output']=base.relative_to(root).as_posix()
    write(root,root/'work/workbooks'/sid/'workbook.json',dump(metadata),args.job)
    index=base/'index.md';body=fm(document_kind='workbook-extraction',domain=domain,source_ids=[sid],source_edition=s.get('source_edition'),source_locations=[o.get('member_path') or o.get('path') for o in occurrences(s)],limitations=metadata['limitations'])
    body+='# Workbook reference — '+sid+'\n\n'+original_links(root,s,index)+'\n\nThis reference preserves supplied worksheets, including hidden-state metadata, cell values, formulas and caches, merged ranges, notes, and drawing anchors. '+str(table_count)+' table parts cover '+str(total_rows)+' source data rows. '+str(fig_count)+' embedded picture occurrences are retained. These extraction counts are not completed visual reviews.\n\n'
    body+='| Worksheet | State | Table parts | Drawings |\n| --- | --- | --- | --- |\n'
    for i,sh in enumerate(metadata['sheets'],1):body+='| ['+esc(sh['name'])+'](sheets/'+('%02d-'%i+slug(sh['name']))+'/index.md) | '+sh['state']+' | '+str(len(sh['table_pages']))+' | '+str(len(sh['drawings']))+' |\n'
    body+='\n## Known limitations\n\n'+'\n'.join('- '+v for v in metadata['limitations'])+'\n\n[Coverage](coverage.md).\n'
    write(root,index,body,args.job)
    coverage=fm(document_kind='extraction-coverage',domain=domain,source_ids=[sid])+'# Workbook coverage\n\n'+dump(metadata['counts'])+'\n\nEvery worksheet was inspected from its OOXML parts. All stored cells, source comments and drawing anchors were recorded. Table parts have continuous row ranges and repeated source headers. Blank margins recorded only by the worksheet dimension are retained in metadata, not fabricated as data rows.\n\nAll '+str(fig_count)+' picture occurrences have retained assets and dedicated pages. They remain unresolved pending substantive/decorative classification, full-figure completeness assessment, textual transcription, Mermaid reconstruction and visual review. No workbook or diagram is marked reviewed.\n\nNext action: visually inspect every drawing and worksheet presentation, reconstruct substantive diagrams, and check number-format and color semantics against the originals.\n\n[Index](index.md).\n'
    write(root,base/'coverage.md',coverage,args.job)
    return {'source_id':sid,'format':'xlsx','output':index.relative_to(root).as_posix(),'counts':metadata['counts'],'table_pages':allpages,'diagrams':diagrams,'status':'needs-review','limitations':metadata['limitations']}

def extract_codes(root,s,args):
    sid=source_id(s);data=json.loads(source_bytes(root,s).decode('utf-8-sig'));defs=data.get('definitions',{})
    base=outbase(root,s);index=base/'index.md';pages=[];nvalues=0;not_enumerated=[]
    for i,(name,d) in enumerate(defs.items(),1):
        pg=base/'code-sets'/(slug(name)+'.md');enum=d.get('enum');loc='#/definitions/'+name;constraints={k:v for k,v in d.items() if k not in ['enum','description']}
        body=fm(document_kind='external-code-set',domain='shared',source_ids=[sid],source_locations=[loc],code_set=name,source_edition=None,limitations=['Publication label is supplied by filename only.','Applicability to a specific message version is not established by a matching type name.'])
        body+='# '+name+'\n\nSource: '+sid+', JSON Pointer '+TICK+loc+TICK+'. '+original_links(root,s,pg)+'.\n\n## Definition and source notes\n\n'+d.get('description','No definition text is supplied.')+'\n\n## Source constraints\n\n'+TICK*3+'json\n'+dump(constraints)+'\n'+TICK*3+'\n\n'
        if enum is not None:
            body+='## Complete enumeration\n\n| Position | Exact code |\n| --- | --- |\n'
            for j,c in enumerate(enum,1):body+='| '+str(j)+' | '+esc(c)+' |\n'
            nvalues+=len(enum)
        else:
            not_enumerated.append(name);body+='## Enumeration availability\n\nThis definition supplies no enum property. This does not establish that the external code set is empty. No values have been invented.\n'
        body+='\nPublication identity and unenumerated values: [issue-000001]('+relative(pg,root/'tracking/issues.md')+'#issue-000001).\n'
        body+='\n## Review evidence\n\nJSON structure parsed and all declared values preserved on '+DATE+'. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.\n\n[Publication index](../index.md).\n'
        write(root,pg,body,args.job);pages.append({'name':name,'path':pg.relative_to(root).as_posix(),'locator':loc,'enum_values':len(enum) if enum is not None else None})
    body=fm(document_kind='code-set-publication',domain='shared',source_ids=[sid],source_edition=None,publication='ISO 20022 external code sets',publication_label=Path(occurrences(s)[0].get('path','')).name,limitations=['Publication date and edition are not declared inside the JSON; filename label is not promoted to confirmed metadata.','23 definitions lack an enum property; valid values for those sets remain unavailable in this file.'])
    body+='# ISO 20022 external code sets\n\nSource: '+sid+'. '+original_links(root,s,index)+'.\n\nThis supplied draft-04 JSON Schema contains '+str(len(defs))+' definitions and '+str(nvalues)+' enumeration values across '+str(len(defs)-len(not_enumerated))+' enumerated definitions. '+str(len(not_enumerated))+' definitions have no enum property. Each complete description, constraint and declared enum value is retained in the focused pages below. The filename contains a publication label; the JSON itself supplies no date or edition metadata.\n\nDo not assume that matching an External…Code type establishes that this publication edition applies to a particular message version. The Bank Transaction Code combinations workbook and description document retain separate source identities and edition evidence.\n\n| Code set | Declared enum values |\n| --- | --- |\n'
    for p in pages:body+='| ['+p['name']+']('+relative(index,root/p['path'])+') | '+str(p['enum_values'] if p['enum_values'] is not None else 'not supplied')+' |\n'
    body+='\n[Coverage](coverage.md).\n';write(root,index,body,args.job)
    write(root,base/'coverage.md',fm(document_kind='extraction-coverage',domain='shared',source_ids=[sid])+'# External code set coverage\n\nAll '+str(len(defs))+' definitions are represented by focused pages. All '+str(nvalues)+' enum array entries are retained in original order, including exact code spelling. Complete source descriptions preserve code meanings and notes. Root properties, references and additionalProperties are retained in the [source file]('+relative(base/'coverage.md',root/(occurrences(s)[0].get('path') or ''))+'). No image objects or tables outside these JSON definitions are claimed.\n\n'+str(len(not_enumerated))+' definitions lack enum arrays. Publication date and edition are not declared in source content. Those are known evidence gaps, not failed extraction or confirmed empty lists.\n\n[Index](index.md).\n',args.job)
    return {'source_id':sid,'format':'json','output':index.relative_to(root).as_posix(),'counts':{'definitions':len(defs),'enum_values':nvalues,'non_enumerated_definitions':len(not_enumerated)},'code_sets':pages,'status':'needs-review','limitations':['Edition date not declared in JSON.','Non-enumerated external code sets have unavailable values.']}

def main():
    global PRESERVE_EXISTING
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--manifest',default='catalog/sources.json');p.add_argument('--source',action='append');p.add_argument('--rows-per-part',type=int,default=200);p.add_argument('--job');p.add_argument('--resume',action='store_true',help='Skip source IDs already present in the extraction results and with existing output; still verify source fingerprint.');a=p.parse_args();root=a.root.resolve()
    if a.job:kb.set_write_context(root,a.job)
    a.source=refresh.job_sources(root,a.job,a.source)
    manifest=json.loads((root/a.manifest).read_text('utf-8-sig'));sources=manifest.get('sources',[]) if isinstance(manifest,dict) else manifest
    resultpath=root/'work/workbook-results.json';old=json.loads(resultpath.read_text('utf-8')) if resultpath.exists() else [];results={r['source_id']:r for r in old}
    priority=['external-code-sets','settlement-and-reconciliation','t2s-administration','corporate-actions','meetings','collateral-management','ccp-clearing','post-trade-matching','investment-funds','fitrr']
    def source_order(s):
        tag=s.get('set_slug','')
        if tag in priority:return priority.index(tag)
        if tag.startswith('t2s'):return 20
        return 30+(['payments-initiation','payments-clearing-and-settlement','cash-management','bank-to-customer-cash-management'].index(tag) if tag in ['payments-initiation','payments-clearing-and-settlement','cash-management','bank-to-customer-cash-management'] else 10)
    for s in sorted(sources,key=source_order):
        sid=source_id(s)
        if a.source and sid not in a.source:continue
        fmt=str(s.get('format','')).lower().lstrip('.')
        if fmt not in ['xlsx','json']:continue
        if fmt=='json' and 'externalcode' not in names(s).lower() and s.get('set_slug')!='external-code-sets':
            print(json.dumps({'source_id':sid,'status':'blocked','error':'JSON format needs source-specific inspection; no automatic converter selected.'}),flush=True);continue
        try:
            PRESERVE_EXISTING=bool(a.resume and sid in results and results[sid].get('source_sha256')==s['sha256'])
            if a.resume and sid in results and refresh.extraction_outputs_valid(root,s,results[sid]):
                source_bytes(root,s)
                print('Unchanged completed extraction: '+sid,flush=True);continue
            result=extract_xlsx(root,s,a) if fmt=='xlsx' else extract_codes(root,s,a)
            result['source_sha256']=s['sha256'];result['output_fingerprints']=refresh.output_fingerprints(root,s,result);results[sid]=result
            write(root,resultpath,dump(list(results.values())),a.job);print(json.dumps({'source_id':sid,'output':result['output'],'counts':result['counts']},ensure_ascii=False),flush=True)
        except Exception as exc:
            problem={'source_id':sid,'status':'blocked','error':str(exc)}
            if a.job:kb.dump(root/'tracking/refresh'/a.job/(sid+'-extraction-error.json'),problem)
            print(json.dumps(problem),flush=True)
    print('Processed '+str(len(results))+' workbook/code sources.',flush=True)
if __name__=='__main__':main()
