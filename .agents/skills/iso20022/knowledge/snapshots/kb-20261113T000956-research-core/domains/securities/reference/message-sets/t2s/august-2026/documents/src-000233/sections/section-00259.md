---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.2 CancellationReport <CxlRpt>", "15.4.2.2.2 Service <Svc>", "15.4.2.2.2.2 SystemCurrency <SysCcy>"]
file_pages: [338]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.2.2.2 SystemCurrency <SysCcy>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 338 to 338.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 338

```text
15.4.2.2.2.2  SystemCurrency <SysCcy>
Presence: [0..1]
Definition: Currency which may be processed by the system. A system may process transactions in a
single currency or in multiple currencies.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 3212
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
15.4.2.2.3  InvoiceDate <InvcDt>
Presence: [1..1]
Definition: Date at which the billing report was created.
Datatype: "ISODate" on page 3319
15.4.2.2.4  BillingIdentification <BllgId>
Presence: [1..1]
Definition: Identification of the billing report.
Datatype: "Max35Text" on page 3328
15.4.2.2.5  BillingPeriod <BllgPrd>
Presence: [1..1]
Definition: Date period which for which the report data is valid.
BillingPeriod <BllgPrd> contains the following elements (see "DatePeriod2" on page 2908 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 2908
   ToDate <ToDt> [1..1] Date 2908
15.4.2.2.6  CancellationReason <CxlRsn>
Presence: [1..1]
Definition: Reason why requested billing information is cancelled.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 338 August 2026
```

