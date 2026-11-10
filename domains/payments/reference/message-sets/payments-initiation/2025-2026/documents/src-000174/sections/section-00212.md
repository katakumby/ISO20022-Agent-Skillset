---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.7 ChargeBearer <ChrgBr>"]
file_pages: [311]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.7 ChargeBearer <ChrgBr>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 311 to 311.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 311

```text
4.4.3.8.7  ChargeBearer <ChrgBr>
Presence: [0..1]
Definition: Specifies if the creditor and/or debtor will bear the charges associated with the processing of
the payment transaction.
Usage: The ChargeBearer applies to the reversal message, not to the original instruction.
Datatype: "ChargeBearerType1Code" on page 588
CodeName Name Definition
DEBT BorneByDebtor All transaction charges are to be borne
by the debtor.
CRED BorneByCreditor All transaction charges are to be borne
by the creditor.
SHAR Shared In a credit transfer context, means that
transaction charges on the sender side
are to be borne by the debtor,
transaction charges on the receiver side
are to be borne by the creditor. In a
direct debit context, means that
transaction charges on the sender side
are to be borne by the creditor,
transaction charges on the receiver side
are to be borne by the debtor.
SLEV FollowingServiceLevel Charges are to be applied following the
rules agreed in the service level and/or
scheme.
4.4.3.8.8  ReversalReasonInformation <RvslRsnInf>
Presence: [0..*]
Definition: Provides detailed information on the reversal reason.
ReversalReasonInformation <RvslRsnInf> contains the following PaymentReversalReason10
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Originator <Orgtr> [0..1] ± 311
   Reason <Rsn> [0..1]  312
{Or     Code <Cd> [1..1] CodeSet 313
Or}     Proprietary <Prtry> [1..1] Text 313
   AdditionalInformation <AddtlInf> [0..*] Text 313
4.4.3.8.8.1  Originator <Orgtr>
Presence: [0..1]
Definition: Party that issues the reversal.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 311 March 2026
```

