---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.14 InformativePriceDetails <InftvPricDtls>"]
file_pages: [3315]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.14 InformativePriceDetails <InftvPricDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3315 to 3315.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3315

```text
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
52.4.5.10.14  InformativePriceDetails <InftvPricDtls>
Presence: [0..2]
Definition: Other quoted price than the one at which the order was executed.
InformativePriceDetails <InftvPricDtls> contains the following elements (see "UnitPrice22" on
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
52.4.5.10.15  SettlementAmount <SttlmAmt>
Presence: [1..1]
Definition: Total amount of money paid /to be paid or received in exchange for the financial instrument
in the individual order.
Impacted by: C3 "ActiveCurrency", C11 "CurrencyAmount"
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3315 May 2026
```

