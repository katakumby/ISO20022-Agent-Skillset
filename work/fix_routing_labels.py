from pathlib import Path
import re
base=Path('domains/securities/reference/message-sets/corporate-actions/2025-2026/diagrams/routing-scenarios')
for p in base.glob('*.mmd'):
 old=p.read_text(encoding='utf-8')
 def wrap(m):
  t=m.group(1)
  if '<br/>' not in t and len(t)>8:
   words=t.split(' ');mid=max(1,len(words)//2);t=' '.join(words[:mid])+'<br/>'+' '.join(words[mid:])
  return '|"'+t+'"|'
 new=re.sub(r'\|"([^"\n]+)"\|',wrap,old)
 if p.stem=='fig-0034':new=new.replace('25D::IPRC/PACK','25D::IPRC<br/>[separator unclear]<br/>PACK')
 if new!=old:
  p.write_text(new,encoding='utf-8');md=p.with_suffix('.md');body=md.read_text(encoding='utf-8').replace(old,new).replace('25D::IPRC/PACK','25D::IPRC [separator unclear] PACK');md.write_text(body,encoding='utf-8')
