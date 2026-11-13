---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.22 Status19Choice", "35.1.29.22.1 AffirmationStatus <AffirmSts>"]
file_pages: [1907]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.22.1 AffirmationStatus <AffirmSts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1907 to 1907.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1907

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}     Proprietary <Prtry> [1..1] ± 1918
Constraints
• StatusRule
If a specific Status is requested, then it must be in line with the statuses available for the message
type requested.
35.1.29.22.1  AffirmationStatus <AffirmSts>
Presence: [1..1]
Definition: Status of affirmation of a trade.
AffirmationStatus <AffirmSts> contains one of the following elements (see
"AffirmationStatus8Choice" on page 1878 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1878
Or}   Proprietary <Prtry> [1..1] ± 1879
35.1.29.22.2  AllocationStatus <AllcnSts>
Presence: [1..1]
Definition: Provides the status of allocation of collateral to cover the instruction.
AllocationStatus <AllcnSts> contains one of the following AllocationSatus3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1907
Or}   Proprietary <Prtry> [1..1] ± 1907
35.1.29.22.2.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of allocation of collateral to cover the instruction.
Datatype: "AllocationStatus1Code" on page 2046
CodeName Name Definition
AOLF FullyAllocated Instruction has been fully covered by
collateral.
AOLP PartiallyAllocated Instruction has been partially covered by
collateral.
35.1.29.22.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the status of allocation of collateral to cover the instruction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1907 March 2026
```

