---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.9 CorporateActionInstruction <CorpActnInstr>", "5.4.9.15 PriceDetails <PricDtls>", "5.4.9.15.4 GenericCashPricePaidPerProduct <GncCshPricPdPerPdct>"]
file_pages: [316]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.9.15.4 GenericCashPricePaidPerProduct <GncCshPricPdPerPdct>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 316 to 316.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 316

```text
GenericCashPriceReceivedPerProduct <GncCshPricRcvdPerPdct> contains one of the following
elements (see "PriceFormat78Choice" on page 1070 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1070
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1070
     PriceValue <PricVal> [1..1] Rate 1071
Or   AmountPrice <AmtPric> [1..1] ± 1071
Or   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1071
Or   AmountPricePerFinancialInstrumentQuantity
<AmtPricPerFinInstrmQty>
[1..1]  1071
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1072
     PriceValue <PricVal> [1..1] Amount C1 1072
     FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± C13 1072
Or   AmountPricePerAmount <AmtPricPerAmt> [1..1]  1073
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1073
     PriceValue <PricVal> [1..1] Amount C1 1073
     Amount <Amt> [1..1] Amount C1 1074
Or}   IndexPoints <IndxPts> [1..1] Quantity 1074
5.4.9.15.4  GenericCashPricePaidPerProduct <GncCshPricPdPerPdct>
Presence: [0..1]
Definition: Generic cash price paid per product by the underlying security holder either as a percentage
or an amount, for example, reinvestment price.
GenericCashPricePaidPerProduct <GncCshPricPdPerPdct> contains one of the following elements
(see "PriceFormat77Choice" on page 1064 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1064
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1065
     PriceValue <PricVal> [1..1] Rate 1065
Or}   AmountPrice <AmtPric> [1..1] ± 1065
5.4.9.16  ShareholderNumber <ShrhldrNb>
Presence: [0..1]
Definition: Reference number assigned to identify an investor or a shareholder with the issuer or the
registration provider (for instance allocation code).
Datatype: "Max25Text" on page 1250
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 316 February 2026
```

