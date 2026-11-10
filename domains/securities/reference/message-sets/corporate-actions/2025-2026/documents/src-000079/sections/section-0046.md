---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Election, Entitlement and Reminder Scenarios", "Election and Final Entitlement Replacement"]
content_origin: "source-transcription"
---

# Election and Final Entitlement Replacement

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Election, Entitlement and Reminder Scenarios / Election and Final Entitlement Replacement.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P251** Election and Final Entitlement Replacement

**P252** This scenario illustrates a classical sequence of corporate action messages for the election phase of a corporate action event following the announcement phase when the account owner instructs first partially and later on sends a second instruction to instruct the remaining part of the eligible balance.

**P253** Once the announcement phase is completed, the account owner may send a CorporateActionInstruction to the account servicer to instruct on one of the proposed options and for a part or all of its eligible balance.

**P254** Once the instruction has been processed by the account servicer, the account servicer sends a CorporateActionInstructionStatusAdvice to the account owner to report the status of the instruction processing. If the instruction is accepted, the account servicer may then also send a CorporateActionMovementPreliminaryAdvice containing the final entitlements and movements to the account owner.

[fig-0026 - original figure evidence](../diagrams/fig-0026.md)

**P256** If the account owner then sends a second CorporateActionInstruction to the account servicer to instruct the remaining part of its eligible balance, and the instruction is accepted too, the account servicer sends a CorporateActionInstructionStatusAdvice to the account owner with a status "accepted". The account servicer then should also send a replacement CorporateActionMovementPreliminaryAdvice containing the updated final entitlement and movements to the account owner.

