---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["2 semt.025.001.01 SecuritiesAccountPositionQueryV01"]
file_pages: [5]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.025.001.01"]
---

# 2 semt.025.001.01 SecuritiesAccountPositionQueryV01

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 5 to 5.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5

```text
2 semt.025.001.01
SecuritiesAccountPositionQueryV01
2.1 MessageDefinition Functionality
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
Approved by the Securities SEG 19 February 2026. semt.025.001.01
SecuritiesAccountPositionQueryV01
Target2-Securities - Securities and Penalty Reporting 5 March 2026
```

