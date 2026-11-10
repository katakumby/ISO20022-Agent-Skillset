---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.11 GrossAmount <GrssAmt>"]
file_pages: [2372]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.11 GrossAmount <GrssAmt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2372 to 2372.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2372

```text
Note: The decimal separator is a dot.
46.4.5.10.11  GrossAmount <GrssAmt>
Presence: [0..1]
Definition: Amount of money redeemed from the fund.
Gross Amount = Quantity * Price.
Impacted by: C3 "ActiveCurrency", C10 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
46.4.5.10.12  HoldingsRedemptionRate <HldgsRedRate>
Presence: [0..1]
Definition: Portion of the investor's holdings redeemed.
Datatype: "PercentageRate" on page 5401
46.4.5.10.13  TradeDateTime <TradDtTm>
Presence: [1..1]
Definition: Date and time at which a price is applied, according to the terms stated in the prospectus.
TradeDateTime <TradDtTm> contains one of the following elements (see "DateAndDateTime2Choice"
on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
46.4.5.10.14  DealingPriceDetails <DealgPricDtls>
Presence: [1..1]
Definition: Price at which the order was executed.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2372 May 2026
```

