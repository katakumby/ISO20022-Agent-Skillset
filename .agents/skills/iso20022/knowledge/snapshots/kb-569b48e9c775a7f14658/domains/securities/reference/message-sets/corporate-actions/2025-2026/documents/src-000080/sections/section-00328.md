---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.19 RateAndAmountDetails <RateAndAmtDtls>", "7.4.13.19.10 TaxOnIncome <TaxOnIncm>"]
file_pages: [448]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.19.10 TaxOnIncome <TaxOnIncm>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 448 to 448.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 448

```text
Definition: Amount included in the dividend/NAV that is identified as gains directly or indirectly derived
from interest payments, for example, in the context of the EU Savings directive.
TaxableIncomePerDividendShare <TaxblIncmPerDvddShr> contains the following elements (see
"RateTypeAndAmountAndStatus26" on page 906 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RateType <RateTp> [1..1]  907
{Or     Code <Cd> [1..1] CodeSet 907
Or}     Proprietary <Prtry> [1..1] ± 907
   Amount <Amt> [1..1] Amount C1 908
   RateStatus <RateSts> [0..1]  C52 908
{Or     Code <Cd> [1..1] CodeSet 908
Or}     Proprietary <Prtry> [1..1] ± 908
7.4.13.19.10  TaxOnIncome <TaxOnIncm>
Presence: [0..1]
Definition: Overall tax withheld at source by fund managers prior to considering the tax obligation of
each unit holder.
TaxOnIncome <TaxOnIncm> contains one of the following elements (see
"RateAndAmountFormat57Choice" on page 1123 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1123
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1123
Or}   Amount <Amt> [1..1] Amount C1 1123
7.4.13.20  PriceDetails <PricDtls>
Presence: [0..1]
Definition: Provides information about the prices related to a corporate action option.
PriceDetails <PricDtls> contains the following CorporateActionPrice86 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 449
   OverSubscriptionDepositPrice <OverSbcptDpstPric> [0..1] ± 449
   MaximumCashToInstruct <MaxCshToInst> [0..1] ± 449
   MinimumCashToInstruct <MinCshToInst> [0..1] ± 450
   MinimumMultipleCashToInstruct <MinMltplCshToInst> [0..1] ± 450
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 448 February 2026
```

