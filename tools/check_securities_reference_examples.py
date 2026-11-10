"""Check literal source377 Document excerpts without repairing supplied content."""
import argparse,hashlib,json,re
from pathlib import Path
from lxml import etree as E
import kb
from curate_intrabalance import block
def main(root):
 sid='src-000377';source=next(s for s in kb.sources(root) if s['source_id']==sid);base=root/source['set_path'];records=json.loads((root/'work/documents'/sid/'records.json').read_text(encoding='utf-8'));rows=[];active=[]
 for p in records['paragraphs']:
  if '<Document' in p['text'] and not active:active=[p]
  elif active:active.append(p)
  if active and '</Document>' in p['text']:
   value='\n'.join(x['text'] for x in active);error=None;root_tag=None
   try:node=E.fromstring(value.encode('utf-8'));root_tag=node.tag
   except E.XMLSyntaxError as e:error=str(e)
   mid=next((m.group() for h in active[0]['heading_path'] if (m:=re.search(r'reda\.\d{3}\.\d{3}\.\d{2}',h))),None)
   rows.append({'message_id':mid,'start_paragraph':active[0]['paragraph_id'],'end_paragraph':active[-1]['paragraph_id'],'heading_path':active[0]['heading_path'],'source_text_sha256':hashlib.sha256(value.encode()).hexdigest(),'well_formed':'fail' if error else 'pass','error':error,'root_qname':root_tag,'namespace_declaration_present':bool(re.search(r'\bxmlns(?:\s|:|=)',value)),'schema_validation':'not-run-source-excerpt-has-no-namespace'});active=[]
 if active:raise ValueError('Unclosed document excerpt')
 report={'source_id':sid,'source_sha256':source['sha256'],'date':'2026-11-09','scope':'All17 literal Document excerpts in source business examples; no repair or namespace insertion','excerpts':len(rows),'well_formed_pass':sum(r['well_formed']=='pass' for r in rows),'well_formed_fail':sum(r['well_formed']=='fail' for r in rows),'namespace_declarations':sum(r['namespace_declaration_present'] for r in rows),'records':rows};kb.dump(root/'tracking/reviews/securities-reference-examples.json',report)
 page=base/'business-examples.md';m,b=kb.metadata(page);m['limitations'].append('Completed Security Creation Status Advice example P398–P418 is not well-formed: opening SctyCreStsAdvc is absent while its closing tag appears at P417; directly confirmed on Word page32. Source remains unchanged (issue-000051).') if not any('P398' in x for x in m['limitations']) else None
 text='## Literal example checks\n\nAll17 source Document excerpts were parsed without repair. Sixteen are well-formed XML fragments, one is not; none declares a namespace, so no complete XSD-validation pass is claimed. The completed Security Creation Status Advice at P398–P418 omits the opening SctyCreStsAdvc tag but closes it at P417. This is present in original OOXML and was directly confirmed in '+kb.link(page,root/'domains/securities/assets/src-000377/word-page-context/page-0032.png','Word page32')+'. Source contents are preserved.\n\n'+kb.table(['Exact message','Source paragraph range','XML well-formedness','Namespace'],[[r['message_id'],r['start_paragraph']+'–'+r['end_paragraph'],r['well_formed'],'not declared'] for r in rows])+'\n'+kb.link(page,root/'tracking/reviews/securities-reference-examples.json','Precise errors and excerpt hashes')+' · '+kb.link(page,root/'tracking/issues.md','issue-000051')+'.\n';kb.put(page,kb.front(m)+block(b,'SECREF-EXAMPLES-CHECK',text))
 for mid in sorted({r['message_id'] for r in rows if r['message_id']}):
  p=root/'domains/securities/reference/messages'/mid/'index.md';mm,bb=kb.metadata(p);kb.put(p,kb.front(mm)+block(bb,'SECREF-EXAMPLES',kb.link(p,page,'June2021 business examples: exact identifiers, source conditions and literal XML checks')))
 print(json.dumps({k:v for k,v in report.items() if k!='records'}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);main(p.parse_args().root.resolve())
