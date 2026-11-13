---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Account Management", "Account Modification", "Rejection - Intermediary"]
content_origin: "source-transcription"
---

# Rejection - Intermediary

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Account Management / Account Modification / Rejection - Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P274** Rejection - Intermediary

**P275** If an AccountModificationInstruction message is not compliant with an agreed SLA, and the scenario involves an intermediary, then the AccountManagementStatusReport message (with a rejected status and reason code) is forwarded by the intermediary to the account owner.

[fig-0028 - original figure evidence](../diagrams/fig-0028.md)

**P277** If there is no SLA between the account owner and servicer, or the linked reference is not recognised, a SecuritiesMessageRejection message is forwarded by the intermediary to the account owner.

[fig-0029 - original figure evidence](../diagrams/fig-0029.md)

