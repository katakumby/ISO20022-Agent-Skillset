---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["6 MX secl.005.001.02 MarginReportV02", "6.4 Message Building Blocks", "6.4.5 ReportDetails <RptDtls>", "6.4.5.4 NonClearingMember <NonClrMmb>"]
file_pages: [242, 243, 244]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.005.001.02"]
---

# 6.4.5.4 NonClearingMember <NonClrMmb>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 242 to 244.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 242

```text
6.4.5.4  NonClearingMember <NonClrMmb>
Presence: [0..*]
Definition: Provides details about the non clearing member identification and account.
NonClearingMember <NonClrMmb> contains the following elements (see
PartyIdentificationAndAccount31 on page 450 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 450
   AlternateIdentification <AltrnId> [0..1] ± 450
   AdditionalInformation <AddtlInf> [0..1] ± C3 451
   ClearingAccount <ClrAcct> [0..1] ± 451
6.4.5.5  MarginCalculationSummary <MrgnClctnSummry>
Presence: [0..1]
Definition: Provides the margin calculation summary per margin account.
MarginCalculationSummary <MrgnClctnSummry> contains the following elements (see
MarginCalculation1 on page 430 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalMarginAmount <TtlMrgnAmt> [1..1] ± 431
   CollateralOnDeposit <CollOnDpst> [0..*] ± 431
   MinimumRequirementDeposit <MinRqrmntDpst> [0..1] Amount   'C1,
  'C7
431
   MarginResult <MrgnRslt> [0..1]  432
{Or     ExcessAmount <XcssAmt> [1..1] Amount   'C1,
  'C7
432
Or}     DeficitAmount <DfcitAmt> [1..1] Amount   'C1,
  'C7
433
6.4.5.6  MarginCalculation <MrgnClctn>
Presence: [1..*]
Definition: Provides the margin details such as the exposure amount and the initial margin.
Impacted by:   'C12 MarginTypePresenceRule  '
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.005.001.02 MarginReportV02
March 2026 242
```

## File page 243

```text
MarginCalculation <MrgnClctn> contains the following elements (see MarginCalculation2 on
page 406 for details)
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
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.005.001.02 MarginReportV02
March 2026 243
```

## File page 244

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
MX secl.005.001.02 MarginReportV02
March 2026 244
```

