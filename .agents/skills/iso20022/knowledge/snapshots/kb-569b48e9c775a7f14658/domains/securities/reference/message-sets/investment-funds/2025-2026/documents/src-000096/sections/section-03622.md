---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.34 AdditionalParameters1", "66.1.28.34.2 Currency <Ccy>"]
file_pages: [4872]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.34.2 Currency <Ccy>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4872 to 4872.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4872

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.28.34.2  Currency <Ccy>
Presence: [0..1]
Definition: Specifies the currency.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
66.1.28.34.3  GeographicalArea <GeoArea>
Presence: [0..1]
Definition: Specifies the geographical area, eg, Asia-Pacific, Europe, Middle-East.
Datatype: "Max35Text" on page 5403
66.1.28.35  ResidualCash1
Definition: Specifies whether there is cash in the account awaiting investment.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ResidualCashIndicator <RsdlCshInd> [1..1] Indicator 4872
   Currency <Ccy> [0..1] CodeSet C1 4872
66.1.28.35.1  ResidualCashIndicator <RsdlCshInd>
Presence: [1..1]
Definition: Indicates whether there is cash in the account awaiting investment.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.28.35.2  Currency <Ccy>
Presence: [0..1]
Definition: Currency of the cash.
Impacted by: C1 "ActiveCurrency"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4872 May 2026
```

