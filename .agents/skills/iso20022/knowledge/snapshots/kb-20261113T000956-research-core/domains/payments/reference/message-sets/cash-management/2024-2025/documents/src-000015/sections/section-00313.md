---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["11 camt.012.001.08 DeleteLimitV08"]
file_pages: [450]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.012.001.08"]
---

# 11 camt.012.001.08 DeleteLimitV08

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 450 to 450.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 450

```text
11 camt.012.001.08
DeleteLimitV08
11.1 MessageDefinition Functionality
Scope
The DeleteLimit message is sent by a member to the transaction administrator.
It is used to request the deletion of one particular, several or all limits set by the member and managed
by the transaction administrator.
The DeleteLimit message may delete several types of current limits (risk or liquidity management limit),
based on a multiple requests.
Usage
The member will submit a DeleteLimit message identifying which limit(s) it wants to delete (current limit
risk/liquidity limit concepts have been merged) based on following criteria:
- type of limit(s) (current/default)
- value of the limit(s) (default and/or current limit(s))
- identification of the counterparty (bilateral limit)
Based on the criteria received within the DeleteLimit message, the transaction administrator will
execute or reject the requested modifications.
The transaction administrator may send a Receipt message as a reply to the DeleteLimit request.
To verify the outcome of the request, the member may submit a GetLimit message with the appropriate
search criteria.
Outline
The DeleteLimitV08 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. LimitDetails
Identifies one particular limit set by the member and managed by the transaction administrator.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.012.001.08 DeleteLimitV08
Cash Management - Maintenance 2024 - 2025 450 February 2025
```

