---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05"]
file_pages: [64, 65]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3 MX secl.002.001.05 TradeLegNotificationCancellationV05

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 64 to 65.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 64

```text
3 MX secl.002.001.05
TradeLegNotificationCancellationV05
3.1 MessageDefinition Functionality
Scope
The TradeLegNotificationCancellation message is sent by the central counterparty (CCP) to a clearing
member to notify the cancellation of a TradeLegNotification message previously sent.
The message definition is intended for use with the ISO20022 Business Application Header.
Usage
The previously sent message must be the Trade Leg Notification message.
Outline
The TradeLegNotificationCancellationV05 MessageDefinition is composed of 9
MessageBuildingBlocks:
A. ClearingMember
Provides the identification of the account owner, that is the clearing member (individual clearing
member or general clearing member).
B. ClearingAccount
Identifies the clearing member account at the Central counterparty through which the trade must be
cleared.
C. DeliveryAccount
An account opened by the central counterparty in the name of the clearing member or its
settlement agent within the account structure, for settlement purposes (gives information about the
clearing member/its settlement agent account at the central securities depository).
D. NonClearingMember
Provides details about the non clearing member identification and account.
E. ClearingDetails
Provides clearing details such as the non clearing member identification or the settlement netting
(or not) eligibility code.
F. TradeLegDetails
Provides details about the trade leg such as the trade date, the settlement date or the trading
currency.
G. SettlementDetails
Provides details about the settlement details of the trade leg such as the settlement currency or the
place of settlement.
H. CancellationReason
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 64
```

## File page 65

```text
Specifies the reason for the cancellation.
I. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 65
```

