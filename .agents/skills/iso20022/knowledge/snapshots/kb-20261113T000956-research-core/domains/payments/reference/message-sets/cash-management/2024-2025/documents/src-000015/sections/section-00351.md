---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["14 camt.015.001.04 ModifyMemberV04"]
file_pages: [495]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.015.001.04"]
---

# 14 camt.015.001.04 ModifyMemberV04

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 495 to 495.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 495

```text
14 camt.015.001.04
ModifyMemberV04
14.1 MessageDefinition Functionality
Scope
The ModifyMember message is sent by a member to the transaction administrator.
It is used to request modifications to the static data related to the profile of a member that the
transaction administrator maintains.
Usage
The transaction administrator is in charge of providing the members with business information. The
term business information covers all information related to the management of the system, that is, not
related to the transactions entered into the system. The type of business information available can vary
depending on the system. Among other things, it can, refer to information about the membership of the
system.
At any time during the operating hours of the system, the member can request the transaction
administrator to modify the information it maintains about the member.
The member will submit a message requesting modifications in one or more of the following criteria:
- identification of the member
- contact information for the member organization: postal address, e-mail address, telephone or fax
number
- identification of contact persons for the member, their role and/or details (postal address, e-mail
address, telephone or fax number)
Based on the criteria received within the Modify Member message, the transaction administrator will
execute or reject the requested modifications.
In principle, the transaction administrator may send a Receipt message as a reply to the ModifyMember
request. To verify the outcome of the request, the member may submit a GetMember message with the
appropriate search criteria.
Outline
The ModifyMemberV04 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. MemberIdentification
Unique and unambiguous identifier of a system member, as assigned by the system, or the system
administrator.
C. NewMemberValueSet
New member values.
Approved by the Payments SEG on 04 February 2025 camt.015.001.04 ModifyMemberV04
Cash Management - Maintenance 2024 - 2025 495 February 2025
```

