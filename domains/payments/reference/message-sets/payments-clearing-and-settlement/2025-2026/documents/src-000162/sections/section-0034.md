---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer", "Debtor Agent and Creditor Agent are not Correspondents - 1"]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor Agent are not Correspondents - 1

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Credit Transfer / Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer / Debtor Agent and Creditor Agent are not Correspondents - 1.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P221** Debtor Agent and Creditor Agent are not Correspondents - 1

**P222** There is an intermediary agent between the debtor agent and creditor agent (so-called 3-party Serial payment). Negative FIToFIPaymentStatusReport messages are exchanged when rejecting an instruction.

[fig-0016 - original figure evidence](../diagrams/fig-0016.md)

**P224** The scenario covers the case where the creditor agent (or branch/head office of creditor agent) services an account for the intermediary agent. In the cases where the intermediary agent services an account for the creditor agent or they are linked through a payment clearing system, the creditor agent will inform about the non-processability by using a PaymentReturn message.

**P225** The debtor agent sends the FIToFICustomerCreditTransfer message to the intermediary agent.

**P226** The intermediary agent may optionally confirm the processability of the FIToFICustomerCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P227** The intermediary agent forwards the FIToFICustomerCreditTransfer message to the creditor agent.

**P228** The creditor agent sends a negative FIToFIPaymentStatusReport message to inform the intermediary agent about the non-processability of the FIToFICustomerCreditTransfer instruction (for example due to missing/incorrect information).

**P229** The intermediary agent might try to repair and re-submit the instruction when possible and inform the debtor agent with an updated FIToFIPaymentStatusReport accordingly.

**P230** Case A

**P231** The intermediary agent has not yet booked the instruction on the account of the debtor agent.

**P232** The intermediary agent forwards the negative FIToFIPaymentStatusReport message to inform the debtor agent about the non-processability of the FIToFICustomerCreditTransfer instruction.

**P233** Case B 

**P234** The intermediary agent has booked the instruction on the account of the debtor agent.

**P235** The intermediary agent sends a PaymentReturn message including the Return reason to the debtor agent to inform the debtor agent about the non-processability of the FIToFICustomerCreditTransfer instruction.

