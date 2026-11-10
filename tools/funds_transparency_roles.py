"""Maintain only directly drawn source95 transparency role contexts."""
from pathlib import Path
import kb
def ensure(root):
 sid='src-000095';base=root/'domains/securities/reference/message-sets/investment-funds/2025-2026'
 definitions={
 'sub-level-account-owner':('Sub-Level Account Owner','The left-hand account-owner role in the source transparency reporting chain. It sends a SecuritiesBalanceTransparencyReport to the Omnibus Account Owner and receives a SecuritiesBalanceTransparencyReportStatusAdvice from that party.','omnibus-account-owner'),
 'omnibus-account-owner':('Omnibus Account Owner','The middle role in the source transparency reporting chain. It receives the sub-level owner’s report and returns status, then sends a report to the Omnibus Account Servicer and receives status. P941 permits a receiver to enrich data before forwarding the aggregated report.','omnibus-account-servicer'),
 'omnibus-account-servicer':('Omnibus Account Servicer','The right-hand servicing role in the source transparency reporting chain. It receives a SecuritiesBalanceTransparencyReport from the Omnibus Account Owner and responds with SecuritiesBalanceTransparencyReportStatusAdvice.','omnibus-account-owner')}
 for slug,(label,definition,other) in definitions.items():
  pid='participant-'+sid+'-'+slug;page=root/'shared/reference/participants'/(pid+'.md')
  if page.exists():continue
  loc={'source_id':sid,'locator':'BusinessTransactions / Statements / Transparency of Holdings Statement; P941–P943; fig-0138','xml_path':'/w:document/w:body/w:p[943]'}
  meta={'template':False,'document_kind':'participant','review_status':'needs-review','participant_id':pid,'title':label,'domain':'securities','source_ids':[sid],'source_editions':['March 2025'],'source_labels':[label],'aliases':[],'role_type':'functional participant role; scoped custody-chain level','message_sets':['investment-funds'],'source_locations':[loc],'identifier_schemes':[],'limitations':['This definition is scoped to the source diagram; it is not an institutional identity or a universal account-role equivalence.','P941 describes the initial sender as an account servicer such as a custodian; the figure labels that endpoint Sub-Level Account Owner. Both contextual labels remain explicit.'],'updated':'2026-11-09'}
  body=kb.front(meta)+'# '+label+'\n\n## Definition and responsibilities\n\n'+definition+'\n\nEvidence: src-000095, P941–P943, '+kb.link(page,base/'documents/src-000095/diagrams/fig-0138.md','source figure 138')+'.\n\n## Relationships and business context\n\nInvestment Funds transparency-of-holdings reporting; related '+kb.link(page,page.parent/('participant-'+sid+'-'+other+'.md'),'adjacent contextual role')+'. A participant can occupy different owner/servicer roles in different account relationships. No institution is permanently assigned to this role.\n\n## Identifiers and unresolved distinctions\n\nNo identifier scheme is specified by P941–P943 for this functional role. No aliases or cross-source equivalence are asserted. The narrative and picture use different contextual labels for the first endpoint; see the flow for both.\n'
  kb.put(page,body)
