---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["20 camt.021.001.06 ReturnGeneralBusinessInformationV06"]
file_pages: [568]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.021.001.06"]
---

# 20 camt.021.001.06 ReturnGeneralBusinessInformationV06

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 568 to 568.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 568

```text
20 camt.021.001.06
ReturnGeneralBusinessInformationV06
20.1 MessageDefinition Functionality
Scope
The ReturnGeneralBusinessInformation message is sent by the transaction administrator to a member
of the system. It is used to provide some or all of the members with information related to the
processing of the system.
The Return General Business Information message can be sent as a response to a related
GetGeneralBusinessInformation message (pull mode) or initiated by the transaction administrator (push
mode). The push of information can take place either at prearranged times or as a warning or alarm
when a problem has occurred.
Usage
The transaction administrator can send general business information messages to the members, which
may request further action from them. General business information can contain either static data
announcing foreseen events affecting the system operations, or dynamic data warning or notifying
about unexpected events.
This type of information can be transmitted in either of the two following ways:
- non-solicited reports are pushed by the transaction administrator to the (selected) members together
with a reference, a qualifier and a subject line
- upon request from the members (pull mode), the transaction administrator delivers the full text/content
of the message back to the user
In either case, the message from the transaction administrator can contain information based on the
following elements:
- subject of the report detailing the purpose and content of the message
- details of the report
- indication of the priority of the report and of its format. (Note that if the format is indicated, the subject
refers to a set of pre-agreed texts. This enumeration has to be agreed upon by the transaction
administrator and the members of the system).
Additional information on the generic design of the Get/Return messages can be found in the MDR Part
1 section How to Use the Cash Management Messages.
Outline
The ReturnGeneralBusinessInformationV06 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Approved by the Payments SEG on 04 February 2025 camt.021.001.06
ReturnGeneralBusinessInformationV06
Cash Management - Maintenance 2024 - 2025 568 February 2025
```

