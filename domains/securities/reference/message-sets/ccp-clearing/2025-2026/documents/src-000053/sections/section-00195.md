---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["8 MX secl.007.001.03 BuyInNotificationV03"]
file_pages: [254]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.007.001.03"]
---

# 8 MX secl.007.001.03 BuyInNotificationV03

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 254 to 254.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 254

```text
8 MX secl.007.001.03
BuyInNotificationV03
8.1 MessageDefinition Functionality
Scope
The BuyInNotification message is sent by the central counterparty (CCP) to a clearing member to notify
the start of the buy in process.
The message definition is intended for use with the ISO 20022 Business Application Header.
Usage
The buy in process is a process by which the CCP buys in stocks to cover failed transactions; the
clearing member is notified that this process has started. Depending on each CCP internal rules, this
message can also be sent, as a warning, by the central counterparty to the clearing member some days
before the buy in process starts.
Outline
The BuyInNotificationV03 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. TransactionIdentification
Unambiguous identification of the transaction as known by the instructing party.
B. ClearingMember
Provides the identification of the clearing member (individual clearing member or general clearing
member).
C. NotificationDetails
Indicates if the message is a notification or a warning and gives the option to specify the buy in
date.
D. OriginalSettlementObligation
Provides details about the original settlement obligation that did not settle and for which the buy in
process will be launched.
E. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.007.001.03 BuyInNotificationV03
March 2026 254
```

