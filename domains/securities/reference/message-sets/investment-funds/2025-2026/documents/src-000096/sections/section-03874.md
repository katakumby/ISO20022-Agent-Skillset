---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.43 Statement Basis", "66.1.43.1 StatementBasisCodeAndDSSCodeChoice", "66.1.43.1.1 StatementBasisAsCode <StmtBsisAsCd>"]
file_pages: [5163]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.43.1.1 StatementBasisAsCode <StmtBsisAsCd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5163 to 5163.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5163

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StatementBasisAsCode <StmtBsisAsCd> [1..1] CodeSet 5163
Or}   StatementBasisAsDSS <StmtBsisAsDSS> [1..1] ± 5163
66.1.43.1.1  StatementBasisAsCode <StmtBsisAsCd>
Presence: [1..1]
Definition: Statement basis expressed as a code.
Datatype: "StatementBasis1Code" on page 5364
CodeName Name Definition
CONT Contractual The statement is based on contractual
settlement date irrespective of settled
data positions.
SETT Settled The statement is based on settled date
positions to the knowledge of the sender
at the time of the statement preparation.
TRAD Traded The statement is based on trade date
positions.
66.1.43.1.2  StatementBasisAsDSS <StmtBsisAsDSS>
Presence: [1..1]
Definition: Statement basis expressed as a data source scheme and a code used within the data source
scheme.
StatementBasisAsDSS <StmtBsisAsDSS> contains the following elements (see
"GenericIdentification7" on page 4538 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [1..1] Text 4539
   Information <Inf> [1..1] Text 4539
66.1.44 Statement Update Type
66.1.44.1  StatementUpdateTypeCodeAndDSSCodeChoice
Definition: Choice between formats for the update type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StatementUpdateTypeAsCode <StmtUpdTpAsCd> [1..1] CodeSet 5163
Or}   StatementUpdateTypeAsDSS <StmtUpdTpAsDSS> [1..1] ± 5164
66.1.44.1.1  StatementUpdateTypeAsCode <StmtUpdTpAsCd>
Presence: [1..1]
Definition: Update type expressed as a code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5163 May 2026
```

