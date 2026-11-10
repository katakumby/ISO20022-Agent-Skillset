from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();sid='src-000362';s=next(x for x in kb.sources(root) if x['source_id']==sid);base=root/s['set_path'];main=base/'diagrams/curated/fig-0005.md';meta,body=kb.metadata(main)
pairs=[
('T2S Dedicated Cash Account Balance Query','T2S Dedicated Cash Account Balance query response','GetAccount','ReturnAccount'),
('T2S Dedicated Cash Account Posting Query','T2S Dedicated Cash Account Posting Query Response','GetTransaction','ReturnTransaction'),
('Immediate Liquidity Transfer Order List Query','Immediate Liquidity Transfer Order List Query Response','GetTransaction','ReturnTransaction'),
('Immediate Liquidity Transfer Order Detail Query','Immediate Liquidity Transfer Order Detail Query Response','GetTransaction','ReturnTransaction'),
('Outstanding AutoCollateralisation Credit Query','Outstanding Auto Collateralisation Credit query response','GetAccount','ReturnAccount'),
('T2S Overall Liquidity Query','T2S Overall Liquidity query response','GetAccount','ReturnAccount'),
('Cash Forecast Query','Cash Forecast query response','GetAccount','ReturnAccount'),
('Liquidity Information Query','Liquidity Information Query Response','GetAccount','ReturnAccount'),
('Limit Utilisation Journal Query','Limit Utilisation Journal Report','LimitUtilisationJournalQuery','LimitUtilisationJournalReport'),
('Limit Utilisation Query','Limit Utilisation Query Response','GetLimit','ReturnLimit'),
('Total collateral value per T2S Dedicated Cash Account query','Total collateral value per T2S Dedicated Cash Account query response','CollateralValue Query','CollateralValue Report'),
('Collateral Value per T2S Dedicated Cash Account query','Collateral Value per T2S Dedicated Cash Account query response','CollateralValue Query','CollateralValue Report'),
('Collateral value of a security query','Collateral Value of a Security query response','CollateralValue Query','CollateralValue Report'),
('Cash Account List Query','Cash Account List Query Response','AccountQueryList','AccountListReport')]
for part in [1,2]:
 p=main.with_name('fig-0005-cash-'+str(part)+'.md');code='flowchart LR\n Cash["Cash accounts — source common branch"]\n';rows=[]
 for i,(q,r,f,b) in enumerate(pairs):
  if (i<7)!=(part==1):continue
  code+=' Cash --> Q'+str(i)+'["'+q+'"]\n Q'+str(i)+' -->|'+f+'| R'+str(i)+'["'+r+'"]\n R'+str(i)+' -.->|'+b+'| Q'+str(i)+'\n';rows.append([i+1,q,f,r,b,'In scope (green)' if i==8 else 'Other context'])
 if part==2:code+=' classDef scope fill:#b1d39b,stroke:#739467\n class Q8,R8 scope\n'
 m=dict(meta);m.update(document_kind='diagram-detail',diagram_id=p.stem,title='Cash-query taxonomy detail '+str(part),parent_diagram='fig-0005',render_status='not-run',visual_review='not-run');m['message_ids']=[] if part==1 else ['camt.064.001.01','camt.065.001.01'];text='# '+m['title']+'\n\n'+kb.link(p,main,'Complete source context and query taxonomy')+'; source src-000362, P131, word/media/image5.jpeg; Word13. Each query node branches from the common cash-account category, sends a solid labelled link rightward and receives a dashed labelled link leftward. Only the source green journal pair belongs to the supplied camt.064/065 scope. No version or family is inferred for other pairs.\n\n```mermaid\n'+code+'```\n\n'+kb.table(['Source row','Query label','Forward link label','Response label','Return link label','Scope'],rows)+'\n';kb.put(p,kb.front(m)+text);kb.put(p.with_suffix('.mmd'),code)
body+='\n## Complete cash-query detail\n\n'+kb.link(main,main.with_name('fig-0005-cash-1.md'),'Pairs1–7')+'; '+kb.link(main,main.with_name('fig-0005-cash-2.md'),'Pairs8–14, including green limit-journal scope')+'. All14 common-branch arrows,28 query/response labels and28 exchange-link labels are retained.\n';kb.put(main,kb.front(meta)+body)
r=json.loads((root/'work/documents'/sid/'records.json').read_text(encoding='utf-8'))
for slug,title,nlo,nhi,qlo,qhi,rlo,rhi in [('business-report','Business report example',169,178,182,202,207,309),('operational-error','Operational error example',314,316,320,340,344,363)]:
 p=base/'examples'/(slug+'.md');m={'template':False,'document_kind':'source-example','manual_curated':True,'review_status':'needs-review','title':title,'domain':'securities','source_ids':[sid],'message_sets':[s['set_slug']],'message_ids':['camt.064.001.01','camt.065.001.01'],'source_locations':[{'source_id':sid,'locator':f'P{nlo}–P{rhi}; Business Examples; original payload excerpts'}],'flow_ids':['flow-src-000362-p137-pull-mode'],'limitations':['These are supplied illustrative examples. Payload fragments omit BAH and document namespace wrapper; not claimed as standalone schema-valid messages.']};text='# '+title+'\n\nSource '+kb.source_link(root,p,s)+'; P'+str(nlo)+'–P'+str(rhi)+'. P162 says the complete instances are embedded in BAH, while the shown excerpts contain only the business message.\n\n'
 for q in r['paragraphs']:
  n=int(q['paragraph_id'][1:])
  if nlo<=n<=nhi and q['text']:text+='**'+q['paragraph_id']+'** '+q['text']+'\n\n'
 for label,lo,hi,mid in [('Query',qlo,qhi,'camt.064.001.01'),('Report',rlo,rhi,'camt.065.001.01')]:
  payload='\n'.join(q['text'] for q in r['paragraphs'] if lo<=int(q['paragraph_id'][1:])<=hi);text+='## '+label+'\n\n'+kb.link(p,root/'domains/securities/reference/messages'/mid/'index.md',mid)+f'; P{lo}–P{hi}.\n\n```xml\n'+payload+'\n```\n\n'
 text+='The example values and identifier strings are preserved exactly, including source whitespace inside AnyBIC values where present. '+kb.link(p,next((base/'flows').glob('flow-src-000362-p137-*.md')),'Source pull flow')+'.\n';kb.put(p,kb.front(m)+text)
print('Two focused query detail views; two supplied scenarios with four payload excerpts')
