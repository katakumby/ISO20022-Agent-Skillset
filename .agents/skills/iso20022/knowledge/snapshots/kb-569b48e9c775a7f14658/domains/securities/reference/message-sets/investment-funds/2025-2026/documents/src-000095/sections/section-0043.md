---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Account Management", "Account Opening", "Direct"]
content_origin: "source-transcription"
---

# Direct

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Account Management / Account Opening / Direct.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P240** Direct

**P241** The account owner sends an AccountOpeningInstruction message to the account servicer to request the opening of a new or supplementary account. 

**P242** The account servicer may send an AccountManagementStatusReport message, with the status Received (RECE) or Accepted (ACCP), in response to the AccountOpeningInstruction message.

**P243** The account servicer sends an AccountDetailsConfirmation message to the account owner with the confirmation type code AccountOpening (ACCO) to confirm the opening of the account.

[fig-0018 - original figure evidence](../diagrams/fig-0018.md)

