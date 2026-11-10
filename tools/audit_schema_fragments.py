"""Independently compare generated declaration fragments against supplied XSD nodes."""
import argparse,json,re,hashlib
from pathlib import Path
from lxml import etree as E
P=argparse.ArgumentParser();P.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);P.add_argument('--message',default='sese.023.001.13');P.add_argument('--save',action='store_true');A=P.parse_args();R=A.root.resolve()
found=list(R.glob('domains/*/reference/messages/'+A.message+'/schema-coverage.json'))+list(R.glob('shared/reference/messages/'+A.message+'/schema-coverage.json'));assert len(found)==1,'Expected one canonical exact message'
C=json.loads(found[0].read_text());S=next(s for s in json.loads((R/'catalog/sources.json').read_text())['sources'] if s['source_id']==C['source_id'])
occ=next(o for o in S['occurrences'] if o.get('archive_member') is None);raw=(R/occ['path']).read_bytes();assert hashlib.sha256(raw).hexdigest()==C['sha256'],'Original fingerprint changed'
schema=E.fromstring(raw,E.XMLParser(resolve_entities=False,no_network=True));XS='http://www.w3.org/2001/XMLSchema'
def signature(n):return (n.tag,tuple(sorted(n.attrib.items())),(n.text or '').strip(),tuple(signature(c) for c in n if isinstance(c.tag,str)))
errors=[];checked=[]
for c in C['components']:
 p=R/c['path'];text=p.read_text(encoding='utf8');blocks=re.findall(r'```xml\s*\n(.*?)\n```',text,re.S)
 matches=schema.xpath(c['schema_path'],namespaces={'xs':XS})
 if len(blocks)!=1 or len(matches)!=1:errors.append({'page':c['path'],'problem':'Expected one declaration block and one source-path match'});continue
 try:equivalent=signature(E.fromstring(blocks[0].encode()))==signature(matches[0])
 except Exception as e:errors.append({'page':c['path'],'problem':str(e)});continue
 if not equivalent:errors.append({'page':c['path'],'problem':'Declaration data model differs'})
 else:checked.append(c['path'])
result={'date':'2026-11-08','message_id':A.message,'source_id':S['source_id'],'source_sha256':C['sha256'],'helper_version':C.get('helper_version'),'declarations_checked':len(checked),'expected_components':len(C['components']),'errors':errors,'result':'pass' if not errors and len(checked)==len(C['components']) else 'fail','scope':'Literal XML data-model equivalence, exact paths and immutable source hash. Does not assert business semantics, cross-reference symbol-space correctness or visual figure review.'}
if A.save:
 p=R/'tracking/reviews'/(A.message+'-schema-fragments.json');p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2));raise SystemExit(bool(errors))
