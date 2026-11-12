---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Account Management", "Status of Account Opening - Direct"]
content_origin: "source-transcription"
---

# Status of Account Opening - Direct

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Account Management / Status of Account Opening - Direct.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P279** Status of Account Opening - Direct

**P280** The account owner sends a RequestForAccountManagementStatusReport message to the account servicer to request the processing status of a previously sent AccountOpeningInstruction message for which an AccountDetailsConfirmation message has not yet been received.

**P281** The account servicer sends an AccountManagementStatusReport message to the account owner with the appropriate status code. More than one AccountManagementStatusReport message may sent to reflect the status as the status changes. 

**P282** Once the AccountOpeningInstruction message has been successfully processed, the account servicer sends the AccountDetailsConfirmation message to the account owner.

**P283** 	

[fig-0030 - original figure evidence](../diagrams/fig-0030.md)

