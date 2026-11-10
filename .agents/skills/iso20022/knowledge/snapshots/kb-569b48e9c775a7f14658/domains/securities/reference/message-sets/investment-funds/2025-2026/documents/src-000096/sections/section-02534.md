---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.16 RedemptionLegDetails <RedLegDtls>", "53.4.5.16.9 TransactionOverhead <TxOvrhd>", "53.4.5.16.9.2 IndividualFee <IndvFee>", "53.4.5.16.9.2.4 StandardRate <StdRate>"]
file_pages: [3571]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.16.9.2.4 StandardRate <StdRate>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3571 to 3571.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3571

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
53.4.5.16.9.2.4  StandardRate <StdRate>
Presence: [0..1]
Definition: Standard fee (charge/commission) rate used to calculate the amount of the charge or fee, as
specified in the fund prospectus or agreed for the account.
Datatype: "PercentageRate" on page 5401
53.4.5.16.9.2.5  DiscountDetails <DscntDtls>
Presence: [0..1]
Definition: Discount or waiver applied to the fee (charge/commission).
Impacted by: C14 "DiscountElementRule"
DiscountDetails <DscntDtls> contains the following ChargeOrCommissionDiscount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C2, C7 3571
   Rate <Rate> [0..1] Rate 3572
   Basis <Bsis> [0..1]  3572
{Or     Code <Cd> [1..1] CodeSet 3572
Or}     Proprietary <Prtry> [1..1] ± 3573
Constraints
• DiscountElementRule
Amount Or Rate Or Basis must be present.
Following Must be True
    /Amount Must be present
 Or    /Rate Must be present
 Or    /Basis Must be present
53.4.5.16.9.2.5.1  Amount <Amt>
Presence: [0..1]
Definition: Difference between the standard fee (charge/commission) amount and the applied fee
(charge/commission) amount.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3571 May 2026
```

