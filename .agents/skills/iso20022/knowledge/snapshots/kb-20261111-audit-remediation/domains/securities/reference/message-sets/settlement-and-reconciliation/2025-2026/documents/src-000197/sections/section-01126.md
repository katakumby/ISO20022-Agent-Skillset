---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.36 Statement79", "35.1.16.36.6 UpdateType <UpdTp>"]
file_pages: [1571]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.36.6 UpdateType <UpdTp>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1571 to 1571.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1571

```text
Frequency <Frqcy> contains one of the following elements (see "Frequency25Choice" on page 1478
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1478
Or}   Proprietary <Prtry> [1..1] ± 1479
35.1.16.36.6  UpdateType <UpdTp>
Presence: [0..1]
Definition: Indicates whether the statement is complete or contains changes only.
UpdateType <UpdTp> contains one of the following elements (see "UpdateType15Choice" on
page 1628 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1628
Or}   Proprietary <Prtry> [1..1] ± 1628
35.1.16.36.7  StatementBasis <StmtBsis>
Presence: [1..1]
Definition: Type of balance on which the statement is prepared.
StatementBasis <StmtBsis> contains one of the following elements (see "StatementBasis8Choice" on
page 1859 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1859
Or}   Proprietary <Prtry> [1..1] ± 1859
35.1.16.36.8  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.16.36.9  SubAccountIndicator <SubAcctInd>
Presence: [1..1]
Definition: Indicates whether the statement reports holdings at sub-safekeeping account level.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1571 March 2026
```

