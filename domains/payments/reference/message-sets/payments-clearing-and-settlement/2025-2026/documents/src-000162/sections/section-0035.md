---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer", "Debtor Agent and Creditor Agent are not Correspondents - 2 "]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor Agent are not Correspondents - 2 

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Credit Transfer / Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer / Debtor Agent and Creditor Agent are not Correspondents - 2 .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P236** Debtor Agent and Creditor Agent are not Correspondents - 2 

**P237** The debtor agent and creditor agent are not correspondents in the currency of the transaction. There is a reimbursement agent between them (so-called 3-party cover payment). Negative FIToFIPaymentStatusReport messages are exchanged when rejecting an instruction.

[fig-0017 - original figure evidence](../diagrams/fig-0017.md)

**P239** Under this scenario, the intermediary agent between the debtor agent and creditor agent has to be seen as a reimbursement agent.

**P240** For the sake of simplicity, it is assumed that debtor agent and creditor agent have the same reimbursement agent. In scope: The debtor agent sends the FIToFICustomerCreditTransfer message to the creditor agent.

**P241** The creditor agent optionally confirms the processability of the FIToFICustomerCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P242** The debtor agent sends a FinancialInstitutionCreditTransfer to the reimbursement agent.

**P243** The reimbursement agent sends a negative FIToFIPaymentStatusReport message to inform the debtor agent about the non-processability of the FinancialInstitutionCreditTransfer instruction (for example due to missing/ incorrect information).

**P244** The debtor agent repairs the cover FinancialInstitutionCreditTransfer instruction and re-sends it to the reimbursement agent.

**P245** The reimbursement agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P246** If for whatever reason the FinancialInstitutionCreditTransfer cannot be repaired and processed, the debtor agent will issue an FIToFIPaymentCancellationRequest message for the FIToFICustomerCreditTransfer message to the creditor agent.

