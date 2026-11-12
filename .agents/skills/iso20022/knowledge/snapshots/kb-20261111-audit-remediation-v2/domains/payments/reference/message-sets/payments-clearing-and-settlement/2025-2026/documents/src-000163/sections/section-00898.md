---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.11 Miscellaneous", "10.1.11.7 OriginalBusinessQuery1"]
file_pages: [1193]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.11.7 OriginalBusinessQuery1

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1193 to 1193.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1193

```text
10.1.11.7  OriginalBusinessQuery1
Definition: Unique identification, as assigned by the original requestor, to unambiguously identify the
business query message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 1193
   MessageNameIdentification <MsgNmId> [0..1] Text 1193
   CreationDateTime <CreDtTm> [0..1] DateTime 1193
10.1.11.7.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the original initiating party, to unambiguously identify
the original query message.
Datatype: "Max35Text" on page 1246
10.1.11.7.2  MessageNameIdentification <MsgNmId>
Presence: [0..1]
Definition: Specifies the query message name identifier to which the message refers.
Datatype: "Max35Text" on page 1246
10.1.11.7.3  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 1239
10.1.12 Party Identification
10.1.12.1  PartyIdentification272
Definition: Specifies the identification of a person or an organisation.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1193 March 2026
```

