---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.11 Margin Call Calculation", "12.1.11.1 MarginCalculation2", "12.1.11.1.2 ExposureAmount <XpsrAmt>", "12.1.11.1.2.2 ReportingAmount <RptgAmt>"]
file_pages: [411]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.11.1.2.2 ReportingAmount <RptgAmt>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 411 to 411.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 411

```text
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
12.1.11.1.2.2  ReportingAmount <RptgAmt>
Presence: [1..1]
Definition: Amount expressed in the reporting currency.
Datatype: ImpliedCurrencyAndAmount on page 472
12.1.11.1.3  TotalMarginAmount <TtlMrgnAmt>
Presence: [1..1]
Definition: Provides the total margin amount.
TotalMarginAmount <TtlMrgnAmt> contains the following elements (see AmountAndDirection20 on
page 378 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C2,
  'C6
378
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 379
12.1.11.1.4  CollateralOnDeposit <CollOnDpst>
Presence: [0..*]
Definition: Provides details on the valuation of the collateral on deposit.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 411
```

