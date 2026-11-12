---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.6 DateDetails <DtDtls>", "8.4.12.6.2 TradingDate <TradgDt>"]
file_pages: [585, 586]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.6.2 TradingDate <TradgDt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 585 to 586.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 585

```text
CoverExpirationDeadline <CoverXprtnDdln> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
8.4.12.6.2  TradingDate <TradgDt>
Presence: [0..1]
Definition: Date/time at which the deal (rights) was agreed.
TradingDate <TradgDt> contains one of the following elements (see "DateFormat43Choice" on
page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
8.4.12.7  RateAndAmountDetails <RateAndAmtDtls>
Presence: [0..1]
Definition: Provides information about rates and amounts related to a corporate action option.
Impacted by: C24 "GrossDistributionRate2Rule", C26 "GrossDistributionRate3Rule", C42
"NetDistributionRate1Rule", C44 "NetDistributionRate2Rule", C63 "SecondLevelTax1Rule", C65
"SecondLevelTax2Rule", C67 "SecondLevelTax3Rule", C73 "WithholdingTaxRate1Rule", C75
"WithholdingTaxRate2Rule"
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 585 February 2026
```

## File page 586

```text
RateAndAmountDetails <RateAndAmtDtls> contains the following CorporateActionRate141
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   GrossDistributionRate <GrssDstrbtnRate> [0..*] ± 587
   NetDistributionRate <NetDstrbtnRate> [0..*] ± 588
   GrossInterestRateUsedForPayment
<GrssIntrstRateUsdForPmt>
[0..*] ± 588
   MaximumAllowedOversubscriptionRate
<MaxAllwdOvrsbcptRate>
[0..1] Rate 589
   ProrationRate <PrratnRate> [0..1] ± 589
   WithholdingTaxRate <WhldgTaxRate> [0..*] ± 589
   SecondLevelTax <ScndLvlTax> [0..*] ± 590
   AdditionalTax <AddtlTax> [0..1] ± 590
   TaxableIncomePerDividendShare
<TaxblIncmPerDvddShr>
[0..*] ± 591
Constraints
• GrossDistributionRate2Rule
If GrossDistributionRate is repeated, then:
- RateTypeAndAmountAndRateStatus/RateType/Code values must all be different in each
occurrence of GrossDistributionRate. (MT 566 NVR C4 ).
• GrossDistributionRate3Rule
Only a single occurrence of either GrossDistributionRate/Amount or GrossDistributionRate/
AmountAndRateStatus may be present. Both elements may not be present together. (MT 566 NVR
C3).
• NetDistributionRate1Rule
If NetDistributionRate is repeated, then RateTypeAndAmountAndRateStatus/RateType/Code values
must all be different in each occurrence of NetDistributionRate. (MT 566 NVR C4 ).
• NetDistributionRate2Rule
Only a single occurrence of either NetDistributionRate/Amount may be present. Both elements may
not be present together. (MT 566 NVR C3).
• SecondLevelTax1Rule
If SecondLevelTax is repeated, then SecondLevelTax/RateTypeAndRate/RateType/Code values
must all be different in each occurrence of SecondLevelTax.
(MT 564 NVR C8).
• SecondLevelTax2Rule
Only a single occurrence of either SecondLevelTax/Amount or SecondLevelTax/Rate or
SecondLevelTax/NotSpecifiedRate may be present, only one of these elements may be present.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 586 February 2026
```

