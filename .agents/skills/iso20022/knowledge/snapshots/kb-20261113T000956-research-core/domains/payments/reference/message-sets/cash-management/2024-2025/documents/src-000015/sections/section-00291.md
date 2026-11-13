---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["10 camt.011.001.08 ModifyLimitV08"]
file_pages: [422]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.011.001.08"]
---

# 10 camt.011.001.08 ModifyLimitV08

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 422 to 422.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 422

```text
10 camt.011.001.08
ModifyLimitV08
10.1 MessageDefinition Functionality
Scope
The ModifyLimit message is sent by a member to the transaction administrator.
It is used to request modifications in the details of one particular, several or all limits set by the member
and managed by the transaction administrator.
Each ModifyLimit message can alter only one type of limit (current or default).
Usage
At any time during the operating hours of the system, the member can request modifications in the
limits it has set. For example, the reason may be to unlock the payments queue regarding a particular
member, or following a risk management decision issued after an exceptional event has occurred.
The member will submit a message requesting modifications in one or more of the following criteria:
- type of limit (current/default)
- identification of the system
- identification of the counterparty
- value of the limit(s) (default and/or current limit(s))
- point in time when the limit becomes effective
Based on the criteria received within the ModifyLimit message, the transaction administrator will
execute or reject the requested modification. The transaction administrator may send a Receipt
message as a reply to the ModifyLimit request. To verify the outcome of the request, the member may
submit a GetLimit message with the appropriate search criteria.
Outline
The ModifyLimitV08 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. LimitDetails
Identifies one particular limit set by the member and managed by the transaction administrator.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.011.001.08 ModifyLimitV08
Cash Management - Maintenance 2024 - 2025 422 February 2025
```

