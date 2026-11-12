---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.1.4 BatchBooking <BtchBookg>"]
file_pages: [276]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.1.4 BatchBooking <BtchBookg>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 276 to 276.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 276

```text
Authorisation <Authstn> contains one of the following elements (see "Authorisation1Choice" on
page 1190 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1190
Or}   Proprietary <Prtry> [1..1] Text 1190
4.4.1.4  BatchBooking <BtchBookg>
Presence: [0..1]
Definition: Identifies whether a single entry per individual transaction or a batch entry for the sum of the
amounts of all transactions within the group of a message is requested.
Usage: Batch booking is used to request and not order a possible batch booking.
Datatype: One of the following values must be used (see "BatchBookingIndicator" on page 1241):
• Meaning When True: Identifies that a batch entry for the sum of the amounts of all transactions in the
batch or message is requested.
• Meaning When False: Identifies that a single entry for each of the transactions in the batch or
message is requested.
4.4.1.5  NumberOfTransactions <NbOfTxs>
Presence: [1..1]
Definition: Number of individual transactions contained in the message.
Datatype: "Max15NumericText" on page 1244
4.4.1.6  ControlSum <CtrlSum>
Presence: [0..1]
Definition: Total of all individual amounts included in the message, irrespective of currencies.
Datatype: "DecimalNumber" on page 1242
4.4.1.7  GroupReturn <GrpRtr>
Presence: [0..1]
Definition: Indicates whether the return applies to the whole group of transactions or to individual
transactions within the original group(s).
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 1242):
• Meaning When True: True
• Meaning When False: False
4.4.1.8  TotalReturnedInterbankSettlementAmount <TtlRtrdIntrBkSttlmAmt>
Presence: [0..1]
Definition: Total amount of money moved between the instructing agent and the instructed agent in the
return message.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
276 March 2026
```

