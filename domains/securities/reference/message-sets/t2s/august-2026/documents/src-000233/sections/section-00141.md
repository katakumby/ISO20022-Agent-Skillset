---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["11 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02", "11.4 Message Building Blocks", "11.4.6 RequestDetails <ReqDtls>", "11.4.6.7 Linkages <Lnkgs>", "11.4.6.7.3 Reference <Ref>", "11.4.6.7.3.6 PoolIdentification <PoolId>"]
file_pages: [189, 190]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.073.001.02"]
---

# 11.4.6.7.3.6 PoolIdentification <PoolId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 189 to 190.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 189

```text
11.4.6.7.3.6  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 3328
11.4.6.7.3.7  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Definition: Identification of a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 3328
11.4.6.7.4  ReferenceOwner <RefOwnr>
Presence: [0..1]
Definition: Party responsible for generating the reference.
ReferenceOwner <RefOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 3059 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C2 3059
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 3060
11.4.7 ProcessingStatus <PrcgSts>
Presence: [1..1]
Definition: Provides details on the processing status of the transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus71Choice" on page 3152 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 3152
Or   Pending <Pdg> [1..1] ± 3153
Or   Rejected <Rjctd> [1..1] ± 3153
Or   Repair <Rpr> [1..1] ± 3153
Or   Denied <Dnd> [1..1] ± 3154
Or   Completed <Cmpltd> [1..1] ± C6 3154
Or}   Proprietary <Prtry> [1..1] ± 3155
11.4.8 UnderlyingIntraBalance <UndrlygIntraBal>
Presence: [0..1]
Definition: Intra-balance movement transaction details.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities 189 August 2026
```

## File page 190

```text
Impacted by: C3 "AdditionalDetailsRule", C6 "BalanceFromToRule"
UnderlyingIntraBalance <UndrlygIntraBal> contains the following IntraBalance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementAmount <SttlmAmt> [1..1] ± 191
   SettlementDate <SttlmDt> [1..1] ± 191
   BalanceFrom <BalFr> [1..1]  191
     Type <Tp> [1..1]  191
{Or       Code <Cd> [1..1] CodeSet 192
Or}       Proprietary <Prtry> [1..1] ± 192
     QuantityBreakdown <QtyBrkdwn> [0..*]  192
       LotNumber <LotNb> [0..1] ± 192
       LotAmount <LotAmt> [0..1] ± 193
       LotQuantity <LotQty> [0..1] ± 193
       CashSubBalanceType <CshSubBalTp> [0..1] ± 193
   BalanceTo <BalTo> [1..1]  194
     Type <Tp> [1..1]  194
{Or       Code <Cd> [1..1] CodeSet 194
Or}       Proprietary <Prtry> [1..1] ± 194
     QuantityBreakdown <QtyBrkdwn> [0..*]  195
       LotNumber <LotNb> [0..1] ± 195
       LotAmount <LotAmt> [0..1] ± 195
       LotQuantity <LotQty> [0..1] ± 196
       CashSubBalanceType <CshSubBalTp> [0..1] ± 196
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 196
   Priority <Prty> [0..1] ± 196
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 197
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
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities 190 August 2026
```

