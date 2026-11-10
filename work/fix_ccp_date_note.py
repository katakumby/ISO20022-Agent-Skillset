from pathlib import Path
p=Path('domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/processes/fig-0011.mmd');a=p.read_text(encoding='utf-8');b=a.replace('  classDef outside','  Date --- Confirm\n  classDef outside');p.write_text(b,encoding='utf-8');md=p.with_suffix('.md');md.write_text(md.read_text(encoding='utf-8').replace(a,b),encoding='utf-8')
