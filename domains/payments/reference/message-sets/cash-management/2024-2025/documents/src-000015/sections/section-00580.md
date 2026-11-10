---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["34 camt.102.001.03 CreateStandingOrderV03"]
file_pages: [755]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.102.001.03"]
---

# 34 camt.102.001.03 CreateStandingOrderV03

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 755 to 755.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 755

```text
34 camt.102.001.03
CreateStandingOrderV03
34.1 MessageDefinition Functionality
Scope
The CreateStandingOrder message is sent by a member to the transaction administrator.
It is used to create a permanent order for the transfer of funds between two accounts belonging to the
same member and being held at the transaction administrator.
Usage
Based on the criteria defined in the CreateStandingOrder message, the transaction administrator will
execute or reject the requested creation and respond with a Receipt message as a reply to the request.
Outline
The CreateStandingOrderV03 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. StandingOrderIdentification
Identifies the standing order.
C. ValueSet
Set of values for the standing order.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.102.001.03 CreateStandingOrderV03
Cash Management - Maintenance 2024 - 2025 755 February 2025
```

