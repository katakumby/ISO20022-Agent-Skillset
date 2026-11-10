---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.39 AcknowledgementReason14Choice"]
file_pages: [1939]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.39 AcknowledgementReason14Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1939 to 1939.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1939

```text
35.1.29.39  AcknowledgementReason14Choice
Definition: Choice of format for the acknowledgement reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1939
Or}   Proprietary <Prtry> [1..1] ± 1939
35.1.29.39.1  Code <Cd>
Presence: [1..1]
Definition: Specifies additional information about the processed instruction.
Datatype: "AcknowledgementReason6Code" on page 2044
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline. Processed on best effort basis.
SMPG MarketPracticeRuleDiscrepency Instruction is accepted but does not
comply with the market practice rule
published for the concerned market or
process.
OTHR Other Other. See Narrative.
NSTP NotStraightThroughProcessing Instruction was not straight through
processing and had to be processed
manually.
LATE MarketDeadlineMissed Instruction was received after market
deadline.
35.1.29.39.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies additional information about the processed instruction.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.40  DeniedStatus15Choice
Definition: Specifies whether the status is provided with a reason or not.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1939 March 2026
```

