"""Keep literal XSD regexes from being interpreted as Markdown links."""
import argparse,json
from pathlib import Path
import kb
def main(root):
 changed=[]
 for s in kb.sources(root):
  if s['format']!='xsd':continue
  folder=root/kb.area(s['domain'])/'reference/messages'/s['message_ids'][0]
  for p in (folder/'types').glob('*.md'):
   text=p.read_text(encoding='utf-8');lines=text.splitlines(keepends=True);different=False
   for i,line in enumerate(lines):
    if line.startswith('| pattern |'):
     cols=line.split(' | ')
     if len(cols)>3 and not cols[2].startswith('`'):
      cols[2]='`'+cols[2]+'`';lines[i]=' | '.join(cols);different=True
   if different:kb.put(p,''.join(lines));changed.append(p.relative_to(root).as_posix())
 kb.dump(root/'tracking/schema-markdown-validation.json',{'date':kb.DATE,'pages_corrected':changed,'purpose':'Literal regular-expression facets render as code, preserving exact XSD values and avoiding accidental Markdown links.'})
 print(json.dumps({'pattern_pages_formatted':len(changed)}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();main(a.root.resolve())
