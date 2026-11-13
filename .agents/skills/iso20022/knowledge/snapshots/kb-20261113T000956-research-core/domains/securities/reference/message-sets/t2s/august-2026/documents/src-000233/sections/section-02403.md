---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.47 AcknowledgementReason25Choice"]
file_pages: [3194]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.47 AcknowledgementReason25Choice

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3194 to 3194.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3194

```text
Reason <Rsn> contains the following elements (see "AcknowledgementReason22" on page 3194 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 3195
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3195
82.1.30.47  AcknowledgementReason25Choice
Definition: Choice of format for the acknowledgement reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3194
Or}   Proprietary <Prtry> [1..1] ± 3194
82.1.30.47.1  Code <Cd>
Presence: [1..1]
Definition: Specifies additional information about the processed instruction.
Datatype: "AcknowledgementReason11Code" on page 3211
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline. Processed on best effort basis.
OTHR Other Other. See Narrative.
SMPG MarketPracticeRuleDiscrepency Instruction is accepted but does not
comply with the market practice rule
published for the concerned market or
process.
82.1.30.47.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies additional information about the processed instruction.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.30.48  AcknowledgementReason22
Definition: Specifies additional information about the processed instruction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3194 August 2026
```

