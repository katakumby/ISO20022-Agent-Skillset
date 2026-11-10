---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.7 AmountOrUnitsOrPercentage <AmtOrUnitsOrPctg>", "44.4.4.9.7.1 UnitsNumber <UnitsNb>"]
file_pages: [2157]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.7.1 UnitsNumber <UnitsNb>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2157 to 2157.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2157

```text
AmountOrUnitsOrPercentage <AmtOrUnitsOrPctg> contains one of the following
FinancialInstrumentQuantity48Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 2157
Or   GrossAmount <GrssAmt> [1..1] Amount C4, C9 2157
Or   NetAmount <NetAmt> [1..1] Amount C4, C9 2157
Or   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 2158
Or}   HoldingsRedemptionRate <HldgsRedRate> [1..1] Rate 2158
44.4.4.9.7.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Number of investment fund units redeemed.
Datatype: "DecimalNumber" on page 5400
44.4.4.9.7.2  GrossAmount <GrssAmt>
Presence: [1..1]
Definition: Amount of money to be redeemed from the fund.
Gross Amount = Quantity * Price.
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
44.4.4.9.7.3  NetAmount <NetAmt>
Presence: [1..1]
Definition: Amount of money to be received following redemption of fund units.
Net Amount = (Quantity * Price) - (Fees + Taxes).
Impacted by: C4 "ActiveOrHistoricCurrency", C9 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2157 May 2026
```

