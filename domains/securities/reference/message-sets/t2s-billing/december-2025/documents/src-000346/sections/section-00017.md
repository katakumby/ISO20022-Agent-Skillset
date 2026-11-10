---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.1 RegulatoryData <RgltryData>"]
file_pages: [37]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.1 RegulatoryData <RgltryData>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 37 to 37.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 37

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 100
         TaxExemption <TaxXmptn> [0..*]  101
           ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 101
           Reason <Rsn> [0..1] Text 101
         Amount <Amt> [1..1] Amount C1, C4 101
         ChargesAndFees <ChrgsAndFees> [0..*]  102
           Type <Tp> [0..1] Text 102
           Description <Desc> [0..1] Text 102
           Rate <Rate> [0..1] Rate 102
           Amount <Amt> [0..1] Amount C1, C4 102
       TotalInvoiceAmount <TtlInvcAmt> [1..1]  103
         Amount <Amt> [1..1] Amount C1, C4 103
         ForeignExchange <FX> [0..1] ± 103
3.4.2.1.1  RegulatoryData <RgltryData>
Presence: [1..1]
Definition: Information about legal and regulatory data exchanged between invoicing and paying party.
RegulatoryData <RgltryData> contains the following InvoiceLegalIssue5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Invoicer <Invcr> [1..1] ± 37
   Invoicee <Invcee> [1..1] ± 38
   InvoiceLegalStatement <InvcLglStmt> [0..1] Text 39
   PaymentMethod <PmtMtd> [0..1]  40
{Or     Code <Cd> [1..1] CodeSet 40
Or}     Proprietary <Prtry> [1..1] Text 40
3.4.2.1.1.1  Invoicer <Invcr>
Presence: [1..1]
Definition: Identification of the organisation issuing the invoice, when it is different from the creditor or
ultimate creditor.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 37 December 2025
```

