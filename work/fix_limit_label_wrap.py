from pathlib import Path
p=Path('domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0005-cash-2.md')
for p in [p,p.with_suffix('.mmd')]:
 t=p.read_text(encoding='utf-8').replace('|LimitUtilisationJournalQuery|','|LimitUtilisation<br/>JournalQuery|').replace('|LimitUtilisationJournalReport|','|LimitUtilisation<br/>JournalReport|');p.write_text(t,encoding='utf-8')
