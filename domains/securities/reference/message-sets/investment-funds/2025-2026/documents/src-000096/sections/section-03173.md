---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.13 AccountingStatementOfHoldings2", "66.1.5.13.1 StatementGeneralDetails <StmtGnlDtls>", "66.1.5.13.1.1 Reference <Ref>"]
file_pages: [4403]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.13.1.1 Reference <Ref>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4403 to 4403.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4403

```text
StatementGeneralDetails <StmtGnlDtls> contains the following Statement6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4403
   StatementDateTime <StmtDtTm> [1..1] ± 4403
   CreationDateTime <CreDtTm> [0..1] ± 4403
   Frequency <Frqcy> [1..1] ± 4404
   UpdateType <UpdTp> [1..1] ± 4404
   ActivityIndicator <ActvtyInd> [1..1] Indicator 4404
   StatementBasis <StmtBsis> [1..1] ± 4404
   ReportNumber <RptNb> [0..1] Text 4404
   AuditedIndicator <AudtdInd> [1..1] Indicator 4405
66.1.5.13.1.1  Reference <Ref>
Presence: [1..1]
Definition: Reference of the statement.
Datatype: "Max35Text" on page 5403
66.1.5.13.1.2  StatementDateTime <StmtDtTm>
Presence: [1..1]
Definition: Date of the statement.
StatementDateTime <StmtDtTm> contains one of the following elements (see
"DateAndDateTimeChoice" on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
66.1.5.13.1.3  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Preparation date of the statement.
CreationDateTime <CreDtTm> contains one of the following elements (see
"DateAndDateTimeChoice" on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4403 May 2026
```

