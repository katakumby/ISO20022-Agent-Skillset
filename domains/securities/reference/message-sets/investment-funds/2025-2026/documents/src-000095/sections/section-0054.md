---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Account Management", "Status of Account Opening - Intermediary"]
content_origin: "source-transcription"
---

# Status of Account Opening - Intermediary

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Account Management / Status of Account Opening - Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P290** Status of Account Opening - Intermediary

**P291** In a scenario involving an intermediary, the account owner sends a RequestForAccountManagementStatusReport message to an intermediary to request the processing status of a previously sent AccountOpeningInstruction message for which an AccountDetailsConfirmation message has not yet been received. The intermediary either forwards the message to another intermediary, or to the account servicer.

**P292** The intermediary may also send an AccountManagementStatusReport message with the status SentToNextParty (STNP) to the account owner. 

**P293** After the receipt of the RequestForAccountManagementStatusReport message, the account servicer sends an AccountManagementStatusReport message, with the appropriate status, to the intermediary. This intermediary in turn forwards the AccountManagementStatusReport message to the previous intermediary in the chain, or to the account owner.

**P294** Once the AccountOpeningInstruction message has been successfully processed, the account servicer sends the AccountDetailsConfirmation message to the intermediary. The intermediary either forwards the message to another intermediary in the chain, or to the account owner.

[fig-0032 - original figure evidence](../diagrams/fig-0032.md)

