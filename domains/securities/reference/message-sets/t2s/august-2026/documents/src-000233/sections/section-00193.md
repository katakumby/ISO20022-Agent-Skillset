---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.1 RegulatoryData <RgltryData>"]
file_pages: [266]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.1 RegulatoryData <RgltryData>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 266 to 266.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 266

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 329
         TaxExemption <TaxXmptn> [0..*]  330
           ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 330
           Reason <Rsn> [0..1] Text 330
         Amount <Amt> [1..1] Amount C1, C4 330
         ChargesAndFees <ChrgsAndFees> [0..*]  331
           Type <Tp> [0..1] Text 331
           Description <Desc> [0..1] Text 331
           Rate <Rate> [0..1] Rate 331
           Amount <Amt> [0..1] Amount C1, C4 331
       TotalInvoiceAmount <TtlInvcAmt> [1..1]  332
         Amount <Amt> [1..1] Amount C1, C4 332
         ForeignExchange <FX> [0..1] ± 332
15.4.2.1.1  RegulatoryData <RgltryData>
Presence: [1..1]
Definition: Information about legal and regulatory data exchanged between invoicing and paying party.
RegulatoryData <RgltryData> contains the following InvoiceLegalIssue5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Invoicer <Invcr> [1..1] ± 266
   Invoicee <Invcee> [1..1] ± 267
   InvoiceLegalStatement <InvcLglStmt> [0..1] Text 268
   PaymentMethod <PmtMtd> [0..1]  269
{Or     Code <Cd> [1..1] CodeSet 269
Or}     Proprietary <Prtry> [1..1] Text 269
15.4.2.1.1.1  Invoicer <Invcr>
Presence: [1..1]
Definition: Identification of the organisation issuing the invoice, when it is different from the creditor or
ultimate creditor.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 266 August 2026
```

