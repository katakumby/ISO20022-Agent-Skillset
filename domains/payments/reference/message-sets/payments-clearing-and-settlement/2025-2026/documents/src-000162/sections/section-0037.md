---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "PaymentReturn with FIToFICustomerCreditTransfer ", "Debtor Agent and the Creditor Agent are Correspondents "]
content_origin: "source-transcription"
---

# Debtor Agent and the Creditor Agent are Correspondents 

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Credit Transfer / PaymentReturn with FIToFICustomerCreditTransfer  / Debtor Agent and the Creditor Agent are Correspondents .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P249** Debtor Agent and the Creditor Agent are Correspondents 

**P250** A return is exchanged after settlement has taken place.

[fig-0018 - original figure evidence](../diagrams/fig-0018.md)

**P252** The scenario covers the case where the debtor agent services an account for the creditor agent and the case where debtor agent and creditor agent are linked through a payment clearing system.

**P253** Where the creditor agent services an account for the debtor agent, the creditor agent will inform about the non- processability of the instruction by using a negative FIToFIPaymentStatusReport (status Reject) message.

**P254** The debtor agent sends the FIToFICustomerCreditTransfer message to the creditor agent.

**P255** The creditor agent sends a PaymentReturn message to inform the debtor agent about the non-processability of the FIToFICustomerCreditTransfer instruction including the return reason (for example due to missing/incorrect information/closed account...).

**P256** The debtor agent optionally confirms the processability of the PaymentReturn message by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P257** Whenever possible, the debtor agent might try to repair and re-submit the instruction. Depending on what has been agreed it may inform the debtor about the repair with an updated FIToFIPaymentStatusReport message.

**P258** Out of Scope

**P259** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

