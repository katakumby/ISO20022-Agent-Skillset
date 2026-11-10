---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.21 SettlementTransactionCondition34Choice", "82.1.19.21.2 Proprietary <Prtry>"]
file_pages: [3002]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.21.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3002 to 3002.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3002

```text
CodeName Name Definition
(eg custodian) in its own books and not
through a securities settlement system
(e.g. CSD system).
BPSS PartialSuccessfulBuyIn Identification of settlement instructions
created as a result of a partial successful
buy-in.
82.1.19.21.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement conditions expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.22  OriginalBusinessInstruction1
Definition: Unique identification, as assigned by the original requestor, to unambiguously identify the
business instruction message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 3002
   MessageNameIdentification <MsgNmId> [0..1] Text 3002
   CreationDateTime <CreDtTm> [0..1] DateTime 3002
82.1.19.22.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the original initiating party, to unambiguously identify
the original instruction message.
Datatype: "Max35Text" on page 3328
82.1.19.22.2  MessageNameIdentification <MsgNmId>
Presence: [0..1]
Definition: Specifies the instruction message name identifier to which the message refers.
Datatype: "Max35Text" on page 3328
82.1.19.22.3  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3002 August 2026
```

