---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["30 camt.069.001.05 GetStandingOrderV05"]
file_pages: [686]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.069.001.05"]
---

# 30 camt.069.001.05 GetStandingOrderV05

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 686 to 686.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 686

```text
30 camt.069.001.05
GetStandingOrderV05
30.1 MessageDefinition Functionality
Scope
The GetStandingOrder message is sent by a member to the transaction administrator.
It is used to request information on the details of one or more standing orders, based on specific
request criteria, especially to query the amount of the overall liquidity available. It will allow to query
both reserved liquidity and liquidity available for normal operations.
Usage
The member can request information based on the following elements:
- individual standing orders (predefined or standing liquidity transfer orders)
- amount
- account to be credited
- account to be debited
- account owner (for on behalf scenario)
- frequency of payment
- daytime or overnight processing
- dates when the standing order begins and ceases to be effective
This message will be answered by a ReturnStandingOrder message.
Outline
The GetStandingOrderV05 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. StandingOrderQueryDefinition
Defines the account query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 686 February 2025
```

