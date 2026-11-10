from pathlib import Path
import sys,json,hashlib
sys.path.insert(0,'tools');import kb
r=Path('.').resolve();sid='src-000365';s=next(x for x in kb.sources(r) if x['source_id']==sid);b=r/s['set_path'];p=b/'diagrams/curated/fig-0007.md';q=b/'diagrams/curated/fig-0008.md';m,t=kb.metadata(p);n,u=kb.metadata(q);a=r/'domains/securities/assets'/sid/'derived-previews';h=[hashlib.sha256((a/f'image{i}.emf.png').read_bytes()).hexdigest() for i in [7,8]];assert h[0]==h[1]
for f in [p,q,q.with_suffix('.mmd')]:
 dest=r/'tracking/history/job-000001/manual-curation-2026-11-09'/f.relative_to(r);dest.parent.mkdir(parents=True,exist_ok=True)
 if not dest.exists():dest.write_bytes(f.read_bytes())
m['title']='Link creation and modification validation/retry activity';m['flow_ids']=sorted(set(m['flow_ids']+n['flow_ids']));m['message_ids']=sorted(set(m['message_ids']+n['message_ids']));m['participants']=sorted(set(m['participants']+n['participants']));m['source_locations']+=n['source_locations'];m['deduplication_basis']='Original EMF bytes differ; complete Windows-rendered source preview PNGs are byte-identical, SHA256 '+h[0]+'. Distinct creation/modification conditions and source occurrences remain separate.';t=t.replace('# Link creation activity with validation and retry','# '+m['title'],1);part=u[u.index('## Roles, activities and alternatives'):u.index('## Review evidence')];t+='\n## Modification context and second source occurrence\n\n'+m['deduplication_basis']+'\n\nSecond original: '+kb.link(p,r/'domains/securities/assets'/sid/'originals/image8.emf','unchanged image8.emf')+'; P133, Word16.\n\n'+part;kb.put(p,kb.front(m)+t)
n.update(document_kind='diagram-alias',canonical_diagram=p.relative_to(r).as_posix(),deduplication_basis=m['deduplication_basis']);kb.put(q,kb.front(n)+'# Shared validation/retry diagram\n\n'+kb.link(q,p,'Canonical creation/modification activity')+'. The complete rendered source artwork is byte-identical; the canonical page preserves both flow contexts, original EMFs, source locators and all six applicable exact definitions.\n')
# Remove only the duplicate generated Mermaid input after preserving its previous bytes in history.
f=q.with_suffix('.mmd');assert r in f.resolve().parents;f.unlink()
f=r/'work/documents'/sid/'curated-figures.json';records=json.loads(f.read_text(encoding='utf-8'));records=[x for x in records if x['source_figure']!='fig-0008'];next(x for x in records if x['source_figure']=='fig-0007')['source_occurrences']=['fig-0007','fig-0008'];kb.dump(f,records)
for f in list((b/'flows').glob('*.md'))+list((r/'shared/reference/participants').glob(f'participant-{sid}-*.md')):
 text=f.read_text(encoding='utf-8');new=text.replace('diagrams/curated/fig-0008.md','diagrams/curated/fig-0007.md')
 if new!=text:kb.put(f,new)
print('Deduplicated pixel-identical complete source activity artwork; both semantic contexts preserved')
