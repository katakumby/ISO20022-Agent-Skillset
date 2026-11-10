---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.9 Date Time Period", "35.1.9.1 DateAndPeriod3Choice", "35.1.9.1.2 StatementPeriod <StmtPrd>"]
file_pages: [1443]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.9.1.2 StatementPeriod <StmtPrd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1443 to 1443.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1443

```text
StatementDate <StmtDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
35.1.9.1.2  StatementPeriod <StmtPrd>
Presence: [1..1]
Definition: Period for the statement.
StatementPeriod <StmtPrd> contains one of the following elements (see "Period7Choice" on
page 1434 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTimeToDateTime <FrDtTmToDtTm> [1..1] ± 1435
Or}   FromDateToDate <FrDtToDt> [1..1] ± 1435
35.1.9.2  DateTimePeriod1
Definition: Time span defined by a start date and time, and an end date and time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 1443
   ToDateTime <ToDtTm> [1..1] DateTime 1443
35.1.9.2.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the period starts.
Datatype: "ISODateTime" on page 2185
35.1.9.2.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the period ends.
Datatype: "ISODateTime" on page 2185
35.1.10 Document
35.1.10.1  DocumentNumber13
Definition: Identification of a document.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1443 March 2026
```

