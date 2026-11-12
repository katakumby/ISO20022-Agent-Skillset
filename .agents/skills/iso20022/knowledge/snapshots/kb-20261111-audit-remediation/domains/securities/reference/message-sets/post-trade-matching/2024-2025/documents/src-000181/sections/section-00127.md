---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04"]
file_pages: [162, 163]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 162 to 163.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 162

```text
6 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV0
4
6.1 MessageDefinition Functionality
Scope
This message is sent from Central Matching Utility (CMU) to an executing party or an instructing party
to advise the status of the SecuritiesTradeConfirmation message previously sent by the party. The
status may be a processing, pending processing, affirmed or disaffirmed, cancel or replacement by an
instructing party, a custodian or an affirming party, internal matching, and/or matching status.
The instructing party is typically the investment manager or an intermediary system/vendor
communicating on behalf of the investment manager or of other categories of investors. The executing
party is typically the broker/dealer or an intermediary system/vendor communicating on behalf of the
broker/dealer.
The ISO 20022 Business Application Header must be used
Usage
Initiator: In central matching the Initiator is the Central Matching Utility.
Respondent: no response is needed by the recipient of the message.
Outline
The SecuritiesTradeConfirmationStatusAdviceV04 MessageDefinition is composed of 13
MessageBuildingBlocks:
A. Identification
Information that unambiguously identifies an SecuritiesTradeConfirmationStatusAdvice message
as known by the account owner (or the instructing party acting on its behalf).
B. References
Link to another transaction that must be processed after, before or at the same time.
C. AffirmationStatus
Provides details on the affitrmation status of a trade.
D. ProcessingStatus
Provides the processing status of a trade.
E. MatchingStatus
Provides details on the matching status of a trade.
F. ReplacementProcessingStatus
Provides the replacement processing status of a trade.
G. CancellationProcessingStatus
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 162 February 2025
```

## File page 163

```text
Provides details on the cancellation status of a trade.
H. PartyTradingDetails
Details of the trading party.
I. CounterpartyTradingDetails
Details of the trading counterparty.
J. ConfirmationParties
Parties used for acting parties that applies either to the whole message or to individual sides.
K. DeliveringSettlementParties
Identifies the chain of delivering settlement parties.
L. ReceivingSettlementParties
Identifies the chain of receiving settlement parties.
M. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 163 February 2025
```

