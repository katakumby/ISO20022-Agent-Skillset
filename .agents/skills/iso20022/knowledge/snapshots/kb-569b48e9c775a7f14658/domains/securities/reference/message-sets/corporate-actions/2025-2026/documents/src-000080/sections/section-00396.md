---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.23 CashMovementDetails <CshMvmntDtls>", "7.4.13.23.14 PriceDetails <PricDtls>", "7.4.13.23.14.3 CashInLieuOfSharePrice <CshInLieuOfShrPric>"]
file_pages: [525]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.23.14.3 CashInLieuOfSharePrice <CshInLieuOfShrPric>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 525 to 525.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 525

```text
GenericCashPriceReceivedPerProduct <GncCshPricRcvdPerPdct> contains one of the following
elements (see "PriceFormat72Choice" on page 1076 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1076
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1076
     PriceValue <PricVal> [1..1] Rate 1077
Or   AmountPrice <AmtPric> [1..1] ± 1077
Or   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1077
Or   AmountPricePerFinancialInstrumentQuantity
<AmtPricPerFinInstrmQty>
[1..1]  1077
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1078
     PriceValue <PricVal> [1..1] Amount C1 1078
     FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± C13 1078
Or   AmountPricePerAmount <AmtPricPerAmt> [1..1]  1079
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1079
     PriceValue <PricVal> [1..1] Amount C1 1079
     Amount <Amt> [1..1] Amount C1 1080
Or}   IndexPoints <IndxPts> [1..1] Quantity 1080
7.4.13.23.14.3  CashInLieuOfSharePrice <CshInLieuOfShrPric>
Presence: [0..1]
Definition: Cash disbursement in lieu of equities; usually in lieu of fractional quantity.
CashInLieuOfSharePrice <CshInLieuOfShrPric> contains one of the following elements (see
"PriceFormat74Choice" on page 1074 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1074
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1075
     PriceValue <PricVal> [1..1] Rate 1075
Or   AmountPrice <AmtPric> [1..1] ± 1075
Or}   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1075
7.4.13.24  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information about the corporate action movement.
Impacted by: C3 "AdditionalInformationRule"
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 525 February 2026
```

