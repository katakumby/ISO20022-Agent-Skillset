---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.1 GroupHeader <GrpHdr>", "5.4.1.4 BatchBooking <BtchBookg>"]
file_pages: [579]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.1.4 BatchBooking <BtchBookg>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 579 to 579.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 579

```text
Authorisation <Authstn> contains one of the following elements (see "Authorisation1Choice" on
page 1190 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1190
Or}   Proprietary <Prtry> [1..1] Text 1190
5.4.1.4  BatchBooking <BtchBookg>
Presence: [0..1]
Definition: Identifies whether a single entry per individual transaction or a batch entry for the sum of the
amounts of all transactions within the group of a message is requested.
Usage: Batch booking is used to request and not order a possible batch booking.
Datatype: One of the following values must be used (see "BatchBookingIndicator" on page 1241):
• Meaning When True: Identifies that a batch entry for the sum of the amounts of all transactions in the
batch or message is requested.
• Meaning When False: Identifies that a single entry for each of the transactions in the batch or
message is requested.
5.4.1.5  NumberOfTransactions <NbOfTxs>
Presence: [1..1]
Definition: Number of individual transactions contained in the message.
Datatype: "Max15NumericText" on page 1244
5.4.1.6  ControlSum <CtrlSum>
Presence: [0..1]
Definition: Total of all individual amounts included in the message, irrespective of currencies.
Datatype: "DecimalNumber" on page 1242
5.4.1.7  GroupReversal <GrpRvsl>
Presence: [0..1]
Definition: Indicates whether the reversal applies to the whole group of transactions or to individual
transactions within the original group.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 1242):
• Meaning When True: True
• Meaning When False: False
5.4.1.8  TotalReversedInterbankSettlementAmount <TtlRvsdIntrBkSttlmAmt>
Presence: [0..1]
Definition: Total amount of money moved between the instructing agent and the instructed agent in the
reversal message.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
579 March 2026
```

