"""Publish manually inspected FITRR source sequence transcriptions and flow evidence.

This is a focused source-specific curation helper. A render or visual review is
never inferred from successful publication; record inspection separately.
"""
import argparse, hashlib, json, re
from pathlib import Path
import kb

SID='src-000320'; DATE='2026-11-09'
PREFIX='FinancialInstrumentReporting'
STATUS=PREFIX+'StatusAdvice'
REF=PREFIX+'ReferenceDataReport'; NON=PREFIX+'NonWorkingDayReport'
TRANS=PREFIX+'EquityTransparencyDataReport OR '+PREFIX+'NonEquityTransparencyDataReport'
TRADE=PREFIX+'EquityTradingActivityReport OR '+PREFIX+'NonEquityTradingActivityReport'
RESULT=PREFIX+'EquityTradingActivityResult OR '+PREFIX+'NonEquityTradingActivityResult'
VOL=PREFIX+'TradingVolumeCapDataReport'
PEOPLE={'RE':('Reporting Entity','reporting-entity'),'CA':('Competent Authority','competent-authority'),'SA':('Supervisory Authority','supervisory-authority'),'RCA':('Relevant Competent Authority','relevant-ca'),'PUB':('Public','public'),'EXT':('3rd Party Systems','third-party-systems'),'BOTH':('Reporting Entity / Competent Authority',None)}

# figure: title, existing flow heading paragraph, narrative paragraphs,
# source business-process table, literal source report label, family evidence.
DATA={
17:('Reference data — direct reporting',175,[176],13,REF,['auth.017','auth.031']),
18:('Reference data — proxy reporting',178,[179,180,181],13,REF,['auth.017','auth.031']),
19:('Reference data — indirect reporting',183,[184],13,REF,['auth.017','auth.031']),
20:('Non-working days — direct reporting',188,[187,189],15,NON,['auth.039','auth.031']),
21:('Non-working days — proxy reporting',191,[192],15,NON,['auth.039','auth.031']),
22:('Non-working days — indirect reporting',194,[195,196],15,NON,['auth.039','auth.031']),
23:('Reference data distribution',198,[199],14,None,['auth.017','auth.036','auth.043','auth.042','auth.039','auth.047','auth.048','auth.050','auth.049']),
24:('Incomplete reference data — direct reminder',203,[202,204],13,None,['auth.031']),
25:('Incomplete reference data — indirect reminder',206,[207],13,None,['auth.031']),
26:('Transparency data — direct reporting',211,[210,212],16,TRANS,['auth.032','auth.033','auth.031']),
27:('Transparency data — proxy reporting',214,[210,215],16,TRANS,['auth.032','auth.033','auth.031']),
28:('Transparency data — indirect reporting',217,[210,218,219],16,TRANS,['auth.032','auth.033','auth.031']),
29:('Trading activity — direct reporting',223,[222,224],17,TRADE,['auth.040','auth.041','auth.031']),
30:('Trading activity — proxy reporting',226,[222,227],17,TRADE,['auth.040','auth.041','auth.031']),
31:('Trading activity — indirect reporting',229,[222,230],17,TRADE,['auth.040','auth.041','auth.031']),
32:('Trading activity results — authority reporting',234,[233,235],18,RESULT,['auth.044','auth.045','auth.031']),
33:('Trading volume cap — direct reporting',238,[239],19,VOL,['auth.035','auth.031']),
34:('Trading volume cap — proxy reporting',241,[242],19,VOL,['auth.035','auth.031']),
35:('Trading volume cap — indirect reporting',244,[245],19,VOL,['auth.035','auth.031']),
36:('Transaction reporting and authority exchange',248,[249],20,None,['auth.016']),
}

