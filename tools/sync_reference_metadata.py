"""Refresh publication metadata from maintained source identities, preserving page content."""
import argparse,json
from pathlib import Path
import kb,catalog
def main(root):
 ss={s['source_id']:s for s in kb.sources(root)};changed=[]
 for r in catalog.records(root):
  ids=r.get('source_ids',[])
  if not ids or any(x not in ss for x in ids):continue
  page=root/r['path'];m,text=kb.metadata(page)
  editions=sorted(set(ss[sid]['source_edition'] for sid in ids if ss[sid].get('source_edition')))
  # Source identity remains authoritative; publication labels are never message versions.
  if m.get('source_editions')!=editions:
   m['source_editions']=editions;kb.put(page,kb.front(m)+text.lstrip());changed.append(r['path'])
 kb.dump(root/'tracking/publication-metadata-validation.json',{'date':kb.DATE,'pages_updated':changed,'scope':'Source publication metadata only; no business statements, source identities, review statuses or original bytes changed.'})
 print(json.dumps({'publication_metadata_pages_updated':len(changed)}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();main(a.root.resolve())
