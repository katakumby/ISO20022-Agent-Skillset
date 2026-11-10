---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["16 camt.017.001.05 ReturnCurrencyExchangeRateV05", "16.2 Structure"]
file_pages: [513]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.017.001.05"]
---

# 16.2 Structure

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 513 to 513.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 513

```text
16.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <RtrCcyXchgRate> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 514
   ReportOrError <RptOrErr> [1..1]  514
{Or     CurrencyExchangeReport <CcyXchgRpt> [1..*]  515
       CurrencyReference <CcyRef> [1..1]  516
         SourceCurrency <SrcCcy> [1..1] CodeSet C1 516
         TargetCurrency <TrgtCcy> [1..1] CodeSet C1 517
       CurrencyExchangeOrError <CcyXchgOrErr> [1..1]  517
{Or         BusinessError <BizErr> [1..*] ± 518
Or}         CurrencyExchange <CcyXchg> [1..1]  518
           ExchangeRate <XchgRate> [1..1] Rate 518
           QuotedCurrency <QtdCcy> [1..1] CodeSet C1 518
           QuotationDate <QtnDt> [1..1] DateTime 519
           LowLimit <LwLmt> [0..1]  519
{Or             Rate <Rate> [1..1] Rate 519
Or}             Percentage <Pctg> [1..1] Rate 519
           HighLimit <HghLmt> [0..1]  519
{Or             Rate <Rate> [1..1] Rate 520
Or}             Percentage <Pctg> [1..1] Rate 520
Or}     OperationalError <OprlErr> [1..*] ± 520
   SupplementaryData <SplmtryData> [0..*] ± C2 520
16.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C2 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 04 February 2025 camt.017.001.05 ReturnCurrencyExchangeRateV05
Cash Management - Maintenance 2024 - 2025 513 February 2025
```

