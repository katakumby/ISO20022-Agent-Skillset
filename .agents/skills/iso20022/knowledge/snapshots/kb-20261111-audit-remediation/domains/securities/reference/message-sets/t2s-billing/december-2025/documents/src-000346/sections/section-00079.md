---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.2 CancellationReport <CxlRpt>", "3.4.2.2.1 RegulatoryData <RgltryData>", "3.4.2.2.1.1 Invoicer <Invcr>"]
file_pages: [105]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.2.1.1 Invoicer <Invcr>

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 105 to 105.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 105

```text
RegulatoryData <RgltryData> contains the following InvoiceLegalIssue5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Invoicer <Invcr> [1..1] ± 105
   Invoicee <Invcee> [1..1] ± 106
   InvoiceLegalStatement <InvcLglStmt> [0..1] Text 107
   PaymentMethod <PmtMtd> [0..1]  108
{Or     Code <Cd> [1..1] CodeSet 108
Or}     Proprietary <Prtry> [1..1] Text 108
3.4.2.2.1.1  Invoicer <Invcr>
Presence: [1..1]
Definition: Identification of the organisation issuing the invoice, when it is different from the creditor or
ultimate creditor.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 105 December 2025
```

