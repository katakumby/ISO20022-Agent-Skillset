---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["19 camt.081.001.02 IntraBalanceMovementModificationReportV02", "19.4 Message Building Blocks", "19.4.4 ReportOrError <RptOrErr>", "19.4.4.1 Modifications <Mods>", "19.4.4.1.5 Modification <Mod>", "19.4.4.1.5.7 RequestDetails <ReqDtls>", "19.4.4.1.5.7.7 Linkages <Lnkgs>", "19.4.4.1.5.7.7.3 Reference <Ref>", "19.4.4.1.5.7.7.3.6 PoolIdentification <PoolId>"]
file_pages: [467, 468]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 19.4.4.1.5.7.7.3.6 PoolIdentification <PoolId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 467 to 468.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 467

```text
19.4.4.1.5.7.7.3.6  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 3328
19.4.4.1.5.7.7.3.7  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Definition: Identification of a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 3328
19.4.4.1.5.7.7.4  ReferenceOwner <RefOwnr>
Presence: [0..1]
Definition: Party responsible for generating the reference.
ReferenceOwner <RefOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 3059 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C2 3059
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 3060
19.4.4.1.5.8  UnderlyingIntraBalance <UndrlygIntraBal>
Presence: [0..1]
Definition: Identifies additional details of the transaction.
Impacted by: C5 "AdditionalDetailsRule", C8 "BalanceFromToRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 467 August 2026
```

## File page 468

```text
UnderlyingIntraBalance <UndrlygIntraBal> contains the following IntraBalance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementAmount <SttlmAmt> [1..1] ± 469
   SettlementDate <SttlmDt> [1..1] ± 469
   BalanceFrom <BalFr> [1..1]  469
     Type <Tp> [1..1]  469
{Or       Code <Cd> [1..1] CodeSet 470
Or}       Proprietary <Prtry> [1..1] ± 470
     QuantityBreakdown <QtyBrkdwn> [0..*]  470
       LotNumber <LotNb> [0..1] ± 470
       LotAmount <LotAmt> [0..1] ± 471
       LotQuantity <LotQty> [0..1] ± 471
       CashSubBalanceType <CshSubBalTp> [0..1] ± 471
   BalanceTo <BalTo> [1..1]  472
     Type <Tp> [1..1]  472
{Or       Code <Cd> [1..1] CodeSet 472
Or}       Proprietary <Prtry> [1..1] ± 472
     QuantityBreakdown <QtyBrkdwn> [0..*]  473
       LotNumber <LotNb> [0..1] ± 473
       LotAmount <LotAmt> [0..1] ± 473
       LotQuantity <LotQty> [0..1] ± 474
       CashSubBalanceType <CshSubBalTp> [0..1] ± 474
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 474
   Priority <Prty> [0..1] ± 474
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 475
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and the receiver, if
InstructionProcessingAdditionalDetails is present, then it must not contain information that can be
provided in a structured field.
• BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of BalanceTo.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 468 August 2026
```

