---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["26 camt.048.001.07 ModifyReservationV07"]
file_pages: [654]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.048.001.07"]
---

# 26 camt.048.001.07 ModifyReservationV07

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 654 to 654.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 654

```text
26 camt.048.001.07
ModifyReservationV07
26.1 MessageDefinition Functionality
Scope
The ModifyReservation message is used to request modifications in the details of one particular
reservation set by the member and managed by the transaction administrator.
Usage
After the receipt of a ModifyReservation message the transaction administrator checks whether the
amount of liquidity on the member account is sufficient to set the reservation.
If there is enough liquidity available, the requested amount will be reserved. In case the requested
amount exceeds the available liquidity, only the available liquidity will be reserved. The difference will
not be blocked at a later point, even if the account balance of the member reaches the level of the initial
reservation request.
The reservation can be effected directly by the member, who has the possibility to:
- reset the reserved liquidity to zero
- change the reservation amount during the day with immediate effect
- input a default reservation amount for the following day(s); valid until a new reservation amount is
requested
After the receipt of a ModifyReservation message the transaction administrator checks whether the
amount of liquidity on the member account is sufficient to set the reservation.
Outline
The ModifyReservationV07 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReservationIdentification
Identification of the default reservation.
C. NewReservationValueSet
New reservation values.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.048.001.07 ModifyReservationV07
Cash Management - Maintenance 2024 - 2025 654 February 2025
```

