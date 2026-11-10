---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01"]
file_pages: [11]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3 camt.077.001.01 BillingReportV01

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 11 to 11.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 11

```text
3 camt.077.001.01
BillingReportV01
3.1 MessageDefinition Functionality
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
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 11 December 2025
```

