---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.25 CashMovementDetails <CshMvmntDtls>", "3.4.11.25.13 ForeignExchangeDetails <FXDtls>"]
file_pages: [233, 234, 235]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.25.13 ForeignExchangeDetails <FXDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 233 to 235.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 233

```text
EarliestPaymentDate <EarlstPmtDt> contains one of the following elements (see
"DateFormat30Choice" on page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
3.4.11.25.13  ForeignExchangeDetails <FXDtls>
Presence: [0..1]
Definition: Exchange rate between the amount and the resulting amount.
ForeignExchangeDetails <FXDtls> contains the following elements (see "ForeignExchangeTerms39"
on page 873 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 873
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 873
   ExchangeRate <XchgRate> [1..1] Rate 873
   ResultingAmount <RsltgAmt> [0..1] Amount C1, C10 874
3.4.11.25.14  RateAndAmountDetails <RateAndAmtDtls>
Presence: [0..1]
Definition: Provides information about the corporate action option.
Impacted by: C21 "DeemedRate1Rule", C22 "DeemedRate2Rule", C44 "GrossDistributionRate2Rule",
C46 "GrossDistributionRate3Rule", C79 "NetDistributionRate1Rule", C81 "NetDistributionRate2Rule",
C106 "SecondLevelTax1Rule", C108 "SecondLevelTax2Rule", C110 "SecondLevelTax3Rule", C115
"WithholdingTaxRate1Rule", C117 "WithholdingTaxRate2Rule"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 233 February 2026
```

## File page 234

```text
RateAndAmountDetails <RateAndAmtDtls> contains the following Rate48 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalTax <AddtlTax> [0..1] ± 236
   GrossDistributionRate <GrssDstrbtnRate> [0..*] ± 236
   GrossInterestRateUsedForPayment
<GrssIntrstRateUsdForPmt>
[0..*] ± 236
   WithholdingTaxRate <WhldgTaxRate> [0..*] ± 237
   SecondLevelTax <ScndLvlTax> [0..*] ± 237
   ChargesFees <ChrgsFees> [0..1] ± 238
   EarlySolicitationFeeRate <EarlySlctnFeeRate> [0..1] ± 238
   FiscalStamp <FsclStmp> [0..1] ± 239
   ThirdPartyIncentiveRate <ThrdPtyIncntivRate> [0..1] ± 239
   NetDistributionRate <NetDstrbtnRate> [0..*] ± 239
   ApplicableRate <AplblRate> [0..1] ± 240
   SolicitationFeeRate <SlctnFeeRate> [0..1] ± 240
   TaxCreditRate <TaxCdtRate> [0..1] ± 241
   TaxOnIncome <TaxOnIncm> [0..1] ± 241
   TaxOnProfits <TaxOnPrfts> [0..1] ± 241
   TaxReclaimRate <TaxRclmRate> [0..1] ± 242
   EqualisationRate <EqulstnRate> [0..1] ± 242
   DeemedRate <DmdRate> [0..*] ± 242
Constraints
• DeemedRate1Rule
If DeemedRate is repeated, then DeemedRate/RateTypeAndAmountAndRateStatus/RateType/Code
values and DeemedRate/RateTypeAndRate/RateType/Code values must all be different in each
occurrence of DeemedRate.
(MT 564 NVR C8).
• DeemedRate2Rule
Only a single occurrence of either DeemedRate/Amount or DeemedRate/Rate or DeemedRate/
NotSpecifiedRate may be present, only one of these elements may be present.
(MT 564 NVR C7).
• GrossDistributionRate2Rule
If GrossDistributionRate is repeated, then:
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 234 February 2026
```

## File page 235

```text
- RateTypeAndAmountAndRateStatus/RateType/Code values must all be different in each
occurrence of GrossDistributionRate. (MT 564 NVR C8).
• GrossDistributionRate3Rule
Only a single occurrence of either GrossDistributionRate/Amount or GrossDistributionRate/
AmountAndRateStatus or GrossDistributionRate/NotSpecifiedRate may be present, and only one of
these elements may be present.
(MT 564 NVR C7).
• NetDistributionRate1Rule
If NetDistributionRate is repeated, then:
- RateTypeAndAmountAndRateStatus/RateType/Code values must all be different in each
occurrence of NetDistributionRate. (MT 564 NVR C8).
• NetDistributionRate2Rule
Only a single occurrence of either NetDistributionRate/Amount or NetDistributionRate/
AmountAndRateStatus or NetDistributionRate/NotSpecifiedRate may be present, and only one of
these elements may be present.
(MT 564 NVR C7).
• SecondLevelTax1Rule
If SecondLevelTax is repeated, then SecondLevelTax/RateTypeAndRate/RateType/Code values
must all be different in each occurrence of SecondLevelTax.
(MT 564 NVR C8).
• SecondLevelTax2Rule
Only a single occurrence of either SecondLevelTax/Amount or SecondLevelTax/Rate or
SecondLevelTax/NotSpecifiedRate may be present, only one of these elements may be present.
(MT 564 NVR C7).
• SecondLevelTax3Rule
If at least one occurrence of SecondLevelTax is present, then at least one occurrence of
WithholdingTaxRate must be present. (MT 564 NVR C19).
On Condition
    /SecondLevelTax[*] is present
Following Must be True
    /WithholdingTaxRate[*] Must be present
• WithholdingTaxRate1Rule
If WithholdingTaxRate is repeated, then WithholdingTaxRate/RateTypeAndRate/RateType/Code
values must all be different in each occurrence of WithholdingTaxRate.
(MT 564 NVR C8).
• WithholdingTaxRate2Rule
Only a single occurrence of either WithholdingTaxRate/Amount or WithholdingTaxRate/Rate or
WithholdingTaxRate/NotSpecifiedRate may be present, only one of these elements may be present.
(MT 564 NVR C7).
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 235 February 2026
```

