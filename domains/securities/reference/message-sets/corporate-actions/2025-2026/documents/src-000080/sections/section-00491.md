---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.14 RateAndAmountDetails <RateAndAmtDtls>"]
file_pages: [650, 651]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.14 RateAndAmountDetails <RateAndAmtDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 650 to 651.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 650

```text
Following Must be True
    /TaxReclaimDocumentationReference Must be absent
• TaxReclaimDocumentationReferencePresenceRule
If TaxReclaimDocumentationReference is present then BeneficialOwnerReference must be absent.
On Condition
    /TaxReclaimDocumentationReference is present
Following Must be True
    /BeneficialOwnerReference Must be absent
• TaxVoucherPresenceRule
At least one of TaxVoucherReference Or TaxReclaimDocumentationReference Or
BeneficialOwnerReference must be present.
Following Must be True
    /TaxVoucherReference Must be present
 Or    /TaxReclaimDocumentationReference Must be present
 Or    /BeneficialOwnerReference Must be present
8.4.12.11.14  RateAndAmountDetails <RateAndAmtDtls>
Presence: [0..1]
Definition: Provides information about the corporate action option.
Impacted by: C13 "DeemedRate1Rule", C14 "DeemedRate2Rule", C25 "GrossDistributionRate2Rule",
C27 "GrossDistributionRate3Rule", C43 "NetDistributionRate1Rule", C45 "NetDistributionRate2Rule",
C64 "SecondLevelTax1Rule", C66 "SecondLevelTax2Rule", C68 "SecondLevelTax3Rule", C74
"WithholdingTaxRate1Rule", C76 "WithholdingTaxRate2Rule"
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 650 February 2026
```

## File page 651

```text
RateAndAmountDetails <RateAndAmtDtls> contains the following Rate51 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalTax <AddtlTax> [0..1] ± 652
   ChargesFees <ChrgsFees> [0..1] ± 653
   FiscalStamp <FsclStmp> [0..1] Rate 653
   GrossDistributionRate <GrssDstrbtnRate> [0..*] ± 653
   EarlySolicitationFeeRate <EarlySlctnFeeRate> [0..1] ± 654
   ThirdPartyIncentiveRate <ThrdPtyIncntivRate> [0..1] ± 654
   GrossInterestRateUsedForPayment
<GrssIntrstRateUsdForPmt>
[0..*] ± 655
   NetDistributionRate <NetDstrbtnRate> [0..*] ± 655
   ApplicableRate <AplblRate> [0..1] ± 656
   SolicitationFeeRate <SlctnFeeRate> [0..1] ± 656
   TaxCreditRate <TaxCdtRate> [0..1] ± 657
   WithholdingTaxRate <WhldgTaxRate> [0..*] ± 657
   SecondLevelTax <ScndLvlTax> [0..*] ± 657
   TaxOnIncome <TaxOnIncm> [0..1] ± 658
   TaxOnProfits <TaxOnPrfts> [0..1] Rate 658
   TaxReclaimRate <TaxRclmRate> [0..1] Rate 658
   EqualisationRate <EqulstnRate> [0..1] Amount C1 658
   DeemedRate <DmdRate> [0..*] ± 659
Constraints
• DeemedRate1Rule
If DeemedRate is repeated, then DeemedRate/RateTypeAndAmountAndRateStatus/RateType/Code
values and DeemedRate/RateTypeAndRate/RateType/Code values must all be different in each
occurrence of DeemedRate.
(MT 566 NVR C4).
• DeemedRate2Rule
Only a single occurrence of either DeemedRate/Amount or DeemedRate/Rate may be present, only
one of those elements may be present.
(MT 566 NVR C3).
• GrossDistributionRate2Rule
If GrossDistributionRate is repeated, then:
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 651 February 2026
```

