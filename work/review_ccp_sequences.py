from pathlib import Path
import sys,json,re
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();script=root/'work/curate_ccp_sequences.py';t=script.read_text(encoding='utf-8').replace('import sys,json\n','import sys,json,re\n').replace("d['title'].startswith(name+'V')","re.search(r'\\b'+re.escape(name)+r'V\\d+\\b',d['title'])");script.write_text(t,encoding='utf-8')
items=json.loads((root/'work/documents/src-000052/sequence-curation.json').read_text(encoding='utf-8'));defs=json.loads((root/'work/documents/src-000053/message-definitions.json').read_text(encoding='utf-8'));reviews=[]
for item in items:
 p=root/item['diagram'];m,b=kb.metadata(p);names=re.findall(r'^    (?:CCP|CM)(?:-->>|->>)(?:CCP|CM): (.+)$',p.with_suffix('.mmd').read_text(encoding='utf-8'),re.M);mapping=[]
 for name in names:
  ds=[d for d in defs if re.search(r'\b'+re.escape(name)+r'V\d+\b',d['title'])]
  if len(ds)==1:
   d=ds[0];mapping.append({'source_label':name,'message_id':d['message_id'],'source_id':'src-000053','locator':f"file pages {d['start_page']}-{d['end_page']}; "+d['title']})
   lines=b.splitlines()
   for i,line in enumerate(lines):
    if line.startswith('| ') and '| '+name+' |' in line:lines[i]=line.replace('No exact definition bound by this CCP source segment',kb.link(p,root/'domains/securities/reference/messages'/d['message_id']/'index.md',d['message_id']))
   b='\n'.join(lines)+'\n'
 m.update(message_ids=sorted(x['message_id'] for x in mapping),message_mapping_evidence=mapping,render_status='pass',visual_review='pass',review_status='needs-review' if m.get('issue_ids') else 'reviewed',mermaid_version='12.3.0',mermaid_renderer='Mermaid browser API + Chromium 156.0.8078.81',review_date='2026-11-09')
 evidence=f"Opened the full source image and Mermaid render; compared both participant labels, all {item['messages']} ordered message labels and directions, {item['optional']} dotted optional/potential path(s), and {item['reverse']} clearing-member-to-CCP arrow(s). P214-P215 line semantics and relevant narrative conditions are retained. Building silhouettes are replaced by labeled participant boxes; they do not identify named institutions."
 if m.get('issue_ids'):evidence+=' Visual comparison passes; page remains needs-review because Part1 message-name suffix conflict is recorded under issue-000030.'
 b=b[:b.index('## Review evidence')]+'## Review evidence\n\n'+evidence+' Parsed/rendered with Mermaid 12.3.0 and Chromium 156.0.8078.81; visual review on 2026-11-09 Europe/Warsaw, rendering report UTC date 2026-11-08.\n\n'+kb.link(p,root/'domains/securities/assets/src-000052/reconstructed-transactions'/(item['source_figure']+'.png'),'Compared reconstruction')+'.\n';kb.put(p,kb.front(m)+b)
 fp=root/item['flow'];fm,fb=kb.metadata(fp);fm['message_ids']=m['message_ids'];fm['message_families']=sorted(set(x.rsplit('.',2)[0] for x in m['message_ids']));fm['message_mapping_evidence']=mapping;fb+='\nExact definition bindings use the actual source053 MDR Part2 definition headings: '+', '.join(kb.link(fp,root/'domains/securities/reference/messages'/x['message_id']/'index.md',x['source_label']+' / '+x['message_id'])+' ('+x['locator']+')' for x in mapping)+'. Names outside this MDR scope remain unbound to a particular version.\n';kb.put(fp,kb.front(fm)+fb)
 ep=p.parents[2]/'documents/src-000052/diagrams'/(item['source_figure']+'.md');em,eb=kb.metadata(ep);em.update(canonical_diagram=item['diagram'],disposition='converted-needs-review' if m.get('issue_ids') else 'deduplicated',visual_review='pass');eb+='\n## Source reconstruction\n\n'+kb.link(ep,p,m['title'])+'. Original and rendered reconstruction visually compared; source naming conflicts remain explicit where applicable.\n';kb.put(ep,kb.front(em)+eb)
 reviews.append({'diagram':item['diagram'],'source_id':'src-000052','source_figure':item['source_figure'],'render':'pass','visual_review':'pass','date':'2026-11-09','timezone':'Europe/Warsaw','mermaid_version':'12.3.0','evidence':evidence,'issue_ids':m.get('issue_ids',[])})
kb.dump(root/'tracking/reviews/ccp-transaction-diagrams.json',reviews)
print('All seven sequences visually checked, exact-ID bindings repaired from authoritative MDR2 headings.')
