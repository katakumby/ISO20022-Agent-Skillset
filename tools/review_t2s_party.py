"""Persist the completed Party Reference Data visual review and focused source examples."""
import argparse, hashlib, json, re
from pathlib import Path
from lxml import etree
import kb

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main(root):
 sid='src-000368'; src=next(s for s in kb.sources(root) if s['source_id']==sid)
 base=root/src['set_path']; doc=base/'documents'/sid; assets=root/'domains/securities/assets'/sid
 manifest=json.loads((root/'work/t2s-party-diagrams.json').read_text(encoding='utf-8'))
 renders={r['diagram']:r for r in json.loads((root/'work/t2s-party-render.json').read_text(encoding='utf-8'))}
 invpath=root/'work/documents'/sid/'media-review-inventory.json'; inv=json.loads(invpath.read_text(encoding='utf-8'))
 report=root/'tracking/reviews/t2s-party-reference-data.json'; records=[]; indexrows=[]
 for item in manifest['outputs']:
  name=item['figure_id']; rr=renders[name]; p=root/item['path']; m,b=kb.metadata(p)
  assert rr['result']=='pass' and digest(p.with_suffix('.mmd'))==item['mermaid_sha256']
  assert digest(root/item['source_preview'])==item['source_preview_sha256']
  status='needs-review' if m.get('issue_ids') else 'reviewed'
  rec={**item,'date':'2026-11-09','render_result':'pass','renderer':rr['renderer'],'renderer_version':rr['version'],'rendered_png':rr['png'],'rendered_png_sha256':digest(root/rr['png']),'visual_review':'pass','review_status':status,'issue_ids':m.get('issue_ids',[]),'checks':['Final rendered reconstruction and source artwork directly compared for all labels, endpoints, directions, decisions, roles and solid/dashed line styles.','Complete Word page composition inspected, including all nine Word-object sequence diagrams and clipped EMF activity figures8/9.','Queuing and error alternatives remain conditional in the narrative rather than mandatory message steps.'],'limitations':['Mermaid changes layout, actor glyphs, arrowhead styling and final-node centre fill; explicit descriptions and complete source images retain these features.','Native hidden content remains separately scoped under issue-000028.']}; records.append(rec)
  m.update(review_status=status,render_status='pass',visual_review='pass',visual_review_date='2026-11-09',renderer='Mermaid '+rr['version'],rendered_svg=rr['svg'],rendered_png=rr['png'],complete_composite_review='pass')
  b=re.sub(r'## Rendering and visual review\n.*','## Rendering and visual review\n\nOn 2026-11-09 this reconstruction parsed and rendered with Mermaid '+rr['version']+' / '+rr['renderer']+'. The final rendering was directly compared with the complete source for labels, participants, connector endpoints/directions, decisions and line styles. All 47 Word pages were inspected for complete composition. **Visible-source fidelity: pass.** Source conflicts remain open where listed. Mermaid changes layout, actor glyphs, arrowhead styling and final-node centre fill; the original and textual relationship description preserve them.\n\n'+kb.link(p,root/rr['svg'],'Rendered SVG')+' · '+kb.link(p,root/rr['png'],'Rendered PNG')+' · '+kb.link(p,report,'Hash-bound review evidence')+'\n',b,flags=re.S)
  kb.put(p,kb.front(m)+b); indexrows.append([name,kb.link(base/'diagrams/party-reference-data/index.md',p,m['title']),status])
  for media in inv['media']:
   for occ in media['occurrences']:
    if occ['figure_id']!=name: continue
    occ.update(canonical_diagram=item['path'],complete_source_image=item['source_preview'],review_status=status)
    media.update(disposition='source-reconstruction',review_status=status,visual_review='pass',complete_composite_review='pass')
    ep=root/occ['evidence_page']; em,eb=kb.metadata(ep);em.update(disposition='source-reconstruction',canonical_diagram=item['path'],review_status=status,visual_review='pass',render_status='pass',complete_source_image=item['source_preview']);kb.put(ep,kb.front(em)+eb)
 legends=[]
 for media in inv['media']:
  for occ in media['occurrences']:
   num=int(occ['figure_id'][4:])
   if num not in [3,4,5,6]: continue
   label={3:'Start Point',4:'End Point',5:'Lozenge (or diamond)',6:'Bar'}[num];ep=root/occ['evidence_page'];em,eb=kb.metadata(ep)
   em.update(review_status='reviewed',disposition='retained-notation-legend',visual_review='pass',render_status='not-applicable',content_origin='source-notation-legend')
   eb=re.sub(r'## Interpretation and pending work\n.*','## Reviewed notation key\n\nThis is the '+label+' symbol in T13 on Word file page15, directly compared with its definition on 2026-11-09. It is retained as substantive notation context, not classified as decorative or as a standalone business flow.\n',eb,flags=re.S);kb.put(ep,kb.front(em)+eb)
   media.update(disposition='retained-notation-legend',review_status='reviewed',visual_review='pass',complete_composite_review='pass');legends.append({'figure_id':occ['figure_id'],'label':label,'original':media['original'],'original_sha256':media['original_sha256'],'source_locator':occ['source_locator'],'visual_review':'pass'})
 kb.dump(invpath,inv)
 raw=json.loads((root/'work/documents'/sid/'records.json').read_text(encoding='utf-8')); reconciliation=json.loads((root/'work/docx-render'/sid/'reconciliation.json').read_text(encoding='utf-8'))
 # Word's COM start range for T1 pointed to a preceding blank page. Correct it by visible page evidence.
 bounds={1:(5,5),2:(5,6),3:(6,6),4:(7,7),5:(10,10),6:(10,11),7:(11,11),8:(12,12),9:(12,13),10:(13,13),11:(13,13),12:(14,14),13:(15,15),14:(16,16),15:(17,18),16:(18,19),17:(20,20),18:(21,21),19:(47,47)}
 table_records=[]
 for table,wr in zip(raw['tables'],reconciliation['tables']):
  assert table['source_table_id']==wr['source_table_id'];num=int(table['source_table_id'][1:]);p=doc/'tables'/(table['table_id']+'.md');m,b=kb.metadata(p);status='needs-review' if num in [1,7,16] else 'reviewed';start,end=bounds[num]
  m.update(review_status=status,visual_review='pass',visual_review_date='2026-11-09',issue_ids=['issue-000046'] if status=='needs-review' else [],rendered_file_pages=list(range(start,end+1)))
  b=re.sub(r'\n<!-- PARTY-TABLE-REVIEW -->.*','',b,flags=re.S);b+='\n\n<!-- PARTY-TABLE-REVIEW -->\nAll physical rows, headers, blank cells, values and split continuations were reconciled with the original and Word file pages '+str(start)+'–'+str(end)+' on 2026-11-09. '+kb.link(p,report,'Review evidence')+'. Literal source contradictions remain open where listed.\n';kb.put(p,kb.front(m)+b)
  table_records.append({'table_id':table['table_id'],'source_table_id':table['source_table_id'],'path':p.relative_to(root).as_posix(),'physical_rows':len(table['rows']),'nonempty_cells':wr['nonempty_cells'],'automatic_matched_cells':wr['matched_nonempty_cells'],'word_file_pages':[start,end],'original_com_range':[wr['word_start_file_page'],wr['word_end_file_page']],'visually_resolved_cells':wr['unmatched_cells'],'transcription_review':'pass','review_status':status})
 contextpath=assets/'word-page-context/manifest.json';context=json.loads(contextpath.read_text(encoding='utf-8'));assert len(context['pages'])==47
 context.update(visual_review='pass',visual_review_date='2026-11-09',review_scope='All47 complete pages visually inventoried;19tables reconciled including17 unmatched text cells and four notation-symbol cells; all20figure occurrences accounted for.');kb.dump(contextpath,context)
 # A source-supported short label within this exact context, not an institution alias.
 p=root/'shared/reference/participants'/('participant-'+sid+'-executing-servicing-party.md');m,b=kb.metadata(p);m['aliases']=sorted(set(m.get('aliases',[])+['Executing Party']));b=re.sub(r'\n<!-- PARTY-EXECUTING-ALIAS -->.*','',b,flags=re.S);kb.put(p,kb.front(m)+b.strip()+'\n\n<!-- PARTY-EXECUTING-ALIAS -->\nFigures7–11 label the servicing lane Executing Party; corresponding T14–T18 activity descriptions explicitly call the same responsible lane Executing/Servicing Party. This is a source-supported local label, not an equivalence across other message sets.\n')
 # Preserve source examples as focused pages, including all literal XML blocks without adding namespaces.
 pars=raw['paragraphs'];starts=[301,356,396,422,511,539,586,660,688,733];word_ranges=[(32,33),(34,34),(35,35),(36,38),(39,39),(40,41),(42,43),(44,44),(45,46)];example_records=[]
 exact={x['message_id'][:8]:x['message_id'] for x in json.loads((root/'work/documents/src-000369/message-definitions.json').read_text(encoding='utf-8'))}
 for j,start in enumerate(starts[:-1]):
  subset=[x for x in pars if start<=int(x['paragraph_id'][1:])<starts[j+1]];title=subset[0]['text'];family=re.search(r'reda\.\d{3}',title).group();p=base/'examples'/('example-'+family+'.md');body='# '+title+'\n\n'+kb.source_link(root,p,src)+'; direct-body P'+str(start)+'–P'+str(starts[j+1]-1)+'; Word file pages '+str(word_ranges[j][0])+'–'+str(word_ranges[j][1])+'. These are source-authored examples. Headings omit the final definition version and XML omits a namespace; no exact-version schema-validity claim is made.\n\n';xml=[];blocks=[]
  for par in subset[1:]:
   txt=par['text'];isp=par.get('style')=='XML Code'
   if isp: xml.append((par['paragraph_id'],txt));continue
   if xml:
    text='\n'.join(x[1] for x in xml);body+='**'+xml[0][0]+'–'+xml[-1][0]+'**\n\n```xml\n'+text+'\n```\n\n';blocks.append((xml[0][0],xml[-1][0],text));xml=[]
   if txt.strip():body+='**'+par['paragraph_id']+'** '+kb.escape_table_markup(txt)+'\n\n'
  if xml:
   text='\n'.join(x[1] for x in xml);body+='**'+xml[0][0]+'–'+xml[-1][0]+'**\n\n```xml\n'+text+'\n```\n';blocks.append((xml[0][0],xml[-1][0],text))
  checks=[]
  for a,z,txt in blocks:
   try:etree.fromstring(txt.encode());result='well-formed'
   except etree.XMLSyntaxError as e:result=str(e).split('\n')[0]
   checks.append({'first_paragraph':a,'last_paragraph':z,'xml_well_formedness':result,'sha256':hashlib.sha256(txt.encode()).hexdigest()})
  issues=['issue-000046'] if family=='reda.041' else [];m={'template':False,'document_kind':'source-example','review_status':'needs-review','domain':'securities','source_ids':[sid],'source_editions':['March 2024'],'message_sets':['t2s-party-reference-data'],'message_families':[family],'related_message_ids':[exact[family]],'source_locations':[{'source_id':sid,'heading_path':subset[0]['heading_path'],'first_paragraph':'P'+str(start),'last_paragraph':'P'+str(starts[j+1]-1),'rendered_file_pages':list(range(word_ranges[j][0],word_ranges[j][1]+1))}],'issue_ids':issues,'limitations':['Examples omit target namespace and full definition version; no exact-schema-validity claim.']}
  if issues:body+='\n## Literal source inconsistency\n\nP588 and XML P616/P638 identify PAYBXXYYAAA, while P592/P599 list BANKXXYYAAA for the same activity-advice changes. Both values are preserved under issue-000046; no identity equivalence is inferred.\n'
  body+='\n## XML inspection\n\n'+kb.table(['Paragraphs','Well-formedness'],[[a['first_paragraph']+'–'+a['last_paragraph'],a['xml_well_formedness']] for a in checks])+'\n'+kb.link(p,root/'domains/securities/reference/messages'/exact[family]/'index.md','Related exact supplied definition '+exact[family])+'\n';kb.put(p,kb.front(m)+body);example_records.append({'path':p.relative_to(root).as_posix(),'family':family,'xml_blocks':checks})
 reportdata={'source_id':sid,'source_sha256':src['sha256'],'date':'2026-11-09','word_pages_inspected':47,'source_figure_occurrences':20,'substantive_figures':16,'render_pass':16,'visual_comparisons':16,'reviewed_figures':11,'needs_review_figures':5,'records':records,'legend_records':legends,'tables':table_records,'physical_rows':sum(x['physical_rows'] for x in table_records),'nonempty_cells':288,'automatic_matched_cells':271,'visually_resolved_cells':17,'page_context_manifest':contextpath.relative_to(root).as_posix(),'examples':example_records,'limitations':['Issue46 source contradictions remain open.','Issue28 native hidden content remains separately scoped.','Word-derived Heading1 errors are rendering field artifacts and not source narrative.']};kb.dump(report,reportdata)
 idx=base/'diagrams/party-reference-data/index.md';im,_=kb.metadata(idx);kb.put(idx,kb.front(im)+'# Party Reference Data source diagrams\n\nAll20 figure occurrences are accounted for:16 source reconstructions and four T13 notation symbols. All16 reconstructions parsed/rendered with Mermaid12.3.0 and were directly compared against complete source composition. Eleven figures are reviewed; five retain source-conflict issue46.\n\n'+kb.table(['Figure','Reference','Status'],indexrows)+'\n'+kb.link(idx,report,'Detailed hash-bound review evidence')+'\n')
 page=doc/'context-review.md';kb.put(page,kb.front({'template':False,'document_kind':'source-context-review','review_status':'needs-review','domain':'securities','source_ids':[sid],'source_editions':['March 2024'],'message_sets':['t2s-party-reference-data'],'issue_ids':['issue-000028','issue-000046']})+'# Party Reference Data source review\n\nAll47 Word-rendered pages were inspected. All19 source tables, '+str(reportdata['physical_rows'])+' physical rows,288 nonempty text cells and four notation-symbol cells were reconciled.271 cells matched rendered text automatically. The17 remaining cells were visually resolved:12 T1 cells are actually on page5 after a blank page4; T2 RTGS definition crosses pages5–6; T6 NCB label/definition crosses pages10–11; T9 definition crosses pages12–13; T15 validation crosses pages17–18. No lost cell text was established.\n\n'+kb.link(page,idx,'All16 substantive diagrams and their review status')+' · '+kb.link(page,report,'Detailed review evidence')+'\n\n## Focused source examples\n\n'+'\n'.join('- '+kb.link(page,root/x['path'],x['family']) for x in example_records)+'\n\nThe examples retain source XML without adding namespaces. Source role, copied-label, audit-response and activity-advice identifier conflicts remain open under issue46. Hidden native content remains separately scoped; this is not approval of the entire collection.\n')
 for nav in [doc/'index.md',base/'index.md']:
  m,b=kb.metadata(nav);b=re.sub(r'\n<!-- PARTY-CONTEXT -->.*','',b,flags=re.S);kb.put(nav,kb.front(m)+b.strip()+'\n\n<!-- PARTY-CONTEXT -->\n'+kb.link(nav,page,'Complete page/table/figure review and source examples')+'\n')
 print(json.dumps({'figures':16,'legends':len(legends),'tables':len(table_records),'pages':47,'examples':len(example_records),'xml_blocks':sum(len(x['xml_blocks']) for x in example_records)}))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();main(a.root.resolve())
