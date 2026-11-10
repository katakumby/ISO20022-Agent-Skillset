---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Election, Entitlement and Reminder Scenarios", "Election and Final Entitlement Cancellation Scenario"]
content_origin: "source-transcription"
---

# Election and Final Entitlement Cancellation Scenario

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Election, Entitlement and Reminder Scenarios / Election and Final Entitlement Cancellation Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P243** Election and Final Entitlement Cancellation Scenario

**P244** This scenario illustrates a classical sequence of corporate action messages for the election phase of a corporate action event following the announcement phase when an instruction may be cancelled by the account owner Once the announcement phase is completed, the account owner may send a CorporateActionInstruction to the account servicer to instruct on one of the proposed options and for a part or all of its eligible balance.

**P245** Once the instruction has been processed by the account servicer, the account servicer sends a CorporateActionInstructionStatusAdvice to the account owner to report the status of the instruction processing. If the instruction is accepted, the account servicer may then also send a CorporateActionMovementPreliminaryAdvice containing the final entitlements and movements to the account owner.

[fig-0025 - original figure evidence](../diagrams/fig-0025.md)

**P247** If the cancellation of the instruction is permitted for the corporate action event and the account owner wants to cancel its instruction, the account owner sends a CorporateActionInstructionCancellationRequest to the account servicer and it may indicate in the message whether a new instruction will be sent later on to instruct on the proposed options.

**P248** Once the instruction cancellation has been processed by the account servicer, the account servicer sends a CorporateActionInstructionCancellationRequestStatusAdvice to the account owner to report the status of the instruction cancellation processing.

**P249** If no other instruction is sent by the account owner before the instruction deadline set by the account servicer, and there is no standing instruction defined by the account owner, the account servicer sends a CorporateActionInstructionStatusAdvice to the account owner indicating that the default action defined for the event was taken into account for the election process.

**P250** The account servicer may then also send a CorporateActionMovementPreliminaryAdvice containing the final entitlements and movements to the account owner.

