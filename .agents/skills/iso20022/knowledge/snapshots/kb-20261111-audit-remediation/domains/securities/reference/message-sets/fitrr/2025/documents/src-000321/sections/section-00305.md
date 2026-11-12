---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.11 Price", "22.1.11.6 SecuritiesTransactionPrice2Choice"]
file_pages: [355]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.11.6 SecuritiesTransactionPrice2Choice

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 355 to 355.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 355

```text
Definition: Currency that will be used but for which no price is yet known.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 417
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
22.1.11.6  SecuritiesTransactionPrice2Choice
Definition: Choice to define the price of the securities transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MonetaryValue <MntryVal> [1..1] ± 355
Or   Percentage <Pctg> [1..1] Rate 355
Or   Yield <Yld> [1..1] Rate 355
Or}   BasisPoints <BsisPts> [1..1] Quantity 356
22.1.11.6.1  MonetaryValue <MntryVal>
Presence: [1..1]
Definition: Price expressed as a monetary value.
MonetaryValue <MntryVal> contains the following elements (see "AmountAndDirection61" on
page 275 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1 275
   Sign <Sgn> [0..1] Indicator 275
22.1.11.6.2  Percentage <Pctg>
Presence: [1..1]
Definition: Price expressed as a rate, that is a percentage.
Datatype: "PercentageRate" on page 454
22.1.11.6.3  Yield <Yld>
Presence: [1..1]
Definition: Price expressed as a yield.
Datatype: "PercentageRate" on page 454
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
355 July 2025
```

