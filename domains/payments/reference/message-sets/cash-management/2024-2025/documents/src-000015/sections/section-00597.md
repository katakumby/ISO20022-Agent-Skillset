---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["36 camt.104.001.01 CreateMemberV01"]
file_pages: [773]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.104.001.01"]
---

# 36 camt.104.001.01 CreateMemberV01

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 773 to 773.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 773

```text
36 camt.104.001.01
CreateMemberV01
36.1 MessageDefinition Functionality
Scope
The ModifyMember message is sent by a member to the transaction administrator.
It is used to create the profile of a member that the transaction administrator maintains.
Usage
Based on the criteria defined in the CreateLimit message, the transaction administrator will execute or
reject the requested creation and respond with a Receipt message as a reply to the request.
Outline
The CreateMemberV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. MemberIdentification
Unique and unambiguous identifier of a system member, as assigned by the system, or the system
administrator.
C. ValueSet
New member values.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.104.001.01 CreateMemberV01
Cash Management - Maintenance 2024 - 2025 773 February 2025
```

