---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.11 Financial Instrument", "35.1.11.3 FinancialInstrument21", "35.1.11.3.4 ProductGroup <PdctGrp>"]
file_pages: [1459]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.11.3.4 ProductGroup <PdctGrp>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1459 to 1459.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1459

```text
CodeName Name Definition
DIST Distribution Income is distributed to the investors in
the fund.
ACCU Accumulation Income is added to the capital of the
fund.
35.1.11.3.4  ProductGroup <PdctGrp>
Presence: [0..1]
Definition: Company specific description of a group of funds.
Datatype: "Max140Text" on page 2191
35.1.11.3.5  UmbrellaName <UmbrllNm>
Presence: [0..1]
Definition: Name of the umbrella fund in which financial instrument is contained.
Datatype: "Max35Text" on page 2192
35.1.11.3.6  BaseCurrency <BaseCcy>
Presence: [0..1]
Definition: Currency of the investment fund class.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 2044
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
35.1.11.3.7  DenominationCurrency <DnmtnCcy>
Presence: [0..1]
Definition: Currency in which a security is issued or redenominated.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 2044
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1459 March 2026
```

