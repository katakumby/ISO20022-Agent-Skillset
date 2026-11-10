---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.2 CancellationReport <CxlRpt>"]
file_pages: [333]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.2 CancellationReport <CxlRpt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 333 to 333.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 333

```text
Definition: Information needed to process a currency exchange or conversion.
ForeignExchange <FX> contains the following elements (see "ForeignExchangeTerms24" on
page 2955 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 2955
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 2955
   ExchangeRate <XchgRate> [1..1] Rate 2956
   ResultingAmount <RsltgAmt> [0..1] Amount C1, C4 2956
15.4.2.2  CancellationReport <CxlRpt>
Presence: [1..1]
Definition: Report on cancelled billing data.
CancellationReport <CxlRpt> contains the following BillingCancellationReport3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RegulatoryData <RgltryData> [0..1]  333
     Invoicer <Invcr> [1..1] ± 334
     Invoicee <Invcee> [1..1] ± 335
     InvoiceLegalStatement <InvcLglStmt> [0..1] Text 336
     PaymentMethod <PmtMtd> [0..1]  337
{Or       Code <Cd> [1..1] CodeSet 337
Or}       Proprietary <Prtry> [1..1] Text 337
   Service <Svc> [0..1]  337
     SystemIdentification <SysId> [1..1] ± 337
     SystemCurrency <SysCcy> [0..1] CodeSet C1 338
   InvoiceDate <InvcDt> [1..1] Date 338
   BillingIdentification <BllgId> [1..1] Text 338
   BillingPeriod <BllgPrd> [1..1] ± 338
   CancellationReason <CxlRsn> [1..1]  338
{Or     Code <Cd> [1..1] Text 339
Or}     Proprietary <Prtry> [1..1] Text 339
15.4.2.2.1  RegulatoryData <RgltryData>
Presence: [0..1]
Definition: Information about legal and regulatory data exchanged between invoicing and paying party.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 333 August 2026
```

