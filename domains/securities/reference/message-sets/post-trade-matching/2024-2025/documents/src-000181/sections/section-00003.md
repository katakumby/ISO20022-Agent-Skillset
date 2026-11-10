---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [3, 4, 5]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.023.001.02", "setr.027.001.05", "setr.029.001.02", "setr.030.001.03", "setr.044.001.04"]
---

# 1 Message Set Overview

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 3 to 5.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3

```text
1 Message Set Overview
Introduction
This document describes the Post Trade Matching message set. It includes the new version of the
MessageDefinitions that have been added as part of the maintenance cycle 2024-2025 (See MCR #
261) and approved by the Securities Standards Evaluation Group on 13 February 2025.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
semt.023.001.02
SecuritiesEndOfProcessReportV02
Sent by an executing party or an instructing party to
the custodian or an affirming party to notify that all the
necessary SecuritiesTradeConfirmation message or
any other notification of the process have been sent.
It may also be sent through Central Matching Utility
(CMU).
The instructing party is typically the investment
manager or an intermediary system/vendor
communicating on behalf of the investment manager.
The executing party is typically the broker/dealer or an
intermediary system/vendor communicating on behalf
of the broker/dealer.
The custodian or an affirming party is typically the
custodian, trustee, financial institution, intermediary
system/vendor communicating on behalf of them, or
their agent.
The ISO 20022 Business Application Header must be
used
setr.027.001.05
SecuritiesTradeConfirmationV05
Sent by an executing party to an instructing party
directly or through Central Matching Utility (CMU) to
provide trade confirmation on a per-account basis
based on instructions provided by the instructing party
in the SecuritiesAllocationInstruction message.
It may also be used to provide trade confirmation on
the trade level from an executing party or an instructing
party to the custodian or an affirming party directly or
through CMU.
The instructing party is typically the investment
manager or an intermediary system/vendor
communicating on behalf of the investment manager or
of other categories of investors.
The executing party is typically the broker/dealer or an
intermediary system/vendor communicating on behalf
of the broker/dealer.
The custodian or the affirming party is typically the
custodian, trustee, financial institution, intermediary
Approved by the Securities SEG on 13 February 2025 Message Set Overview
Post Trade Matching - Maintenance 2024 - 2025 3 February 2025
```

## File page 4

```text
MessageDefinition Definition
system/vendor communicating on behalf of them, or
their agent.
setr.029.001.02
SecuritiesTradeConfirmationCancellationV02
Sent by an executing party to an instructing party
directly or through Central Matching Utility (CMU) to
cancel the referenced SecuritiesTradeConfirmation
message that was previously sent.
The instructing party is typically the investment
manager or an intermediary system/vendor
communicating on behalf of the investment manager or
of other categories of investors.
The executing party is typically the broker/dealer or an
intermediary system/vendor communicating on behalf
of the broker/dealer.
It may also be used to cancel the trade confirmation
previously sent from an executing party or an
instructing party to a custodian or an affirming party
directly or through CMU.
The ISO 20022 Business Application Header must be
used
setr.030.001.03
SecuritiesTradeConfirmationResponseV03
Sent by an instructing party, a custodian or an affirming
party to an executing party (local matching) or to
Central Matching Utility (CMU) to affirm (accept) or
disaffirm (reject) (central matching) the
SecuritiesTradeConfirmation message. If accepting the
SecuritiesTradeConfirmation message, then the trade
is ready for settlement processing. If rejecting the
SecuritiesTradeConfirmation message, then the trade
is not ready for settlement.
The executing party is typically the broker/dealer or an
intermediary system/vendor communicating on behalf
of the broker/dealer.
The instructing party is typically the investment
manager or an intermediary system/vendor
communicating on behalf of the investment manager or
of other categories of investors.
The custodian or an affirming party is typically the
custodian, trustee, financial institution, intermediary
system/vendor communicating on behalf of them, or
their agent.
The ISO 20022 Business Application Header must be
used
Approved by the Securities SEG on 13 February 2025 Message Set Overview
Post Trade Matching - Maintenance 2024 - 2025 4 February 2025
```

## File page 5

```text
MessageDefinition Definition
setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
This message is sent from Central Matching Utility
(CMU) to an executing party or an instructing party to
advise the status of the SecuritiesTradeConfirmation
message previously sent by the party. The status may
be a processing, pending processing, affirmed or
disaffirmed, cancel or replacement by an instructing
party, a custodian or an affirming party, internal
matching, and/or matching status.
The instructing party is typically the investment
manager or an intermediary system/vendor
communicating on behalf of the investment manager or
of other categories of investors. The executing party is
typically the broker/dealer or an intermediary system/
vendor communicating on behalf of the broker/dealer.
The ISO 20022 Business Application Header must be
used
Approved by the Securities SEG on 13 February 2025 Message Set Overview
Post Trade Matching - Maintenance 2024 - 2025 5 February 2025
```

