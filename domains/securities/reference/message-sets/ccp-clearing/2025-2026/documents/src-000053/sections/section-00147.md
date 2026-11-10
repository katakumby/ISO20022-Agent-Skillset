---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04"]
file_pages: [191]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5 MX secl.004.001.04 NetPositionV04

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 191 to 191.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 191

```text
5 MX secl.004.001.04
NetPositionV04
5.1 MessageDefinition Functionality
Scope
The Net Position Report message is sent by the central counterparty (CCP) to a clearing member to
confirm the net position of all trade legs reported during the day.
The message definition is intended for use with the ISO 20022 Business Application Header.
Usage
The central counterparty (CCP) nets all the positions per clearing account and sends the Net Position
report message to the Clearing member.
Outline
The NetPositionV04 MessageDefinition is composed of 6 MessageBuildingBlocks:
A. ReportParameters
Provides parameters of the margin report such as the creation date and time, the report currency or
the calculation date and time.
B. Pagination
Provides information about the number of used pages.
C. ClearingMember
Provides the identification of the account owner, that is the clearing member (individual clearing
member or general clearing member).
D. ClearingSegment
Clearing organisation that will clear the trade.
Note: This field allows Clearing Member Firm to segregate flows coming from clearing
counterparty's clearing system. Indeed, Clearing Member Firms receive messages from the same
system (same sender) and this field allows them to know if the message is related to equities or
derivatives.
E. NetPositionReport
Provides the net position details such as the average deal price and net quantity.
F. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 191
```

