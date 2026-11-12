---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.2 StatementOfInvestmentFundTransactions2", "66.1.5.2.1 StatementGeneralDetails <StmtGnlDtls>"]
file_pages: [4348]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.2.1 StatementGeneralDetails <StmtGnlDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4348 to 4348.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4348

```text
Constraints
• TransactionOnAccountOrSubAccountDetailsRule
If StatementGeneralDetails/ActivityIndicator is "true" or "1" (Yes), then either TransactionOnAccount
or SubAccountDetails must be present. If StatementGeneralDetails/ActivityIndicator is "false" or "0"
(No), then TransactionOnAccount and SubAccountDetails are not allowed.
66.1.5.2.1  StatementGeneralDetails <StmtGnlDtls>
Presence: [0..1]
Definition: General information related to the investment fund statement of transactions that is being
cancelled.
StatementGeneralDetails <StmtGnlDtls> contains the following Statement8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4348
   StatementPeriod <StmtPrd> [1..1] ± 4348
   CreationDateTime <CreDtTm> [0..1] ± 4348
   Frequency <Frqcy> [0..1] CodeSet 4349
   UpdateType <UpdTp> [1..1] CodeSet 4349
   ActivityIndicator <ActvtyInd> [1..1] Indicator 4349
   ReportNumber <RptNb> [0..1] Text 4350
66.1.5.2.1.1  Reference <Ref>
Presence: [1..1]
Definition: Reference of the statement.
Datatype: "Max35Text" on page 5403
66.1.5.2.1.2  StatementPeriod <StmtPrd>
Presence: [1..1]
Definition: Period on which the statement is reporting.
StatementPeriod <StmtPrd> contains the following elements (see "DatePeriodDetails" on page 4464
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 4464
   ToDate <ToDt> [1..1] Date 4464
66.1.5.2.1.3  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Creation date of the statement.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4348 May 2026
```

