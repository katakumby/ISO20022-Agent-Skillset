---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Account Management", "Status of Account Modification - Intermediary"]
content_origin: "source-transcription"
---

# Status of Account Modification - Intermediary

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Account Management / Status of Account Modification - Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P296** Status of Account Modification - Intermediary

**P297** In a scenario involving an intermediary, the account owner sends a RequestForAccountManagementStatusReport message to an intermediary to request the processing status of a previously sent AccountModificationInstruction message for which an AccountDetailsConfirmation message has not yet been received. The intermediary either forwards the message to another intermediary, or to the account servicer.

**P298** The intermediary may also send an AccountManagementStatusReport message with the status SentToNextParty (STNP) to the account owner. 

**P299** After the receipt of the RequestForAccountManagementStatusReport message, the account servicer sends an AccountManagementStatusReport message, with the appropriate status, to the intermediary. This intermediary in turn forwards the AccountManagementStatusReport message to the previous intermediary in the chain, or to the account owner.

**P300** Once the AccountModificationInstruction message has been successfully processed, the account servicer sends the AccountDetailsConfirmation message to the intermediary. The intermediary either forwards the message to another intermediary in the chain, or to the account owner.

[fig-0033 - original figure evidence](../diagrams/fig-0033.md)

