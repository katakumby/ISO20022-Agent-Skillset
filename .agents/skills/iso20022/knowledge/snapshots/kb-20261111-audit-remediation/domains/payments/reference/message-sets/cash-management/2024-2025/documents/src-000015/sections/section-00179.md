---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.4 Payment <Pmt>", "5.4.2.1.3.2.1.4.8 Priority <Prty>"]
file_pages: [294]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.4.8 Priority <Prty>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 294 to 294.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 294

```text
CodeName Name Definition
institution) to pay a stated sum to a
named recipient (the payee)).
BKT BookTransfer Transfer that is a movement of cash on
the books of the account servicer.
DCP DebitCardPayment Payment instrument is a debit card. (The
payment originated using a debit card
scheme.).
CCP CreditCardPayment Payment instrument is a credit card.
(The payment originated using a credit
card scheme.).
RTI Return Entry related to a returned or unpaid
item.
CAN CancellationRequest Reverse entry that is the result of the
cancellation of a previously booked
entry.
5.4.2.1.3.2.1.4.8  Priority <Prty>
Presence: [0..1]
Definition: Urgency or order of importance that the originator would like the recipient of the payment
instruction to apply to the processing of the payment instruction.
.
Priority <Prty> contains one of the following Priority1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 294
Or}   Proprietary <Prtry> [1..1] Text 294
5.4.2.1.3.2.1.4.8.1  Code <Cd>
Presence: [1..1]
Definition: Priority code, in a coded form.
Datatype: "Priority5Code" on page 871
CodeName Name Definition
HIGH High Priority level is high.
LOWW Low Priority level is low.
NORM Normal Priority level is normal.
URGT Urgent Priority level is urgent (highest priority
possible).
5.4.2.1.3.2.1.4.8.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Priority code bilaterally agreed between parties.
Datatype: "Max35Text" on page 889
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 294 February 2025
```

