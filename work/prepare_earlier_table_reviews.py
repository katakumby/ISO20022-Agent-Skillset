from pathlib import Path
import sys,json,ast,subprocess
sys.path.insert(0,'tools');import kb
from local_runtime import executable
root=Path('.').resolve();p=root/'tools/checkpoint.py';text=p.read_text(encoding='utf-8');entry=('issue-000060','bank-to-customer source consistency defects','payments','src-000004','T14/P116 Word13-14; T15/P118 Word14-15; P159/P269/P445 versus T18-T20/P165/P275/P451 Word23-38; T18 row41/66 versus P221/P258; T19 row46/50 versus P342/P348; P517/T21 versus P523/P526 Word38-39','T14 uses Cash Position Evaluation Position versus System lane; T15 Receive notification Initiator says Account Servicer while description/diagram assigns receipt to owner. Example narratives2010 conflict with2015 payload dates. T18 slash/hyphen reference and0.1085/0.185 exchange rate differ; T19 hyphen/underscore reference andDMCT/BOOK code differ. Reporting-request narrative asks Statement but table requests camt.052.001.09 at10:05 and XML.08 at17:15. Table tag labels differ from payload/schema. Four exact enveloped XSD checks pass without resolving these business conflicts.','Preserve all original values, leading-zero code examples, role assignments and exact request versions. Keep visual fidelity, XML schema validity and source/business consistency separate; do not silently repair sources.')
if 'issue-000060' not in text:
 tree=ast.parse(text);a=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='KNOWN' for t in n.targets));lines=text.splitlines(keepends=True);lines.insert(a.end_lineno-1,' '+repr(entry)+',\n');kb.put(p,''.join(lines))
exe=executable('pdftoppm','ISO20022_PDFTOPPM')
for sid in ['src-000052','src-000079','src-000180','src-000347','src-000350','src-000353']:
 r=json.loads((root/'work/docx-render'/sid/'reconciliation.json').read_text(encoding='utf-8'));pages=sorted({pg for t in r['tables'] for pg in range(t['word_start_file_page'],t['word_end_file_page']+1)});dest=root/'domains/securities/assets'/sid/'table-page-renders';dest.mkdir(parents=True,exist_ok=True)
 for pg in pages:
  target=dest/f'word-page-{pg:03d}'
  if not target.with_suffix('.png').exists():subprocess.run([str(exe),'-f',str(pg),'-l',str(pg),'-r','120','-png','-singlefile',str(root/'work/docx-render'/sid/'document.pdf'),str(target)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 kb.dump(root/'work/docx-render'/sid/'table-review-plan.json',{'source_id':sid,'pages':pages,'tables':r['tables'],'output':dest.relative_to(root).as_posix()});print(sid,len(pages),flush=True)
