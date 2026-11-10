---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01"]
file_pages: [240]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15 camt.077.001.01 BillingReportV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 240 to 240.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 240

```text
15 camt.077.001.01
BillingReportV01
15.1 MessageDefinition Functionality
The BillingReport message is exchanged between the system transaction administrator and a system
member. It aims at providing the invoice or invoice cancellation and informing about data providing
cumulative or itemised details backing an invoice.
BillingReport is used for the following usages:
- Invoice
The Cumulative Invoice will consist of the following:
- Sum of the total number of units per service item for each CSD or CB;
- Sum of the amounts based on the total number of units per service item for each CSD or CB;
- Cancellation status of the invoice data.
- Invoice Cancellation
- Cumulative Billing Data Query Response:
The BillingReport message is also used to inform the system member about details backing an invoice.
This can be sent via cumulative billing data or itemised billing data as response to an invoice query
message.
Itemised Billing Data Query Response: The BillingReport message is also used to inform the system
member about details backing an invoice. This can be via cumulative billing data or itemised billing data
as response to an invoice query message.
Outline
The BillingReportV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Defines the characteristics specific to the message, such as the identification or the creation date
and time.
B. BillingReportOrError
Report on billing data or operational error.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 240 August 2026
```

