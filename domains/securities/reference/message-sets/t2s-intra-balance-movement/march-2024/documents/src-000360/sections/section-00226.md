---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["12 camt.081.001.02 IntraBalanceMovementModificationReportV02", "12.4 Message Building Blocks", "12.4.4 ReportOrError <RptOrErr>", "12.4.4.1 Modifications <Mods>", "12.4.4.1.5 Modification <Mod>", "12.4.4.1.5.7 RequestDetails <ReqDtls>", "12.4.4.1.5.7.7 Linkages <Lnkgs>", "12.4.4.1.5.7.7.3 Reference <Ref>", "12.4.4.1.5.7.7.3.6 PoolIdentification <PoolId>"]
file_pages: [276, 277]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 12.4.4.1.5.7.7.3.6 PoolIdentification <PoolId>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 276 to 277.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 276

```text
12.4.4.1.5.7.7.3.6  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 497
12.4.4.1.5.7.7.3.7  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Definition: Identification of a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 497
12.4.4.1.5.7.7.4  ReferenceOwner <RefOwnr>
Presence: [0..1]
Definition: Party responsible for generating the reference.
ReferenceOwner <RefOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 419 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C5 419
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 420
12.4.4.1.5.8  UnderlyingIntraBalance <UndrlygIntraBal>
Presence: [0..1]
Definition: Identifies additional details of the transaction.
Impacted by: C5 "AdditionalDetailsRule", C8 "BalanceFromToRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
276 March 2024
```

## File page 277

```text
UnderlyingIntraBalance <UndrlygIntraBal> contains the following IntraBalance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementAmount <SttlmAmt> [1..1] ± 278
   SettlementDate <SttlmDt> [1..1] ± 278
   BalanceFrom <BalFr> [1..1]  278
     Type <Tp> [1..1]  278
{Or       Code <Cd> [1..1] CodeSet 279
Or}       Proprietary <Prtry> [1..1] ± 279
     QuantityBreakdown <QtyBrkdwn> [0..*]  279
       LotNumber <LotNb> [0..1] ± 279
       LotAmount <LotAmt> [0..1] ± 280
       LotQuantity <LotQty> [0..1] ± 280
       CashSubBalanceType <CshSubBalTp> [0..1] ± 280
   BalanceTo <BalTo> [1..1]  281
     Type <Tp> [1..1]  281
{Or       Code <Cd> [1..1] CodeSet 281
Or}       Proprietary <Prtry> [1..1] ± 281
     QuantityBreakdown <QtyBrkdwn> [0..*]  282
       LotNumber <LotNb> [0..1] ± 282
       LotAmount <LotAmt> [0..1] ± 282
       LotQuantity <LotQty> [0..1] ± 283
       CashSubBalanceType <CshSubBalTp> [0..1] ± 283
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 283
   Priority <Prty> [0..1] ± 283
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 284
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and the receiver, if
InstructionProcessingAdditionalDetails is present, then it must not contain information that can be
provided in a structured field.
• BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of BalanceTo.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
277 March 2024
```

