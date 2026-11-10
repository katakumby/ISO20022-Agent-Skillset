---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.5 BatchBooking <BtchBookg>"]
file_pages: [300]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.5 BatchBooking <BtchBookg>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 300 to 300.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 300

```text
4.4.3.5  BatchBooking <BtchBookg>
Presence: [0..1]
Definition: Identifies whether a single entry per individual transaction or a batch entry for the sum of the
amounts of all transactions within the group of a message is requested.
Usage: Batch booking is used to request and not order a possible batch booking.
Datatype: One of the following values must be used (see "BatchBookingIndicator" on page 605):
• Meaning When True: Identifies that a batch entry for the sum of the amounts of all transactions in the
batch or message is requested.
• Meaning When False: Identifies that a single entry for each of the transactions in the batch or
message is requested.
4.4.3.6  PaymentInformationReversal <PmtInfRvsl>
Presence: [0..1]
Definition: Indicates whether or not the reversal applies to the complete original payment information
group or to individual transactions within that group.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 605):
• Meaning When True: True
• Meaning When False: False
4.4.3.7  ReversalReasonInformation <RvslRsnInf>
Presence: [0..*]
Definition: Provides detailed information on the reversal reason.
ReversalReasonInformation <RvslRsnInf> contains the following PaymentReversalReason10
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Originator <Orgtr> [0..1] ± 300
   Reason <Rsn> [0..1]  301
{Or     Code <Cd> [1..1] CodeSet 302
Or}     Proprietary <Prtry> [1..1] Text 302
   AdditionalInformation <AddtlInf> [0..*] Text 302
4.4.3.7.1  Originator <Orgtr>
Presence: [0..1]
Definition: Party that issues the reversal.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 300 March 2026
```

