---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["6 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02", "6.4 Message Building Blocks", "6.4.6 RequestDetails <ReqDtls>", "6.4.6.7 Linkages <Lnkgs>", "6.4.6.7.3 Reference <Ref>", "6.4.6.7.3.6 PoolIdentification <PoolId>"]
file_pages: [106, 107]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.073.001.02"]
---

# 6.4.6.7.3.6 PoolIdentification <PoolId>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 106 to 107.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 106

```text
6.4.6.7.3.6  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 497
6.4.6.7.3.7  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Definition: Identification of a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 497
6.4.6.7.4  ReferenceOwner <RefOwnr>
Presence: [0..1]
Definition: Party responsible for generating the reference.
ReferenceOwner <RefOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 419 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C5 419
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 420
6.4.7 ProcessingStatus <PrcgSts>
Presence: [1..1]
Definition: Provides details on the processing status of the transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus71Choice" on page 450 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 450
Or   Pending <Pdg> [1..1] ± 450
Or   Rejected <Rjctd> [1..1] ± 451
Or   Repair <Rpr> [1..1] ± 451
Or   Denied <Dnd> [1..1] ± 452
Or   Completed <Cmpltd> [1..1] ± C5 452
Or}   Proprietary <Prtry> [1..1] ± 452
6.4.8 UnderlyingIntraBalance <UndrlygIntraBal>
Presence: [0..1]
Definition: Intra-balance movement transaction details.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
106 March 2024
```

## File page 107

```text
Impacted by: C3 "AdditionalDetailsRule", C6 "BalanceFromToRule"
UnderlyingIntraBalance <UndrlygIntraBal> contains the following IntraBalance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementAmount <SttlmAmt> [1..1] ± 108
   SettlementDate <SttlmDt> [1..1] ± 108
   BalanceFrom <BalFr> [1..1]  108
     Type <Tp> [1..1]  108
{Or       Code <Cd> [1..1] CodeSet 109
Or}       Proprietary <Prtry> [1..1] ± 109
     QuantityBreakdown <QtyBrkdwn> [0..*]  109
       LotNumber <LotNb> [0..1] ± 109
       LotAmount <LotAmt> [0..1] ± 110
       LotQuantity <LotQty> [0..1] ± 110
       CashSubBalanceType <CshSubBalTp> [0..1] ± 110
   BalanceTo <BalTo> [1..1]  111
     Type <Tp> [1..1]  111
{Or       Code <Cd> [1..1] CodeSet 111
Or}       Proprietary <Prtry> [1..1] ± 111
     QuantityBreakdown <QtyBrkdwn> [0..*]  112
       LotNumber <LotNb> [0..1] ± 112
       LotAmount <LotAmt> [0..1] ± 112
       LotQuantity <LotQty> [0..1] ± 113
       CashSubBalanceType <CshSubBalTp> [0..1] ± 113
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 113
   Priority <Prty> [0..1] ± 113
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 114
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and the receiver, if
InstructionProcessingAdditionalDetails is present, then it must not contain information that can be
provided in a structured field.
• BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of BalanceTo.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
107 March 2024
```

