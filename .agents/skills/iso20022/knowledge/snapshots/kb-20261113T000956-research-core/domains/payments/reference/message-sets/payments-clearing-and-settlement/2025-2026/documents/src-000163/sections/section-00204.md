---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.2 OriginalMessageNameIdentification <OrgnlMsgNmId>"]
file_pages: [289]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.2.2 OriginalMessageNameIdentification <OrgnlMsgNmId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 289 to 289.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 289

```text
Definition: Point to point reference, as assigned by the original instructing party, to unambiguously
identify the original message.
Datatype: "Max35Text" on page 1246
4.4.2.2  OriginalMessageNameIdentification <OrgnlMsgNmId>
Presence: [1..1]
Definition: Specifies the original message name identifier to which the message refers.
Datatype: "Max35Text" on page 1246
4.4.2.3  OriginalCreationDateTime <OrgnlCreDtTm>
Presence: [0..1]
Definition: Date and time at which the original message was created.
Datatype: "ISODateTime" on page 1239
4.4.2.4  ReturnReasonInformation <RtrRsnInf>
Presence: [0..*]
Definition: Provides detailed information on the return reason.
Impacted by: C62 "ReturnReasonRule"
ReturnReasonInformation <RtrRsnInf> contains the following PaymentReturnReason7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Originator <Orgtr> [0..1] ± 289
   Reason <Rsn> [0..1]  290
{Or     Code <Cd> [1..1] CodeSet 291
Or}     Proprietary <Prtry> [1..1] Text 291
   AdditionalInformation <AddtlInf> [0..*] Text 291
Constraints
• ReturnReasonRule
If Reason/Code is equal to NARR, then AddititionalInformation must be present.
On Condition
    /Reason/Code is present
 And    /Reason/Code is within DataType <<Code>> ValidationRuleNarrative1Code
 And    /Reason is present
Following Must be True
    /AdditionalInformation[1] Must be present
4.4.2.4.1  Originator <Orgtr>
Presence: [0..1]
Definition: Party that issues the return.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
289 March 2026
```

