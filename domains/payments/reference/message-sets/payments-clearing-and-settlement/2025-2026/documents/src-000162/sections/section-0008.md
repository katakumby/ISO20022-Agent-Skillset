---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Scope and Functionality", "Background"]
content_origin: "source-transcription"
---

# Background

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path Scope and Functionality / Background.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P81** Background

**P82** This Message Definition Report covers a set of eight MessageDefinitions developed by SWIFT and approved by the ISO 20022 Payments Standards Evaluation Group (SEG) in January 2026.

**P83** These messages are specifically designed to support the clearing and settlement of credit transfers, direct debits and reversals directly between banks or across an automated clearing house (ACH) and real time gross settlement systems (RTGS). 

**P84** In 2015, the FinancialInstitutionDirectDebit message was added as a result of reverse engineering the existing SWIFT FIN MT 204 Financial Markets Direct Debit Message in order to bridge the gap detected at the occasion of the migration of several market infrastructures worldwide from their SWIFT FIN portfolio of messages (MT 103, MT 103+, MT 202, MT 204, MT 900, MT 910) to ISO 20022. 

**P85** In 2016, the FIToFIPaymentStatusRequest message was added to accommodate the need, initially identified for real time payments, to launch an investigation on a previously sent payment instruction, where an (expected) FIToFIPaymentStatusReport message is missing. 

