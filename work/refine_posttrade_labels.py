from pathlib import Path
b=Path('domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions')
for p in b.glob('*.mmd'):
 a=p.read_text(encoding='utf-8');n=a.replace('config:\n','config:\n  themeCSS: ".messageText {stroke:#ffffff !important;stroke-width:4px !important;paint-order:stroke;stroke-linejoin:round;} .actor-line {stroke-dasharray:6 5;stroke:#999999;}"\n');p.write_text(n,encoding='utf-8');md=p.with_suffix('.md');md.write_text(md.read_text(encoding='utf-8').replace(a,n),encoding='utf-8')
