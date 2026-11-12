---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["15 camt.016.001.04 GetCurrencyExchangeRateV04", "15.4 Message Building Blocks", "15.4.2 CurrencyQueryDefinition <CcyQryDef>", "15.4.2.2 CurrencyCriteria <CcyCrit>"]
file_pages: [508]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.016.001.04"]
---

# 15.4.2.2 CurrencyCriteria <CcyCrit>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 508 to 508.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 508

```text
15.4.2.2  CurrencyCriteria <CcyCrit>
Presence: [0..1]
Definition: Defines of the currency query criteria.
CurrencyCriteria <CcyCrit> contains one of the following CurrencyCriteriaDefinition1Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QueryName <QryNm> [1..1] Text 508
Or}   NewCriteria <NewCrit> [1..1]  508
     NewQueryName <NewQryNm> [0..1] Text 508
     SearchCriteria <SchCrit> [1..*]  508
       SourceCurrency <SrcCcy> [1..1] CodeSet C1 509
       TargetCurrency <TrgtCcy> [1..1] CodeSet C1 509
15.4.2.2.1  QueryName <QryNm>
Presence: [1..1]
Definition: Recalls the criteria (search and return criteria) defined in a preceding query.
Datatype: "Max35Text" on page 889
15.4.2.2.2  NewCriteria <NewCrit>
Presence: [1..1]
Definition: Defines the criteria based on which the information is extracted.
NewCriteria <NewCrit> contains the following CurrencyExchangeCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NewQueryName <NewQryNm> [0..1] Text 508
   SearchCriteria <SchCrit> [1..*]  508
     SourceCurrency <SrcCcy> [1..1] CodeSet C1 509
     TargetCurrency <TrgtCcy> [1..1] CodeSet C1 509
15.4.2.2.2.1  NewQueryName <NewQryNm>
Presence: [0..1]
Definition: Name of the query defined by the search criteria and return criteria.
Datatype: "Max35Text" on page 889
15.4.2.2.2.2  SearchCriteria <SchCrit>
Presence: [1..*]
Definition: Defines the criteria based on which the information is extracted.
Approved by the Payments SEG on 04 February 2025 camt.016.001.04 GetCurrencyExchangeRateV04
Cash Management - Maintenance 2024 - 2025 508 February 2025
```

