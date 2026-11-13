---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["24 camt.046.001.08 GetReservationV08"]
file_pages: [624]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.046.001.08"]
---

# 24 camt.046.001.08 GetReservationV08

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 624 to 624.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 624

```text
24 camt.046.001.08
GetReservationV08
24.1 MessageDefinition Functionality
Scope
The GetReservation message is sent by a member to the transaction administrator.
It is used to request information on the details of one or more reservation facilities set by the member
and managed by the transaction administrator.
Usage
The member can request reservations information based on the following elements:
- identification of the system;
- identification of the account;
- status of the reservation (default and/or current);
- type of reservation.
This message will be replied to by a ReturnReservation message.
Outline
The GetReservationV08 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReservationQueryDefinition
Definition of the reservation query.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.046.001.08 GetReservationV08
Cash Management - Maintenance 2024 - 2025 624 February 2025
```

