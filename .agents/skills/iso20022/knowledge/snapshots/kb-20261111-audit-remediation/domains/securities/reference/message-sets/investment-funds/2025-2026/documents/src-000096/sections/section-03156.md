---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.7 CustodyStatementOfHoldings2", "66.1.5.7.1 StatementGeneralDetails <StmtGnlDtls>", "66.1.5.7.1.5 UpdateType <UpdTp>"]
file_pages: [4385]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.7.1.5 UpdateType <UpdTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4385 to 4385.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4385

```text
Definition: Frequency of the statement.
Frequency <Frqcy> contains one of the following elements (see
"FrequencyCodeAndDSSCode1Choice" on page 5129 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FrequencyAsCode <FrqcyAsCd> [1..1] CodeSet 5129
Or}   FrequencyAsDSS <FrqcyAsDSS> [1..1] ± 5130
66.1.5.7.1.5  UpdateType <UpdTp>
Presence: [1..1]
Definition: Indicates whether the report is complete or contains changes only.
UpdateType <UpdTp> contains one of the following elements (see
"StatementUpdateTypeCodeAndDSSCodeChoice" on page 5163 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StatementUpdateTypeAsCode <StmtUpdTpAsCd> [1..1] CodeSet 5163
Or}   StatementUpdateTypeAsDSS <StmtUpdTpAsDSS> [1..1] ± 5164
66.1.5.7.1.6  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.5.7.1.7  StatementBasis <StmtBsis>
Presence: [1..1]
Definition: Type of balance on which the statement is prepared.
StatementBasis <StmtBsis> contains one of the following elements (see
"StatementBasisCodeAndDSSCodeChoice" on page 5162 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StatementBasisAsCode <StmtBsisAsCd> [1..1] CodeSet 5163
Or}   StatementBasisAsDSS <StmtBsisAsDSS> [1..1] ± 5163
66.1.5.7.1.8  ReportNumber <RptNb>
Presence: [0..1]
Definition: Sequential number of the statement.
Datatype: "Max5NumericText" on page 5404
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4385 May 2026
```

