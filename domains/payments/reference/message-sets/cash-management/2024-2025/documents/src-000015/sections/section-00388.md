---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["18 camt.019.001.07 ReturnBusinessDayInformationV07"]
file_pages: [535, 536]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.019.001.07"]
---

# 18 camt.019.001.07 ReturnBusinessDayInformationV07

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 535 to 536.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 535

```text
18 camt.019.001.07
ReturnBusinessDayInformationV07
18.1 MessageDefinition Functionality
Scope
The ReturnBusinessDayInformation message is sent by the transaction administrator to a member of
the system.
It is used to provide information on different types of administrative data linked to the system.
The ReturnBusinessDayInformation message can be sent as a response to a related GetBusines
DayInformation message (pull mode), or initiated by the transaction administrator (push mode). The
push of information can take place either at prearranged times or as a warning or alarm when a
problem has occurred.
Usage
The transaction administrator is in charge of providing the members with business information. The
term business day information covers all information related to the management of the system, that is,
not related to the transactions or requests created in the system. The type of business information
available can vary depending on the system.
The member can request information about the static data of the system through a series of criteria,
corresponding to the known information stored within the transaction administrator. Based on the
criteria received within the request, the transaction administrator will select items that match the request
and report them to the requester.
The transaction administrator may also send a ReturnBusinessDayInformation message with pre-
defined information at times previously agreed with the member or to warn the member about a
particular problem that may have arisen and which needs attention.
The message from the transaction administrator can contain information based on the following
elements:
- identification of the system
- status of the system and period in which this status is valid
- currency within the system concerned and details of the hours of availability linked to that particular
currency
- events related to the functioning of the system and the timing of their occurrence
Additional information on the generic design of the Get/Return messages can be found in the MDR Part
1 section How to Use the Cash Management Messages.
Outline
The ReturnBusinessDayInformationV07 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 535 February 2025
```

## File page 536

```text
Common business identification for the message.
B. ReportOrError
Reports on business day information.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 536 February 2025
```

