from pathlib import Path
import hashlib,json,re,kb
root=Path(__file__).resolve().parents[1];base=root/'domains/payments/reference/message-sets/cash-management/2024-2025/diagrams/operational-cash';report=root/'work/operational-cash-curation.json';r=json.loads(report.read_text(encoding='utf-8'))
for n,name in [(7,'ReturnTransaction'),(11,'ReturnLimit')]:
 p=base/f'fig-{n:04d}.md';m,b=kb.metadata(p);old='Note right of B: Execution Delay\ndeactivate B\nB->>A: '+name+'\n';new='Note right of B: Execution Delay\nB->>A: '+name+'\ndeactivate B\n';b=b.replace(old,new);code=p.with_suffix('.mmd').read_text(encoding='utf-8').replace(old,new);kb.put(p,kb.front(m)+b);kb.put(p.with_suffix('.mmd'),code)
 next(x for x in r['outputs'] if x['figure_id']==f'fig-{n:04d}')['mermaid_sha256']=hashlib.sha256(code.encode()).hexdigest()
kb.dump(report,r)
