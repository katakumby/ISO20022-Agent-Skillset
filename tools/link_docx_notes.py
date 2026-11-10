"""Preserve DOCX footnote/endnote text and link every source reference to its cell or paragraph."""
import argparse,hashlib,io,json,re,zipfile
from pathlib import Path
from lxml import etree
import kb
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';NS={'w':W}

def main(root):
    results=[]
    for src in kb.sources(root):
        if src['format']!='docx':continue
        data=kb.read_source(root,src);assert hashlib.sha256(data).hexdigest()==src['sha256'];sid=src['source_id'];out=root/src['set_path']/'documents'/sid;report=json.loads((root/'work/documents'/sid/'records.json').read_text(encoding='utf-8'))
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            doc=etree.fromstring(z.read('word/document.xml'));tree=doc.getroottree();body=doc.find('w:body',NS);bodypars=[x for x in body if x.tag=='{'+W+'}p'];bodytables=[x for x in body if x.tag=='{'+W+'}tbl'];records=[]
            for kind,member in [('footnote','word/footnotes.xml'),('endnote','word/endnotes.xml')]:
                if member not in z.namelist():continue
                notes=etree.fromstring(z.read(member))
                for note in notes:
                    nid=note.get('{'+W+'}id');text='\n'.join(''.join(p.itertext()) for p in note.findall('w:p',NS));plain='\n'.join(''.join(p.xpath('.//w:t/text()',namespaces=NS)) for p in note.findall('w:p',NS))
                    if not plain.strip():continue
                    occurrences=[]
                    for ref in doc.xpath('.//w:'+kind+'Reference[@w:id="'+nid+'"]',namespaces=NS):
                        ancestors=list(ref.iterancestors());top=next((a for a in ancestors if a.getparent() is body),None);loc={'xml_path':tree.getpath(ref),'direct_body_paragraph':None,'table_id':None,'row':None,'column':None}
                        if top in bodypars:loc['direct_body_paragraph']='P'+str(bodypars.index(top)+1)
                        elif top in bodytables:
                            ti=bodytables.index(top)+1;loc['table_id']='T'+str(ti);cell=next((a for a in ancestors if a.tag=='{'+W+'}tc'),None);row=next((a for a in ancestors if a.tag=='{'+W+'}tr'),None)
                            if row is not None and cell is not None:loc['row']=sum(a.tag=='{'+W+'}tr' for a in row.itersiblings(preceding=True))+1;loc['column']=sum(a.tag=='{'+W+'}tc' for a in cell.itersiblings(preceding=True))+1
                        occurrences.append(loc)
                    records.append({'kind':kind,'id':nid,'source_member':member,'declaration_xml_path':'/w:'+kind+'s/w:'+kind+'[@w:id="'+nid+'"]','text':plain,'occurrences':occurrences,'disposition':'linked-to-source-occurrences' if occurrences else 'retained-with-no-document-reference-found'})
        if not records:results.append({'source_id':sid,'substantive_notes':0,'note_references':0});continue
        page=out/'linked-notes.md';meta={'template':False,'document_kind':'source-notes','review_status':'needs-review','source_ids':[sid],'source_editions':list({e for p in [out/'index.md'] if p.exists() for e in kb.metadata(p)[0].get('source_editions',[])}),'domain':src['domain'],'message_sets':[src['set_slug']],'limitations':['Note text and reference locations are preserved from OOXML. Rendered footnote numbering can differ from internal IDs.','A note not referenced in the document is retained explicitly; absence of a reference is not proof that it is decorative.']};bodytext='# Linked footnotes and endnotes\n\n'+kb.source_link(root,page,src)+'\n\n';table_links={}
        for r in records:
            anchor=r['kind']+'-'+r['id'];bodytext+='## '+anchor+'\n\n'+r['text']+'\n\nSource: `'+r['source_member']+'`, `'+r['declaration_xml_path']+'`.\n\n'
            for o in r['occurrences']:
                if o['table_id']:
                    tn=int(o['table_id'][1:]);tp=out/'tables'/f'tbl-{tn:04d}.md';bodytext+='- '+kb.link(page,tp,o['table_id'])+', physical row '+str(o['row'])+', physical cell '+str(o['column'])+'; `'+o['xml_path']+'`.\n';table_links.setdefault(tp,[]).append((anchor,o))
                else:bodytext+='- '+str(o['direct_body_paragraph'] or 'Other source object')+'; `'+o['xml_path']+'`.\n'
            if not r['occurrences']:bodytext+='No reference occurrence found in `word/document.xml`; the note is retained.\n'
            bodytext+='\n'
        kb.put(page,kb.front(meta)+bodytext)
        for tp,notes in table_links.items():
            m,b=kb.metadata(tp);b=re.sub(r'\n<!-- LINKED-DOCX-NOTES -->.*?<!-- /LINKED-DOCX-NOTES -->\n?','\n',b,flags=re.S);b+='\n<!-- LINKED-DOCX-NOTES -->\n## Source footnotes and endnotes\n\n'+'\n'.join('- Physical row '+str(o['row'])+', cell '+str(o['column'])+': '+kb.link(tp,Path(str(page)+'#'+a),a) for a,o in notes)+'\n<!-- /LINKED-DOCX-NOTES -->\n';m['linked_note_reference_count']=len(notes);kb.put(tp,kb.front(m)+b.strip()+'\n')
        nav=out/'index.md'
        if nav.exists():
            m,b=kb.metadata(nav);b=re.sub(r'\n<!-- LINKED-DOCX-NOTES -->.*?<!-- /LINKED-DOCX-NOTES -->\n?','\n',b,flags=re.S);kb.put(nav,kb.front(m)+b.strip()+'\n\n<!-- LINKED-DOCX-NOTES -->\n'+kb.link(nav,page,'Footnotes/endnotes with precise cell and paragraph associations')+'\n<!-- /LINKED-DOCX-NOTES -->\n')
        entry={'source_id':sid,'source_sha256':src['sha256'],'path':page.relative_to(root).as_posix(),'substantive_notes':len(records),'note_references':sum(len(r['occurrences']) for r in records),'records':records};results.append(entry)
    kb.dump(root/'catalog/docx-notes.json',{'updated':kb.DATE,'records':results});print(json.dumps({'sources':len(results),'notes':sum(x['substantive_notes'] for x in results),'references':sum(x['note_references'] for x in results)}))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();main(a.root.resolve())
