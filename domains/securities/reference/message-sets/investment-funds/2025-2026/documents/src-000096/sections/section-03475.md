---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.3 InvestmentFundTransaction3", "66.1.26.3.18 SettlementAmount <SttlmAmt>"]
file_pages: [4725]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.3.18 SettlementAmount <SttlmAmt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4725 to 4725.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4725

```text
CodeName Name Definition
RVCD ReversalCredit Debit entry used to reverse a previously
booked credit entry.
RVDB ReversalDebit Credit entry used to reverse a previously
booked debit entry.
66.1.26.3.18  SettlementAmount <SttlmAmt>
Presence: [0..1]
Definition: Amount of money to be moved between the debtor and creditor, before deduction of
charges, expressed in the currency as ordered by the initiating party.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
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
66.1.26.3.19  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Date on which the debtor expects the amount of money to be available to the creditor.
Datatype: "ISODate" on page 5388
66.1.26.3.20  TradeDateTime <TradDtTm>
Presence: [1..1]
Definition: Date and time at which a price is applied, according to the terms stated in the prospectus.
TradeDateTime <TradDtTm> contains one of the following elements (see "DateAndDateTimeChoice"
on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
66.1.26.3.21  CumDividendIndicator <CumDvddInd>
Presence: [1..1]
Definition: Indicates whether the dividend is included, ie, cum-dividend, in the executed price. When the
dividend is not included, the price will be ex-dividend.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4725 May 2026
```

