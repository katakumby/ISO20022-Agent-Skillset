---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "FIToFICustomerCreditTransfer", "Debtor Agent and Creditor Agent are Correspondents "]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor Agent are Correspondents 

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Credit Transfer / FIToFICustomerCreditTransfer / Debtor Agent and Creditor Agent are Correspondents .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P177** Debtor Agent and Creditor Agent are Correspondents 

**P178** The debtor agent and creditor agent are correspondents in the currency of the transaction.

[fig-0012 - original figure evidence](../diagrams/fig-0012.md)

**P180** The scenario caters for the debtor agent servicing an account for the creditor agent and vice versa. It also covers the case where debtor agent and creditor agent are linked directly across a payment clearing and settlement system.

**P181** The debtor agent sends the FIToFICustomerCreditTransfer message to the creditor agent.

**P182** The creditor agent optionally confirms the processability of the FIToFICustomerCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P183** Out of Scope 

**P184** The 'On Us' scenario where the debtor agent is also the creditor agent

**P185** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

