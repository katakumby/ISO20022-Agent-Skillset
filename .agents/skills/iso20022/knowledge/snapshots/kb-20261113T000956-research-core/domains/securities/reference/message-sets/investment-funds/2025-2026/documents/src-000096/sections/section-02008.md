---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.12 TradeDateTime <TradDtTm>"]
file_pages: [2830]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.12 TradeDateTime <TradDtTm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2830 to 2830.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2830

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
49.4.5.9.12  TradeDateTime <TradDtTm>
Presence: [1..1]
Definition: Date and time at which a price is applied, according to the terms stated in the prospectus.
TradeDateTime <TradDtTm> contains one of the following elements (see "DateAndDateTime2Choice"
on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
49.4.5.9.13  DealingPriceDetails <DealgPricDtls>
Presence: [1..1]
Definition: Price at which the order was executed.
DealingPriceDetails <DealgPricDtls> contains the following elements (see "UnitPrice22" on
page 5109 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 5109
   Value <Val> [1..1] ± 5110
   PriceMethod <PricMtd> [0..1] CodeSet 5110
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity 5110
   TaxableIncomePerShare <TaxblIncmPerShr> [0..1] Amount C1 5110
   TaxableIncomePerShareCalculated
<TaxblIncmPerShrClctd>
[0..1]  5111
{Or     Code <Cd> [1..1] CodeSet 5111
Or}     Proprietary <Prtry> [1..1] ± 5111
   PriceDifferenceReason <PricDiffRsn> [0..1] Text 5112
49.4.5.9.14  InformativePriceDetails <InftvPricDtls>
Presence: [0..2]
Definition: Other quoted price than the one at which the order was executed.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2830 May 2026
```

