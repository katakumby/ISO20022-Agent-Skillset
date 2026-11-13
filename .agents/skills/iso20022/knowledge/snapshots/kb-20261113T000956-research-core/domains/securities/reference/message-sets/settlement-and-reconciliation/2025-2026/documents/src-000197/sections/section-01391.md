---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.28 Statement Update Type"]
file_pages: [1860]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.28 Statement Update Type

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1860 to 1860.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1860

```text
35.1.28 Statement Update Type
35.1.28.1  StatementType5Choice
Definition: Choice of format for the statement type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1860
Or}   Proprietary <Prtry> [1..1] ± 1860
35.1.28.1.1  Code <Cd>
Presence: [1..1]
Definition: Statement type expressed as an ISO 20022 code.
Datatype: "SecuritiesStatementType1Code" on page 2143
CodeName Name Definition
CUST Custody Statement is a custody statement.
ACCT Accounting Statement is an accounting statement.
35.1.28.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Statement type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29 Status
35.1.29.1  SettlementStatus32Choice
Definition: Choice of format for the settlement status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1860 March 2026
```

