---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.8 Date Time", "35.1.8.9 Period2"]
file_pages: [1442]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.8.9 Period2

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1442 to 1442.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1442

```text
DateCode <DtCd> contains one of the following elements (see "SettlementDateCode8Choice" on
page 1438 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1438
Or}   Proprietary <Prtry> [1..1] ± 1438
35.1.8.9  Period2
Definition: Time span defined by a start date and time, and an end date and time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 1442
   ToDate <ToDt> [1..1] Date 1442
35.1.8.9.1  FromDate <FrDt>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODate" on page 2185
35.1.8.9.2  ToDate <ToDt>
Presence: [1..1]
Definition: Date and time at which the range ends.
Datatype: "ISODate" on page 2185
35.1.9 Date Time Period
35.1.9.1  DateAndPeriod3Choice
Definition: Choice between a date and period.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StatementDate <StmtDt> [1..1] ± 1442
Or}   StatementPeriod <StmtPrd> [1..1] ± 1443
35.1.9.1.1  StatementDate <StmtDt>
Presence: [1..1]
Definition: Date of the statement.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1442 March 2026
```

