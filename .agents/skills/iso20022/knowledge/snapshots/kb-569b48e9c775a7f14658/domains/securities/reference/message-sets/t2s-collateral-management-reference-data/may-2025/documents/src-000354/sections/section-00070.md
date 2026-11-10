---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.6 Price"]
file_pages: [75]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.6 Price

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 75 to 75.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 75

```text
Definition: Nation with its own government.
Impacted by: C2 "Country"
Datatype: "CountryCode" on page 78
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
10.1.6 Price
10.1.6.1  PriceRateOrAmount6Choice
Definition: Choice of formats for the price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 75
Or   Amount <Amt> [1..1] Amount 75
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C5 75
10.1.6.1.1  Rate <Rate>
Presence: [1..1]
Definition: Price expressed as a rate, that is percentage.
Datatype: "PercentageRate" on page 82
10.1.6.1.2  Amount <Amt>
Presence: [1..1]
Definition: Price expressed as an implied currency and amount.
Datatype: "ImpliedCurrencyAndAmount" on page 77
10.1.6.1.3  AmountWithCurrency <AmtWthCcy>
Presence: [1..1]
Definition: Price expressed as an explicit currency and amount.
Impacted by: C2 "ActiveOrHistoricCurrency", C5 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 76
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 17 April 2025. Message Items Types
Target2-Securities - Collateral Management Reference Data 75 May 2025
```

