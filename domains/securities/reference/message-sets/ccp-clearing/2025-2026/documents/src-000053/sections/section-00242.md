---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04"]
file_pages: [316, 317]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11 MX secl.010.001.04 SettlementObligationReportV04

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 316 to 317.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 316

```text
11 MX secl.010.001.04
SettlementObligationReportV04
11.1 MessageDefinition Functionality
Scope
The SettlementObligationReport message is sent by the central counterparty (CCP) to a clearing
member to report on the settlement obligation that will be submitted for settlement.
The message definition is intended for use with the ISO20022 Business Application Header.
Usage
The SettlementObligationReport message may also be sent to a third party processing the settlement
obligation(s) on behalf of more than one clearing member.
The Settlement Obligation Report message is provided per delivery account and per instrument. The
report can be provided for one specific delivering party or one specific receiving party. It can also be
generated per non clearing member.
Outline
The SettlementObligationReportV04 MessageDefinition is composed of 8 MessageBuildingBlocks:
A. ReportParameters
Provides details about the report such as the report identification, the creation date and time.
B. Pagination
Page number of the message (within a report) and continuation indicator to indicate that the report
is to continue or that the message is the last page of the report.
C. ClearingMember
Provides the identification of the clearing member (individual clearing member or general clearing
member).
D. ClearingSegment
Clearing organisation that will clear the trade.
Note: This field allows Clearing Member Firm to segregate flows coming from clearing
counterparty's clearing system. Indeed, Clearing Member Firms receive messages from the same
system (same sender) and this field allows them to know if the message is related to equities or
derivatives.
E. DeliveryAccount
Provides the identification of the account used for netting. This is an account opened by the central
counterparty in the name of the clearing member or its settlement agent within the account
structure, for settlement purposes (gives information about the clearing member/its settlement
agent account at the central securities depository).
F. ReportDetails
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 316
```

## File page 317

```text
Provides details on the settlement obligation report.
G. SettlementParties
Provides details about the receiving parties involved in the settlement chain.
H. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 317
```