def sequence(num,report):
    events=[]; notes=[]
    def send(a,b,label,arrow='->>'):events.append(('message',a,b,label,arrow))
    def frame(kind,label=''):events.append((kind,label))
    direct={17,20,26,29,32,33};proxy={18,21,27,30,34};indirect={19,22,28,31,35}
    if num in direct:
        sender='BOTH' if num==20 else 'CA' if num==32 else 'RE';actors=[sender,'SA'];send(sender,'SA',report);send('SA',sender,STATUS)
    elif num in proxy:
        actors=['RE','CA','SA'];send('RE','CA',report,'-)' if num==34 else '->>')
        success='Validation Success' if num==18 else 'Validation Successful'
        failure='Validation Failures' if num==21 else 'Validation Failure'
        frame('alt','Competent Authority Validation Checks (Schema; Filename; Reporting Entity) — '+success)
        send('CA','SA',report);send('SA','CA',STATUS);send('CA','RE',STATUS)
        frame('else',failure);send('CA','RE',STATUS);frame('end')
        if num==34:notes.append('The first source arrow has an open head, unlike the filled heads on later arrows. Its distinct glyph is retained; no transport or timing semantics is inferred.')
    elif num in indirect:
        actors=['RE','CA','SA'];frame('loop','Capture all Relevant Messages');send('RE','CA',report)
        frame('alt','Message Received Correctly — All data is correct');send('CA','RE',STATUS);send('CA','SA',report)
        frame('else','Some data errors');send('CA','RE',STATUS)
        condition='Dates with no Errors' if num==22 else 'Instrument with no Errors' if num==35 else 'Instruments with no Errors'
        frame('alt',condition);send('CA','SA',report);frame('end');frame('end');frame('end')
        frame('alt','Message Received Correctly — All data is correct');send('SA','CA',STATUS)
        frame('else','Some data errors');send('SA','CA',STATUS);send('CA','RE',STATUS);frame('end')
        notes.append('The source loop/first alternative covers the Reporting Entity and Competent Authority lifelines while report arrows and the inner alternative cross that frame boundary to the Supervisory Authority. Mermaid expands these frames to the participating lifelines. Conditions, all arrows, order and the crossing-frame feature are retained in text; frame geometry is not identical.')
    elif num==23:
        actors=['PUB','RE','CA','SA','EXT'];send('SA','EXT','Request Data (Out of Scope)','--)');send('EXT','SA','Download Data (Out of Scope)','--)')
        for suffix in ['ReferenceDataReport','ReferenceDataDeltaReport','ReferenceDataIndexReport','InvalidReferenceDataReport','ReferenceDataIndexReport']:send('SA','CA',PREFIX+suffix)
        frame('rect','rgb(248, 245, 235)');frame('note','over CA,SA: Source fragment: consider Publish Weekly / Monthly')
        for suffix in ['NonWorkingDayReport','CountryCodeReport','CurrencyCodeReport','InstrumentClassificationReport','MarketIdentificationCodeReport']:send('SA','CA',PREFIX+suffix)
        frame('end');send('SA','PUB',REF);send('SA','PUB',PREFIX+'ReferenceDataDeltaReport')
        notes.extend(['The source consider operator has no native Mermaid sequence equivalent. A shaded group plus an explicit note retains the exact operator and label; it is not recast as opt or a mandatory publication schedule.','ReferenceDataIndexReport occurs twice from SA to CA and both arrows are retained. The two final arrows go to Public (full report, then delta report). The Reporting Entity lifeline is present but has no connected arrow in this picture.','Request Data and Download Data are explicitly out of scope. No ISO message identifier is assigned to those arrows.'])
    elif num in (24,25):
        actors=['RE','SA'] if num==24 else ['RE','CA','SA']
        if num==24:send('SA','RE',STATUS)
        else:send('SA','CA',STATUS);send('CA','RE',STATUS)
    else:
        actors=['RE','CA','RCA'];send('RE','CA','TransactionReportingMessage');send('CA','RE','TransactionReportingMessagesStatusAdvice');send('CA','RCA','TransactionReportingMessage');send('RCA','CA','TransactionReportingMessagesStatusAdvice')
        notes.append('TransactionReportingMessage and TransactionReportingMessagesStatusAdvice are literal picture labels. T7 identifies the transaction-reporting family auth.016; the generic status label is not silently equated with auth.031.')
    code='sequenceDiagram\n'+'\n'.join('  actor '+p+' as '+PEOPLE[p][0] for p in actors)+'\n';rows=[];stack=[]
    for e in events:
        if e[0]=='message':
            _,a,b,label,arrow=e;code+='  '+a+arrow+b+': '+label.replace(' OR ','<br/>OR<br/>')+'\n';rows.append([len(rows)+1,PEOPLE[a][0],PEOPLE[b][0],label,' / '.join(stack) or 'Outside conditional frame'])
        elif e[0]=='note':code+='  Note '+e[1]+'\n'
        elif e[0]=='end':code+='  end\n';stack.pop()
        elif e[0]=='else':code+='  else '+e[1]+'\n';stack[-1]=e[1]
        else:code+='  '+e[0]+' '+e[1].replace(';','#59;')+'\n';stack.append(e[1])
    return actors,events,code,rows,notes

