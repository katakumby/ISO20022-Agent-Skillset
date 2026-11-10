---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["70 semt.025.001.01 SecuritiesAccountPositionQueryV01"]
file_pages: [2401]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.025.001.01"]
---

# 70 semt.025.001.01 SecuritiesAccountPositionQueryV01

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2401 to 2401.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2401

```text
70 semt.025.001.01
SecuritiesAccountPositionQueryV01
70.1 MessageDefinition Functionality
The SecuritiesAccountPositionQuery message is sent by an account owner to an account servicer or
servicing party to request an account view on the position at a particular point in time period, or during a
particular time period, where all positions are summarised in the account structure that is compatible
with the query.
Usage:
The message may also be used to:
-re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
-re-send to a third party a copy of a message for information (the sub-function of the message is
CopyDuplicate).
Outline
The SecuritiesAccountPositionQueryV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. Statement
Defines the criteria used to report on the securities account position.
B. SearchCriteria
Provides the criteria in the form of business attributes to extract the securities account position
result set.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.025.001.01
SecuritiesAccountPositionQueryV01
Target2-Securities 2401 August 2026
```

