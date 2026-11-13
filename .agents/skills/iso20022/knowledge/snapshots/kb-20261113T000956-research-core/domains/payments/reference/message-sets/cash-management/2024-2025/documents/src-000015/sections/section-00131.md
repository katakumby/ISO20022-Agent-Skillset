---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.4 ReturnCriteria <RtrCrit>", "4.4.2.2.2.4.4 PaymentReturnCriteria <PmtRtrCrit>", "4.4.2.2.2.4.4.19 DebtorAgentIndicator <DbtrAgtInd>"]
file_pages: [204]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.4.4.19 DebtorAgentIndicator <DbtrAgtInd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 204 to 204.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 204

```text
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.19  DebtorAgentIndicator <DbtrAgtInd>
Presence: [0..1]
Definition: Indicates whether the debtor agent is requested.
Usage: this is the former FirstAgent.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.20  InstructingReimbursementAgentIndicator <InstgRmbrsmntAgtInd>
Presence: [0..1]
Definition: Indicates whether the instructing reimbursement agent is requested.
Usage: this is the former InstructingAgentCorrespondent.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.21  InstructedReimbursementAgentIndicator <InstdRmbrsmntAgtInd>
Presence: [0..1]
Definition: Indicates whether the instructed reimbursement agent is requested.
Usage: this is the former InstructedAgentCorrespondent.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.22  IntermediaryIndicator <IntrmyInd>
Presence: [0..1]
Definition: Indicates whether the intermediary is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.23  CreditorAgentIndicator <CdtrAgtInd>
Presence: [0..1]
Definition: Indicates whether the creditor agent is requested.
Usage: this is the former FinalAgent.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 204 February 2025
```

