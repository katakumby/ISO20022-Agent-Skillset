---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["16 camt.017.001.05 ReturnCurrencyExchangeRateV05", "16.4 Message Building Blocks", "16.4.2 ReportOrError <RptOrErr>", "16.4.2.1 CurrencyExchangeReport <CcyXchgRpt>"]
file_pages: [515]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.017.001.05"]
---

# 16.4.2.1 CurrencyExchangeReport <CcyXchgRpt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 515 to 515.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 515

```text
ReportOrError <RptOrErr> contains one of the following ExchangeRateReportOrError3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrencyExchangeReport <CcyXchgRpt> [1..*]  515
     CurrencyReference <CcyRef> [1..1]  516
       SourceCurrency <SrcCcy> [1..1] CodeSet C1 516
       TargetCurrency <TrgtCcy> [1..1] CodeSet C1 517
     CurrencyExchangeOrError <CcyXchgOrErr> [1..1]  517
{Or       BusinessError <BizErr> [1..*] ± 518
Or}       CurrencyExchange <CcyXchg> [1..1]  518
         ExchangeRate <XchgRate> [1..1] Rate 518
         QuotedCurrency <QtdCcy> [1..1] CodeSet C1 518
         QuotationDate <QtnDt> [1..1] DateTime 519
         LowLimit <LwLmt> [0..1]  519
{Or           Rate <Rate> [1..1] Rate 519
Or}           Percentage <Pctg> [1..1] Rate 519
         HighLimit <HghLmt> [0..1]  519
{Or           Rate <Rate> [1..1] Rate 520
Or}           Percentage <Pctg> [1..1] Rate 520
Or}   OperationalError <OprlErr> [1..*] ± 520
16.4.2.1  CurrencyExchangeReport <CcyXchgRpt>
Presence: [1..*]
Definition: Reports on currency exchange information.
Approved by the Payments SEG on 04 February 2025 camt.017.001.05 ReturnCurrencyExchangeRateV05
Cash Management - Maintenance 2024 - 2025 515 February 2025
```

