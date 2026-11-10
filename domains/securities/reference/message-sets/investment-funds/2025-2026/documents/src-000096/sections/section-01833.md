---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.5 AmountOrUnits <AmtOrUnits>"]
file_pages: [2581]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.5 AmountOrUnits <AmtOrUnits>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2581 to 2581.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2581

```text
OrderType <OrdrTp> contains one of the following elements (see "FundOrderType4Choice" on
page 4740 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4741
Or}   Proprietary <Prtry> [1..1] ± 4741
47.4.4.8.5  AmountOrUnits <AmtOrUnits>
Presence: [1..1]
Definition: Amount of money or the number of units for the subscription order.
AmountOrUnits <AmtOrUnits> contains one of the following FinancialInstrumentQuantity49Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 2581
Or   GrossAmount <GrssAmt> [1..1] Amount C4, C9 2581
Or   NetAmount <NetAmt> [1..1] Amount C4, C9 2582
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 2582
47.4.4.8.5.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Number of investment fund units to be subscribed.
Datatype: "DecimalNumber" on page 5400
47.4.4.8.5.2  GrossAmount <GrssAmt>
Presence: [1..1]
Definition: Amount of money to be paid by the investor when subscribing to fund units.
Gross amount = (Quantity * Price) + (Fees + Taxes).
Impacted by: C4 "ActiveOrHistoricCurrency", C9 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2581 May 2026
```

