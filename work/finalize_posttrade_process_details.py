from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();base=root/'domains/securities/reference/message-sets/post-trade-matching/2024-2025'
# Targeted final changes to avoid regenerating curated flow/participant text.
for n in [7,8,9,11,12,13]:
 p=base/'diagrams/processes'/f'fig-{n:04d}.md';m,b=kb.metadata(p);mp=p.with_suffix('.mmd');c=mp.read_text(encoding='utf-8')
 if n in [7,8,9]:c+=' style CancelEndpoint fill:none,stroke:none\n';b=b.replace('Unlabelled endpoint symbols preserve source geometry','The invisible endpoint cue preserves the point at which a source arrow terminates without a labelled receiving action; this is a reconstruction cue, not an added lifecycle event. Unlabelled source symbols preserve source geometry');m['limitations'].append('The cancellation arrow terminates in blank CMU space in the source; an invisible endpoint cue anchors it in Mermaid and does not create an event or receiving action.')
 else:c+=' style Match fill:#ff8500,stroke:black\n'
 b=b[:b.index('```mermaid\n')]+ '```mermaid\n'+c+'```'+b[b.index('```',b.index('```mermaid\n')+11)+3:];kb.put(mp,c);kb.put(p,kb.front(m)+b)
for slug,old,new in [('party','Plain associations connect it with ten named business actors.','Eleven plain rays associate it with surrounding business actors; several source endpoints stop short of actor symbols.'),('financial-intermediary','It has no visible connection to Party or another actor; no responsibility or relationship is inferred from proximity.','A plain ray extends from near Party toward this actor, ending short of its symbol as do several other source rays; no specific responsibility, direction or inheritance is inferred.')]:
 p=root/'shared/reference/participants'/('participant-src-000180-'+slug+'.md');text=p.read_text(encoding='utf-8').replace(old,new);kb.put(p,text)
# Remove repeated identical additions introduced while correcting overview draft.
for p in list((root/'shared/reference/participants').glob('participant-src-000180-*.md'))+list((base/'flows').glob('flow-src-000180-p120-*.md')):
 text=p.read_text(encoding='utf-8');parts=text.split('\n\n');seen=set();clean=[]
 for q in parts:
  if q.startswith('Source context: [') and q in seen:continue
  if q.startswith('## Curated process interpretation') and q in seen:continue
  if q in seen and q.startswith('The source begins with Order Process'):continue
  if q in seen and q.startswith('[Complete source diagram reconstruction]'):continue
  seen.add(q);clean.append(q)
 kb.put(p,'\n\n'.join(clean))
