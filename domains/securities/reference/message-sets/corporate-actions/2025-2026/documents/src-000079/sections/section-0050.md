---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Confirmation and Reversal", "Reversal"]
content_origin: "source-transcription"
---

# Reversal

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Confirmation and Reversal / Reversal.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P270** Reversal

**P271** This scenario illustrates a classical sequence of corporate action messages for the confirmation and phase of a corporate action event when a reversal occurs.

**P272** Once the announcement phase and the election phase (in the cases of elective corporate action events) are completed and the account servicer has confirmed to the account owner that the movements have been applied on its account, and for some reasons, the movements must be reversed, the account servicer may optionally send a reversal CorporateActionMovementPreliminaryAdvice to the account owner to pre-advise him that the securities and/or cash movements are going to be reversed. The account servicer may also indicate the reason for the reversal.

**P273** The account servicer must also send a CorporateActionMovementReversalAdvice to the account owner to confirm the reversal of the movements have been carried out. The account servicer may also indicate the reason for the reversal into the CorporateActionMovementReversalAdvice.

[fig-0029 - original figure evidence](../diagrams/fig-0029.md)

