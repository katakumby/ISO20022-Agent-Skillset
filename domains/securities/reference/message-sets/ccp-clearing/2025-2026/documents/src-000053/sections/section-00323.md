---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.11 Margin Call Calculation", "12.1.11.1 MarginCalculation2", "12.1.11.1.7 MarginTypeAmount <MrgnTpAmt>"]
file_pages: [414, 415]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.11.1.7 MarginTypeAmount <MrgnTpAmt>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 414 to 415.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 414

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
12.1.11.1.7  MarginTypeAmount <MrgnTpAmt>
Presence: [0..1]
Definition: Provides margin calculation details such as the initial margin amount, the variation margin
amount or other margin type amounts.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 414
```

## File page 415

```text
MarginTypeAmount <MrgnTpAmt> contains the following Margin3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InitialMargin <InitlMrgn> [0..1]  416
     OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
416
     ReportingAmount <RptgAmt> [1..1] Amount 417
   VariationMargin <VartnMrgn> [0..*]  417
     FinancialInstrumentIdentification <FinInstrmId> [0..1] ±   'C8,
C9, C10,
  'C11,
  'C12
418
     TotalVariationMargin <TtlVartnMrgn> [1..*]  420
       ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 420
       AmountDetails <AmtDtls> [1..1]  421
         OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
421
         ReportingAmount <RptgAmt> [1..1] Amount 421
     TotalMarkToMarket <TtlMrkToMkt> [1..1]  422
       OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
422
       ReportingAmount <RptgAmt> [1..1] Amount 423
     MarkToMarketNetted <MrkToMktNetd> [0..*]  423
       OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
423
       ReportingAmount <RptgAmt> [1..1] Amount 424
     MarkToMarketGross <MrkToMktGrss> [0..*]  424
       OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
424
       ReportingAmount <RptgAmt> [1..1] Amount 425
     MarkToMarketFails <MrkToMktFls> [0..*]  425
       OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
425
       ReportingAmount <RptgAmt> [1..1] Amount 426
     FailsHaircut <FlsHrcut> [0..1]  426
       OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
426
       ReportingAmount <RptgAmt> [1..1] Amount 427
   OtherMargin <OthrMrgn> [0..*]  C17 427
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 415
```

