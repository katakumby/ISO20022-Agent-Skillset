---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.67 Statement80", "35.1.16.67.4 StatementPeriod <StmtPrd>"]
file_pages: [1607]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.67.4 StatementPeriod <StmtPrd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1607 to 1607.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1607

```text
Definition: Reference common to all pages of a statement.
Datatype: "Max35Text" on page 2192
35.1.16.67.4  StatementPeriod <StmtPrd>
Presence: [1..1]
Definition: Period for the statement.
StatementPeriod <StmtPrd> contains one of the following elements (see "Period7Choice" on
page 1434 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTimeToDateTime <FrDtTmToDtTm> [1..1] ± 1435
Or}   FromDateToDate <FrDtToDt> [1..1] ± 1435
35.1.16.67.5  Frequency <Frqcy>
Presence: [0..1]
Definition: Frequency of the statement.
Frequency <Frqcy> contains one of the following elements (see "Frequency25Choice" on page 1478
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1478
Or}   Proprietary <Prtry> [1..1] ± 1479
35.1.16.67.6  UpdateType <UpdTp>
Presence: [0..1]
Definition: Indicates whether the statement is complete or contains changes only.
UpdateType <UpdTp> contains one of the following elements (see "UpdateType15Choice" on
page 1628 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1628
Or}   Proprietary <Prtry> [1..1] ± 1628
35.1.16.67.7  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1607 March 2026
```

