---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "18.1 MessageDefinition Functionality"]
file_pages: [556, 557]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.024.001.14"]
---

# 18.1 MessageDefinition Functionality

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 556 to 557.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 556

```text
18 sese.024.001.14
SecuritiesSettlementTransactionStatusAdvic
eV14
18.1 MessageDefinition Functionality
Scope
An account servicer sends a SecuritiesSettlementTransactionStatusAdvice to an account owner to
advise the status of a securities settlement transaction instruction previously sent by the account owner
or the status of a settlement transaction existing in the books of the servicer for the account of the
owner. The status may be a processing, pending processing, internal matching, matching and/or
settlement status.
The status advice may be sent as a response to the request of the account owner or not.
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
The SecuritiesSettlementTransactionStatusAdviceV14 MessageDefinition is composed of 8
MessageBuildingBlocks:
A. TransactionIdentification
Provides unambiguous transaction identification information.
B. Linkages
Link to another transaction - provided for information only.
C. ProcessingStatus
Provides details on the processing status of the transaction.
D. InferredMatchingStatus
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 556 March 2026
```

## File page 557

```text
Provides the matching status of an instruction as per the account servicer based on an allegement.
At this time no matching took place on the market (at the Central Securities Depository (CSD)/
International Central Securities Depository (ICSD)).
E. MatchingStatus
Provides the matching status of the instruction.
F. SettlementStatus
Provides the status of settlement of a transaction.
G. TransactionDetails
Identifies the details of the transaction.
H. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 557 March 2026
```

