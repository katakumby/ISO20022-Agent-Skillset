from pathlib import Path
import re
p=Path('domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0002.mmd');c=p.read_text(encoding='utf-8');c=re.sub(r'actor (\w+) as "([^"]+)"',r'actor \1("\2")',c);c=re.sub(r'usecase (\w+) as "([^"]+)"',r'\1("\2")',c);p.write_text(c,encoding='utf-8');p=p.with_suffix('.md');b=p.read_text(encoding='utf-8');b=re.sub(r'```mermaid\n.*?```','```mermaid\n'+c+'```',b,flags=re.S);p.write_text(b,encoding='utf-8')
