---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["27 camt.049.001.07 DeleteReservationV07"]
file_pages: [663]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.049.001.07"]
---

# 27 camt.049.001.07 DeleteReservationV07

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 663 to 663.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 663

```text
27 camt.049.001.07
DeleteReservationV07
27.1 MessageDefinition Functionality
Scope
The DeleteReservation message is used to request the deletion of one particular reservation by the
member and managed by the transaction administrator.
Usage
The deletion of a reservation in the system, will not only reset the reserved liquidity to zero, but also
delete the reservation itself from the system: only the default reservation for the current business day
remains in the system.
Outline
The DeleteReservationV07 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. CurrentReservation
Identifies the current reservation to delete.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.049.001.07 DeleteReservationV07
Cash Management - Maintenance 2024 - 2025 663 February 2025
```

