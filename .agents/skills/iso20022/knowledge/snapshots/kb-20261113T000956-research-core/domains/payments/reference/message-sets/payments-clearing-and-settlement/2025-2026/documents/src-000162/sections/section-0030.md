---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "FIToFICustomerCreditTransfer", "Debtor Agent and Creditor Agent are not Correspondents - 1 "]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor Agent are not Correspondents - 1 

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Credit Transfer / FIToFICustomerCreditTransfer / Debtor Agent and Creditor Agent are not Correspondents - 1 .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P186** Debtor Agent and Creditor Agent are not Correspondents - 1 

**P187** There is an intermediary agent between the debtor agent and creditor agent (the so-called 3-party serial payment). 

**P188** 0

[fig-0013 - original figure evidence](../diagrams/fig-0013.md)

**P189** The scenario also covers the payment clearing system case where the agent between the debtor agent and the creditor agent is a clearing and/or settlement agent.

**P190** For sake of simplicity, the scenario is limited to one intermediary agent between the debtor agent and the creditor agent.

**P191** The debtor agent sends the FIToFICustomerCreditTransfer message to the Intermediary agent.

**P192** The Intermediary agent optionally confirms the processability of the FIToFICustomerCreditTransfer by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P193** The intermediary agent forwards the FIToFICustomerCreditTransfer message to the creditor agent.

**P194** The creditor agent optionally confirms the processability of the FIToFICustomerCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the intermediary agent.

**P195** Out of Scope

**P196** The intermediary agent may send a status update to the debtor agent.

**P197** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

