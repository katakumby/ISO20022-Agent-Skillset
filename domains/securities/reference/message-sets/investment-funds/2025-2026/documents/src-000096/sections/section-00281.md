---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["19 semt.003.001.02 AccountingStatementOfHoldingsV02", "19.4 Message Building Blocks", "19.4.5 StatementGeneralDetails <StmtGnlDtls>", "19.4.5.7 StatementBasis <StmtBsis>"]
file_pages: [394]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.02"]
---

# 19.4.5.7 StatementBasis <StmtBsis>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 394 to 394.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 394

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
19.4.5.7  StatementBasis <StmtBsis>
Presence: [1..1]
Definition: Type of balance on which the statement is prepared.
StatementBasis <StmtBsis> contains one of the following elements (see
"StatementBasisCodeAndDSSCodeChoice" on page 5162 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StatementBasisAsCode <StmtBsisAsCd> [1..1] CodeSet 5163
Or}   StatementBasisAsDSS <StmtBsisAsDSS> [1..1] ± 5163
19.4.5.8  ReportNumber <RptNb>
Presence: [0..1]
Definition: Sequential number of the statement.
Datatype: "Max5NumericText" on page 5404
19.4.5.9  AuditedIndicator <AudtdInd>
Presence: [1..1]
Definition: Indicates whether the statement is audited.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
19.4.6 AccountDetails <AcctDtls>
Presence: [1..1]
Definition: The safekeeping or investment account.
Approved by the Securities SEG on 27 January 2026 semt.003.001.02
AccountingStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 394 May 2026
```

