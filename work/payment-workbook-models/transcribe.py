"""Explicit transcription of eight visually inspected supplied workbook figures."""
from pathlib import Path
import json,collections
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
results=json.loads((ROOT/'work/workbook-results.json').read_text('utf-8'))
models=[]

def model(sid,fid,title,names,edges,meaning,unprinted='',datatypes='',no_stereotype='',notes=None):
    sid='src-'+sid.zfill(6);fid='fig-'+str(fid).zfill(4)
    no=set(unprinted.split());dt=set(datatypes.split());ns=set(no_stereotype.split())
    nodes=[{'id':n,'name':n,'package':('(package not printed)' if n in no else 'DICO_BusinessComponentsDataTypes' if n in dt else 'DICO_BusinessComponents'),'stereotype':None if n in ns else 'BusinessComponent'} for n in names.split()]
    ee=[]
    for line in edges.strip().splitlines():
        a,kind,b,*label=line.strip().split('|');ee.append({'a':a,'b':b,'kind':'--|>' if kind=='inherit' else '--','label':label[0] if label else ''})
    ids={n['id'] for n in nodes}
    assert all(e['a'] in ids and e['b'] in ids for e in ee)
    source=next(d for r in results if r['source_id']==sid for d in r['diagrams'] if d['figure_id']==fid)
    m={'id':fid,'source_id':sid,'title':title,'nodes':nodes,'edges':ee,'meaning':meaning,'limitations':[],'source':source,'render_prefix':sid+'-'+fid,'review_status':'needs-review'}
    code=['classDiagram','direction LR']
    groups=collections.defaultdict(list)
    for n in nodes:groups[n['package']].append(n)
    for pkg,nn in groups.items():
        if pkg!='(package not printed)':code.append('namespace '+pkg+' {')
        for n in nn:
            code.append('class '+n['id']+'["'+n['name']+'"]'+(' {\n<<'+n['stereotype']+'>>\n}' if n['stereotype'] else ''))
        if pkg!='(package not printed)':code.append('}')
    for e in ee:code.append(e['a']+' '+e['kind']+' '+e['b']+(' : '+e['label'] if e['label'] else ''))
    for note in notes or []:code.append('note "'+note+'"')
    m['mermaid']='\n'.join(code)+'\n';models.append(m)
    folder=OUT/sid;folder.mkdir(parents=True,exist_ok=True)
    (folder/(m['render_prefix']+'.mmd')).write_text(m['mermaid'],'utf-8')
    return m

model('175',2,'Payments initiation conceptual model',
'''ContactPoint PaymentProcessing Mandate CreditTransferMandate DirectDebitMandate Document PaymentIdentification PaymentStatus PaymentObligation Payment PaymentExecution PaymentInstruction CashSettlement PaymentTerms BankingTransaction PaymentInitiation CurrencyExchange Tax CashAccount Cheque Garnishment PaymentTracker''',
'''ContactPoint|assoc|PaymentProcessing|- RelatedPayment
ContactPoint|assoc|Document|+ PlaceOfStorage / + StoredDocument
Document|assoc|PaymentObligation|+ AssociatedDocument
PaymentObligation|assoc|Payment|+ PaymentOffset
PaymentObligation|assoc|PaymentTerms
BankingTransaction|assoc|PaymentObligation
Garnishment|inherit|PaymentObligation
Payment|assoc|PaymentIdentification|+ PaymentRelatedIdentifications
Payment|assoc|PaymentStatus|+ PaymentStatus
Payment|assoc|PaymentExecution
Payment|assoc|PaymentProcessing|+ ProcessingInstructions
PaymentProcessing|assoc|Mandate|+ MandatePaymentType / + RelatedMandate
CreditTransferMandate|inherit|Mandate
DirectDebitMandate|inherit|Mandate
PaymentInitiation|inherit|PaymentExecution
PaymentExecution|assoc|PaymentInstruction|+ Previous / + Next
PaymentInstruction|assoc|CashSettlement|+ SettlementInstruction
CashSettlement|assoc|CashAccount|+ SettlementAccount
CashAccount|assoc|Cheque
Tax|assoc|CashAccount|+ TaxAccount
Payment|assoc|Tax|+ TaxOnPayment
Payment|assoc|CurrencyExchange|- RelatedPayment / - ExchangeRateData
CurrencyExchange|assoc|Tax
CurrencyExchange|assoc|PaymentTracker|- RelatedPaymentTracker
Payment|assoc|CashAccount|+ RelatedPaymentSettlement''',
'Payment connects obligation, processing, identification, status, execution, tax, currency exchange and settlement account. Initiation specializes execution; credit-transfer and direct-debit mandates specialize Mandate; Garnishment specializes PaymentObligation. The long lower association connects Payment and CashAccount. Relationship-end labels are retained together without inferring message sender/receiver roles.',
unprinted='ContactPoint Mandate CreditTransferMandate DirectDebitMandate Document CurrencyExchange Tax Garnishment PaymentTracker')

