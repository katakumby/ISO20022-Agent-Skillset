from pathlib import Path
base=Path('domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated')
for n,node in [(7,'J'),(8,'Fork')]:
 for ext in ['.md','.mmd']:
  p=base/(f'fig-{n:04d}'+ext);t=p.read_text(encoding='utf-8').replace(node+'[" "]',node+'@{ shape: fork }');p.write_text(t,encoding='utf-8')
