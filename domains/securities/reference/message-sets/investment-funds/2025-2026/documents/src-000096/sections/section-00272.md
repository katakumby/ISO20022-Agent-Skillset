---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["18 semt.002.001.02 CustodyStatementOfHoldingsV02", "18.4 Message Building Blocks", "18.4.5 StatementGeneralDetails <StmtGnlDtls>", "18.4.5.2 StatementDateTime <StmtDtTm>"]
file_pages: [381]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.02"]
---

# 18.4.5.2 StatementDateTime <StmtDtTm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 381 to 381.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 381

```text
18.4.5.2  StatementDateTime <StmtDtTm>
Presence: [1..1]
Definition: Date of the statement.
StatementDateTime <StmtDtTm> contains one of the following elements (see
"DateAndDateTimeChoice" on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
18.4.5.3  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Preparation date of the statement.
CreationDateTime <CreDtTm> contains one of the following elements (see
"DateAndDateTimeChoice" on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
18.4.5.4  Frequency <Frqcy>
Presence: [1..1]
Definition: Frequency of the statement.
Frequency <Frqcy> contains one of the following elements (see
"FrequencyCodeAndDSSCode1Choice" on page 5129 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FrequencyAsCode <FrqcyAsCd> [1..1] CodeSet 5129
Or}   FrequencyAsDSS <FrqcyAsDSS> [1..1] ± 5130
18.4.5.5  UpdateType <UpdTp>
Presence: [1..1]
Definition: Indicates whether the report is complete or contains changes only.
UpdateType <UpdTp> contains one of the following elements (see
"StatementUpdateTypeCodeAndDSSCodeChoice" on page 5163 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StatementUpdateTypeAsCode <StmtUpdTpAsCd> [1..1] CodeSet 5163
Or}   StatementUpdateTypeAsDSS <StmtUpdTpAsDSS> [1..1] ± 5164
Approved by the Securities SEG on 27 January 2026 semt.002.001.02 CustodyStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 381 May 2026
```

