---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.76 Statement62", "35.1.16.76.5 UpdateType <UpdTp>"]
file_pages: [1622]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.76.5 UpdateType <UpdTp>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1622 to 1622.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1622

```text
StatementDateTime <StmtDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
35.1.16.76.5  UpdateType <UpdTp>
Presence: [0..1]
Definition: Indicates whether the statement is complete or contains changes only.
UpdateType <UpdTp> contains one of the following elements (see "UpdateType15Choice" on
page 1628 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1628
Or}   Proprietary <Prtry> [1..1] ± 1628
35.1.16.76.6  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.16.77  LegalFramework3Choice
Definition: Choice of format for the legal framework.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1622
Or}   Proprietary <Prtry> [1..1] ± 1623
35.1.16.77.1  Code <Cd>
Presence: [1..1]
Definition: Legal framework expressed as an ISO 20022 code.
Datatype: "LegalFramework1Code" on page 2086
CodeName Name Definition
FRAN PensionLivree Relates to the French legal framework
for repos, that is, relates to a "Pension
Livrée".
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1622 March 2026
```

