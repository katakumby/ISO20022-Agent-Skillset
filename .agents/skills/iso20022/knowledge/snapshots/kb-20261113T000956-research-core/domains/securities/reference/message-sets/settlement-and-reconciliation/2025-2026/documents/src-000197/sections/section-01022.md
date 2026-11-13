---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.11 Financial Instrument", "35.1.11.3 FinancialInstrument21", "35.1.11.3.8 RequestedNAVCurrency <ReqdNAVCcy>"]
file_pages: [1460]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.11.3.8 RequestedNAVCurrency <ReqdNAVCcy>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1460 to 1460.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1460

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
35.1.11.3.8  RequestedNAVCurrency <ReqdNAVCcy>
Presence: [0..1]
Definition: Currency to be used for pricing the fund. This currency must be among the set of currencies
in which the price may be expressed, as stated in the prospectus.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 2044
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
35.1.11.3.9  DualFundIndicator <DualFndInd>
Presence: [0..1]
Definition: Indicates whether the fund has two prices.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.11.3.10  CountryOfDomicile <CtryOfDmcl>
Presence: [0..1]
Definition: Country where the fund has legal domicile as reflected in the ISIN classification.
Impacted by: C7 "Country"
Datatype: "CountryCode" on page 2057
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
35.1.11.3.11  RegisteredDistributionCountry <RegdDstrbtnCtry>
Presence: [0..*]
Definition: Countries where the fund is registered for distribution.
Impacted by: C7 "Country"
Datatype: "CountryCode" on page 2057
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1460 March 2026
```

