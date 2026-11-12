---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["17 camt.018.001.05 GetBusinessDayInformationV05"]
file_pages: [522]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.018.001.05"]
---

# 17 camt.018.001.05 GetBusinessDayInformationV05

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 522 to 522.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 522

```text
17 camt.018.001.05
GetBusinessDayInformationV05
17.1 MessageDefinition Functionality
Scope
The GetBusinessDayInformation message is sent by a member to the transaction administrator.
It is used to request information on different types of administrative data linked to the system.
Usage
The transaction administrator is in charge of providing the members with business information. The
term business day information covers all information related to the management of the system, not
related to the transactions created in the system. The type of business day information available can
vary depending on the system.
At any time during the operating hours of the system, the member can query the transaction
administrator to get information about the static data of the system.
The member can request information based on the following elements:
- identification of the system
- currency within the system concerned
- status of the system
- period of availability of a given currency linked to the system concerned (in case the system handles
more than one currency)
- closure information (dates when the system will be inactive and reasons for this inactivity)
- event indicator (types of event and precise timing of their occurrence within the system concerned)
This message will be replied to by a ReturnBusinessDayInformation message. Additional information on
the generic design of the Get/Return messages can be found in the section How to Use the Cash
Management Messages.
Outline
The GetBusinessDayInformationV05 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. BusinessDayInformationQueryDefinition
Defines the business day information query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.018.001.05 GetBusinessDayInformationV05
Cash Management - Maintenance 2024 - 2025 522 February 2025
```

