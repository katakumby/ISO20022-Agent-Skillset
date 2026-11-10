---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.17 Price", "12.1.17.3 PriceRateOrAmount3Choice", "12.1.17.3.1 Rate <Rate>"]
file_pages: [465]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.17.3.1 Rate <Rate>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 465 to 465.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 465

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 465
Or}   Amount <Amt> [1..1] Amount   'C2 465
12.1.17.3.1  Rate <Rate>
Presence: [1..1]
Definition: Price expressed as a rate, that is percentage.
Datatype: PercentageRate on page 491
12.1.17.3.2  Amount <Amt>
Presence: [1..1]
Definition: Price expressed as a currency and value.
Impacted by:   'C2 ActiveOrHistoricCurrency  '
Datatype: ActiveOrHistoricCurrencyAnd13DecimalAmount on page 471
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
12.1.17.4  Price4
Definition: Provides the value and optionaly the type of price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 465
   Type <Tp> [0..1] CodeSet 466
12.1.17.4.1  Value <Val>
Presence: [1..1]
Definition: Value of the price.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 465
```

