---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit", "FIToFIPaymentStatusReport to confirm Processability of FIToFICustomerDirectDebit instruction"]
content_origin: "source-transcription"
---

# FIToFIPaymentStatusReport to confirm Processability of FIToFICustomerDirectDebit instruction

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Direct Debit / Positive FI To FI Payment Status Report with Direct Debit / FIToFIPaymentStatusReport to confirm Processability of FIToFICustomerDirectDebit instruction.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P529** FIToFIPaymentStatusReport to confirm Processability of FIToFICustomerDirectDebit instruction

**P530** In this scenario, the FIToFIPaymentStatusReport message is used to confirm the processability of a FIToFICustomerDirectDebit instruction. 

**P531** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

**P532** The clearing and settlement agent confirms the processability of the FIToFICustomerDirectDebit instruction by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P533** The clearing and settlement agent sends an FIToFICustomerDirectDebit message, together with potentially the Mandate Related Information (MRI) to the debtor agent immediately for information purposes only.

**P534** The debtor agent sends a positive FIToFIPaymentStatusReport message to the clearing and settlement agent. This positive status message may subsequently be forwarded to the creditor agent. 

