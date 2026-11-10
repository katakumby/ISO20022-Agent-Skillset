---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Confirmation and Reversal", "Confirmation"]
content_origin: "source-transcription"
---

# Confirmation

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Confirmation and Reversal / Confirmation.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P265** Confirmation

**P266** This scenario illustrates a classical sequence of corporate action messages for the confirmation phase of a corporate action event following the announcement and election phases.

[fig-0028 - original figure evidence](../diagrams/fig-0028.md)

**P269** Once the announcement phase and the election phase (in the cases of elective corporate action events) are completed, the account servicer may send a CorporateActionMovementPreliminaryAdvice containing the final entitlements and movements to the account owner so as to pre-advise him about the upcoming securities and/or cash movements. The account servicer must also send a CorporateActionConfirmation to the account owner to confirm that the cash and/or securities have been credited and/or debited from/to its account.

