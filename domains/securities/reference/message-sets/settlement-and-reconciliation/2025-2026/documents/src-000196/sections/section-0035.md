---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Description of BusinessActivities", "Securities Financing Instruction", "Modification Process "]
content_origin: "source-transcription"
---

# Modification Process 

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Description of BusinessActivities / Securities Financing Instruction / Modification Process .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P214** Modification Process 

**P215** Several types of modification of securities financing transaction may occur. For activity diagram illustration purposes, the types of modification are regarded as two categories:

**P216** Changes that do not impact the securities position

**P217** Changes impacting the securities position

**P218** For all changes, it is assumed that the opening leg has been settled and that it is still possible to modify the closing leg details.

**P219** Important Notes

**P220** If the opening leg is pending and the change impacts the closing leg, SecuritiesFinancingModificationInstruction is sent.

**P221** If the opening leg is pending and the change impacts the opening leg, a cancel and a new message will be sent out.

**P222** If the opening leg is settled but not the closing and a change impacts the closing leg, SecuritiesFinancingModificationInstruction will be sent 

**P223** If the opening leg is settled and a change is sent for the opening leg. Nothing can be done except request an earlier termination of the closing leg.

**P224** These above will be clearly stated in the Securities Financing High Level model.

