---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.7 CustodyStatementOfHoldings2", "66.1.5.7.1 StatementGeneralDetails <StmtGnlDtls>", "66.1.5.7.1.1 Reference <Ref>"]
file_pages: [4384]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.7.1.1 Reference <Ref>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4384 to 4384.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4384

```text
StatementGeneralDetails <StmtGnlDtls> contains the following Statement7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4384
   StatementDateTime <StmtDtTm> [1..1] ± 4384
   CreationDateTime <CreDtTm> [0..1] ± 4384
   Frequency <Frqcy> [1..1] ± 4384
   UpdateType <UpdTp> [1..1] ± 4385
   ActivityIndicator <ActvtyInd> [1..1] Indicator 4385
   StatementBasis <StmtBsis> [1..1] ± 4385
   ReportNumber <RptNb> [0..1] Text 4385
66.1.5.7.1.1  Reference <Ref>
Presence: [1..1]
Definition: Reference of the statement.
Datatype: "Max35Text" on page 5403
66.1.5.7.1.2  StatementDateTime <StmtDtTm>
Presence: [1..1]
Definition: Date of the statement.
StatementDateTime <StmtDtTm> contains one of the following elements (see
"DateAndDateTimeChoice" on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
66.1.5.7.1.3  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Preparation date of the statement.
CreationDateTime <CreDtTm> contains one of the following elements (see
"DateAndDateTimeChoice" on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
66.1.5.7.1.4  Frequency <Frqcy>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4384 May 2026
```

