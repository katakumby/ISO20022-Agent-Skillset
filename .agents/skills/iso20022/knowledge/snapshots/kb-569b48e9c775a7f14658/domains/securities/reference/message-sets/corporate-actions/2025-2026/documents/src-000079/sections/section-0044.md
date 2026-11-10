---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Election, Entitlement and Reminder Scenarios", "Election and Final Entitlement "]
content_origin: "source-transcription"
---

# Election and Final Entitlement 

Source: [src-000079](../../../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Locator: heading path BusinessTransactions / Election, Entitlement and Reminder Scenarios / Election and Final Entitlement .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P238** Election and Final Entitlement 

**P239** This scenario illustrates a classical sequence of corporate action messages for the election phase of a corporate action event following the announcement phase when a single instruction is sent by the account owner.

**P240** Once the announcement phase is completed, the account owner may send a CorporateActionInstruction to the account servicer to instruct on one of the proposed options and for a part or all of its eligible balance.

**P241** Once the instruction has been processed by the account servicer, the account servicer sends a CorporateActionInstructionStatusAdvice to the account owner to report the status of the instruction processing. If the instruction is accepted, the account servicer may then also send a CorporateActionMovementPreliminaryAdvice containing the final entitlements and movements to the account owner.

[fig-0024 - original figure evidence](../diagrams/fig-0024.md)

