---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.2 Service <Svc>", "3.4.2.1.2.2 SystemCurrency <SysCcy>"]
file_pages: [41]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.2.2 SystemCurrency <SysCcy>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 41 to 41.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 41

```text
3.4.2.1.2.2  SystemCurrency <SysCcy>
Presence: [0..1]
Definition: Currency which may be processed by the system. A system may process transactions in a
single currency or in multiple currencies.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 143
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
3.4.2.1.3  InvoiceDate <InvcDt>
Presence: [1..1]
Definition: Date at which the billing report was created.
Datatype: "ISODate" on page 148
3.4.2.1.4  BillingIdentification <BllgId>
Presence: [1..1]
Definition: Unique identification of the billing report.
Datatype: "Max35Text" on page 153
3.4.2.1.5  BillingPeriod <BllgPrd>
Presence: [1..1]
Definition: Date period for which the report data is valid.
BillingPeriod <BllgPrd> contains the following elements (see "DatePeriod2" on page 114 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 115
   ToDate <ToDt> [1..1] Date 115
3.4.2.1.6  ResponsiblePartyIdentification <RspnsblPtyId>
Presence: [0..1]
Definition: Unique identification of the party responsible for the referenced party (that is, which has a
contractual responsibility for the billed customer).
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 41 December 2025
```

