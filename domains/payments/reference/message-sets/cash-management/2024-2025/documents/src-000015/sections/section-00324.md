---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["12 camt.013.001.04 GetMemberV04"]
file_pages: [464]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.013.001.04"]
---

# 12 camt.013.001.04 GetMemberV04

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 464 to 464.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 464

```text
12 camt.013.001.04
GetMemberV04
12.1 MessageDefinition Functionality
Scope
The GetMember message is sent by a member to the transaction administrator.
It is used to request information on static data maintained by the transaction administrator and related
to the participants in the system and their membership status vis-a-vis this system.
Usage
The transaction administrator is in charge of providing the members with business information. The
term business information covers all information related to the management of the system, that is, not
related to the transactions entered into the system. The type of business information available can vary
depending on the system. Among other things, it can refer to information about the membership of the
system.
At any time during the operating hours of the system, the member can query the transaction
administrator to get information about the static data related to the members of the system.
The member can request information based on the following elements:
- identification of the member within the system
- membership status
- type of member
- contact details for the member: name, address
- account number of the member
- identification of contact persons for the member
This message will be replied to by a ReturnMember message.
Additional information on the generic design of the Get/Return messages can be found in the MDR Part
1 section How to Use the Cash Management Messages.
Outline
The GetMemberV04 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. MemberQueryDefinition
Definition of the member query.
C. SupplementaryData
Approved by the Payments SEG on 04 February 2025 camt.013.001.04 GetMemberV04
Cash Management - Maintenance 2024 - 2025 464 February 2025
```

