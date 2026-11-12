---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["9 camt.010.001.09 ReturnLimitV09"]
file_pages: [391, 392]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.010.001.09"]
---

# 9 camt.010.001.09 ReturnLimitV09

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 391 to 392.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 391

```text
9 camt.010.001.09
ReturnLimitV09
9.1 MessageDefinition Functionality
Scope
The ReturnLimit message is sent by the transaction administrator to a member of the system.
It is used to provide information on the details of one or more limits set by the member (or on behalf of
the member) and managed by the transaction administrator.
The ReturnLimit message can be sent as a response to a related GetLimit message (pull mode) or
initiated by the transaction administrator (push mode). The push of information can take place either at
prearranged times or as a warning or alarm when a problem has occurred.
Usage
At any time during the operating hours of the system, the member can query the transaction
administrator to get information about the limit(s) that the transaction administrator manages for the
member.
The transaction administrator may also send a ReturnLimit message with pre-defined information at
times previously agreed with the member or to warn the member about a particular problem that may
have arisen and which needs attention.
The message from the transaction administrator can contain information on the following elements:
- type of risk and/or liquidity limit
- value of the limit(s) (default and/or current limit(s) for risk and/or liquidity management)
- identification of the system
- status of the limit(s) (default and/or current limit(s) for risk and/or liquidity management)
- point in time when the limit becomes effective
- identification of the counterparty
Additional information on the generic design of the Get/Return messages can be found in the section
How to Use the Cash Management Messages.
Outline
The ReturnLimitV09 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Reports on limits.
C. SupplementaryData
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 391 February 2025
```

## File page 392

```text
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 392 February 2025
```

