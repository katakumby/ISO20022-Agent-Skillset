---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.2 OriginalGroupInformation <OrgnlGrpInf>", "5.4.2.2 OriginalMessageNameIdentification <OrgnlMsgNmId>"]
file_pages: [591]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.2.2 OriginalMessageNameIdentification <OrgnlMsgNmId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 591 to 591.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 591

```text
Definition: Point to point reference, as assigned by the original instructing party, to unambiguously
identify the original message.
Datatype: "Max35Text" on page 1246
5.4.2.2  OriginalMessageNameIdentification <OrgnlMsgNmId>
Presence: [1..1]
Definition: Specifies the original message name identifier to which the message refers.
Datatype: "Max35Text" on page 1246
5.4.2.3  OriginalCreationDateTime <OrgnlCreDtTm>
Presence: [0..1]
Definition: Date and time at which the original message was created.
Datatype: "ISODateTime" on page 1239
5.4.2.4  ReversalReasonInformation <RvslRsnInf>
Presence: [0..*]
Definition: Provides detailed information on the reversal reason.
ReversalReasonInformation <RvslRsnInf> contains the following PaymentReversalReason10
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Originator <Orgtr> [0..1] ± 591
   Reason <Rsn> [0..1]  592
{Or     Code <Cd> [1..1] CodeSet 593
Or}     Proprietary <Prtry> [1..1] Text 593
   AdditionalInformation <AddtlInf> [0..*] Text 593
5.4.2.4.1  Originator <Orgtr>
Presence: [0..1]
Definition: Party that issues the reversal.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
591 March 2026
```

