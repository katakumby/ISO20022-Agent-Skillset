from pathlib import Path
import sys,re,json
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();sid='src-000356';s=next(x for x in kb.sources(root) if x['source_id']==sid);base=root/s['set_path'];main=base/'diagrams/curated/fig-0002.md';meta,body=kb.metadata(main);code=re.search(r'```mermaid\n(.*?)```',body,re.S).group(1);lines=code.splitlines();leaf=[l for l in lines if re.match(r' (Ins|Sec|Cash|Day|Dyn|Static) -->',l)]
overview='\n'.join(l for l in lines if l not in leaf)
cash='flowchart LR\n Cash["Cash account"]\n'+'\n'.join(l for l in leaf if l.startswith(' Cash'))+'\n'
other='flowchart LR\n Ins["Instructions"]\n Sec["Security account"]\n Day["Settlement day"]\n Dyn["Dynamic data queries"]\n Static["Static data"]\n'+'\n'.join(l for l in leaf if not l.startswith(' Cash'))+'\n'
md=[]
for suffix,title,c in [('overview','Modes, actors and six query categories',overview),('cash','Fourteen cash-account queries',cash),('other','Other query-category detail',other)]:
 name='fig-0002-'+suffix;p=main.parent/(name+'.md');m=dict(meta);m.update(document_kind='diagram-detail',diagram_id=name,title=title,parent_diagram='fig-0002',review_status='needs-review',render_status='not-run',visual_review='not-run');text='# '+title+'\n\nFocused view of '+kb.link(p,main,'the complete source query taxonomy')+'. Source src-000356, direct-body P130, word/media/image2.png. This view partitions the artwork for readable retrieval; it adds no new query permissions or message bindings.\n\n```mermaid\n'+c+'```\n\n'+kb.link(p,root/'domains/securities/assets'/sid/'originals/image2.png','Complete unchanged source')+'.\n';kb.put(p,kb.front(m)+text);kb.put(root/'work/documents'/sid/'curated-mermaid-details'/(name+'.mmd'),c);md.append(kb.link(main,p,title))
body+='\n## Focused taxonomy views\n\n'+'\n'.join('- '+x for x in md)+'\n\nAll25 leaf boxes are preserved across the cash-account and other-category details; the complete source and full reconstruction remain above.\n';kb.put(main,kb.front(meta)+body)
