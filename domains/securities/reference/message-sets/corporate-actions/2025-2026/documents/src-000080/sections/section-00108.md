---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.22 PriceDetails <PricDtls>", "3.4.11.22.2 OverSubscriptionDepositPrice <OverSbcptDpstPric>"]
file_pages: [164]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.22.2 OverSubscriptionDepositPrice <OverSbcptDpstPric>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 164 to 164.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 164

```text
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
3.4.11.22.2  OverSubscriptionDepositPrice <OverSbcptDpstPric>
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
3.4.11.22.3  MaximumCashToInstruct <MaxCshToInst>
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
3.4.11.22.4  MinimumCashToInstruct <MinCshToInst>
Presence: [0..1]
Definition: Minimum cash amount that may be instructed.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 164 February 2026
```