m=model('164',2,'Payments clearing and settlement conceptual model',
'''ServiceLevel BankTransaction PaymentProcessing PaymentExecution Payment PaymentIdentification SettlementTimeRequest PaymentStatus Mandate DirectDebitMandate DirectDebit CreditTransferMandate ContactPoint Party Organisation OrganisationIdentification CashClearingSystemMember CashSettlement CashAccount PaymentPartyRole CreditorAgentRole DebtorAgentRole PaymentInstruction DateTimePeriod System ClearingSystem CashClearingSystem''',
'''ServiceLevel|assoc|PaymentProcessing
BankTransaction|assoc|PaymentProcessing
PaymentProcessing|assoc|PaymentExecution
PaymentExecution|assoc|Payment
Payment|assoc|PaymentIdentification
Payment|assoc|SettlementTimeRequest
Payment|assoc|PaymentStatus
Payment|assoc|CashAccount|- Account
Payment|assoc|PaymentPartyRole
PaymentProcessing|assoc|Mandate|+ MandatePaymentType / + RelatedMandate
PaymentProcessing|assoc|ContactPoint|- RelatedPayment
DirectDebitMandate|inherit|Mandate
CreditTransferMandate|inherit|Mandate
DirectDebitMandate|assoc|DirectDebit
ContactPoint|assoc|Party|+ RelatedParty
Organisation|inherit|Party
Organisation|assoc|Organisation|+ ParentOrganisation / + Branch
Organisation|assoc|OrganisationIdentification
OrganisationIdentification|assoc|CashClearingSystemMember|+ ClearingSystemMemberIdentificationType
CashSettlement|assoc|CashAccount|+ SettlementAccount
PaymentInstruction|assoc|CashSettlement|+ SettlementInstruction
PaymentInstruction|inherit|PaymentExecution
CashAccount|assoc|PaymentPartyRole
CreditorAgentRole|inherit|PaymentPartyRole
DebtorAgentRole|inherit|PaymentPartyRole
PaymentInstruction|assoc|DateTimePeriod|- ProcessingValidityTime
DateTimePeriod|assoc|System|- VersionValidityPeriod
ClearingSystem|inherit|System
CashClearingSystem|inherit|ClearingSystem''',
'Payment processing connects execution, service level, bank-transaction classification, mandate and contact point. Payment connects account, payment-party role, identification, timing request and status. Cash settlement connects instruction and cash account. Role and system specializations, organisation self-association and every unlabelled source line are retained. The source places “+ ClearingSystemMemberIdentificationType” above the organisation-identification/member region, away from its connector. The label is assigned to the existing OrganisationIdentification–CashClearingSystemMember line using the same workbook FullBusinessModel!A2990:F2990 and inverse A635:F635, which explicitly identify both endpoints and this association-end name. This is a documented resolution of layout ambiguity, not an added relationship; see issue-000025. No CashClearingSystemMember–CashClearingSystem association is drawn in the supplied figure.',
unprinted='Mandate ContactPoint Party Organisation OrganisationIdentification CashClearingSystemMember',datatypes='DateTimePeriod')

model('016',2,'Operational cash-management role players',
'''Role RolePlayer InformationPartyRole PaymentPartyRole SystemPartyRole System Party IdentificationIssuerRole InstructingAgentRole CashClearingSystemMember ClearingMemberRole ClearingSystem Person Organisation TransactionAdministrator CashClearingSystem FinancialInstitution''',
'''Role|assoc|RolePlayer|+ Player
InformationPartyRole|inherit|Role
PaymentPartyRole|inherit|Role
SystemPartyRole|inherit|Role
IdentificationIssuerRole|inherit|InformationPartyRole
InstructingAgentRole|inherit|PaymentPartyRole
ClearingMemberRole|inherit|SystemPartyRole
TransactionAdministrator|inherit|SystemPartyRole
SystemPartyRole|assoc|System|+ RelatedSystem / + PartyRole
System|inherit|RolePlayer
Party|inherit|RolePlayer
ClearingSystem|inherit|System
CashClearingSystem|inherit|ClearingSystem
Person|inherit|Party
Organisation|inherit|Party
FinancialInstitution|inherit|Organisation
ClearingMemberRole|assoc|CashClearingSystemMember|+ ClearingMember / - ClearingSystemMemberIdentification
TransactionAdministrator|assoc|CashClearingSystem''',
'Role associates with its RolePlayer. Information, payment and system-party roles specialize Role, while Party and System specialize RolePlayer. System roles and clearing-member identification remain distinct from the party or institution playing them. TransactionAdministrator specializes SystemPartyRole and associates with CashClearingSystem.',datatypes='CashClearingSystemMember')

