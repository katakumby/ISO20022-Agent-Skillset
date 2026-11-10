---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.2 CancellationReport <CxlRpt>", "15.4.2.2.1 RegulatoryData <RgltryData>", "15.4.2.2.1.1 Invoicer <Invcr>"]
file_pages: [334]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.2.1.1 Invoicer <Invcr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 334 to 334.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 334

```text
RegulatoryData <RgltryData> contains the following InvoiceLegalIssue5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Invoicer <Invcr> [1..1] ± 334
   Invoicee <Invcee> [1..1] ± 335
   InvoiceLegalStatement <InvcLglStmt> [0..1] Text 336
   PaymentMethod <PmtMtd> [0..1]  337
{Or     Code <Cd> [1..1] CodeSet 337
Or}     Proprietary <Prtry> [1..1] Text 337
15.4.2.2.1.1  Invoicer <Invcr>
Presence: [1..1]
Definition: Identification of the organisation issuing the invoice, when it is different from the creditor or
ultimate creditor.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 334 August 2026
```

