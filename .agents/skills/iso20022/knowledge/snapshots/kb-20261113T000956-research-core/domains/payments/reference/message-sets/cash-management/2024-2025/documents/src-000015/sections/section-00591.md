---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["35 camt.103.001.03 CreateReservationV03"]
file_pages: [767]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.103.001.03"]
---

# 35 camt.103.001.03 CreateReservationV03

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 767 to 767.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 767

```text
35 camt.103.001.03
CreateReservationV03
35.1 MessageDefinition Functionality
Scope
The CreateReservation message is used to request for the creation of one particular reservation by the
member and managed by the transaction administrator.
Usage
Based on the criteria defined in the CreateReservation message, the transaction administrator will
execute or reject the requested creation and respond with a Receipt message as a reply to the request.
Outline
The CreateReservationV03 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReservationIdentification
Identification of the default reservation.
C. ValueSet
New reservation values.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.103.001.03 CreateReservationV03
Cash Management - Maintenance 2024 - 2025 767 February 2025
```

