---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [4, 5]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05", "secl.002.001.05", "secl.003.001.05", "secl.004.001.04", "secl.005.001.02", "secl.006.001.02", "secl.007.001.03", "secl.008.001.03", "secl.009.001.03", "secl.010.001.04"]
---

# 1 Message Set Overview

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 4 to 5.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4

```text
1 Message Set Overview
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
secl.001.001.05
TradeLegNotificationV05
The TradeLegNotification message is sent by the
central counterparty (CCP) to a clearing member to
report the trade that has been executed by the trading
platform.
The message definition is intended for use with the
ISO20022 Business Application Header.
secl.002.001.05
TradeLegNotificationCancellationV05
The TradeLegNotificationCancellation message is sent
by the central counterparty (CCP) to a clearing
member to notify the cancellation of a
TradeLegNotification message previously sent.
The message definition is intended for use with the
ISO20022 Business Application Header.
secl.003.001.05
TradeLegStatementV05
The TradeLegStatement message is sent by the
central counterparty (CCP) to a clearing member to
report all trades that have been executed by the
trading platform.
The message definition is intended for use with the
ISO20022 Business Application Header.
secl.004.001.04
NetPositionV04
The Net Position Report message is sent by the central
counterparty (CCP) to a clearing member to confirm
the net position of all trade legs reported during the
day.
The message definition is intended for use with the
ISO 20022 Business Application Header.
secl.005.001.02
MarginReportV02
The MarginReport message is sent by the central
counterparty (CCP) to a clearing member to report on:
- the exposure resulting from the trade positions
- the value of the collateral held by the CCP (market
value of this collateral) and
- the resulting difference representing the risk
encountered by the CCP.
The message definition is intended for use with the
ISO20022 Business Application Header.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Set Overview
March 2026 4
```

## File page 5

```text
MessageDefinition Definition
secl.006.001.02
DefaultFundContributionReportV02
The DefaultFundContributionReport message is sent
by the central counterparty (CCP) to a Clearing
member to report on the calculation of the default fund
contribution and the potential net excess or deficit.
The message definition is intended for use with the
ISO20022 Business Application Header.
secl.007.001.03
BuyInNotificationV03
The BuyInNotification message is sent by the central
counterparty (CCP) to a clearing member to notify the
start of the buy in process.
The message definition is intended for use with the
ISO 20022 Business Application Header.
secl.008.001.03
BuyInResponseV03
The BuyInResponse message is sent by the clearing
member to the central counterparty as a response to
the previous buy-in notification message.
The message definition is intended for use with the
ISO 20022 Business Application Header.
secl.009.001.03
BuyInConfirmationV03
The Buy In Confirmation message is sent by the
central counterparty (CCP) to the clearing member to
confirm the details of the transaction resulting from the
buy in.
The message definition is intended for use with the
ISO 20022 Business Application Header.
secl.010.001.04
SettlementObligationReportV04
The SettlementObligationReport message is sent by
the central counterparty (CCP) to a clearing member to
report on the settlement obligation that will be
submitted for settlement.
The message definition is intended for use with the
ISO20022 Business Application Header.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Set Overview
March 2026 5
```

