---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["9 MX secl.008.001.03 BuyInResponseV03"]
file_pages: [274]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.008.001.03"]
---

# 9 MX secl.008.001.03 BuyInResponseV03

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 274 to 274.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 274

```text
9 MX secl.008.001.03
BuyInResponseV03
9.1 MessageDefinition Functionality
Scope
The BuyInResponse message is sent by the clearing member to the central counterparty as a response
to the previous buy-in notification message.
The message definition is intended for use with the ISO 20022 Business Application Header.
Usage
The BuyInResponse may be sent in response to the BuyInNotification message. However, the use of
this message in the buy in process is optional and depends on the rules set by each central
counterparty.
Outline
The BuyInResponseV03 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. TransactionIdentification
Unambiguous identification of the transaction as known by the instructing party.
B. BuyInResponseDetails
Provides response details such as a request for delay and the number of days associated to that
request.
C. OriginalSettlementObligationDetails
Provides details about the original settlement obligation that did not settle and for which the buy in
process will be launched.
D. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.008.001.03 BuyInResponseV03
March 2026 274
```

