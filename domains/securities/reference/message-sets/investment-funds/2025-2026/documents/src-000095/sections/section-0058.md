---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Account Management", "Account Closure and Reactivation - Direct"]
content_origin: "source-transcription"
---

# Account Closure and Reactivation - Direct

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Account Management / Account Closure and Reactivation - Direct.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P311** Account Closure and Reactivation - Direct

**P312** The account owner sends an AccountModificationInstruction message to the account servicer to instruct the closure of its account (AccountStatusUpdateInstruction/UpdateInstruction/Code is CLOS). The account servicer may respond with an AccountManagementStatusReport message with the status Received (RECE). The account owner subsequently sends an AccountModificationInstruction message to instruct the reactivation of the account (AccountStatusUpdateInstruction/UpdateInstruction/Code is REAC). 

**P313** When the account servicer has actioned the instruction, it sends an AccountDetailsConfirmation message with the confirmation type code AccountModification (ACCM) and confirms the account status is enabled (InvestmentAccount/AccountStatus/Enabled).

[fig-0037 - original figure evidence](../diagrams/fig-0037.md)

