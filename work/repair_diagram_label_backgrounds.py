from pathlib import Path
for n in [1,19]:
 p=Path('domains/securities/reference/message-sets/corporate-actions/2025-2026/diagrams/activities')/f'fig-{n:04d}.mmd';old=p.read_text(encoding='utf-8');new=old.replace('config:\n','config:\n  themeCSS: ".edgeLabel p {background-color:#ffffff !important;} .edgeLabel {background-color:#ffffff !important;} .edgeLabel rect {fill:#ffffff !important;opacity:1!important;}"\n');p.write_text(new,encoding='utf-8');md=p.with_suffix('.md');md.write_text(md.read_text(encoding='utf-8').replace(old,new),encoding='utf-8')
