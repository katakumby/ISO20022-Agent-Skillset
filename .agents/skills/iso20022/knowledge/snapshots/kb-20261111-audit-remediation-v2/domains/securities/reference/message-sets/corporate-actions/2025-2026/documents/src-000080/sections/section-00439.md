---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.7 RateAndAmountDetails <RateAndAmtDtls>", "8.4.12.7.9 TaxableIncomePerDividendShare <TaxblIncmPerDvddShr>"]
file_pages: [591]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.7.9 TaxableIncomePerDividendShare <TaxblIncmPerDvddShr>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 591 to 591.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 591

```text
8.4.12.7.9  TaxableIncomePerDividendShare <TaxblIncmPerDvddShr>
Presence: [0..*]
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
8.4.12.8  PriceDetails <PricDtls>
Presence: [0..1]
Definition: Provides information about the prices related to a corporate action option.
Impacted by: C23 "GenericCashPriceReceivedPerProductGuideline"
PriceDetails <PricDtls> contains the following CorporateActionPrice84 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 591
   OverSubscriptionDepositPrice <OverSbcptDpstPric> [0..1] ± 592
Constraints
• GenericCashPriceReceivedPerProductGuideline
GenericCashPriceReceivedPerProduct is the price received in the course of an event. The specific
meaning (redemption price, subscription price, reinvestment price, ETC.) is derived from the event
type.
8.4.12.8.1  CashInLieuOfSharePrice <CshInLieuOfShrPric>
Presence: [0..1]
Definition: Cash disbursement in lieu of equities; usually in lieu of fractional quantity.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 591 February 2026
```

