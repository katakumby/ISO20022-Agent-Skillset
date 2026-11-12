---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11"]
file_pages: [951, 952]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.034.001.11"]
---

# 28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 951 to 952.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 951

```text
28 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
28.1 MessageDefinition Functionality
Scope
An securities financing transaction account servicer sends a SecuritiesFinancingStatusAdvice to an
account owner to advise the status of a securities financing transaction previously instructed by the
account owner.
The status advice may be sent as a response to the request of the account owner or not.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure managing securities
financing transactions on behalf of their participants
- an agent (sub-custodian) managing securities financing transactions on behalf of their global
custodian customer, or
- a custodian managing securities financing transactions on behalf of an investment management
institution or a broker/dealer.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesFinancingStatusAdviceV11 MessageDefinition is composed of 8 MessageBuildingBlocks:
A. TransactionIdentification
Provides unambiguous transaction identification information.
B. ProcessingStatus
Processing status of the transaction.
C. MatchingStatus
Provides the matching status of the instruction.
D. InferredMatchingStatus
Provides the matching status of an instruction as per the account servicer based on an allegement.
At this time no matching took place on the market (at the Central Securities Depository (CSD)/
International Central Securities Depository (ICSD)).
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 951 March 2026
```

## File page 952

```text
E. SettlementStatus
Provides the status of settlement of a transaction.
F. RepoCallRequestStatus
Provides the status of the repurchase agreement call request.
G. TransactionDetails
Identifies the details of the transaction.
H. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 952 March 2026
```

