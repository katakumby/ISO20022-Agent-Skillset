---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["16 camt.017.001.05 ReturnCurrencyExchangeRateV05", "16.4 Message Building Blocks", "16.4.2 ReportOrError <RptOrErr>", "16.4.2.1 CurrencyExchangeReport <CcyXchgRpt>", "16.4.2.1.1 CurrencyReference <CcyRef>", "16.4.2.1.1.2 TargetCurrency <TrgtCcy>"]
file_pages: [517]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.017.001.05"]
---

# 16.4.2.1.1.2 TargetCurrency <TrgtCcy>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 517 to 517.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 517

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
16.4.2.1.1.2  TargetCurrency <TrgtCcy>
Presence: [1..1]
Definition: Currency into which an amount is to be converted in a currency conversion.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 849
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
16.4.2.1.2  CurrencyExchangeOrError <CcyXchgOrErr>
Presence: [1..1]
Definition: Reports either on currency exchange information or on a business error.
CurrencyExchangeOrError <CcyXchgOrErr> contains one of the following
ExchangeRateReportOrError4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BusinessError <BizErr> [1..*] ± 518
Or}   CurrencyExchange <CcyXchg> [1..1]  518
     ExchangeRate <XchgRate> [1..1] Rate 518
     QuotedCurrency <QtdCcy> [1..1] CodeSet C1 518
     QuotationDate <QtnDt> [1..1] DateTime 519
     LowLimit <LwLmt> [0..1]  519
{Or       Rate <Rate> [1..1] Rate 519
Or}       Percentage <Pctg> [1..1] Rate 519
     HighLimit <HghLmt> [0..1]  519
{Or       Rate <Rate> [1..1] Rate 520
Or}       Percentage <Pctg> [1..1] Rate 520
Approved by the Payments SEG on 04 February 2025 camt.017.001.05 ReturnCurrencyExchangeRateV05
Cash Management - Maintenance 2024 - 2025 517 February 2025
```

