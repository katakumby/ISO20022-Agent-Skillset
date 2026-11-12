---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.20 PeriodDetails <PrdDtls>", "3.4.11.20.7 DepositorySuspensionPeriodForWithdrawal <DpstrySspnsnPrdForWdrwl>"]
file_pages: [155, 156]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.20.7 DepositorySuspensionPeriodForWithdrawal <DpstrySspnsnPrdForWdrwl>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 155 to 156.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 155

```text
Definition: Period during which the participant of the account servicer can revoke change or withdraw its
instructions.
AccountServicerRevocabilityPeriod <AcctSvcrRvcbltyPrd> contains one of the following elements
(see "Period6Choice" on page 854 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 854
Or}   PeriodCode <PrdCd> [1..1] CodeSet 855
3.4.11.20.7  DepositorySuspensionPeriodForWithdrawal <DpstrySspnsnPrdForWdrwl>
Presence: [0..1]
Definition: Period defining the last date on which withdrawal in street name requests on the outturn
security will be accepted and the date on which the suspension will be released and withdrawal by
transfer processing on the outturn security will resume.
DepositorySuspensionPeriodForWithdrawal <DpstrySspnsnPrdForWdrwl> contains one of the
following elements (see "Period12Choice" on page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
3.4.11.21  RateAndAmountDetails <RateAndAmtDtls>
Presence: [0..1]
Definition: Provides information about rates and amounts related to a corporate action option.
Impacted by: C43 "GrossDistributionRate2Rule", C45 "GrossDistributionRate3Rule", C78
"NetDistributionRate1Rule", C80 "NetDistributionRate2Rule", C105 "SecondLevelTax1Rule", C107
"SecondLevelTax2Rule", C109 "SecondLevelTax3Rule", C114 "WithholdingTaxRate1Rule", C116
"WithholdingTaxRate2Rule"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 155 February 2026
```

## File page 156

```text
RateAndAmountDetails <RateAndAmtDtls> contains the following CorporateActionRate139
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalTax <AddtlTax> [0..1] ± 157
   GrossDistributionRate <GrssDstrbtnRate> [0..*] ± 157
   NetDistributionRate <NetDstrbtnRate> [0..*] ± 158
   GrossInterestRateUsedForPayment
<GrssIntrstRateUsdForPmt>
[0..*] ± 159
   MaximumAllowedOversubscriptionRate
<MaxAllwdOvrsbcptRate>
[0..1] ± 160
   ProrationRate <PrratnRate> [0..1] ± 160
   WithholdingTaxRate <WhldgTaxRate> [0..*] ± 161
   SecondLevelTax <ScndLvlTax> [0..*] ± 161
   TaxableIncomePerDividendShare
<TaxblIncmPerDvddShr>
[0..*] ± 161
   IssuerDeclaredExchangeRate <IssrDclrdXchgRate> [0..1] ± 162
   TaxOnIncome <TaxOnIncm> [0..1] ± 162
   BidInterval <BidIntrvl> [0..1] ± 162
Constraints
• GrossDistributionRate2Rule
If GrossDistributionRate is repeated, then:
- RateTypeAndAmountAndRateStatus/RateType/Code values must all be different in each
occurrence of GrossDistributionRate. (MT 564 NVR C8).
• GrossDistributionRate3Rule
Only a single occurrence of either GrossDistributionRate/Amount or GrossDistributionRate/
AmountAndRateStatus or GrossDistributionRate/NotSpecifiedRate may be present, only one of
these elements may be present. (MT 564 NVR C7).
• NetDistributionRate1Rule
If NetDistributionRate is repeated, then RateTypeAndAmountAndRateStatus/RateType/Code values
must all be different in each occurrence of NetDistributionRate. (MT 564 NVR C8).
• NetDistributionRate2Rule
Only a single occurrence of either NetDistributionRate/Amount or NetDistributionRate/
AmountAndRateStatus or NetDistributionRate/NotSpecifiedRate may be present, and only one of
these elements may be present. (MT 564 NVR C7).
• SecondLevelTax1Rule
If SecondLevelTax is repeated, then SecondLevelTax/RateTypeAndRate/RateType/Code values
must all be different in each occurrence of SecondLevelTax.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 156 February 2026
```

