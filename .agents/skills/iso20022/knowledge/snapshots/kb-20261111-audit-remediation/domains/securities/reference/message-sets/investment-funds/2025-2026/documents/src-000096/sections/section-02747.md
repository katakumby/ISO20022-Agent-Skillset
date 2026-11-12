---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.11 InformativePriceDetails <InftvPricDtls>"]
file_pages: [3876]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.11 InformativePriceDetails <InftvPricDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3876 to 3876.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3876

```text
PriceDetails <PricDtls> contains the following elements (see "UnitPrice22" on page 5109 for details)
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
55.4.5.19.11  InformativePriceDetails <InftvPricDtls>
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
55.4.5.19.12  CumDividendIndicator <CumDvddInd>
Presence: [1..1]
Definition: Indicates whether the dividend is included, that is, cum-dividend, in the executed price. When
the dividend is not included, the price will be ex-dividend.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3876 May 2026
```

