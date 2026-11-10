---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>", "3.4.11.24.19 AmountDetails <AmtDtls>"]
file_pages: [199]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.24.19 AmountDetails <AmtDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 199 to 199.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 199

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
3.4.11.24.19  AmountDetails <AmtDtls>
Presence: [0..1]
Definition: Provides information about the amounts related to a securities movement.
AmountDetails <AmtDtls> contains the following CorporateActionAmounts60 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C2, C18 199
   SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C2, C18 200
3.4.11.24.19.1  WithholdingTaxAmount <WhldgTaxAmt>
Presence: [0..1]
Definition: Amount of a cash distribution that will be withheld by the tax authorities of the jurisdiction of
the issuer, for which a relief at source and/or reclaim may be possible.
Impacted by: C2 "ActiveCurrency", C18 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1156
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 199 February 2026
```

