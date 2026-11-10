---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.19 RateAndAmountDetails <RateAndAmtDtls>"]
file_pages: [442]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.19 RateAndAmountDetails <RateAndAmtDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 442 to 442.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 442

```text
DocumentationDeadline <DcmnttnDdln> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
7.4.13.19  RateAndAmountDetails <RateAndAmtDtls>
Presence: [0..1]
Definition: Provides information about rates and amounts related to a corporate action option.
Impacted by: C31 "GrossDistributionRate2Rule", C33 "GrossDistributionRate3Rule", C50
"NetDistributionRate1Rule", C52 "NetDistributionRate2Rule", C72 "SecondLevelTax1Rule", C74
"SecondLevelTax2Rule", C76 "SecondLevelTax3Rule", C80 "WithholdingTaxRate1Rule", C82
"WithholdingTaxRate2Rule"
RateAndAmountDetails <RateAndAmtDtls> contains the following CorporateActionRate140
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalTax <AddtlTax> [0..1] ± 443
   GrossDistributionRate <GrssDstrbtnRate> [0..*] ± 444
   NetDistributionRate <NetDstrbtnRate> [0..*] ± 444
   GrossInterestRateUsedForPayment
<GrssIntrstRateUsdForPmt>
[0..*] ± 445
   MaximumAllowedOversubscriptionRate
<MaxAllwdOvrsbcptRate>
[0..1] ± 446
   ProrationRate <PrratnRate> [0..1] ± 446
   WithholdingTaxRate <WhldgTaxRate> [0..*] ± 447
   SecondLevelTax <ScndLvlTax> [0..*] ± 447
   TaxableIncomePerDividendShare
<TaxblIncmPerDvddShr>
[0..*] ± 447
   TaxOnIncome <TaxOnIncm> [0..1] ± 448
Constraints
• GrossDistributionRate2Rule
If GrossDistributionRate is repeated, then:
- RateTypeAndAmountAndRateStatus/RateType/Code values must all be different in each
occurrence of GrossDistributionRate.
(MT 564 NVR C8).
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 442 February 2026
```

