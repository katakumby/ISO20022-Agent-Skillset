---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.66 Statement83", "35.1.16.66.2 Frequency <Frqcy>"]
file_pages: [1605]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.66.2 Frequency <Frqcy>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1605 to 1605.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1605

```text
35.1.16.66.2  Frequency <Frqcy>
Presence: [0..1]
Definition: Frequency of the statement.
Frequency <Frqcy> contains one of the following elements (see "Frequency25Choice" on page 1478
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1478
Or}   Proprietary <Prtry> [1..1] ± 1479
35.1.16.66.3  UpdateType <UpdTp>
Presence: [0..1]
Definition: Indicates whether the statement is complete or contains changes only.
UpdateType <UpdTp> contains one of the following elements (see "UpdateType15Choice" on
page 1628 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1628
Or}   Proprietary <Prtry> [1..1] ± 1628
35.1.16.66.4  StatementBasis <StmtBsis>
Presence: [0..1]
Definition: Type of balance on which the statement is prepared.
StatementBasis <StmtBsis> contains one of the following elements (see "StatementBasis7Choice" on
page 1858 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1858
Or}   Proprietary <Prtry> [1..1] ± 1858
35.1.16.66.5  StatementType <StmtTp>
Presence: [0..1]
Definition: Type of balance on which the statement is prepared.
StatementType <StmtTp> contains one of the following elements (see "StatementType5Choice" on
page 1860 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1860
Or}   Proprietary <Prtry> [1..1] ± 1860
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1605 March 2026
```

