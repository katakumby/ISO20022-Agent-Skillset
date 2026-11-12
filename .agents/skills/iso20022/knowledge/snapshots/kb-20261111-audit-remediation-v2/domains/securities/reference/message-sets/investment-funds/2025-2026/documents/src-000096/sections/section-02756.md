---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.18 TransactionOverhead <TxOvrhd>", "55.4.5.19.18.5 IndividualFee <IndvFee>", "55.4.5.19.18.5.5 DiscountDetails <DscntDtls>"]
file_pages: [3886]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.18.5.5 DiscountDetails <DscntDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3886 to 3886.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3886

```text
55.4.5.19.18.5.5  DiscountDetails <DscntDtls>
Presence: [0..1]
Definition: Discount or waiver applied to the fee (charge/commission).
Impacted by: C15 "DiscountElementRule"
DiscountDetails <DscntDtls> contains the following ChargeOrCommissionDiscount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C2, C8 3886
   Rate <Rate> [0..1] Rate 3887
   Basis <Bsis> [0..1]  3887
{Or     Code <Cd> [1..1] CodeSet 3887
Or}     Proprietary <Prtry> [1..1] ± 3887
Constraints
• DiscountElementRule
Amount Or Rate Or Basis must be present.
Following Must be True
    /Amount Must be present
 Or    /Rate Must be present
 Or    /Basis Must be present
55.4.5.19.18.5.5.1  Amount <Amt>
Presence: [0..1]
Definition: Difference between the standard fee (charge/commission) amount and the applied fee
(charge/commission) amount.
EXAMPLE:
Standard charge is EUR 100
Discount is EUR 30
Applied charge is EUR 70.
Impacted by: C2 "ActiveCurrency", C8 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3886 May 2026
```

