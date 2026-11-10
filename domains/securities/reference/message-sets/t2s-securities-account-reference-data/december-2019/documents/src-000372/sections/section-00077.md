---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["11 Message Items Types", "11.1 MessageComponents", "11.1.4 Miscellaneous", "11.1.4.2 OriginalBusinessInstruction1", "11.1.4.2.2 MessageNameIdentification <MsgNmId>"]
file_pages: [83]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.1.4.2.2 MessageNameIdentification <MsgNmId>

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 83 to 83.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 83

```text
Datatype: "Max35Text" on page 100
11.1.4.2.2  MessageNameIdentification <MsgNmId>
Presence: [0..1]
Definition: Specifies the instruction message name identifier to which the message refers.
Datatype: "Max35Text" on page 100
11.1.4.2.3  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 97
11.1.4.3  OriginalBusinessQuery1
Definition: Unique identification, as assigned by the original requestor, to unambiguously identify the
business query message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 83
   MessageNameIdentification <MsgNmId> [0..1] Text 83
   CreationDateTime <CreDtTm> [0..1] DateTime 83
11.1.4.3.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the original initiating party, to unambiguously identify
the original query message.
Datatype: "Max35Text" on page 100
11.1.4.3.2  MessageNameIdentification <MsgNmId>
Presence: [0..1]
Definition: Specifies the query message name identifier to which the message refers.
Datatype: "Max35Text" on page 100
11.1.4.3.3  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 97
11.1.4.4  Pagination1
Definition: Number used to sequence pages when it is not possible for data to be conveyed in a single
message and the data has to be split across several pages (messages).
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
Message Items Types
Target2-Securities - Securities Account Reference Data 83 December 2019
```

