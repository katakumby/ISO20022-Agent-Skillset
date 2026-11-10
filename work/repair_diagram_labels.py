from pathlib import Path
import sys
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();d=root/'domains/securities/reference/message-sets/corporate-actions/2025-2026/diagrams/activities'
for n in [1,19]:
 p=d/f'fig-{n:04d}.mmd';old=p.read_text(encoding='utf-8');new='---\nconfig:\n  flowchart:\n    htmlLabels: true\n---\n'+old;p.write_text(new,encoding='utf-8');md=p.with_suffix('.md');t=md.read_text(encoding='utf-8');md.write_text(t.replace(old,new),encoding='utf-8')
