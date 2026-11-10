---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.23 AcknowledgementReason9"]
file_pages: [3159]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.23 AcknowledgementReason9

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3159 to 3159.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3159

```text
82.1.30.23  AcknowledgementReason9
Definition: Specifies additional information about the processed instruction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 3159
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3159
82.1.30.23.1  Code <Cd>
Presence: [1..1]
Definition: Reason provided for the status.
Code <Cd> contains one of the following elements (see "AcknowledgementReason12Choice" on
page 3159 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3159
Or}   Proprietary <Prtry> [1..1] ± 3160
82.1.30.23.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 3327
82.1.30.24  AcknowledgementReason12Choice
Definition: Choice of format for the acknowledgement reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3159
Or}   Proprietary <Prtry> [1..1] ± 3160
82.1.30.24.1  Code <Cd>
Presence: [1..1]
Definition: Specifies additional information about the processed instruction.
Datatype: "AcknowledgementReason5Code" on page 3211
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline. Processed on best effort basis.
SMPG MarketPracticeRuleDiscrepency Instruction is accepted but does not
comply with the market practice rule
published for the concerned market or
process.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3159 August 2026
```

