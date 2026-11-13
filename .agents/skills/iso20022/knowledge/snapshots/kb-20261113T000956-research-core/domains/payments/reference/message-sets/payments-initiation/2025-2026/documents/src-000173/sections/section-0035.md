---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Creditor Agent "]
content_origin: "source-transcription"
---

# Negative CustomerPaymentStatusReport - Creditor Agent 

Source: [src-000173](../../../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Locator: heading path BusinessTransactions / Negative Customer and FIToFIPaymentStatusReport with Direct Debit / Negative CustomerPaymentStatusReport - Creditor Agent .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P234** Negative CustomerPaymentStatusReport - Creditor Agent 

**P235** A negative CustomerPaymentStatusReport message is initiated by the creditor agent to reject a CustomerDirectDebitInitiation message. (Only the messages that are part of the scope of the direct debit are illustrated in the diagram):

[fig-0020 - original figure evidence](../diagrams/fig-0020.md)

**P237** The creditor sends the CustomerDirectDebitInitiation message to its Agent (the creditor agent).

**P238** The creditor agent sends a negative CustomerPaymentStatusReport message to the creditor to inform him about the non processability of the CustomerDirectDebitInitiation instruction, for instance due to missing information.

