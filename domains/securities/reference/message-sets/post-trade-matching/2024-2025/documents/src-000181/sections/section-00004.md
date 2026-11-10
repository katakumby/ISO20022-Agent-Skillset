---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 semt.023.001.02 SecuritiesEndOfProcessReportV02"]
file_pages: [6]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.023.001.02"]
---

# 2 semt.023.001.02 SecuritiesEndOfProcessReportV02

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 6 to 6.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 6

```text
2 semt.023.001.02
SecuritiesEndOfProcessReportV02
2.1 MessageDefinition Functionality
Scope
Sent by an executing party or an instructing party to the custodian or an affirming party to notify that all
the necessary SecuritiesTradeConfirmation message or any other notification of the process have been
sent.
It may also be sent through Central Matching Utility (CMU).
The instructing party is typically the investment manager or an intermediary system/vendor
communicating on behalf of the investment manager.
The executing party is typically the broker/dealer or an intermediary system/vendor communicating on
behalf of the broker/dealer.
The custodian or an affirming party is typically the custodian, trustee, financial institution, intermediary
system/vendor communicating on behalf of them, or their agent.
The ISO 20022 Business Application Header must be used
Usage
Initiator: Executing Party, CMU or Instructing Party
Respondent: Custodian or an affirming party does not need to respond.
Outline
The SecuritiesEndOfProcessReportV02 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. Pagination
Number used to sequence pages when it is not possible for data to be conveyed in a single
message and the data has to be split across several pages (messages).
B. ReportGeneralDetails
Notifies the type of report transmitted.
C. ConfirmationParties
Parties involved in the confirmation of the details of a trade.
D. Investor
Party that identifies the underlying investor.
E. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 13 February 2025 semt.023.001.02
SecuritiesEndOfProcessReportV02
Post Trade Matching - Maintenance 2024 - 2025 6 February 2025
```

