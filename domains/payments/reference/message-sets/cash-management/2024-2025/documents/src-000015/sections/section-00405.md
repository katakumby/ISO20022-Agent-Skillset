---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["19 camt.020.001.04 GetGeneralBusinessInformationV04"]
file_pages: [558]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.020.001.04"]
---

# 19 camt.020.001.04 GetGeneralBusinessInformationV04

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 558 to 558.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 558

```text
19 camt.020.001.04
GetGeneralBusinessInformationV04
19.1 MessageDefinition Functionality
Scope
The GetGeneralBusinessInformation message is sent by a member to the transaction administrator.
It is used to request information on a broadcast-type message previously sent by the transaction
administrator to all or some of the members, giving information related to the processing business.
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
The Get General Business Information message is used in this second context. At any time during the
operating hours of the system, the member can query the transaction administrator to get information
about a report of general business information previously sent.
The member can request information based on the following elements:
- reference of the report previously delivered
- subject of the report previously delivered, detailing the purpose and content of the message
- priority of the report previously sent, and indication of its format. (Note that if the format is indicated,
the subject refers to a set of pre-agreed texts. This enumeration has to be agreed upon by the
transaction administrator and the members of the system.)
- details of the previously sent message
This message will be replied to by a ReturnGeneralBusinessInformation message.
Additional information on the generic design of the Get/Return messages can be found in the section
How to Use the Cash Management Messages.
Outline
The GetGeneralBusinessInformationV04 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Approved by the Payments SEG on 04 February 2025 camt.020.001.04
GetGeneralBusinessInformationV04
Cash Management - Maintenance 2024 - 2025 558 February 2025
```

