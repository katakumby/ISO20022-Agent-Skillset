---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.55 NumberCount1Choice", "82.1.19.55.2 TotalNumber <TtlNb>", "82.1.19.55.2.1 CurrentInstructionNumber <CurInstrNb>"]
file_pages: [3043]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.55.2.1 CurrentInstructionNumber <CurInstrNb>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3043 to 3043.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3043

```text
82.1.19.55.2.1  CurrentInstructionNumber <CurInstrNb>
Presence: [1..1]
Definition: Sequential number of the instruction in a range of linked settlement instructions.
Datatype: "Exact3NumericText" on page 3325
82.1.19.55.2.2  TotalOfLinkedInstructions <TtlOfLkdInstrs>
Presence: [1..1]
Definition: Total number of settlement instructions that are linked together.
Datatype: "Exact3NumericText" on page 3325
82.1.19.56  OriginalBusinessQuery1
Definition: Unique identification, as assigned by the original requestor, to unambiguously identify the
business query message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 3043
   MessageNameIdentification <MsgNmId> [0..1] Text 3043
   CreationDateTime <CreDtTm> [0..1] DateTime 3043
82.1.19.56.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the original initiating party, to unambiguously identify
the original query message.
Datatype: "Max35Text" on page 3328
82.1.19.56.2  MessageNameIdentification <MsgNmId>
Presence: [0..1]
Definition: Specifies the query message name identifier to which the message refers.
Datatype: "Max35Text" on page 3328
82.1.19.56.3  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 3320
82.1.19.57  Registration9Choice
Definition: Choice of format for the registration information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3044
Or}   Proprietary <Prtry> [1..1] ± 3044
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3043 August 2026
```

