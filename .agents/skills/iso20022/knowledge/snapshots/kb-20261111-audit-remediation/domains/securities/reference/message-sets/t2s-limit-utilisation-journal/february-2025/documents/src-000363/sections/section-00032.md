---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.6 Miscellaneous", "4.1.6.3 MessageHeader1"]
file_pages: [34]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.6.3 MessageHeader1

Source: [src-000363](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 34 to 34.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 34

```text
• Meaning When True: Yes
• Meaning When False: No
4.1.6.3  MessageHeader1
Definition: Set of characteristics, such as the identification or the creation date and time, specific to the
message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 34
   CreationDateTime <CreDtTm> [0..1] DateTime 34
4.1.6.3.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 46
4.1.6.3.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 43
4.1.6.4  OriginalBusinessInstruction1
Definition: Unique identification, as assigned by the original requestor, to unambiguously identify the
business instruction message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 34
   MessageNameIdentification <MsgNmId> [0..1] Text 34
   CreationDateTime <CreDtTm> [0..1] DateTime 35
4.1.6.4.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the original initiating party, to unambiguously identify
the original instruction message.
Datatype: "Max35Text" on page 46
4.1.6.4.2  MessageNameIdentification <MsgNmId>
Presence: [0..1]
Definition: Specifies the instruction message name identifier to which the message refers.
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
Message Items Types
Target2-Securities - Limit Utilisation Journal 34 February 2025
```

