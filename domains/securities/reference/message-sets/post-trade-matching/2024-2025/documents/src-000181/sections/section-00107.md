---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02"]
file_pages: [140]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.029.001.02"]
---

# 4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 140 to 140.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 140

```text
4 setr.029.001.02
SecuritiesTradeConfirmationCancellationV02
4.1 MessageDefinition Functionality
Scope
Sent by an executing party to an instructing party directly or through Central Matching Utility (CMU) to
cancel the referenced SecuritiesTradeConfirmation message that was previously sent.
The instructing party is typically the investment manager or an intermediary system/vendor
communicating on behalf of the investment manager or of other categories of investors.
The executing party is typically the broker/dealer or an intermediary system/vendor communicating on
behalf of the broker/dealer.
It may also be used to cancel the trade confirmation previously sent from an executing party or an
instructing party to a custodian or an affirming party directly or through CMU.
The ISO 20022 Business Application Header must be used
Usage
Initiator: Both in local and central matching, the Initiator may be either the Executing Party or Instructing
Party.
Respondent: Instructing party, a custodian or an affirming party optionally responds with
SecuritiesTradeConfirmationResponse (accept or reject) message.
Outline
The SecuritiesTradeConfirmationCancellationV02 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. Identification
Information that unambiguously identifies an SecuritiesTradeConfirmationCancellation message as
known by the account owner (or the instructing party acting on its behalf).
B. References
Link to another transaction that must be processed after, before or at the same time.
C. OtherBusinessParties
Chain of parties involved in the settlement of a transaction, including receipts and deliveries, book
transfers, treasury deals, or other activities, resulting in the movement of a security or amount of
money from one account to another.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 13 February 2025 setr.029.001.02
SecuritiesTradeConfirmationCancellationV02
Post Trade Matching - Maintenance 2024 - 2025 140 February 2025
```

