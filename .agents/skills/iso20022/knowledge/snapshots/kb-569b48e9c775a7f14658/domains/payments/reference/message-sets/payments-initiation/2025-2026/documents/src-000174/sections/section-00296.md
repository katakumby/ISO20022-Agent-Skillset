---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.3 RequestedAdviceType <ReqdAdvcTp>", "5.4.2.3.2 DebitAdvice <DbtAdvc>", "5.4.2.3.2.1 Code <Cd>"]
file_pages: [428]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.3.2.1 Code <Cd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 428 to 428.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 428

```text
DebitAdvice <DbtAdvc> contains one of the following AdviceType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 428
Or}   Proprietary <Prtry> [1..1] Text 428
5.4.2.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Advice type, in a coded form.
Datatype: "AdviceType1Code" on page 587
CodeName Name Definition
ADWD AdviceWithDetails Advice with transaction details is
requested.
ADND AdviceWithoutDetails Advice without transaction details is
requested.
5.4.2.3.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Advice type, in a proprietary form.
Datatype: "Max35Text" on page 609
5.4.2.4  BatchBooking <BtchBookg>
Presence: [0..1]
Definition: Identifies whether a single entry per individual transaction or a batch entry for the sum of the
amounts of all transactions within the group of a message is requested.
Usage: Batch booking is used to request and not order a possible batch booking.
Datatype: One of the following values must be used (see "BatchBookingIndicator" on page 605):
• Meaning When True: Identifies that a batch entry for the sum of the amounts of all transactions in the
batch or message is requested.
• Meaning When False: Identifies that a single entry for each of the transactions in the batch or
message is requested.
5.4.2.5  NumberOfTransactions <NbOfTxs>
Presence: [0..1]
Definition: Number of individual transactions contained in the payment information group.
Datatype: "Max15NumericText" on page 608
5.4.2.6  ControlSum <CtrlSum>
Presence: [0..1]
Definition: Total of all individual amounts included in the group, irrespective of currencies.
Datatype: "DecimalNumber" on page 606
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 428 March 2026
```