model('016',3,'Operational cash-management payment-related components',
'''PaymentExecution DateTimePeriod PaymentInstruction Account Balance PaymentObligation Payment CashAccount CashBalance PaymentStatus CashSettlement CashEntry CreditInstrument BookEntry''',
'''PaymentInstruction|inherit|PaymentExecution
PaymentInstruction|assoc|PaymentExecution|+ Previous / + Next
PaymentInstruction|assoc|DateTimePeriod|- ProcessingValidityTime
Account|assoc|DateTimePeriod|+ ReportedPeriod
Account|assoc|Balance
CashAccount|inherit|Account
CashBalance|inherit|Balance
PaymentExecution|assoc|Payment
Payment|assoc|PaymentObligation|+ PaymentOffset
Payment|assoc|CashAccount
CashAccount|assoc|CashBalance
Payment|assoc|PaymentStatus
Payment|assoc|CreditInstrument|+ RelatedPayment / + CreditMethod
CashAccount|assoc|CashSettlement|+ SettlementAccount / + RelatedSettlementInstruction
CashAccount|assoc|CashEntry
CashEntry|assoc|CashBalance|+ CashBalanceEntry
CashEntry|assoc|BookEntry|+ RelatedBookEntry
BookEntry|inherit|CreditInstrument
BookEntry|assoc|CashSettlement|+ RelatedSettlementInstruction''',
'Payment instruction has both a generalization to PaymentExecution and a separate Previous/Next association. Payment relates to its obligation, status, cash account and credit method. BookEntry specializes CreditInstrument and connects CashEntry and CashSettlement. Cash-account, balance and date-period relationships are preserved without deriving payment directions.',datatypes='DateTimePeriod')

model('016',4,'Operational transactions, system and account model',
'''PartyIdentificationInformation DateTimePeriod PaymentInstruction StandingOrder CashAccount CashStandingOrder CashManagementService Limit LiquidityManagementLimit CurrencyExchange Account System SystemBusinessInformation InformationQualifier SystemIdentification SystemEventInformation SystemAvailability SystemStatus ClearingSystem CashClearingSystem TransactionAdministrator SystemPartyRole SystemMemberRole Balance CashBalance''',
'''PartyIdentificationInformation|assoc|DateTimePeriod|- RelatedIdentification / + ValidityPeriod
DateTimePeriod|assoc|PaymentInstruction|- ProcessingValidityTime
PaymentInstruction|assoc|StandingOrder|+ PaymentInstructionTrigger
StandingOrder|assoc|CashAccount|+ RelatedCreditStandingOrder / + CreditAccount
StandingOrder|assoc|CashAccount|+ RelatedDebitStandingOrder / + DebitAccount
CashStandingOrder|inherit|StandingOrder
CashAccount|assoc|CashStandingOrder
CashStandingOrder|assoc|CashManagementService|+ StandingOrder / + RelatedCashServices
CashManagementService|assoc|LiquidityManagementLimit
LiquidityManagementLimit|inherit|Limit
CurrencyExchange|assoc|LiquidityManagementLimit|- RelatedLimitManagement
CurrencyExchange|assoc|Account|- ReportedAccount
CurrencyExchange|assoc|TransactionAdministrator|+ CurrencyExchangeForTransactionAdministrator
Account|assoc|System
Account|assoc|Balance|+ Account / + Balance
CashAccount|assoc|CashBalance
CashBalance|inherit|Balance
SystemMemberRole|assoc|CashBalance|+ Counterparty
SystemMemberRole|assoc|Account|- SystemMember
SystemMemberRole|assoc|SystemStatus|+ MemberStatus
SystemMemberRole|inherit|SystemPartyRole
TransactionAdministrator|inherit|SystemPartyRole
TransactionAdministrator|assoc|CashClearingSystem
CashClearingSystem|inherit|ClearingSystem
ClearingSystem|inherit|System
System|assoc|SystemBusinessInformation|+ SystemGeneratedInformation
SystemBusinessInformation|assoc|InformationQualifier
System|assoc|SystemIdentification|+ IdentificationForSystem
System|assoc|SystemEventInformation|+ Event
System|assoc|SystemAvailability|+ Availability
System|assoc|SystemStatus|+ Status''',
'Standing orders have separate credit-account and debit-account associations. CashStandingOrder specializes StandingOrder and links cash-management services. Liquidity limits connect service and exchange context. System information, identification, events, availability and status are separate components. SystemMemberRole and TransactionAdministrator specialize SystemPartyRole; their account, balance, system-status and clearing-system associations are retained. CashAccount and Account remain separate visible nodes; the source view does not draw a generalization between them.',datatypes='DateTimePeriod InformationQualifier SystemEventInformation SystemAvailability')

