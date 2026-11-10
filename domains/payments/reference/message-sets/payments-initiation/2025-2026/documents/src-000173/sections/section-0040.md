---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit", "Confirmation of Processability of CustomerDirectDebitInitiation"]
content_origin: "source-transcription"
---

# Confirmation of Processability of CustomerDirectDebitInitiation

Source: [src-000173](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Positive Customer and FIToFIPaymentStatusReport with Direct Debit / Confirmation of Processability of CustomerDirectDebitInitiation.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P266** Confirmation of Processability of CustomerDirectDebitInitiation

**P267** This scenario shows the use of the CustomerPaymentStatusReport message and FIToFIPaymentStatusReport message to confirm the processability of a CustomerDirectDebitInitiation instruction, followed by an FIToFICustomerDirectDebit message (only the messages that are part of the scope of the direct debit are illustrated in the diagram):

[fig-0023 - original figure evidence](../diagrams/fig-0023.md)

**P269** The positive CustomerPaymentStatusReport and FIToFIPaymentStateReport messages are optional. 

**P270** To provide added value to its creditor, a bank may send a CustomerPaymentStatusReport message with an updated status to inform the creditor about the status of the transaction. The status updates may be provided throughout the life-cycle of the transaction.

**P271** A ‘mixed’ CustomerPaymentStatusReport or FIToFIPaymentStatusReport message may be exchanged, that is, the status is ‘partially accepted’ at group level, indicating that the group contains a mix of accepted, pending or rejected transactions. 

**P272** The creditor sends the CustomerDirectDebitInitiation message to its Agent (the creditor agent).

**P273** The creditor agent confirms the processability of the CustomerDirectDebitInitiation instruction by sending a positive CustomerPaymentStatusReport message to the creditor.

**P274** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

**P275** The clearing and settlement agent confirms the processability of the FIToFICustomerDirectDebit instruction by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P276** The clearing and settlement agent sends an FIToFICustomerDirectDebit message, optionally with the Mandate Related Information (MRI) to the debtor agent immediately for information purposes only.

**P277** The debtor agent sends a positive FIToFIPaymentStatusReport message to the clearing and settlement agent. This positive status message may subsequently be forwarded to the creditor agent.

