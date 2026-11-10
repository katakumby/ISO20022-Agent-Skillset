---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.42 Statement64", "35.1.16.42.6 UpdateType <UpdTp>"]
file_pages: [1579]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.42.6 UpdateType <UpdTp>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1579 to 1579.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1579

```text
Frequency <Frqcy> contains one of the following elements (see "Frequency25Choice" on page 1478
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1478
Or}   Proprietary <Prtry> [1..1] ± 1479
35.1.16.42.6  UpdateType <UpdTp>
Presence: [0..1]
Definition: Indicates whether the statement is complete or contains changes only.
UpdateType <UpdTp> contains one of the following elements (see "UpdateType15Choice" on
page 1628 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1628
Or}   Proprietary <Prtry> [1..1] ± 1628
35.1.16.42.7  StatementStructure <StmtStr>
Presence: [1..1]
Definition: Specifies whether the statement is sorted by status or transaction.
Datatype: "StatementStructure1Code" on page 2171
CodeName Name Definition
STAT Statuses Statement is sorted by status.
TRAN Transactions Statement is sorted by transaction.
35.1.16.42.8  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.16.43  RepurchaseType22Choice
Definition: Choice of format for the repurchase transaction type information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1580
Or}   Proprietary <Prtry> [1..1] ± 1580
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1579 March 2026
```

