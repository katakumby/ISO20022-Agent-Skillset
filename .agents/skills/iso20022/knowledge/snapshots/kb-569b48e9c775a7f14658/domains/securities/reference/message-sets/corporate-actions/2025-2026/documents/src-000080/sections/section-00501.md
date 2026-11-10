---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.15 PriceDetails <PricDtls>", "8.4.12.11.15.3 CashInLieuOfSharePrice <CshInLieuOfShrPric>"]
file_pages: [661]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.15.3 CashInLieuOfSharePrice <CshInLieuOfShrPric>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 661 to 661.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 661

```text
GenericCashPriceReceivedPerProduct <GncCshPricRcvdPerPdct> contains one of the following
elements (see "PriceFormat76Choice" on page 1080 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1081
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1081
     PriceValue <PricVal> [1..1] Rate 1082
Or   AmountPrice <AmtPric> [1..1] ± 1082
Or   AmountPricePerFinancialInstrumentQuantity
<AmtPricPerFinInstrmQty>
[1..1]  1082
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1082
     PriceValue <PricVal> [1..1] Amount C1 1083
     FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± C13 1083
Or   AmountPricePerAmount <AmtPricPerAmt> [1..1]  1083
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1084
     PriceValue <PricVal> [1..1] Amount C1 1084
     Amount <Amt> [1..1] Amount C1 1084
Or}   IndexPoints <IndxPts> [1..1] Quantity 1084
8.4.12.11.15.3  CashInLieuOfSharePrice <CshInLieuOfShrPric>
Presence: [0..1]
Definition: Cash disbursement in lieu of equities; usually in lieu of fractional quantity.
CashInLieuOfSharePrice <CshInLieuOfShrPric> contains one of the following elements (see
"PriceFormat77Choice" on page 1064 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1064
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1065
     PriceValue <PricVal> [1..1] Rate 1065
Or}   AmountPrice <AmtPric> [1..1] ± 1065
8.4.13 AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 661 February 2026
```

