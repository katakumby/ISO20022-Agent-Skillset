---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["31 camt.070.001.06 ReturnStandingOrderV06"]
file_pages: [707]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.070.001.06"]
---

# 31 camt.070.001.06 ReturnStandingOrderV06

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 707 to 707.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 707

```text
31 camt.070.001.06
ReturnStandingOrderV06
31.1 MessageDefinition Functionality
Scope
The ReturnStandingOrder message is sent by a transaction administrator to a member.
It is used to provide information on the details of one or more standing orders, based on specific
request and return criteria.
in response to a request a on information on standing and predefined orders.
Usage
The ReturnStandingOrder message lists the standing order based on the following possible return
criteria:
- Generic standing order details,
- Details of a specific predefined or standing liquidity transfer orders,
- Details on the set to which the standing order belongs to,
- List of all predefined and standing liquidity transfer standing orders and/or per set,
- Total amount of predefined and standing liquidity transfer orders defined in the system.
Outline
The ReturnStandingOrderV06 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Reports on standing orders.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 707 February 2025
```

