from pathlib import Path
import json,sys
sys.path.insert(0,'tools');import kb
r=Path('.').resolve();b=r/'domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025'
for p in [b/'documents/src-000362/tables/tbl-0012.md',b/'documents/src-000362/visual-coverage.md']:
 m,t=kb.metadata(p);m['issue_ids']=['issue-000048'];t+='\nTracked source chronology conflict: '+kb.link(p,r/'tracking/issues.md','issue-000048')+'.\n';kb.put(p,kb.front(m)+t)
p=r/'tracking/reviews/t2s-limit-journal-figure-coverage.json';d=json.loads(p.read_text(encoding='utf-8'));d['issue_ids']=['issue-000048'];kb.dump(p,d)
