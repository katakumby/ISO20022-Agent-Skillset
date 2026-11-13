---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [3]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.076.001.01", "camt.077.001.01"]
---

# 1 Message Set Overview

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 3 to 3.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3

```text
1 Message Set Overview
Introduction
This document describes the Target2-Securities - Billing message set. It includes the new billing
MessageDefinitions that have been developed in the scope of the Target2-Securities Business
Justification (See BJ#042) and approved by the Securities SEG on 20 November 2025 and the
Payments SEG on 01 December 2025, under the lead of the Securities SEG.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
camt.076.001.01
BillingReportRequestV01
The BillingReportRequest message is sent by the
system member to the system transaction
administrator to request cumulative or itemised billing
data. The billing data may be cumulative information or
aggregated information on the level of a single
securities or a dedicated cash account within a given
period for each service item.
camt.077.001.01
BillingReportV01
The BillingReport message is exchanged between the
system transaction administrator and a system
member. It aims at providing the invoice or invoice
cancellation and informing about data providing
cumulative or itemised details backing an invoice.
BillingReport is used for the following usages:
- Invoice
The Cumulative Invoice will consist of the following:
- Sum of the total number of units per service item for
each CSD or CB;
- Sum of the amounts based on the total number of
units per service item for each CSD or CB;
- Cancellation status of the invoice data.
- Invoice Cancellation
- Cumulative Billing Data Query Response:
The BillingReport message is also used to inform the
system member about details backing an invoice. This
can be sent via cumulative billing data or itemised
billing data as response to an invoice query message.
Itemised Billing Data Query Response: The
BillingReport message is also used to inform the
system member about details backing an invoice. This
can be via cumulative billing data or itemised billing
data as response to an invoice query message.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Set Overview
Target2-Securities - Billing 3 December 2025
```

