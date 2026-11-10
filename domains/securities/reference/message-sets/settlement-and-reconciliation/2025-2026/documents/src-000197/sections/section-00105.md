---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 semt.013.001.07 IntraPositionMovementInstructionV07", "5.1 MessageDefinition Functionality"]
file_pages: [150]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.014.001.09"]
---

# 5.1 MessageDefinition Functionality

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 150 to 150.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 150

```text
5 semt.014.001.09
IntraPositionMovementStatusAdviceV09
5.1 MessageDefinition Functionality
Scope
An account servicer sends a IntraPositionMovementStatusAdvice to an account owner to advise the
status of an intra-position movement instruction previously sent by the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The IntraPositionMovementStatusAdviceV09 MessageDefinition is composed of 6
MessageBuildingBlocks:
A. TransactionIdentification
Unambiguous identification of a transaction as per the account owner (or the instructing party
managing the account).
B. Linkage
Link to another transaction that triggered the intra-position movement.
C. ProcessingStatus
Provides details on the processing status of the transaction.
D. SettlementStatus
Provides the status of settlement of a transaction.
E. TransactionDetails
Identifies the details of the transaction.
F. SupplementaryData
Approved by the Securities SEG on 27 January 2026 semt.014.001.09
IntraPositionMovementStatusAdviceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 150 March 2026
```

