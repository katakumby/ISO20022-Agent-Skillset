---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.12 Financial Instrument", "7.1.12.2 FinancialInstrument21", "7.1.12.2.7 DenominationCurrency <DnmtnCcy>"]
file_pages: [338]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.12.2.7 DenominationCurrency <DnmtnCcy>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 338 to 338.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 338

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
7.1.12.2.7  DenominationCurrency <DnmtnCcy>
Presence: [0..1]
Definition: Currency in which a security is issued or redenominated.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 492
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
7.1.12.2.8  RequestedNAVCurrency <ReqdNAVCcy>
Presence: [0..1]
Definition: Currency to be used for pricing the fund. This currency must be among the set of currencies
in which the price may be expressed, as stated in the prospectus.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 492
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
7.1.12.2.9  DualFundIndicator <DualFndInd>
Presence: [0..1]
Definition: Indicates whether the fund has two prices.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
• Meaning When True: Yes
• Meaning When False: No
7.1.12.2.10  CountryOfDomicile <CtryOfDmcl>
Presence: [0..1]
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 338 March 2026
```

