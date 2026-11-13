---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "15.4.2.1.8.3 ServiceCategoryTotals <SvcCtgyTtls>", "15.4.2.1.8.3.4 ServiceCategory <SvcCtgy>", "15.4.2.1.8.3.4.1 Code <Cd>"]
file_pages: [290]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.8.3.4.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 290 to 290.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 290

```text
ServiceCategory <SvcCtgy> contains one of the following ServiceCategory1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 290
Or}   Proprietary <Prtry> [1..1] Text 290
15.4.2.1.8.3.4.1  Code <Cd>
Presence: [1..1]
Definition: Service category, as published in an external reason code list.
Datatype: "ExternalServiceCategory1Code" on page 3245
15.4.2.1.8.3.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Service category, in a proprietary form.
Datatype: "Max4AlphaNumericText" on page 3328
15.4.2.1.8.3.5  ServiceItemTotals <SvcItmTtls>
Presence: [0..*]
Definition: Totals related to the invoice.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 290 August 2026
```

