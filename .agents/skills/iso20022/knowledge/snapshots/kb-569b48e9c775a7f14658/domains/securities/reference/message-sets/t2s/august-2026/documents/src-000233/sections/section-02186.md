---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.13 Financial Instrument", "82.1.13.4 FinancialInstrument21", "82.1.13.4.4 ProductGroup <PdctGrp>"]
file_pages: [2949]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.13.4.4 ProductGroup <PdctGrp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2949 to 2949.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2949

```text
CodeName Name Definition
DIST Distribution Income is distributed to the investors in
the fund.
ACCU Accumulation Income is added to the capital of the
fund.
82.1.13.4.4  ProductGroup <PdctGrp>
Presence: [0..1]
Definition: Company specific description of a group of funds.
Datatype: "Max140Text" on page 3326
82.1.13.4.5  UmbrellaName <UmbrllNm>
Presence: [0..1]
Definition: Name of the umbrella fund in which financial instrument is contained.
Datatype: "Max35Text" on page 3328
82.1.13.4.6  BaseCurrency <BaseCcy>
Presence: [0..1]
Definition: Currency of the investment fund class.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 3212
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
82.1.13.4.7  DenominationCurrency <DnmtnCcy>
Presence: [0..1]
Definition: Currency in which a security is issued or redenominated.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 3212
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2949 August 2026
```

