---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "3.4.2.1.8.3 ServiceCategoryTotals <SvcCtgyTtls>", "3.4.2.1.8.3.4 ServiceCategory <SvcCtgy>", "3.4.2.1.8.3.4.1 Code <Cd>"]
file_pages: [61]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.8.3.4.1 Code <Cd>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 61 to 61.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 61

```text
ServiceCategory <SvcCtgy> contains one of the following ServiceCategory1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 61
Or}   Proprietary <Prtry> [1..1] Text 61
3.4.2.1.8.3.4.1  Code <Cd>
Presence: [1..1]
Definition: Service category, as published in an external reason code list.
Datatype: "ExternalServiceCategory1Code" on page 147
3.4.2.1.8.3.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Service category, in a proprietary form.
Datatype: "Max4AlphaNumericText" on page 153
3.4.2.1.8.3.5  ServiceItemTotals <SvcItmTtls>
Presence: [0..*]
Definition: Totals related to the invoice.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 61 December 2025
```

