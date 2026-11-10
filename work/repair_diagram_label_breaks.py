from pathlib import Path
base=Path('domains/securities/reference/message-sets/corporate-actions/2025-2026/diagrams/activities')
for n,pairs in [(1,[('"Corporate Action Instruction"','"Corporate Action<br/>Instruction"'),('"Corporate Action Narrative"','"Corporate Action<br/>Narrative"')]),(19,[('"CA Cancellation Advice"','"CA Cancellation<br/>Advice"')])]:
 p=base/f'fig-{n:04d}.mmd';old=p.read_text(encoding='utf-8');new=old
 for a,b in pairs:new=new.replace(a,b)
 p.write_text(new,encoding='utf-8');md=p.with_suffix('.md');md.write_text(md.read_text(encoding='utf-8').replace(old,new),encoding='utf-8')
