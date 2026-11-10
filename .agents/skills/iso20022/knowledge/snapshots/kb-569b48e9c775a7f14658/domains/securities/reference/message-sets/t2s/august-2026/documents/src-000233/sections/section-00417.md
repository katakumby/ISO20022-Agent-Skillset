---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["22 camt.084.001.02 IntraBalanceMovementPostingReportV02", "22.4 Message Building Blocks", "22.4.5 CashAccountOwner <CshAcctOwnr>"]
file_pages: [532, 533]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 22.4.5 CashAccountOwner <CshAcctOwnr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 532 to 533.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 532

```text
22.4.5 CashAccountOwner <CshAcctOwnr>
Presence: [0..1]
Definition: Party that owns the account.
CashAccountOwner <CshAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
22.4.6 CashAccountServicer <CshAcctSvcr>
Presence: [0..1]
Definition: Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
CashAccountServicer <CshAcctSvcr> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 2919 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  2920
     BICFI <BICFI> [0..1] IdentifierSet C3 2920
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 2920
     LEI <LEI> [0..1] IdentifierSet 2920
     Name <Nm> [0..1] Text 2921
     PostalAddress <PstlAdr> [0..1] ± 2921
     Other <Othr> [0..1] ± 2921
   BranchIdentification <BrnchId> [0..1]  2922
     Identification <Id> [0..1] Text 2922
     LEI <LEI> [0..1] IdentifierSet 2922
     Name <Nm> [0..1] Text 2922
     PostalAddress <PstlAdr> [0..1] ± 2923
22.4.7 SubBalance <SubBal>
Presence: [0..*]
Definition: Identifies the transactions.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities 532 August 2026
```

## File page 533

```text
SubBalance <SubBal> contains the following IntraBalancePosting5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BalanceFrom <BalFr> [1..1]  534
     Type <Tp> [1..1]  535
{Or       Code <Cd> [1..1] CodeSet 535
Or}       Proprietary <Prtry> [1..1] ± 535
     QuantityBreakdown <QtyBrkdwn> [0..*]  536
       LotNumber <LotNb> [0..1] ± 536
       LotAmount <LotAmt> [0..1] ± 536
       LotQuantity <LotQty> [0..1] ± 536
       CashSubBalanceType <CshSubBalTp> [0..1] ± 537
   Movement <Mvmnt> [1..*]  C12 537
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 539
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 539
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 539
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 539
     PoolIdentification <PoolId> [0..1] Text 540
     CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 540
     BalanceTo <BalTo> [1..1]  540
       Type <Tp> [1..1]  540
{Or         Code <Cd> [1..1] CodeSet 541
Or}         Proprietary <Prtry> [1..1] ± 541
       QuantityBreakdown <QtyBrkdwn> [0..*]  541
         LotNumber <LotNb> [0..1] ± 541
         LotAmount <LotAmt> [0..1] ± 542
         LotQuantity <LotQty> [0..1] ± 542
         CashSubBalanceType <CshSubBalTp> [0..1] ± 542
     SettledAmount <SttldAmt> [1..1] ± 542
     PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 543
     RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 543
     EffectiveSettlementDate <FctvSttlmDt> [1..1] ± 543
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities 533 August 2026
```

