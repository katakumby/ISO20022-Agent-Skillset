from pathlib import Path
p=Path('domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0010.md')
for p in [p,p.with_suffix('.mmd')]:
 t=p.read_text(encoding='utf-8').replace('class Request,Receive,Validate,Reject,Process,Report covered','class Request,Receive,Validate,Valid,Reject,Process,Report covered').replace('style S fill:#4678bb,stroke:#4678bb','style S fill:#4678bb,stroke:#4678bb\n style Merge fill:black,stroke:black');p.write_text(t,encoding='utf-8')
