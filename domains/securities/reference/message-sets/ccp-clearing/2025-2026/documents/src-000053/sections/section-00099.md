---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05"]
file_pages: [124]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4 MX secl.003.001.05 TradeLegStatementV05

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 124 to 124.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 124

```text
4 MX secl.003.001.05
TradeLegStatementV05
4.1 MessageDefinition Functionality
Scope
The TradeLegStatement message is sent by the central counterparty (CCP) to a clearing member to
report all trades that have been executed by the trading platform.
The message definition is intended for use with the ISO20022 Business Application Header.
Usage
The TradeLegStatement message may be either sent:
- during the day (to report trades execution by batch) or
- as an end of day report.
Outline
The TradeLegStatementV05 MessageDefinition is composed of 6 MessageBuildingBlocks:
A. StatementParameters
Provides various statement parameters such as the statement identification, the statement date
and time or the statement frequency.
B. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
C. ClearingMember
Provides the identification of the account owner, that is the clearing member (individual clearing
member or general clearing member).
D. ClearingAccount
Identifies the clearing member account at the Central counterparty through which the trade must be
cleared (sometimes called position account).
E. StatementDetails
Provides the statement details.
F. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 124
```

