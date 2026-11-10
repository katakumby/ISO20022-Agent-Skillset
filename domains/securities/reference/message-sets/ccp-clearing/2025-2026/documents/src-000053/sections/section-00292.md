---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.3 Amount", "12.1.3.3 AmountAndDirection27", "12.1.3.3.4 ForeignExchangeDetails <FXDtls>"]
file_pages: [381]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.3.3.4 ForeignExchangeDetails <FXDtls>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 381 to 381.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 381

```text
Constraints
• ActiveOrHistoricCurrency
(Rule)
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
Error handling:
– Error severity: Fatal
– Error Code: D00006
– Error Text: Invalid currency code.
• CurrencyAmount
(Rule)
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Error handling:
– Error severity: Fatal
– Error Code: D00007
– Error Text: Invalid currency code or too many decimal digits.
12.1.3.3.4  ForeignExchangeDetails <FXDtls>
Presence: [0..1]
Definition: Information needed to process a currency exchange or conversion.
ForeignExchangeDetails <FXDtls> contains the following elements (see ForeignExchangeTerms17
on page 385 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet   'C1 386
   QuotedCurrency <QtdCcy> [1..1] CodeSet   'C1 386
   ExchangeRate <XchgRate> [1..1] Rate 387
   ResultingAmount <RsltgAmt> [1..1] Amount   'C1,
  'C7
387
12.1.4 Collateral
12.1.4.1  Collateral3
Definition: Provides the current and market value of the collateral held.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 381
```

