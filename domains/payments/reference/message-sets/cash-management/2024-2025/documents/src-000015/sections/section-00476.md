---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["25 camt.047.001.08 ReturnReservationV08"]
file_pages: [636]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.047.001.08"]
---

# 25 camt.047.001.08 ReturnReservationV08

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 636 to 636.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 636

```text
25 camt.047.001.08
ReturnReservationV08
25.1 MessageDefinition Functionality
Scope
The ReturnReservation message is sent by the transaction administrator to a member.
It is used to provide information on the details of one or more reservation facilities set by the member
and managed by the transaction administrator.
The ReturnReservation message can be sent as a response to a related Get Reservation message
(pull mode) or initiated by the transaction administrator (push mode). The push of information can take
place either at prearranged times or as a warning or alarm when a problem has occurred.
Usage
At any time during the operating hours of the system, the member can query the transaction
administrator to get information about the reservations facilities that the transaction administrator
manages for the member.
The transaction administrator will send reservations information to the member based on the following
elements:
- identification of the system
- identification of the account
- status of the reservation (default and/or current )
- type of reservation.
Outline
The ReturnReservationV08 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Reports on reservations.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.047.001.08 ReturnReservationV08
Cash Management - Maintenance 2024 - 2025 636 February 2025
```

