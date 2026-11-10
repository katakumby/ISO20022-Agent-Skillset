"""Prepare source-grounded Bank Transaction Code diagram reconstructions; no review inference."""
from pathlib import Path
from local_runtime import executable
import argparse,json,sys,re,subprocess,hashlib
from PIL import Image
from lxml import etree as ET
sys.path.insert(0,str(Path(__file__).resolve().parent)); import kb
from extract_workbooks import fm,write,relative,esc
ap=argparse.ArgumentParser();ap.add_argument('--root',default=str(Path(__file__).resolve().parents[1]));a=ap.parse_args();ROOT=Path(a.root).resolve();SID='src-000003';DATE='2026-11-09';W=ROOT/'work/btc-diagrams';W.mkdir(parents=True,exist_ok=True);(W/'mmd').mkdir(exist_ok=True)
S=next(s for s in kb.sources(ROOT) if s['source_id']==SID)
DATA=json.loads((ROOT/'work/documents'/SID/'smartart.json').read_text('utf-8'))
PAGE={1:9,2:10,3:24,4:37,5:39,6:41,7:43,8:45,9:56,10:58,11:59,12:60,13:61}
TITLES={1:'Proprietary component example',2:'Bank Transaction Code domains',3:'Payments families',4:'Cash Management families',5:'Derivatives families',6:'Loans, Deposits and Syndications families',7:'Trade Services families',8:'Securities families',9:'Account Management families',10:'Foreign Exchange families',11:'Precious Metal families',12:'Commodities families',13:'Exceptional Securities sub-families: Custody Collection'}
CROPS={2:(980,170,1250,410),3:(100,140,1300,690),4:(490,395,610,795),5:(485,275,610,825),6:(575,170,845,865),7:(450,185,565,400),8:(620,185,715,585),9:(595,185,710,610),10:(535,185,650,510),11:(610,250,715,755),12:(545,185,660,460),13:(535,255,635,560),14:(535,185,645,465),15:(535,185,650,465),16:(525,185,645,715)}
models=[]
for g in sorted(DATA['graphs'],key=lambda g:int(re.search(r'data(\d+)',g['data_part']).group(1))):
 n=int(re.search(r'data(\d+)',g['data_part']).group(1));fid='fig-%04d'%(n+3);pts=[p for p in g['points'] if p['text'] and p['attributes'].get('type','node')=='node']; ids={p['attributes']['modelId']:'N'+str(i+1) for i,p in enumerate(pts)}; names={p['attributes']['modelId']:p['text'] for p in pts}; edges=[c for c in g['connections'] if c['attributes']['srcId'] in ids and c['attributes']['destId'] in ids and c['attributes'].get('type','parOf')=='parOf']; edges.sort(key=lambda c:(list(ids).index(c['attributes']['srcId']),int(c['attributes'].get('srcOrd','0'))))
 code='flowchart LR\n';nodes=[]
 for p in pts:
  id=ids[p['attributes']['modelId']];label=p['text'].strip();code+=f'  {id}["{label.replace(chr(34),"&quot;").replace(chr(10),"<br/>")}"]\n';nodes.append({'id':id,'source_model_id':p['attributes']['modelId'],'label':label,'source_path':p['xml_path']})
 for e in edges: code+=f'  {ids[e["attributes"]["srcId"]]} --- {ids[e["attributes"]["destId"]]}\n'
 code+='  classDef generic fill:#dce8ee,stroke:#1b637f,color:#444,font-style:italic;\n'
 for no in nodes:
  if no['label'].lower().startswith('generic family'):code+='  class '+no['id']+' generic;\n'
 limits=['The source uses connector lines without arrowheads. Mermaid lines represent the displayed taxonomy/structure, not message directions or a time sequence. Layout and box colors differ to keep labels readable; generic-family emphasis is preserved.']
 if n in [8,13]: limits.append('The source SmartArt node includes a separate trailing C under Custody Collection. It is retained verbatim; the source supplies no explanation of this character.')
 if n==3:limits.append('The figure is an overview, not an exhaustive current code list: it does not separately display the four generic families and does not add entries from later detailed tables. The original alternating left/right arrangement is represented as sibling branches.')
 if n in [5,9,11,12]:limits.append('Some labels extend beyond the small source boxes in Word rendering. All source SmartArt text is preserved, and the original full page is retained.')
 occurrence=next(o for o in DATA['occurrences'] if o['relationships']['dm']['member']==g['data_part'])
 models.append({'figure_id':fid,'title':TITLES[n],'file_page':PAGE[n],'nodes':nodes,'edges':[{'from':ids[e['attributes']['srcId']],'to':ids[e['attributes']['destId']],'source_path':e['xml_path'],'source_order':e['attributes'].get('srcOrd')} for e in edges],'smartart_data_part':g['data_part'],'smartart_evidence':g['output'],'source_occurrence':occurrence,'mermaid':code,'limitations':limits,'review_status':'needs-review'})
