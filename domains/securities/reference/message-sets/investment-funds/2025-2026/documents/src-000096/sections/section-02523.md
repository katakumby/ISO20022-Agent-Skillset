---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.16 RedemptionLegDetails <RedLegDtls>", "53.4.5.16.2 FinancialInstrumentDetails <FinInstrmDtls>", "53.4.5.16.2.9 SeriesIdentification <SrsId>", "53.4.5.16.2.9.1 SeriesDate <SrsDt>"]
file_pages: [3558]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.16.2.9.1 SeriesDate <SrsDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3558 to 3558.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3558

```text
Constraints
• SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
53.4.5.16.2.9.1  SeriesDate <SrsDt>
Presence: [0..1]
Definition: Issue date of the fund series. It is typically applicable to a redemption order, subscription
order confirmation or redemption order confirmation, but may be specified in the subscription order, if
known.
SeriesDate <SrsDt> contains one of the following elements (see "DateFormat42Choice" on page 4467
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   YearMonth <YrMnth> [1..1] YearMonth 4467
Or}   YearMonthDay <YrMnthDay> [1..1] Date 4467
53.4.5.16.2.9.2  SeriesName <SrsNm>
Presence: [0..1]
Definition: Name of the fund series. It is typically applicable to a redemption order, subscription order
confirmation or redemption order confirmation, but may be specified in the subscription, if known.
Datatype: "Max35Text" on page 5403
53.4.5.16.3  FinancialInstrumentQuantityChoice <FinInstrmQtyChc>
Presence: [0..1]
Definition: Amount of money, number of units or percentage for the subscription leg of the switch order.
FinancialInstrumentQuantityChoice <FinInstrmQtyChc> contains one of the following
FinancialInstrumentQuantity50Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 3558
Or   PercentageOfTotalSubscriptionAmount
<PctgOfTtlSbcptAmt>
[1..1] Rate 3559
Or   NetAmount <NetAmt> [1..1] Amount C3, C8 3559
Or   GrossAmount <GrssAmt> [1..1] Amount C3, C8 3559
Or   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 3560
Or}   HoldingsRedemptionRate <HldgsRedRate> [1..1] Rate 3560
53.4.5.16.3.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Number of investment fund units redeemed.
Datatype: "DecimalNumber" on page 5400
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3558 May 2026
```

