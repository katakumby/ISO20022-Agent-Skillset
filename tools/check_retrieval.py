"""Evidence-oriented retrieval checks for this supplied corpus, not model answers."""
import argparse,json
from pathlib import Path
import kb,catalog

def run(root):
 checks=[]
 def record(name,passed,evidence,limitation=None):checks.append({'test':name,'pass':bool(passed),'evidence':evidence,'limitations':[limitation] if limitation else []})
 rr=list(catalog.records(root));ss=kb.sources(root)
 family=catalog.lookup(root,'semt.002',100)['records'];expected_family={r['message_id'] for r in rr if r.get('document_kind')=='message-index' and r.get('message_family')=='semt.002'};record('Family preserves all supplied canonical definitions',{r.get('message_id') for r in family}==expected_family and bool(expected_family),[r['path'] for r in family])
 one=catalog.lookup(root,'sese.023.001.13',10)['records'];record('Exact identifier resolves once',len(one)==1,[r['path'] for r in one])
 for mid,expected in [('head.001.001.04','AppHdr'),('head.002.001.01','Xchg')]:
  s=kb.canonical_schemas(root,ss)[0][mid];rec=catalog.lookup(root,mid,10)['records'];record(mid+' retains its own header root',s['roots']==[expected] and len(rec)==1,{'roots':s['roots'],'path':rec[0]['path'] if rec else None,'source_id':s['source_id']})
 context=root/'shared/reference/concepts/business-application-header-and-business-file-header.md';record('BAH versus Business File Header context exists',context.exists(),str(context.relative_to(root)))
 dup=next(s for s in ss if s['format']=='xsd' and len(s['occurrences'])>1);rec=catalog.lookup(root,dup['message_ids'][0],100)['records'];record('Loose and archived duplicate has one canonical definition',len(rec)==1 and any(o.get('archive_member') for o in dup['occurrences']),{'source_id':dup['source_id'],'occurrences':dup['occurrences'],'canonical':[r['path'] for r in rec]})
 owners=[r for r in rr if r.get('document_kind')=='participant' and 'account owner' in (r.get('title','')+' '+' '.join(r.get('source_labels',[]))).lower()]
 servicers=[r for r in rr if r.get('document_kind')=='participant' and 'account servicer' in (r.get('title','')+' '+' '.join(r.get('source_labels',[]))).lower()]
 record('Account owner and servicer stay scoped across flows',len(owners)>1 and len(servicers)>1,{'owner_paths':[r['path'] for r in owners[:5]],'servicer_paths':[r['path'] for r in servicers[:5]]},'Same source labels across collections do not establish institutional identity or equivalence.')
 reuse=[r for r in rr if r.get('document_kind')=='participant' and len(r.get('flows',r.get('flow_ids',[])))>1];record('Same contextual participant reused in multiple processes',bool(reuse),[{'path':r['path'],'flows':r.get('flows',r.get('flow_ids'))[:5]} for r in reuse[:3]])
 for label,pattern in [('Cancellation request','cancellation-request'),('Settlement reversal','reversal-advice')]:
  matches=[r for r in rr if r.get('document_kind')=='business-flow' and r.get('flow_id')=='flow-settlement-reconciliation-'+pattern]
  texts='\n'.join((root/r['path']).read_text(encoding='utf-8') for r in matches).lower()
  marker='open transaction' if pattern=='cancellation-request' else 'confirmed'
  record(label+' retains distinct source preconditions',bool(matches) and marker in texts,[r['path'] for r in matches])
 ca=[r for r in rr if r.get('document_kind')=='business-flow' and 'corporate-actions' in r['path'] and 'movement-reversal' in r['path']]
 record('Corporate-action movement reversal is retrievable',bool(ca),[r['path'] for r in ca])
 pay=[r for r in rr if r.get('document_kind')=='message-index' and r.get('message_id') in ['camt.003.001.08','camt.053.001.14']]
 groups={r['message_id']:r.get('message_sets') for r in pay};record('Operational cash management and bank-to-customer reporting remain separate','cash-management' in groups.get('camt.003.001.08',[]) and 'bank-to-customer-cash-management' in groups.get('camt.053.001.14',[]),groups)
 s=kb.canonical_schemas(root,ss)[0]['seev.001.001.13'];rec=catalog.lookup(root,'seev.001.001.13',10)['records'];has_documentation=any('seev.001.001.13' in x.get('defined_message_ids',x.get('message_ids',[])) for x in ss if x['format'] in ['docx','pdf']);record('Schema/message documentation availability remains explicit',bool(rec) and (has_documentation or bool(rec[0].get('limitations'))),{'source_id':s['source_id'],'path':rec[0]['path'] if rec else None,'collection':s['collection']},'Business actors and purpose are not inferred from the XSD alone.')
 results=catalog.query(root,'participant','account owner',3);record('Search is bounded and carries provenance/status',len(results['records'])<=3 and all(r.get('path') and r.get('source_ids') and r.get('review_status') for r in results['records']),results)
 for mid in ['semt.041.001.02','semt.042.001.01']:
  result=catalog.lookup(root,mid,5)['records'];roles=catalog.roles(root,mid,5)['records'];record('Documentation-only '+mid+' exposes unavailable schema and available role evidence',len(result)==1 and ((mid in kb.canonical_schemas(root,ss)[0] and bool(result[0].get('namespace'))) or (result[0].get('schema_status')=='not-supplied' and result[0].get('namespace') is None and len(roles)==1 and roles[0].get('status')=='documentation-only-business-evidence' and roles[0].get('source_provenance'))),{'message':result,'roles':roles})
 # Cross-reference IDs are checked independently of Markdown links.
 participants={r['participant_id']:r['path'] for r in rr if r.get('participant_id')};flows={r['flow_id']:r['path'] for r in rr if r.get('flow_id')};unresolved=[]
 for r in rr:
  for key,index in [('participants',participants),('participant_ids',participants),('flows',flows),('flow_ids',flows)]:
   values=r.get(key,[])
   if not isinstance(values,list):continue
   for value in values:
    if isinstance(value,str) and value.startswith(('participant-','flow-')) and value not in index:unresolved.append({'path':r['path'],'field':key,'identifier':value})
 record('Participant and flow identifiers resolve',not unresolved,unresolved)
 out={'date':kb.DATE,'checks':checks,'pass':all(x['pass'] for x in checks),'scope':'Retrieval and cross-reference behavior on supplied evidence; not a claim of completed visual or business-semantic review.'}
 kb.dump(root/'tracking/retrieval-validation.json',out);print(json.dumps({'checks':len(checks),'passed':sum(x['pass'] for x in checks),'failures':[x['test'] for x in checks if not x['pass']]}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();run(a.root.resolve())
