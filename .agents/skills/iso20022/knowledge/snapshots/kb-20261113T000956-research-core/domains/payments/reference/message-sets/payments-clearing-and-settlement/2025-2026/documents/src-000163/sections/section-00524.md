---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.1.1 MessageIdentification <MsgId>"]
file_pages: [718]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.1.1 MessageIdentification <MsgId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 718 to 718.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 718

```text
Constraints
• TotalInterbankSettlementAmountAndDateRule
If TotalInterbankSettlementAmount is present, then InterbankSettlementDate must be present.
On Condition
    /TotalInterbankSettlementAmount is present
Following Must be True
    /InterbankSettlementDate Must be present
6.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the instructing party, and sent to the next party in the
chain to unambiguously identify the message.
Usage: The instructing party has to make sure that MessageIdentification is unique per instructed party
for a pre-agreed period.
Datatype: "Max35Text" on page 1246
6.4.1.2  CreationDateTime <CreDtTm>
Presence: [1..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 1239
6.4.1.3  ExpiryDateTime <XpryDtTm>
Presence: [0..1]
Definition: Date and time on which the payment should be expired if it has not settled.
Datatype: "ISODateTime" on page 1239
6.4.1.4  BatchBooking <BtchBookg>
Presence: [0..1]
Definition: Identifies whether a single entry per individual transaction or a batch entry for the sum of the
amounts of all transactions within the group of a message is requested.
Usage: Batch booking is used to request and not order a possible batch booking.
Datatype: One of the following values must be used (see "BatchBookingIndicator" on page 1241):
• Meaning When True: Identifies that a batch entry for the sum of the amounts of all transactions in the
batch or message is requested.
• Meaning When False: Identifies that a single entry for each of the transactions in the batch or
message is requested.
6.4.1.5  NumberOfTransactions <NbOfTxs>
Presence: [1..1]
Definition: Number of individual transactions contained in the message.
Datatype: "Max15NumericText" on page 1244
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
718 March 2026
```

