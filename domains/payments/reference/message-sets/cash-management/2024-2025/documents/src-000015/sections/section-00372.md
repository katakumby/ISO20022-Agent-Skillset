---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["16 camt.017.001.05 ReturnCurrencyExchangeRateV05", "16.4 Message Building Blocks", "16.4.2 ReportOrError <RptOrErr>", "16.4.2.1 CurrencyExchangeReport <CcyXchgRpt>", "16.4.2.1.2 CurrencyExchangeOrError <CcyXchgOrErr>", "16.4.2.1.2.1 BusinessError <BizErr>"]
file_pages: [518]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.017.001.05"]
---

# 16.4.2.1.2.1 BusinessError <BizErr>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 518 to 518.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 518

```text
16.4.2.1.2.1  BusinessError <BizErr>
Presence: [1..*]
Definition: Reason the requested business information is not given.
BusinessError <BizErr> contains the following elements (see "ErrorHandling3" on page 816 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  816
{Or     Code <Cd> [1..1] CodeSet 817
Or}     Proprietary <Prtry> [1..1] Text 817
   Description <Desc> [0..1] Text 817
16.4.2.1.2.2  CurrencyExchange <CcyXchg>
Presence: [1..1]
Definition: Requested business information.
CurrencyExchange <CcyXchg> contains the following CurrencyExchange20 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExchangeRate <XchgRate> [1..1] Rate 518
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 518
   QuotationDate <QtnDt> [1..1] DateTime 519
   LowLimit <LwLmt> [0..1]  519
{Or     Rate <Rate> [1..1] Rate 519
Or}     Percentage <Pctg> [1..1] Rate 519
   HighLimit <HghLmt> [0..1]  519
{Or     Rate <Rate> [1..1] Rate 520
Or}     Percentage <Pctg> [1..1] Rate 520
16.4.2.1.2.2.1  ExchangeRate <XchgRate>
Presence: [1..1]
Definition: The value of one currency expressed in relation to another currency. ExchangeRate
expresses the ratio between UnitCurrency and QuotedCurrency (ExchangeRate = UnitCurrency/
QuotedCurrency).
Datatype: "BaseOneRate" on page 886
16.4.2.1.2.2.2  QuotedCurrency <QtdCcy>
Presence: [1..1]
Definition: Currency into which the base currency is converted, in a currency exchange.
Impacted by: C1 "ActiveOrHistoricCurrency"
Approved by the Payments SEG on 04 February 2025 camt.017.001.05 ReturnCurrencyExchangeRateV05
Cash Management - Maintenance 2024 - 2025 518 February 2025
```

