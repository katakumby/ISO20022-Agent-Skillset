---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.11 Margin Call Calculation"]
file_pages: [406, 407, 408]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.11 Margin Call Calculation

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 406 to 408.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 406

```text
12.1.11 Margin Call Calculation
12.1.11.1  MarginCalculation2
Definition: Provides the details on the margin calculation per financial instrument or per currency.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 406
```

## File page 407

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ±   'C8,
C9, C10,
  'C11,
  'C12
409
   ExposureAmount <XpsrAmt> [0..1]  410
     OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
410
     ReportingAmount <RptgAmt> [1..1] Amount 411
   TotalMarginAmount <TtlMrgnAmt> [1..1] ± 411
   CollateralOnDeposit <CollOnDpst> [0..*] ± 411
   MinimumRequirementDeposit <MinRqrmntDpst> [0..1] Amount   'C1,
  'C7
412
   MarginResult <MrgnRslt> [0..1]  412
{Or     ExcessAmount <XcssAmt> [1..1] Amount   'C1,
  'C7
413
Or}     DeficitAmount <DfcitAmt> [1..1] Amount   'C1,
  'C7
413
   MarginTypeAmount <MrgnTpAmt> [0..1]  414
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
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 407
```

## File page 408

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
       Type <Tp> [1..1]  428
{Or         Code <Cd> [1..1] CodeSet 428
Or}         Proprietary <Prtry> [1..1] ± 429
       Amount <Amt> [1..1]  429
         OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
429
         ReportingAmount <RptgAmt> [1..1] Amount 430
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 430
Constraints
• MarginTypePresenceRule
(Rule)
On Condition
    /MarginTypeAmount is present
Following Must be True
    /MarginTypeAmount/InitialMargin Must be present
 Or    /MarginTypeAmount/VariationMargin[*] Must be present
 Or    /MarginTypeAmount/OtherMargin[*] Must be present
Error handling:
– Error severity: Fatal
– Error Code: X00240
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 408
```