def main(root):
    source=next(s for s in kb.sources(root) if s['source_id']==SID);base=root/source['set_path'];out=base/'diagrams/fitrr-sequences';flows=base/'flows'
    d=json.loads((root/'work/documents'/SID/'records.json').read_text(encoding='utf-8'));pars={int(x['paragraph_id'][1:]):x for x in d['paragraphs']};tables={int(x['source_table_id'][1:]):x for x in d['tables']}
    inventory=json.loads((root/'work/documents'/SID/'media-review-inventory.json').read_text(encoding='utf-8'));media={int(o['figure_id'][4:]):(m,o) for m in inventory['media'] for o in m['occurrences']}
    msg=json.loads((root/'catalog/messages.json').read_text(encoding='utf-8'))['records'];byfam={}
    for m in msg:
        if 'fitrr' in m.get('message_sets',[]):byfam.setdefault(m['message_family'],[]).append(m)
    participant_dir=root/'shared/reference/participants'
    def part(slug):return participant_dir/(f'participant-{SID}-{slug}.md')
    def plink(page,role):
        if role=='BOTH':return kb.link(page,part('reporting-entity'),'Reporting Entity')+' / '+kb.link(page,part('competent-authority'),'Competent Authority')
        return kb.link(page,part(PEOPLE[role][1]),PEOPLE[role][0])
    # These are source-scoped diagram/narrative roles; no institutional aliases.
    for slug,title,definition,nums in [('public','Public','Recipients of the published instrument reference data, including investment firms, reporting entities and academics in the distribution narrative. The diagram keeps this audience separate from its Reporting Entity lifeline.',[199,200]),('third-party-systems','3rd Party Systems','External systems from which the Supervisory Authority requests and downloads additional data in the distribution picture. Both exchanges are explicitly outside this message-set scope.',[199,200])]:
        page=part(slug);meta={'template':False,'document_kind':'participant','review_status':'needs-review','participant_id':page.stem,'title':title,'domain':'securities','domains':['securities'],'message_sets':['fitrr'],'source_ids':[SID],'source_editions':['July 2025'],'role_kind':'functional participant role','source_labels':[title],'aliases':[],'source_locations':[{'source_id':SID,'paragraph_id':'P'+str(n),'xml_path':pars[n]['xml_path'],'heading_path':pars[n]['heading_path']} for n in nums],'limitations':['Definition is scoped to the distribution picture and narrative; no general institutional equivalence or identifier scheme is asserted.']}
        kb.put(page,kb.front(meta)+'# '+title+'\n\n'+definition+'\n\n## Responsibilities and relationships\n\n'+('Receives full and delta reference-data reports from the Supervisory Authority. No outgoing message is drawn.' if slug=='public' else 'Receives an out-of-scope data request from the Supervisory Authority and returns an out-of-scope download.')+'\n\n## Provenance and navigation\n\n'+kb.source_link(root,page,source)+'; P199–P200, BusinessTransactions / Reference Data Distribution BusinessTransaction.\n\n'+kb.link(page,out/'fig-0023.md','Distribution diagram')+'\n\nIdentifier schemes are not specified for this role in the cited passage.\n')
    outputs=[];participant_usage={};message_usage={}
    for number,(title,heading,nums,tn,report,families) in DATA.items():
        candidates=list(flows.glob(f'flow-{SID}-p{heading}-*.md'));assert len(candidates)==1,(heading,candidates)
        flow=candidates[0];fm,fb=kb.metadata(flow);page=out/f'fig-{number:04d}.md';mmd=page.with_suffix('.mmd');item,occ=media[number]
        actors,events,code,rows,notes=sequence(number,report)
        pids=sorted({f'participant-{SID}-'+PEOPLE[a][1] for a in actors if a!='BOTH'}|({f'participant-{SID}-reporting-entity',f'participant-{SID}-competent-authority'} if 'BOTH' in actors else set()))
        midrecords=[m for f in families for m in byfam.get(f,[])];mids=[m['message_id'] for m in midrecords]
        if number==32:notes.append('T18 names Supervisory Authority in its Role row, but the definition, P233–P235 and this figure assign submission of non-delegated calculation results to the Competent Authority. Both statements are retained; issue-000032.')
        if number in (33,34,35):notes.append('T6 uses FinancialInstrumentsTradingVolumeCapDataReport while the picture uses FinancialInstrumentReportingTradingVolumeCapDataReport. The contextual family link auth.035 comes from T6; the source picture label is retained literally.')
        meta={'template':False,'document_kind':'diagram','review_status':'needs-review','manual_curated':True,'diagram_id':f'fig-{number:04d}','title':title,'domain':'securities','source_ids':[SID],'source_editions':['July 2025'],'message_sets':['fitrr'],'message_ids':mids,'message_families':families,'participant_ids':pids,'flow_ids':[fm['flow_id']],'content_origin':'source-reconstruction','diagram_kind':'sequenceDiagram','original_asset':item['original'],'source_locations':[{'source_id':SID,'locator':occ['source_locator'],'heading_path':occ['heading_path'],'xml_path':occ['xml_path'],'figure_id':occ['figure_id']}],'render_status':'not-run','visual_review':'not-run','limitations':notes,'updated':DATE}
        body='# '+title+'\n\n'+kb.source_link(root,page,source)+'; '+occ['source_locator']+'; '+' / '.join(occ['heading_path'])+'.\n\n'+kb.link(page,root/item['original'],'Original image')+' · '+kb.link(page,root/item['preview'],'Readable original preview')+' · '+kb.link(page,flow,'Flow, conditions and narrative responsibilities')+'\n\n## Source reconstruction\n\n```mermaid\n'+code+'```\n\n## Actors and relationships\n\n'+'\n'.join('- '+plink(page,a) for a in actors)+'\n\n'+kb.table(['Order','Sender','Receiver','Literal source message / exchange','Source condition or fragment'],rows)+'\nThe source activation bars are execution markers without specified duration. Vertical message ordering is retained; synchronous versus asynchronous transport behavior is not inferred. OR-labelled message alternatives remain alternatives, not two required transmissions.\n\n'
        body+='## Qualifications\n\n'+('\n'.join('- '+x for x in notes) if notes else 'No source discrepancy was identified in this picture transcription. Wider source and business review remains separate.')+'\n\n## Rendering and visual review\n\nPending parse/render and direct visual comparison. Publication alone does not establish a review pass.\n'
        kb.put(page,kb.front(meta)+body);kb.put(mmd,code)
        # Promote the existing source segment, preserving its literal narrative.
        fm.update(document_kind='business-flow',title=title,participants=pids,participant_ids=pids,message_ids=mids,message_families=families,manual_curated=True,related_diagrams=[page.relative_to(root).as_posix()],limitations=notes+['Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.','The described flow is scoped to this publication; it is not advice on current regulation.'])
        fbody='# '+title+'\n\n'+kb.source_link(root,flow,source)+'; '+' / '.join(pars[heading]['heading_path'])+'.\n\n## Purpose, trigger, preconditions and outcomes\n\n'
        for tnum in ([20,21] if number==36 else [tn]):
            t=tables[tnum];tp=base/f'documents/{SID}/tables/tbl-{tnum:04d}.md';fbody+='Source process definition '+kb.link(flow,tp,'T'+str(tnum))+' (the overall process conditions also apply to its reporting variant):\n\n'+kb.table(t['rows'][0],t['rows'][1:])+'\n'
        if number in (24,25):fbody+='Reminder-specific trigger: the SA checks venue submissions and expected records and identifies incomplete or missing reference data (P202). The recipient must correct the situation in the next reporting window; the general process conditions above do not replace that reminder trigger.\n\n'
        fbody+='## Participants and responsibilities\n\n'+'\n'.join('- '+plink(flow,a) for a in actors)+'\n\n'+('The RE initiates its data submission; the CA or SA performs the checks assigned by the chosen reporting model. The ordered exchanges and source narrative below retain the actual responsible party.\n\n' if number not in (23,24,25,32,36) else 'Initiation and responsibility follow the explicit message directions and narrative below; a participant appearing on a lifeline is not automatically a sender.\n\n')
        fbody+='## Ordered exchanges and decision points\n\n'+kb.table(['Order','Sender','Receiver','Literal source message / exchange','Source condition or fragment'],rows)+'\n'+kb.link(flow,page,'Reconstructed sequence and retained original')+'\n\n## Source narrative and additional participants\n\n'
        for n in nums:
            if pars[n]['text'].strip():fbody+='**P'+str(n)+'** '+pars[n]['text'].strip()+'\n\n'
        fbody+='## Supplied message definitions\n\n'+('\n'.join('- '+kb.link(flow,root/m['path'],m['message_id']+' — '+m['message_name']) for m in midrecords) or 'No exact message mapping established.')+'\n\nFamily mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.\n\n## Alternative and exceptional paths\n\n'
        fbody+=('The CA returns a failure status instead of forwarding a failed message. Successful validation forwards the report to the SA and returns the SA status through the CA.\n\n' if number in (18,21,27,30,34) else 'The source conditions and narrative above define the applicable alternatives. Repeated arrows and all error branches are retained; no additional cancellation or reversal route is invented.\n\n')
        fbody+='## Limitations\n\n'+'\n'.join('- '+x for x in fm['limitations'])+'\n';kb.put(flow,kb.front(fm)+fbody)
        ep=root/occ['evidence_page'];em,eb=kb.metadata(ep);em.update(canonical_diagram=page.relative_to(root).as_posix(),disposition='canonical-reconstruction-created-needs-review');eb=re.sub(r'\n<!-- FITRR-SEQUENCE -->.*','',eb,flags=re.S);kb.put(ep,kb.front(em)+eb.strip()+'\n\n<!-- FITRR-SEQUENCE -->\n'+kb.link(ep,page,'Canonical sequence reconstruction and review evidence')+'\n')
        for pid in pids:participant_usage.setdefault(pid,[]).append((flow,title,fm['flow_id'],mids,page))
        for m in midrecords:message_usage.setdefault(m['message_id'],[]).append((flow,title,page))
        outputs.append({'figure_id':occ['figure_id'],'path':page.relative_to(root).as_posix(),'flow_path':flow.relative_to(root).as_posix(),'mermaid_sha256':hashlib.sha256(mmd.read_bytes()).hexdigest(),'original':item['original'],'original_sha256':item['original_sha256'],'source_preview':item['preview'],'message_count':len(rows),'limitations':notes})
    for pid,uses in participant_usage.items():
        p=participant_dir/(pid+'.md');pm,pb=kb.metadata(p);pm['flow_ids']=sorted(set(pm.get('flow_ids',[])+[x[2] for x in uses]));pm['message_ids']=sorted(set(pm.get('message_ids',[])+[m for x in uses for m in x[3]]));pb=re.sub(r'\n<!-- FITRR-SEQUENCES -->.*','',pb,flags=re.S);pb+='\n\n<!-- FITRR-SEQUENCES -->\n## Source-reviewed sequence participation\n\n'+ '\n'.join('- '+kb.link(p,x[0],x[1])+' · '+kb.link(p,x[4],'literal sender/receiver and conditions') for x in uses)+'\n';kb.put(p,kb.front(pm)+pb.strip()+'\n')
    for mid,uses in message_usage.items():
        p=root/'domains/securities/reference/messages'/mid/'mdr-evidence.md';pm,pb=kb.metadata(p);pb=re.sub(r'\n<!-- FITRR-SEQUENCES -->.*','',pb,flags=re.S);pb+='\n\n<!-- FITRR-SEQUENCES -->\n## Related FITRR business flows\n\n'+ '\n'.join('- '+kb.link(p,x[0],x[1])+' · '+kb.link(p,x[2],'source sequence') for x in uses)+'\n\nThese links use source-supported family context; exact-version applicability is separately documented in the message evidence.\n';kb.put(p,kb.front(pm)+pb.strip()+'\n')
    ip=out/'index.md';kb.put(ip,kb.front({'template':False,'document_kind':'diagram-index','review_status':'needs-review','domain':'securities','message_sets':['fitrr'],'source_ids':[SID],'source_editions':['July 2025']})+'# FITRR sequence diagrams\n\n'+kb.table(['Figure','Sequence','Flow'],[[r['figure_id'],kb.link(ip,root/r['path'],DATA[int(r['figure_id'][4:])][0]),kb.link(ip,root/r['flow_path'],'Conditions and responsibilities')] for r in outputs]))
    for nav in [base/'index.md',base/'participants.md']:
        nm,nb=kb.metadata(nav);nb=re.sub(r'\n<!-- FITRR-SEQUENCE-INDEX -->.*','',nb,flags=re.S);kb.put(nav,kb.front(nm)+nb.strip()+'\n\n<!-- FITRR-SEQUENCE-INDEX -->\n'+kb.link(nav,ip,'Curated FITRR sequences, reusable flows and participant links')+'\n')
    kb.dump(root/'work/fitrr-sequences.json',{'source_id':SID,'source_sha256':source['sha256'],'outputs':outputs});print(json.dumps({'diagrams':len(outputs),'flows':len(outputs),'participants_linked':len(participant_usage),'messages_linked':len(message_usage)}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();main(a.root.resolve())
