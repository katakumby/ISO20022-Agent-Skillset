---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.2 CancellationReport <CxlRpt>"]
file_pages: [104]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.2 CancellationReport <CxlRpt>

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 104 to 104.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 104

```text
Definition: Information needed to process a currency exchange or conversion.
ForeignExchange <FX> contains the following elements (see "ForeignExchangeTerms24" on
page 115 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 115
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 116
   ExchangeRate <XchgRate> [1..1] Rate 116
   ResultingAmount <RsltgAmt> [0..1] Amount C1, C4 116
3.4.2.2  CancellationReport <CxlRpt>
Presence: [1..1]
Definition: Report on cancelled billing data.
CancellationReport <CxlRpt> contains the following BillingCancellationReport3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RegulatoryData <RgltryData> [0..1]  104
     Invoicer <Invcr> [1..1] ± 105
     Invoicee <Invcee> [1..1] ± 106
     InvoiceLegalStatement <InvcLglStmt> [0..1] Text 107
     PaymentMethod <PmtMtd> [0..1]  108
{Or       Code <Cd> [1..1] CodeSet 108
Or}       Proprietary <Prtry> [1..1] Text 108
   Service <Svc> [0..1]  108
     SystemIdentification <SysId> [1..1] ± 108
     SystemCurrency <SysCcy> [0..1] CodeSet C1 109
   InvoiceDate <InvcDt> [1..1] Date 109
   BillingIdentification <BllgId> [1..1] Text 109
   BillingPeriod <BllgPrd> [1..1] ± 109
   CancellationReason <CxlRsn> [1..1]  109
{Or     Code <Cd> [1..1] Text 110
Or}     Proprietary <Prtry> [1..1] Text 110
3.4.2.2.1  RegulatoryData <RgltryData>
Presence: [0..1]
Definition: Information about legal and regulatory data exchanged between invoicing and paying party.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 104 December 2025
```

