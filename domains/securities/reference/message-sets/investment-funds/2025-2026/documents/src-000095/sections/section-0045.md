---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Account Management", "Account Opening", "Rejection - Direct"]
content_origin: "source-transcription"
---

# Rejection - Direct

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Account Management / Account Opening / Rejection - Direct.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P251** Rejection - Direct

**P252** If an AccountOpeningInstruction message is not compliant with an agreed SLA, then an AccountManagementStatusReport message is sent by the account servicer to the account owner with a rejected status and reason code. 

[fig-0020 - original figure evidence](../diagrams/fig-0020.md)

**P254** If there is no SLA between the account owner and servicer, or the linked reference is not recognised, a SecuritiesMessageRejection message is sent by the account servicer to the account owner.

[fig-0021 - original figure evidence](../diagrams/fig-0021.md)

