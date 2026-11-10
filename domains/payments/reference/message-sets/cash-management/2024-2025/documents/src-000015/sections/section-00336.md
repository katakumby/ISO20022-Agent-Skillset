---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["13 camt.014.001.05 ReturnMemberV05"]
file_pages: [476, 477]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.014.001.05"]
---

# 13 camt.014.001.05 ReturnMemberV05

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 476 to 477.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 476

```text
13 camt.014.001.05
ReturnMemberV05
13.1 MessageDefinition Functionality
Scope
The ReturnMember message is sent by the transaction administrator to a member of the system.
It is used to provide information on static data maintained by the transaction administrator and related to
the participants in the system and their membership status vis-a-vis this system.
The ReturnMember message can be sent as a response to a related GetMember message (pull mode)
or initiated by the transaction administrator (push mode). The push of information can take place either
at prearranged times or as a warning or alarm when a problem has occurred.
Usage
The transaction administrator is in charge of providing the members with business information. The
term business information covers all information related to the management of the system, that is, not
related to the transactions entered into in the system. The type of business information available can
vary depending on the system. Among other things, it can refer to information about the membership of
the system.
The member can request information about the members of the system through a series of criteria,
corresponding to the known information stored within the transaction administrator. Based on the
criteria received within the request, the transaction administrator will select items that will match with the
request and report them to the requestor.
The transaction administrator may also send a Return Member message with pre-defined information at
times previously agreed with the member or to warn the member about a particular problem that may
have arisen and which needs the member(s) attention.
The message from the transaction administrator can contain information based on the following
elements:
- identification of the member within the system
- membership status
- type of member
- contact details for the member: name, address
- identification of the member's account
- identification of contact persons for the member, their role and details.
Outline
The ReturnMemberV05 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 476 February 2025
```

## File page 477

```text
Common business identification for the message.
B. ReportOrError
Reports on members.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 477 February 2025
```

