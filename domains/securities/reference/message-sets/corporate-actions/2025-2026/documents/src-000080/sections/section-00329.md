---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.20 PriceDetails <PricDtls>", "7.4.13.20.1 CashInLieuOfSharePrice <CshInLieuOfShrPric>"]
file_pages: [449]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.20.1 CashInLieuOfSharePrice <CshInLieuOfShrPric>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 449 to 449.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 449

```text
7.4.13.20.1  CashInLieuOfSharePrice <CshInLieuOfShrPric>
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
7.4.13.20.2  OverSubscriptionDepositPrice <OverSbcptDpstPric>
Presence: [0..1]
Definition: Amount of money required per over-subscribed equity as defined by the issuer.
OverSubscriptionDepositPrice <OverSbcptDpstPric> contains one of the following elements (see
"PriceFormat74Choice" on page 1074 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1074
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1075
     PriceValue <PricVal> [1..1] Rate 1075
Or   AmountPrice <AmtPric> [1..1] ± 1075
Or}   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1075
7.4.13.20.3  MaximumCashToInstruct <MaxCshToInst>
Presence: [0..1]
Definition: Maximum cash amount that may be instructed.
MaximumCashToInstruct <MaxCshToInst> contains one of the following elements (see
"PriceFormat61Choice" on page 1066 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountPrice <AmtPric> [1..1]  1066
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1067
     PriceValue <PricVal> [1..1] Amount C1 1067
Or}   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1067
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 449 February 2026
```