model('006',2,'Bank-to-customer account conceptual model',
'''AccountPartyRole AccountServicerRole AccountOwnerRole AccountStatus AccountIdentification Account Balance Entry CashEntry CashAccount SecuritiesAccount Interest Tax Payment PaymentIdentification''',
'''AccountServicerRole|inherit|AccountPartyRole
AccountOwnerRole|inherit|AccountPartyRole
Account|assoc|AccountPartyRole|+ PartyRole
Account|assoc|AccountStatus|+ Status
Account|assoc|AccountIdentification
Account|assoc|Balance
Account|assoc|Account|+ SubAccount / + ParentAccount
Account|assoc|Entry
CashAccount|inherit|Account
SecuritiesAccount|inherit|Account
CashEntry|inherit|Entry
CashEntry|assoc|CashAccount
Balance|assoc|Interest|+ AccountBalance
Interest|assoc|Tax|+ InterestTax
CashAccount|assoc|Payment|- Account
Payment|assoc|PaymentIdentification|+ PaymentRelatedIdentifications''',
'AccountOwnerRole and AccountServicerRole specialize AccountPartyRole. This preserves their conceptual role distinction without equating either with an institution. Account has status, identification, balance, entries and a parent/sub-account self-association. Cash and securities accounts specialize Account; CashEntry specializes Entry. Interest, interest tax, payment and payment identification remain explicitly connected.',unprinted='AccountServicerRole AccountOwnerRole Interest Tax Payment PaymentIdentification')

model('006',3,'Bank-to-customer accounts, balances and entries',
'''GenericIdentification AccountStatus DateTimePeriod AccountIdentification Account SecuritiesAccount AccountLink CashAccount Entry SecuritiesEntry CashEntry Balance CashBalance SecuritiesBalance BankTransaction Payment PaymentIdentification''',
'''Account|assoc|Account|+ SubAccount / + ParentAccount
CashAccount|inherit|Account
SecuritiesAccount|inherit|Account
SecuritiesAccount|assoc|AccountLink
AccountLink|assoc|CashAccount
Account|assoc|GenericIdentification|+ Type
GenericIdentification|assoc|BankTransaction|+ IdentificationForBankTransaction
Account|assoc|AccountStatus|+ Status
Account|assoc|DateTimePeriod|+ ReportedPeriod
Account|assoc|AccountIdentification|+ Identification
Account|assoc|Entry|+ Entry
Entry|assoc|BankTransaction|+ BankTransactionCode
SecuritiesEntry|inherit|Entry
CashEntry|inherit|Entry
Account|assoc|Balance
Entry|assoc|Balance|+ BalanceEntry
CashBalance|inherit|Balance
SecuritiesBalance|inherit|Balance
CashAccount|assoc|Payment|- Account
CashAccount|assoc|CashBalance
Payment|assoc|PaymentIdentification|+ PaymentRelatedIdentifications''',
'Account, Entry and Balance each have cash and securities specializations. AccountLink connects SecuritiesAccount and CashAccount. Account types and bank transactions link to GenericIdentification; Entry connects BankTransaction through the printed BankTransactionCode end label. The general Account–Balance and specific CashAccount–CashBalance lines are both retained. Most source boxes omit stereotypes; only the printed BusinessComponent stereotypes are reconstructed.',unprinted='Payment PaymentIdentification',datatypes='GenericIdentification DateTimePeriod',no_stereotype='GenericIdentification AccountStatus DateTimePeriod AccountIdentification Account SecuritiesAccount AccountLink CashAccount Entry SecuritiesEntry CashEntry Balance CashBalance SecuritiesBalance')

model('006',4,'Bank-to-customer cash balance and availability',
'''Entry Balance Account DateTimePeriod Limit CashEntry CashAvailability CashBalance''',
'''Entry|assoc|Balance|+ BalanceEntry
Balance|assoc|Account
Account|assoc|DateTimePeriod|+ ReportedPeriod
DateTimePeriod|assoc|Limit|+ ValidityPeriod
CashEntry|inherit|Entry
CashEntry|assoc|CashAvailability|Availability
CashBalance|inherit|Balance
CashBalance|assoc|CashAvailability|+ Availability''',
'CashEntry and CashBalance specialize Entry and Balance respectively and each associates separately with CashAvailability. Balance relates to Account; Account reports a DateTimePeriod, also used as the Limit validity period. The CashEntry–CashAvailability label is printed without a plus sign, unlike the CashBalance association.',datatypes='DateTimePeriod',no_stereotype='Balance Limit CashAvailability CashBalance')

(OUT/'models.json').write_text(json.dumps(models,ensure_ascii=False,indent=2),'utf-8')
print(json.dumps([{'source':m['source_id'],'figure':m['id'],'nodes':len(m['nodes']),'relationships':len(m['edges'])} for m in models]))