models.insert(0,{'figure_id':'fig-0002','title':'Domain, family and sub-family hierarchy','file_page':6,'source_occurrence':{'source_locator':'T1 row 1 cell 2 composite; /w:document/w:body/w:tbl[1]'},'mermaid':'flowchart TB\n  D["Domain"] --- F["Family"]\n  F --- S["SubFamily"]\n','nodes':[{'id':'D','label':'Domain'},{'id':'F','label':'Family'},{'id':'S','label':'SubFamily'}],'edges':[{'from':'D','to':'F'},{'from':'F','to':'S'}],'limitations':['The original is a three-level pyramid assembled from fourteen EMF pieces and shape text. Word renders its front faces dark; the visible level labels agree with the adjacent T1 definitions. The diagram preserves the hierarchy in readable boxes and does not reproduce the three-dimensional shading. AlternateContent fallback also contains Product family/Product sub-family labels; the complete original parts remain retained.'],'review_status':'needs-review'})
models.insert(1,{'figure_id':'fig-0003','title':'Bank Transaction Code component structure','file_page':8,'source_occurrence':{'source_locator':'P116; image15.png; source table T2 on rendered page 7 clarifies multiplicities/type names'},'mermaid':'''classDiagram
 direction LR
 class BkTxCd["BkTxCd : BankTransactionCodeStructure4"]
 class Domn["Domn : BankTransactionCodeStructure5"] {
  ExternalBankTransactionDomain1Code Cd
 }
 class Fmly["Fmly : BankTransactionCodeStructure6"] {
  ExternalBankTransactionFamily1Code Cd
  ExternalBankTransactionSubFamily1Code SubFmlyCd
 }
 class Prtry["Prtry : ProprietaryBankTransactionCodeStructure1"] {
  Max35Text Cd
  Max35Text Issr
 }
 BkTxCd "1" *-- "0..1" Domn
 BkTxCd "1" *-- "0..1" Prtry
 Domn "1" *-- "1" Fmly
 note for Domn "Cd required; length 1..4"
 note for Fmly "Cd and SubFmlyCd required; each length 1..4"
 note for Prtry "Cd required; Issr optional; each length 1..35"
''','nodes':[{'id':k,'label':v} for k,v in [('BkTxCd','BankTransactionCodeStructure4'),('Domn','BankTransactionCodeStructure5'),('Fmly','BankTransactionCodeStructure6'),('Prtry','ProprietaryBankTransactionCodeStructure1')]],'edges':[{'from':'BkTxCd','to':'Domn'},{'from':'BkTxCd','to':'Prtry'},{'from':'Domn','to':'Fmly'}],'limitations':['Source XML-structure boxes and sequences are reconstructed with native class notation: composition means displayed structural containment, not business ownership. Sequence order is Domn then Prtry, domain Cd then Fmly, family Cd then SubFmlyCd, proprietary Cd then Issr. Source type labels truncated in the image are completed only from adjacent T2. The source is a publication illustration, not an independently supplied schema definition. The business requirement that Domain or Proprietary be present is separate from the displayed optional children.'],'review_status':'needs-review'})
exe=executable('pdftoppm','ISO20022_PDFTOPPM');asset=ROOT/'shared/assets'/SID/'figure-crops';asset.mkdir(parents=True,exist_ok=True)
for m in models:
 fid=m['figure_id'];(W/'mmd'/(fid+'.mmd')).write_text(m['mermaid'],'utf-8');pg=m['file_page'];temp=W/f'page-{pg:02}-300dpi'
 if not temp.with_suffix('.png').exists():subprocess.run([exe,'-r','300','-f',str(pg),'-l',str(pg),'-singlefile','-png',str(ROOT/'work/docx-render'/SID/'document.pdf'),str(temp)],check=True)
 box=CROPS[int(fid[-4:])];im=Image.open(temp.with_suffix('.png'));crop=im.crop(tuple(round(c*2.5) for c in box));crop.save(asset/(fid+'.png'));m['crop']=(asset/(fid+'.png')).relative_to(ROOT).as_posix();m['crop_bbox_120dpi']=box
(W/'models.json').write_text(json.dumps(models,ensure_ascii=False,indent=2),'utf-8');print(json.dumps({'diagrams':len(models),'nodes':sum(len(m['nodes']) for m in models),'edges':sum(len(m['edges']) for m in models),'review_status':'needs-review'}))
