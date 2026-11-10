---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.25 CashMovementDetails <CshMvmntDtls>", "3.4.11.25.1 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [204]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.25.1 CreditDebitIndicator <CdtDbtInd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 204 to 204.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 204

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TaxOnIncome <TaxOnIncm> [0..1] ± 241
     TaxOnProfits <TaxOnPrfts> [0..1] ± 241
     TaxReclaimRate <TaxRclmRate> [0..1] ± 242
     EqualisationRate <EqulstnRate> [0..1] ± 242
     DeemedRate <DmdRate> [0..*] ± 242
   PriceDetails <PricDtls> [0..1]  C42 243
     GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 244
     GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 244
     CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 245
Constraints
• ExemptionTypeUsageRule
The lists of exemption type codes to be used in ExemptionType are provided in the document
"ETYP-ITYP Exemption & Income Type Codes" available on the SMPG website at www.smpg.info.
• GenericCashPricePerProductGuideline
GenericCashPriceReceivedPerProduct and GenericCashPricePaidPerProduct are prices received or
paid in the course of an event. The specific meaning (redemption price, subscription price,
reinvestment price.) is derived from the event type.
• IncomeType2Rule
If at least one occurrence of OtherIncomeType is present, then IncomeType must be present.
On Condition
    /OtherIncomeType[*] is present
Following Must be True
    /IncomeType Must be present
• IncomeTypeUsageRule
The lists of income type codes to be used in IncomeType are provided in the document "ETYP-ITYP
Exemption & Income Type Codes" available on the SMPG website at www.smpg.info.
• IssuerOfferorTaxabilityIndicatorUsageRule
The IssuerOfferorTaxabilityIndicator may only be used when no tax rate is provided in the message
and it must not be used in events such as dividend or interest.
The list of proprietary IssuerOfferorTaxabilityIndicator codes that may be used are provided in the
document "TXAP Taxability Codes" available on the SMPG website at www.smpg.info.
3.4.11.25.1  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Indicates whether the value is a debit or a credit.
Datatype: "CreditDebitCode" on page 1205
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 204 February 2026
```

