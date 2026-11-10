---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.2.1 OriginalMessageIdentification <OrgnlMsgId>"]
file_pages: [289]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.2.1 OriginalMessageIdentification <OrgnlMsgId>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 289 to 289.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 289

```text
4.4.2.1  OriginalMessageIdentification <OrgnlMsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the original instructing party, to unambiguously
identify the original message.
Datatype: "Max35Text" on page 609
4.4.2.2  OriginalMessageNameIdentification <OrgnlMsgNmId>
Presence: [1..1]
Definition: Specifies the original message name identifier to which the message refers.
Datatype: "Max35Text" on page 609
4.4.2.3  OriginalCreationDateTime <OrgnlCreDtTm>
Presence: [0..1]
Definition: Date and time at which the original message was created.
Datatype: "ISODateTime" on page 603
4.4.2.4  ReversalReasonInformation <RvslRsnInf>
Presence: [0..*]
Definition: Provides detailed information on the reversal reason.
ReversalReasonInformation <RvslRsnInf> contains the following PaymentReversalReason10
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Originator <Orgtr> [0..1] ± 289
   Reason <Rsn> [0..1]  290
{Or     Code <Cd> [1..1] CodeSet 291
Or}     Proprietary <Prtry> [1..1] Text 291
   AdditionalInformation <AddtlInf> [0..*] Text 291
4.4.2.4.1  Originator <Orgtr>
Presence: [0..1]
Definition: Party that issues the reversal.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 289 March 2026
```

