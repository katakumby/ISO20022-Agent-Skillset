---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["16 camt.017.001.05 ReturnCurrencyExchangeRateV05", "16.4 Message Building Blocks", "16.4.2 ReportOrError <RptOrErr>", "16.4.2.1 CurrencyExchangeReport <CcyXchgRpt>", "16.4.2.1.2 CurrencyExchangeOrError <CcyXchgOrErr>", "16.4.2.1.2.2 CurrencyExchange <CcyXchg>", "16.4.2.1.2.2.3 QuotationDate <QtnDt>"]
file_pages: [519]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.017.001.05"]
---

# 16.4.2.1.2.2.3 QuotationDate <QtnDt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 519 to 519.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 519

```text
Datatype: "ActiveOrHistoricCurrencyCode" on page 849
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
16.4.2.1.2.2.3  QuotationDate <QtnDt>
Presence: [1..1]
Definition: Date and time at which an exchange rate is quoted.
Datatype: "ISODateTime" on page 883
16.4.2.1.2.2.4  LowLimit <LwLmt>
Presence: [0..1]
Definition: Lowest limit defined for the exchange rate.
Usage: The currency authority publishes the exchange rate based on the price formed in the foreign
exchange market, allowing it to float up and down within the prescribed fluctuation range. It is the lowest
exchange rate supported in foreign exchange market transactions.
LowLimit <LwLmt> contains one of the following ExchangeRateOrPercentage1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 519
Or}   Percentage <Pctg> [1..1] Rate 519
16.4.2.1.2.2.4.1  Rate <Rate>
Presence: [1..1]
Definition: Rate is expressed an currency exchange rate.
Datatype: "BaseOneRate" on page 886
16.4.2.1.2.2.4.2  Percentage <Pctg>
Presence: [1..1]
Definition: Rate is expressed as a percentage relative to the reference rate.
Datatype: "PercentageRate" on page 887
16.4.2.1.2.2.5  HighLimit <HghLmt>
Presence: [0..1]
Definition: Highest limit defined for the exchange rate.
Approved by the Payments SEG on 04 February 2025 camt.017.001.05 ReturnCurrencyExchangeRateV05
Cash Management - Maintenance 2024 - 2025 519 February 2025
```

