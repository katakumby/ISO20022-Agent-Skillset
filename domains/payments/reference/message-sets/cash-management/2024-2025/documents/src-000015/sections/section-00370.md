---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["16 camt.017.001.05 ReturnCurrencyExchangeRateV05", "16.4 Message Building Blocks", "16.4.2 ReportOrError <RptOrErr>", "16.4.2.1 CurrencyExchangeReport <CcyXchgRpt>", "16.4.2.1.1 CurrencyReference <CcyRef>"]
file_pages: [516]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.017.001.05"]
---

# 16.4.2.1.1 CurrencyReference <CcyRef>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 516 to 516.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 516

```text
CurrencyExchangeReport <CcyXchgRpt> contains the following CurrencyExchangeReport4
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CurrencyReference <CcyRef> [1..1]  516
     SourceCurrency <SrcCcy> [1..1] CodeSet C1 516
     TargetCurrency <TrgtCcy> [1..1] CodeSet C1 517
   CurrencyExchangeOrError <CcyXchgOrErr> [1..1]  517
{Or     BusinessError <BizErr> [1..*] ± 518
Or}     CurrencyExchange <CcyXchg> [1..1]  518
       ExchangeRate <XchgRate> [1..1] Rate 518
       QuotedCurrency <QtdCcy> [1..1] CodeSet C1 518
       QuotationDate <QtnDt> [1..1] DateTime 519
       LowLimit <LwLmt> [0..1]  519
{Or         Rate <Rate> [1..1] Rate 519
Or}         Percentage <Pctg> [1..1] Rate 519
       HighLimit <HghLmt> [0..1]  519
{Or         Rate <Rate> [1..1] Rate 520
Or}         Percentage <Pctg> [1..1] Rate 520
16.4.2.1.1  CurrencyReference <CcyRef>
Presence: [1..1]
Definition: Source and target currencies for which information is request.
CurrencyReference <CcyRef> contains the following CurrencySourceTarget1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SourceCurrency <SrcCcy> [1..1] CodeSet C1 516
   TargetCurrency <TrgtCcy> [1..1] CodeSet C1 517
16.4.2.1.1.1  SourceCurrency <SrcCcy>
Presence: [1..1]
Definition: Currency of the amount to be converted in a currency conversion.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 849
Approved by the Payments SEG on 04 February 2025 camt.017.001.05 ReturnCurrencyExchangeRateV05
Cash Management - Maintenance 2024 - 2025 516 February 2025
```

