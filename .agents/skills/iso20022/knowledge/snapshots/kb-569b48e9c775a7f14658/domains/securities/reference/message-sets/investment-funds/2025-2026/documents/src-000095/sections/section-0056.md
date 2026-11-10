---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Account Management", "Request for Account Management Status Rejection - Direct"]
content_origin: "source-transcription"
---

# Request for Account Management Status Rejection - Direct

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Account Management / Request for Account Management Status Rejection - Direct.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P302** Request for Account Management Status Rejection - Direct

**P303** If a RequestForAccountManagementStatusReport message is not compliant with an agreed SLA or if the account cannot be uniquely identified by the account servicer, then an AccountManagementStatusReport message with a rejected status and reason code is sent by the account servicer to the account owner. 

[fig-0034 - original figure evidence](../diagrams/fig-0034.md)

**P305** If there is no SLA between the account owner and servicer or the linked reference is not recognised, a SecuritiesMessageRejection message is sent by the account servicer to the account owner.

[fig-0035 - original figure evidence](../diagrams/fig-0035.md)

**P307** For scenarios involving an intermediary, the AccountManagementStatusReport message or the SecuritiesMessageRejection message is forwarded by the intermediary to the account owner.

