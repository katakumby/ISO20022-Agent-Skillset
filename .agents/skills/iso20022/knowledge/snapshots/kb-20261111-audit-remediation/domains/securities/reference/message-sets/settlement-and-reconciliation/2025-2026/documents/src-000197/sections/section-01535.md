---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.30 Transaction Type", "35.1.30.3 TransactionActivity3Choice"]
file_pages: [2034]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.30.3 TransactionActivity3Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2034 to 2034.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2034

```text
Definition: Trade conditions expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.30.3  TransactionActivity3Choice
Definition: Choice of format for the transaction activity identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2034
Or}   Proprietary <Prtry> [1..1] ± 2034
35.1.30.3.1  Code <Cd>
Presence: [1..1]
Definition: Transaction type expressed as an ISO 20022 code.
Datatype: "TransactionActivity1Code" on page 2173
CodeName Name Definition
BOLE BorrowingLendingActivity Transaction relates to lending/borrowing.
CLAI MarketClaim Transaction relates to a market claim
following a corporate action.
COLL CollateralActivity Transaction relates to collateral.
CORP CorporateActionActivity Transaction relates to corporate action.
SETT SettlementandClearingActivity Transaction relates to settlement and
clearing.
35.1.30.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Transaction type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2034 March 2026
```

