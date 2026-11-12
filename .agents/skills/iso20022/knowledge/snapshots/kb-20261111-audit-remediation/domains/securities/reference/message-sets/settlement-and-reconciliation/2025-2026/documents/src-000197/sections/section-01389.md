---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.11 SettlementDetails221", "35.1.26.11.24 CashSubBalanceType <CshSubBalTp>"]
file_pages: [1858]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.11.24 CashSubBalanceType <CshSubBalTp>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1858 to 1858.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1858

```text
35.1.26.11.24  CashSubBalanceType <CshSubBalTp>
Presence: [0..1]
Definition: Specifies the cash sub balance type indicator, for example, the restriction type for a market
infrastructure.
CashSubBalanceType <CshSubBalTp> contains the following elements (see
"GenericIdentification30" on page 1502 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.27 Statement Basis
35.1.27.1  StatementBasis7Choice
Definition: Choice of format for the statement basis.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1858
Or}   Proprietary <Prtry> [1..1] ± 1858
35.1.27.1.1  Code <Cd>
Presence: [1..1]
Definition: Statement basis expressed as an ISO 20022 code.
Datatype: "StatementBasis1Code" on page 2171
CodeName Name Definition
CONT Contractual The statement is based on contractual
settlement date irrespective of settled
data positions.
SETT Settled The statement is based on settled date
positions to the knowledge of the sender
at the time of the statement preparation.
TRAD Traded The statement is based on trade date
positions.
35.1.27.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Statement basis expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1858 March 2026
```

