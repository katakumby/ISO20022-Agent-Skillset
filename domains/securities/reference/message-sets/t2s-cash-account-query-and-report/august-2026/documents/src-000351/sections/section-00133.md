---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.7 Miscellaneous", "7.1.7.2 MessageHeader1", "7.1.7.2.1 MessageIdentification <MsgId>"]
file_pages: [148]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.7.2.1 MessageIdentification <MsgId>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 148 to 148.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 148

```text
7.1.7.2.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 183
7.1.7.2.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 180
7.1.7.3  OriginalBusinessInstruction1
Definition: Unique identification, as assigned by the original requestor, to unambiguously identify the
business instruction message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 148
   MessageNameIdentification <MsgNmId> [0..1] Text 148
   CreationDateTime <CreDtTm> [0..1] DateTime 148
7.1.7.3.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the original initiating party, to unambiguously identify
the original instruction message.
Datatype: "Max35Text" on page 183
7.1.7.3.2  MessageNameIdentification <MsgNmId>
Presence: [0..1]
Definition: Specifies the instruction message name identifier to which the message refers.
Datatype: "Max35Text" on page 183
7.1.7.3.3  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 180
7.1.8 Party Identification
7.1.8.1  PartyIdentification274
Definition: Set of elements used to identify a person or an organisation.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 148 August 2026
```

