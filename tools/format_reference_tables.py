"""Escape raw XML labels in Markdown tables without changing their text values."""
import argparse,json,html
from pathlib import Path
import kb
def main(root,pdf_tables_only=False):
 changed=[]
 if pdf_tables_only:
  paths=[]
  for source in kb.sources(root):
   tf=root/'work/documents'/source['source_id']/'tables.json'
   if source['format']=='pdf' and tf.exists():paths.extend(root/t['output'] for t in json.loads(tf.read_text(encoding='utf-8')))
 else:paths=[p for base in [root/'shared/reference',root/'domains'] for p in base.rglob('*.md')]
 for p in paths:
   text=p.read_text(encoding='utf-8');lines=text.splitlines(keepends=True);fenced=False
   for i,line in enumerate(lines):
    if line.startswith('```'):fenced=not fenced
    if not fenced and line.startswith('|'):lines[i]=kb.escape_table_markup(line)
   new=''.join(lines)
   if html.unescape(new)!=html.unescape(text):raise ValueError('Literal text or links changed: '+str(p))
   if new!=text:kb.put(p,new);changed.append(p.relative_to(root).as_posix())
 kb.dump(root/'tracking'/('pdf-table-format-validation.json' if pdf_tables_only else 'table-format-validation.json'),{'date':kb.DATE,'pages_checked':len(paths),'pages_corrected':changed,'decoded_text_preservation':'pass','purpose':'Raw XML angle-bracket labels are escaped in Markdown tables; exact code spans, links and source values are retained.'})
 print(json.dumps({'table_pages_formatted':len(changed)}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--pdf-tables-only',action='store_true');a=p.parse_args();main(a.root.resolve(),a.pdf_tables_only)
