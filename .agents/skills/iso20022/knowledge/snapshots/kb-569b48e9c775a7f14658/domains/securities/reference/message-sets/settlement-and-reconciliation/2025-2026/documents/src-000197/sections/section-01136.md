---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.44 UnilateralSplit3Choice", "35.1.16.44.1 Code <Cd>"]
file_pages: [1581]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.44.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1581 to 1581.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1581

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1581
Or}   Proprietary <Prtry> [1..1] ± 1581
35.1.16.44.1  Code <Cd>
Presence: [1..1]
Definition: Unilateral split expressed as an ISO 20022 code.
Datatype: "SecuritiesTransactionType5Code" on page 2160
CodeName Name Definition
TRAD Trade Relates to the settlement of a trade.
35.1.16.44.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unilateral split expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.45  ForeignExchangeTerms23
Definition: Provides information about the terms of the foreign exchange transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 1581
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 1582
   ExchangeRate <XchgRate> [1..1] Rate 1582
   ResultingAmount <RsltgAmt> [1..1] Amount C1, C9 1582
35.1.16.45.1  UnitCurrency <UnitCcy>
Presence: [1..1]
Definition: Currency in which the rate of exchange is expressed in a currency exchange. In the example
1GBP = xxxCUR, the unit currency is GBP.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 2044
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1581 March 2026
```

