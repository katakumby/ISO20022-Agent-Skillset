---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["15 camt.084.001.02 IntraBalanceMovementPostingReportV02", "15.4 Message Building Blocks", "15.4.5 CashAccountOwner <CshAcctOwnr>"]
file_pages: [341, 342]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 15.4.5 CashAccountOwner <CshAcctOwnr>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 341 to 342.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 341

```text
15.4.5 CashAccountOwner <CshAcctOwnr>
Presence: [0..1]
Definition: Party that owns the account.
CashAccountOwner <CshAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 420 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 420
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 420
15.4.6 CashAccountServicer <CshAcctSvcr>
Presence: [0..1]
Definition: Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
CashAccountServicer <CshAcctSvcr> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 400 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  401
     BICFI <BICFI> [0..1] IdentifierSet C6 401
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 402
     LEI <LEI> [0..1] IdentifierSet 402
     Name <Nm> [0..1] Text 402
     PostalAddress <PstlAdr> [0..1] ± 402
     Other <Othr> [0..1] ± 403
   BranchIdentification <BrnchId> [0..1]  404
     Identification <Id> [0..1] Text 404
     LEI <LEI> [0..1] IdentifierSet 404
     Name <Nm> [0..1] Text 404
     PostalAddress <PstlAdr> [0..1] ± 404
15.4.7 SubBalance <SubBal>
Presence: [0..*]
Definition: Identifies the transactions.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
341 March 2024
```

## File page 342

```text
SubBalance <SubBal> contains the following IntraBalancePosting5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BalanceFrom <BalFr> [1..1]  343
     Type <Tp> [1..1]  344
{Or       Code <Cd> [1..1] CodeSet 344
Or}       Proprietary <Prtry> [1..1] ± 344
     QuantityBreakdown <QtyBrkdwn> [0..*]  345
       LotNumber <LotNb> [0..1] ± 345
       LotAmount <LotAmt> [0..1] ± 345
       LotQuantity <LotQty> [0..1] ± 345
       CashSubBalanceType <CshSubBalTp> [0..1] ± 346
   Movement <Mvmnt> [1..*]  C12 346
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 348
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 348
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 348
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 348
     PoolIdentification <PoolId> [0..1] Text 349
     CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 349
     BalanceTo <BalTo> [1..1]  349
       Type <Tp> [1..1]  349
{Or         Code <Cd> [1..1] CodeSet 350
Or}         Proprietary <Prtry> [1..1] ± 350
       QuantityBreakdown <QtyBrkdwn> [0..*]  350
         LotNumber <LotNb> [0..1] ± 350
         LotAmount <LotAmt> [0..1] ± 351
         LotQuantity <LotQty> [0..1] ± 351
         CashSubBalanceType <CshSubBalTp> [0..1] ± 351
     SettledAmount <SttldAmt> [1..1] ± 351
     PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 352
     RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 352
     EffectiveSettlementDate <FctvSttlmDt> [1..1] ± 352
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
342 March 2024
```

