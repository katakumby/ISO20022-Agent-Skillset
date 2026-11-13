---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09"]
file_pages: [708, 709]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.027.001.09"]
---

# 21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 708 to 709.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 708

```text
21 sese.027.001.09
SecuritiesTransactionCancellationRequestSt
atusAdviceV09
21.1 MessageDefinition Functionality
Scope
An account servicer sends an SecuritiesTransactionCancellationRequestStatusAdvice to an account
owner to advise the status of a securities transaction cancellation request previously sent by the
account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information
using the relevant elements in the Business Application Header.
Outline
The SecuritiesTransactionCancellationRequestStatusAdviceV09 MessageDefinition is composed of 5
MessageBuildingBlocks:
A. CancellationRequestReference
Reference to the unambiguous identification of the cancellation request as per the account owner.
B. TransactionIdentification
Unambiguous identification of the transaction as known by the account servicer.
C. ProcessingStatus
Provides details on the processing status of the request.
D. TransactionDetails
Identifies the details of the transaction.
E. SupplementaryData
Approved by the Securities SEG on 27 January 2026 sese.027.001.09
SecuritiesTransactionCancellationRequestStatusAd
viceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 708 March 2026
```

## File page 709

```text
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.027.001.09
SecuritiesTransactionCancellationRequestStatusAd
viceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 709 March 2026
```

