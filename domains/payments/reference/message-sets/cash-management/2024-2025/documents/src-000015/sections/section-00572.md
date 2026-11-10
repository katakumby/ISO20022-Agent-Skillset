---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["33 camt.101.001.02 CreateLimitV02"]
file_pages: [745]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.101.001.02"]
---

# 33 camt.101.001.02 CreateLimitV02

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 745 to 745.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 745

```text
33 camt.101.001.02
CreateLimitV02
33.1 MessageDefinition Functionality
Scope
The CreateLimit message is sent by a member to the transaction administrator.
It is used to create one or several limits set by the member and managed by the transaction
administrator.
Usage
Based on the criteria defined in the CreateLimit message, the transaction administrator will execute or
reject the requested creation and respond with a Receipt message as a reply to the request.
Outline
The CreateLimitV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. LimitData
Identifies one particular limit set by the member and managed by the transaction administrator.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.101.001.02 CreateLimitV02
Cash Management - Maintenance 2024 - 2025 745 February 2025
```

