from pathlib import Path
root=Path('.').resolve()
paths=[root/'domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/diagrams/curated/fig-0002.md',root/'domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/diagrams/curated/fig-0002-cash.md',root/'work/documents/src-000356/curated-mermaid-details/fig-0002-cash.mmd']
paths+=list((root/'work/documents/src-000356').glob('*/fig-0002.mmd'))
for p in paths:
 t=p.read_text(encoding='utf-8');p.write_text(t.replace('Immediate Liquidity Transfer Order List Query','Immediate Liquidity Transfer Order List'),encoding='utf-8')
print([str(p.relative_to(root)) for p in paths])
