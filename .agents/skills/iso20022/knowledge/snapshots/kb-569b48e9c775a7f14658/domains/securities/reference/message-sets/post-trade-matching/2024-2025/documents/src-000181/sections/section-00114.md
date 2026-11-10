---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03"]
file_pages: [148]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.030.001.03"]
---

# 5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 148 to 148.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 148

```text
5 setr.030.001.03
SecuritiesTradeConfirmationResponseV03
5.1 MessageDefinition Functionality
Scope
Sent by an instructing party, a custodian or an affirming party to an executing party (local matching) or
to Central Matching Utility (CMU) to affirm (accept) or disaffirm (reject) (central matching) the
SecuritiesTradeConfirmation message. If accepting the SecuritiesTradeConfirmation message, then the
trade is ready for settlement processing. If rejecting the SecuritiesTradeConfirmation message, then the
trade is not ready for settlement.
The executing party is typically the broker/dealer or an intermediary system/vendor communicating on
behalf of the broker/dealer.
The instructing party is typically the investment manager or an intermediary system/vendor
communicating on behalf of the investment manager or of other categories of investors.
The custodian or an affirming party is typically the custodian, trustee, financial institution, intermediary
system/vendor communicating on behalf of them, or their agent.
The ISO 20022 Business Application Header must be used
Usage
Initiator: Both in local and central matching, the Initiator may be the Instructing Party, Custodian or
Affirming party.
Respondent: Executing party does not need to respond if an affirmation. Executing party may respond
with modification or cancellation of the rejected SecuritiesTradeConfirmation message.
Outline
The SecuritiesTradeConfirmationResponseV03 MessageDefinition is composed of 6
MessageBuildingBlocks:
A. Identification
Information that unambiguously identifies an SecuritiesTradeConfirmationResponse message as
known by the account owner (or the instructing party acting on its behalf).
B. References
Link to another transaction that must be processed after, before or at the same time.
C. Status
Provides details on the processing status of the trade.
D. ClearingDetails
Provides clearing member information.
E. ConfirmationParties
Parties involved in the confirmation of the details of a trade.
Approved by the Securities SEG on 13 February 2025 setr.030.001.03
SecuritiesTradeConfirmationResponseV03
Post Trade Matching - Maintenance 2024 - 2025 148 February 2025
```

