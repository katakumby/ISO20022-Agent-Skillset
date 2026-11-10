---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.11 Margin Call Calculation", "12.1.11.1 MarginCalculation2", "12.1.11.1.7 MarginTypeAmount <MrgnTpAmt>", "12.1.11.1.7.2 VariationMargin <VartnMrgn>", "12.1.11.1.7.2.3 TotalMarkToMarket <TtlMrkToMkt>"]
file_pages: [422]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.11.1.7.2.3 TotalMarkToMarket <TtlMrkToMkt>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 422 to 422.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 422

```text
Definition: Amount expressed in the reporting currency.
Datatype: ImpliedCurrencyAndAmount on page 472
12.1.11.1.7.2.3  TotalMarkToMarket <TtlMrkToMkt>
Presence: [1..1]
Definition: Net unrealised profit or loss on the value of the netted, gross and failing positions.
TotalMarkToMarket <TtlMrkToMkt> contains the following Amount2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
422
   ReportingAmount <RptgAmt> [1..1] Amount 423
12.1.11.1.7.2.3.1  OriginalCurrencyAmount <OrgnlCcyAmt>
Presence: [0..1]
Definition: Amount expressed in the original currency.
Impacted by:   'C1 ActiveCurrency  ',   'C7 CurrencyAmount  '
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
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 422
```

