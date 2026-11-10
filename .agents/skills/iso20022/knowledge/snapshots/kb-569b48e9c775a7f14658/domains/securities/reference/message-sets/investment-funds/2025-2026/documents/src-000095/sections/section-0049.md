---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Account Management", "Account Modification", "Intermediary"]
content_origin: "source-transcription"
---

# Intermediary

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Account Management / Account Modification / Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P266** Intermediary

**P267** In the scenario involving an intermediary, the account owner sends an AccountModificationInstruction message to an intermediary. The intermediary either forwards the message to another intermediary, or to the account servicer. The account servicer sends an AccountDetailsConfirmation message to the intermediary from which the AccountModificationInstruction message was received. This intermediary then forwards the AccountDetailsConfirmation message to the previous intermediary in the chain, or to the account owner.

[fig-0025 - original figure evidence](../diagrams/fig-0025.md)

