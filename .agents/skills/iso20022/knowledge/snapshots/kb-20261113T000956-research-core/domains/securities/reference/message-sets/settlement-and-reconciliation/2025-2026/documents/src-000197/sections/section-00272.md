---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07"]
file_pages: [406]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.020.001.07"]
---

# 11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 406 to 406.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 406

```text
11 semt.020.001.07
SecuritiesMessageCancellationAdviceV07
11.1 MessageDefinition Functionality
Scope
An account servicer sends a SecuritiesMessageCancellationAdvice to an account owner to inform of
the cancellation of a securities message previously sent by an account servicer.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
The previously sent message may be:
- a securities settlement transaction confirmation
- a report (transactions, pending transactions, allegements, accounting and custody securities balance)
- a allegement notification (when sent by mistake or because the counterparty cancelled its instruction)
- a portfolio transfer notification
- an intra-position movement confirmation
- a transaction generation notification
The previously sent message cannot be a status advice message (any). If a status advice should not
have been sent, a new status advice with the correct status should be sent, not a cancellation advice.
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information
using the relevant elements in the Business Application Header.
Outline
Approved by the Securities SEG on 27 January 2026 semt.020.001.07
SecuritiesMessageCancellationAdviceV07
Settlement And Reconciliation - Maintenance 2025 - 2026 406 March 2026
```

