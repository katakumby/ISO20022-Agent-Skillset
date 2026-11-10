"""Local ISO 20022 catalog. Standard library except lxml for schema extraction.

Every path is relative to --root; original sources are never modified.
"""
from __future__ import annotations
import argparse, collections, hashlib, json, os, re, sys, zipfile, shutil, datetime, tempfile
from pathlib import Path
from urllib.parse import quote, unquote

DATE = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
_WRITE_CONTEXT = None
if __name__ == '__main__': sys.modules['kb'] = sys.modules[__name__]
XS = 'http://www.w3.org/2001/XMLSchema'
COLLECTIONS = {
 'business_application_header':('shared','business-application-header','Business Application Header','march-2024'),
 'ExternalCodeSets':('shared','external-code-sets','External code sets','2026-q2'),
 'settlement_and_reconciliation':('securities','settlement-and-reconciliation','Settlement and Reconciliation','2025-2026'),
 'corporate_actions':('securities','corporate-actions','Corporate Actions','2025-2026'),
 'securities_events_general_meeting_proxy_voting':('securities','meetings','Meetings',None),
 'collateral_management_collateral_management':('securities','collateral-management','Collateral Management',None),
 'central_counterparty_clearing_ccp_clearing':('securities','ccp-clearing','CCP Clearing','2025-2026'),
 'post_trade_matching':('securities','post-trade-matching','Post-Trade Matching','2024-2025'),
 'investment_funds':('securities','investment-funds','Investment Funds','2025-2026'),
 'transactions_and_financial_instruments_data_reporting_fitrr':('securities','fitrr','Transactions and Financial Instruments Data Reporting','2025'),
 'target2securities_t2s':('securities','t2s','TARGET2-Securities','august-2026'),
 'payments_initiation':('payments','payments-initiation','Payments Initiation','2025-2026'),
 'payments_clearing_and_settlement':('payments','payments-clearing-and-settlement','Payments Clearing and Settlement','2025-2026'),
 'cash_management':('payments','cash-management','Cash Management','2024-2025'),
 'banktocustomer_cash_management':('payments','bank-to-customer-cash-management','Bank-to-Customer Cash Management','2025-2026'),
}
T2S = {
 'Administration':('shared','march-2024',['admi.005.001.02','admi.006.001.01','admi.007.001.01']),
 'Billing':('securities','december-2025',['camt.076.001.01','camt.077.001.01']),
 'BusinessFileHeader':('shared','june-2024',['head.002.001.01']),
 'CashAccountQueryAndReport':('securities','august-2026',['acmt.025.001.02','acmt.026.001.02']+['reda.%s.001.01'%x for x in ['038','039','040']]),
 'CollateralManagementReferenceData':('securities','may-2025',['reda.%s.001.01'%x for x in ['024','025','026','027','028','044','075','077']]),
 'CollateralReporting':('securities','march-2024',['colr.001.001.02','colr.002.001.02']),
 'IntraBalanceMovement':('securities','march-2024',['camt.%s.001.02'%x for x in ['066','067','068','072','073','074','075','078','079','080','081','082','083','084','085']]),
 'LimitUtilisationJournal':('securities','february-2025',['camt.064.001.01','camt.065.001.01']),
 'LinkReferenceData':('securities','december-2024',['reda.%s.001.01'%x for x in ['045','046','047','049','050','051']]),
 'PartyReferenceData':('securities','march-2024',['reda.014.001.02','reda.015.001.01','reda.016.001.01','reda.017.001.02','reda.022.001.02','reda.031.001.01','reda.041.001.02','reda.042.001.01','reda.043.001.02']),
 'SecuritiesAccountReferenceData':('securities','december-2019',['reda.%s.001.01'%x for x in ['018','019','020','021','023','032','035','036','037']]),
 'SecuritiesAndPenaltyReporting':('securities','march-2026',['semt.%s.001.01'%x for x in ['025','026','027','040','044']]),
 'SecuritiesReferenceData':('securities','june-2021',['reda.%s.001.01'%x for x in ['006','007','008','009','010','012','013','029','030','033','034']]),
 'SettlementRestrictions':('securities','september-2025',['semt.%s.001.01'%x for x in ['028','029','030','031','032','033','034']]),
}
def slug(s): return re.sub(r'[^a-z0-9]+','-',re.sub(r'([a-z])([A-Z])',r'\1-\2',s).lower()).strip('-')
def area(domain): return 'shared' if domain=='shared' else 'domains/'+domain
def set_write_context(root,job):
 global _WRITE_CONTEXT
 if not re.fullmatch(r'job-\d{6,}',job):raise ValueError('Invalid job ID')
 _WRITE_CONTEXT={'root':Path(root).resolve(),'job':job,'run':datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')}

def write_bytes(path,data):
 path=Path(path)
 if path.exists() and path.read_bytes()==data:return False
 resolved=path.resolve()
 root=_WRITE_CONTEXT['root'] if _WRITE_CONTEXT else next((p for p in resolved.parents if (p/'AGENTS.md').exists()),None)
 if root:
  if not resolved.is_relative_to(root):raise ValueError('Output escapes configured repository')
  relative=resolved.relative_to(root)
  if relative.parts and relative.parts[0]=='raw-input':raise ValueError('Supplied raw inputs are read-only')
  if path.exists() and relative.parts[0] not in ('work',) and not relative.as_posix().startswith('tracking/history/'):
   old=path.read_bytes()
   job=_WRITE_CONTEXT['job'] if _WRITE_CONTEXT else 'unassigned'
   run=_WRITE_CONTEXT['run'] if _WRITE_CONTEXT else datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
   dest=root/'tracking/history'/job/run/(hashlib.sha256(old).hexdigest()[:12])/relative
   dest.parent.mkdir(parents=True,exist_ok=True)
   if not dest.exists():dest.write_bytes(old)
 path.parent.mkdir(parents=True,exist_ok=True)
 handle,temporary=tempfile.mkstemp(prefix='.'+path.name+'.',suffix='.tmp',dir=path.parent)
 try:
  with os.fdopen(handle,'wb') as f:f.write(data);f.flush();os.fsync(f.fileno())
  os.replace(temporary,path)
 finally:
  if os.path.exists(temporary):os.unlink(temporary)
 return True

def dump(path,obj):
 return write_bytes(path,(json.dumps(obj,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))

def put(path,text):
 return write_bytes(path,text.encode('utf-8'))

def rel(from_file,to):return quote(os.path.relpath(to,Path(from_file).parent).replace('\\','/'),safe='/#:.')
def link(from_file,to,label):return '['+str(label)+']('+rel(from_file,to)+')'
def escape_table_markup(s):
 # Preserve authored links, code spans and navigation anchors, but display XML tags literally.
 protected=[]
 def hold(m):protected.append(m.group());return '\x00'+str(len(protected)-1)+'\x00'
 s=re.sub(r'`[^`\n]*`|\]\(<[^>]*>\)|<br\s*/?>|<a id="issue-\d+"></a>',hold,s)
 s=s.replace('<','&lt;').replace('>','&gt;')
 return re.sub(r'\x00(\d+)\x00',lambda m:protected[int(m.group(1))],s)
def esc(s): return escape_table_markup(str(s if s is not None else '')).replace('|','\\|').replace('\r','').replace('\n','<br>')
def table(headers,rows):return '| '+' | '.join(map(esc,headers))+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+''.join('| '+' | '.join(map(esc,r))+' |\n' for r in rows)+'\n'
def front(meta): return '---\n'+''.join(k+': '+json.dumps(v,ensure_ascii=False)+'\n' for k,v in meta.items())+'---\n\n'
def metadata(path):
 text=path.read_text(encoding='utf-8-sig')
 if not text.startswith('---\n'):return {},text
 end=text.find('\n---',4)
 if end<0:return {},text
 meta={}
 for line in text[4:end].splitlines():
  if ':' not in line:continue
  k,v=line.split(':',1)
  try: meta[k]=json.loads(v.strip())
  except ValueError:meta[k]=v.strip().strip('"\'')
 return meta,text[end+4:]
def read_source(root,s):
 errors=[]
 for o in sorted(s.get('occurrences',[]),key=lambda x:x.get('availability','current')!='current'):
  try:
   p=(Path(root)/o['path']).resolve()
   if not p.is_relative_to(Path(root).resolve()):raise ValueError('Source escapes repository')
   if o.get('archive_member'):
    if o.get('archive_sha256') and hashlib.sha256(p.read_bytes()).hexdigest()!=o['archive_sha256']:raise ValueError('Parent archive changed')
    with zipfile.ZipFile(p) as z:data=z.read(o['archive_member'])
   else:data=p.read_bytes()
   expected=s.get('sha256') or o.get('sha256')
   if expected and hashlib.sha256(data).hexdigest()!=expected:raise ValueError('Content checksum changed')
   return data
  except Exception as exc:errors.append({'path':o['path'],'member':o.get('archive_member'),'error':str(exc)})
 raise ValueError('No verified occurrence: '+json.dumps(errors,ensure_ascii=False))
def sources(root):
 path=root/'catalog/sources.json'
 return json.loads(path.read_text(encoding='utf-8'))['sources'] if path.exists() else []

def source_link(root,page,s):
 occurrences=s.get('occurrences',[])
 if not occurrences:return s.get('source_id','Unknown source')+' (original unavailable)'
 o=next((o for o in occurrences if o.get('availability','current')=='current'),occurrences[0])
 suffix=((' archive member '+chr(96)+o['archive_member']+chr(96)) if o.get('archive_member') else '')
 if o.get('availability','current')!='current':return s['source_id']+'; historical '+o['path']+suffix+' (original unavailable at this occurrence)'
 return link(page,root/o['path'],s['source_id'])+suffix

def canonical_schemas(root,ss=None):
 from refresh import canonical_schemas as resolve
 return resolve(Path(root),ss)

def inventory(root,selection=None,job=None):
 if selection is None or job is None:raise ValueError('Inventory requires an explicit selection and job; use refresh.scan for discovery')
 import refresh
 return refresh.register(root,selection,job)


def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);sub=p.add_subparsers(dest='command',required=True)
 inv=sub.add_parser('inventory');inv.add_argument('--selection',type=Path);inv.add_argument('--job')
 scan_p=sub.add_parser('scan');scan_p.add_argument('--path',action='append');scan_p.add_argument('--limit',type=int,default=20)
 impact_p=sub.add_parser('impact');ig=impact_p.add_mutually_exclusive_group(required=True);ig.add_argument('--message');ig.add_argument('--set',dest='set_slug')
 impact_p.add_argument('--edition');impact_p.add_argument('--scan',type=Path);impact_p.add_argument('--routing',type=Path)
 reb=sub.add_parser('rebuild');reb.add_argument('--selection',type=Path);reb.add_argument('--job')
 val=sub.add_parser('validate');val.add_argument('--checksums',action='store_true');val.add_argument('--selection',type=Path);val.add_argument('--job')
 finish=sub.add_parser('checkpoint-refresh');finish.add_argument('--selection',type=Path,required=True);finish.add_argument('--job',required=True);finish.add_argument('--next',required=True);finish.add_argument('--status',choices=['in-progress','needs-review','blocked'],default='needs-review')
 list_p=sub.add_parser('list');list_p.add_argument('--kind');list_p.add_argument('--limit',type=int,default=10)
 message_p=sub.add_parser('message');message_p.add_argument('identifier');message_p.add_argument('--limit',type=int,default=10)
 roles_p=sub.add_parser('roles');roles_p.add_argument('identifier');roles_p.add_argument('--limit',type=int,default=10)
 search_p=sub.add_parser('search');search_p.add_argument('query');search_p.add_argument('--kind');search_p.add_argument('--limit',type=int,default=10)
 args=p.parse_args();root=args.root.resolve()
 import refresh
 selection=refresh.read_json(args.selection) if getattr(args,'selection',None) else None
 job=getattr(args,'job',None) or (selection or {}).get('job_id')
 if job:set_write_context(root,job)
 if args.command=='scan':out=refresh.bounded(refresh.scan(root,args.path),args.limit)
 elif args.command=='impact':
  out=refresh.impact(root,args.message,args.set_slug,args.edition,refresh.read_json(args.scan) if args.scan else None,refresh.read_json(args.routing) if args.routing else None)
 elif args.command=='inventory':
  if not selection or not job:raise ValueError('Inventory writes require --selection FILE --job JOB_ID; use scan for discovery')
  out=refresh.register(root,selection,job)
 elif args.command=='checkpoint-refresh':
  refresh.complete(root,selection,job,args.next,args.status);out={'job_id':job,'status':args.status}
 else:
  import catalog
  if args.command=='rebuild':
   if selection:
    refresh.check_selection(root,selection,True)
    if not job:raise ValueError('Scoped rebuild requires --job')
   catalog.rebuild(root,selection=selection);return
  elif args.command=='validate':
   if selection:out=refresh.validate_selection(root,selection,args.checksums,job)
   else:out=catalog.validate(root,args.checksums)
   if not out['pass']:print(json.dumps(out,ensure_ascii=False));raise SystemExit(1)
  elif args.command=='message':out=catalog.lookup(root,args.identifier,args.limit)
  elif args.command=='roles':out=catalog.roles(root,args.identifier,args.limit)
  else:out=catalog.query(root,args.kind,getattr(args,'query',None),args.limit)
 print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__':
 try:main()
 except (ValueError,FileNotFoundError) as exc:print(json.dumps({'error':str(exc)},ensure_ascii=False),file=sys.stderr);raise SystemExit(2)
