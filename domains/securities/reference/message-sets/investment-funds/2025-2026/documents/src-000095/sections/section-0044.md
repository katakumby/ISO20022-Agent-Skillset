---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Account Management", "Account Opening", "Intermediary"]
content_origin: "source-transcription"
---

# Intermediary

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Account Management / Account Opening / Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P245** Intermediary

**P246** In a scenario involving an intermediary, the account owner sends an AccountOpeningInstruction message to an intermediary. The intermediary either forwards the message to another intermediary, or to the account servicer. 

**P247** The intermediary may send an AccountManagementStatusReport message, with the status Received (RECE), Accepted (ACCP) or SentToNextParty (STNP), to the account owner, in response to the AccountOpeningInstruction message.

**P248** The account servicer may send an AccountManagementStatusReport message, with the status Received (RECE) or Accepted (ACCP), to the intermediary, in response to the AccountOpeningInstruction message.

**P249** The account servicer sends an AccountDetailsConfirmation message to the intermediary with the confirmation type code AccountOpening (ACCO) to confirm the opening of the account.. This intermediary, in turn, either forwards the AccountDetailsConfirmation message to the previous intermediary in the chain, or to the account owner.

[fig-0019 - original figure evidence](../diagrams/fig-0019.md)

