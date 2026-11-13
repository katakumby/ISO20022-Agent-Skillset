---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.4 Collateral", "12.1.4.1 Collateral3", "12.1.4.1.3 CollateralType <CollTp>"]
file_pages: [383]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.4.1.3 CollateralType <CollTp>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 383 to 383.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 383

```text
Datatype: ActiveCurrencyAndAmount on page 470
Constraints
• ActiveCurrency
(Rule)
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
Error handling:
– Error severity: Fatal
– Error Code: D00005
– Error Text: Invalid currency code
• CurrencyAmount
(Rule)
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Error handling:
– Error severity: Fatal
– Error Code: D00007
– Error Text: Invalid currency code or too many decimal digits.
12.1.4.1.3  CollateralType <CollTp>
Presence: [1..1]
Definition: Provides the type of collateral, such as securities or cash.
Datatype: CollateralType2Code on page 475
CodeName Name Definition
CASH Cash Collateral type is cash.
SECU Securities Collateral type is securities.
12.1.4.2  Collateral6
Definition: Provides the current and market value of the collateral held.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PostHaircutValue <PstHrcutVal> [1..1] Amount   'C1,
  'C7
384
   MarketValue <MktVal> [1..1] Amount   'C1,
  'C7
384
   CollateralType <CollTp> [1..1] CodeSet 385
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 383
```

