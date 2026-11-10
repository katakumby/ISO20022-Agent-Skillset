---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.7 AmountOrUnits <AmtOrUnits>", "50.4.4.9.7.1 UnitsNumber <UnitsNb>"]
file_pages: [3065]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.7.1 UnitsNumber <UnitsNb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3065 to 3065.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3065

```text
AmountOrUnits <AmtOrUnits> contains one of the following FinancialInstrumentQuantity49Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 3065
Or   GrossAmount <GrssAmt> [1..1] Amount C4, C9 3065
Or   NetAmount <NetAmt> [1..1] Amount C4, C9 3065
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 3066
50.4.4.9.7.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Number of investment fund units to be subscribed.
Datatype: "DecimalNumber" on page 5400
50.4.4.9.7.2  GrossAmount <GrssAmt>
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
50.4.4.9.7.3  NetAmount <NetAmt>
Presence: [1..1]
Definition: Amount of money to be invested in the fund.
Net Amount = Quantity * Price.
Impacted by: C4 "ActiveOrHistoricCurrency", C9 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3065 May 2026
```

