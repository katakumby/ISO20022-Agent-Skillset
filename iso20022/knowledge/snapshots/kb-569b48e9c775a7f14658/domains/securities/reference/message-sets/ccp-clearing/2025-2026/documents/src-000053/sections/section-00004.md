---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05"]
file_pages: [6, 7]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2 MX secl.001.001.05 TradeLegNotificationV05

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 6 to 7.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 6

```text
2 MX secl.001.001.05
TradeLegNotificationV05
2.1 MessageDefinition Functionality
Scope
The TradeLegNotification message is sent by the central counterparty (CCP) to a clearing member to
report the trade that has been executed by the trading platform.
The message definition is intended for use with the ISO20022 Business Application Header.
Usage
The CCP reports both sides of the trade from the clearing member perspective. The CCP sends a
message to the global clearing member of the seller and a message to the global clearing member of
the buyer. Note: An individual clearing member only clear its own trades.
Outline
The TradeLegNotificationV05 MessageDefinition is composed of 8 MessageBuildingBlocks:
A. ClearingMember
Provides the identification of the clearing member (individual clearing member or general clearing
member).
B. ClearingAccount
Identifies the clearing member account at the CCP through which the trade must be cleared
(sometimes called position account).
C. DeliveryAccount
An account opened by the central counterparty in the name of the clearing member or its
settlement agent within the account structure, for settlement purposes (gives information about the
clearing member/its settlement agent account at the central securities depository).
D. NonClearingMember
Provides details about the non clearing member identification and account.
E. ClearingDetails
Provides clearing details such as the settlement netting (or not) eligibility code or the clearing
segment.
F. TradeLegDetails
Provides details about the trade leg such as the trade date, the settlement date or the trading
currency.
G. SettlementDetails
Provides details about the settlement details of the trade leg such the settlement amount or the
place of settlement.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 6
```

## File page 7

```text
H. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 7
```

