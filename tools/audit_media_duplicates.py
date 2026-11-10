"""Build byte-identity groups for extracted DOCX media with every source occurrence.

Equal assets are deduplication candidates only: surrounding labels, grouped objects,
and source meaning still require reconciliation before reusing a reconstruction.
"""
import argparse,json,hashlib
from pathlib import Path
import kb

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=ap.parse_args();root=a.root.resolve();groups={};media_count=0
 for f in sorted((root/'work/documents').glob('*/media-review-inventory.json')):
  d=json.loads(f.read_text(encoding='utf-8'))
  for m in d['media']:
   path=root/m['original'];h=hashlib.sha256(path.read_bytes()).hexdigest()
   if h!=m['original_sha256']:raise ValueError('Changed extracted original '+str(path))
   media_count+=1;g=groups.setdefault(h,{'sha256':h,'asset_identity':'media-sha256-'+h,'occurrences':[]})
   g['occurrences'].append({'source_id':d['source_id'],'original':m['original'],'preview':m.get('preview'),'source_occurrences':m.get('occurrences',[]),'disposition':m.get('disposition'),'canonical_reconstructions':[x.get('canonical_diagram') for x in m.get('occurrences',[]) if x.get('canonical_diagram')]})
 values=sorted(groups.values(),key=lambda x:x['sha256']);dups=[x for x in values if len(x['occurrences'])>1]
 for g in values:
  g['source_count']=len(set(x['source_id'] for x in g['occurrences']));g['reuse_status']='requires-complete-figure-and-context-review' if len(g['occurrences'])>1 else 'unique-asset'
 kb.dump(root/'catalog/docx-media-identities.json',{'updated':'2026-11-09','media_occurrences':media_count,'unique_contents':len(groups),'duplicate_groups':len(dups),'cross_publication_duplicate_groups':sum(x['source_count']>1 for x in dups),'limitations':['Byte-identical embedded media are not automatically equivalent complete figures: drawing composition, surrounding labels and context may differ.','A group is not marked deduplicated until its canonical reconstruction has been reviewed and every relevant occurrence context reconciled.'],'groups':values})
 p=root/'catalog/docx-media-identities.md';kb.put(p,kb.front(dict(template=False,document_kind='media-identity-index',review_status='needs-review'))+'# DOCX media byte identities\n\n'+f'{media_count} media occurrences have {len(groups)} distinct byte contents. {len(dups)} byte-identical groups include repeated occurrences; {sum(x["source_count"]>1 for x in dups)} groups span publications.\n\nEqual bytes identify candidates for reusing a reconstruction. They do not prove that the complete figure or its business meaning is equivalent: surrounding objects, labels and source context require review. Original media remain unchanged and every occurrence is retained.\n\n'+kb.link(p,root/'catalog/docx-media-identities.json','Full identities and precise source occurrence locators')+'.\n\n'+kb.table(['SHA-256','Occurrences','Publications','Original assets'],[[g['sha256'],len(g['occurrences']),g['source_count'],'; '.join(kb.link(p,root/o['original'],o['source_id']+'/'+Path(o['original']).name) for o in g['occurrences'])] for g in dups]))
 print(json.dumps({'media_occurrences':media_count,'unique_contents':len(groups),'duplicate_groups':len(dups),'cross_publication_groups':sum(x['source_count']>1 for x in dups)}))
if __name__=='__main__':main()

