---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Account Management", "Account Opening", "Rejection - Intermediary"]
content_origin: "source-transcription"
---

# Rejection - Intermediary

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Account Management / Account Opening / Rejection - Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P256** Rejection - Intermediary

**P257** If an AccountOpeningInstruction message is not compliant with an agreed SLA, and the scenario involves an intermediary, then the AccountManagementStatusReport message (with a rejected status and reason code) is forwarded by the intermediary to the account owner.

[fig-0022 - original figure evidence](../diagrams/fig-0022.md)

**P259** If there is no SLA between the account owner and servicer, or the linked reference is not recognised, a SecuritiesMessageRejection message is forwarded by the intermediary to the account owner.

[fig-0023 - original figure evidence](../diagrams/fig-0023.md)

