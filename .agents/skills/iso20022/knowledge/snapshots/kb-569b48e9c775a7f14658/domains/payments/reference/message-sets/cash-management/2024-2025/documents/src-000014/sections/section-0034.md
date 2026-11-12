---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Liquidity Management", "Liquidity Debit Transfer"]
content_origin: "source-transcription"
---

# Liquidity Debit Transfer

Source: [src-000014](../../../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Locator: heading path BusinessTransactions / Liquidity Management / Liquidity Debit Transfer.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P177** Liquidity Debit Transfer

**P178** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with the ability to manage their liquidity.

**P179** At any time during the operating hours of the system, a member can request the transaction administrator to execute the transfer of funds between two accounts that the transaction administrator maintains for the member. For this, the member can send a LiquidityDebitTransfer message to the transaction administrator. In this message, the member will identify the accounts involved in the transfer. The transaction administrator will process the request and reply with a Receipt message that may contain the status of the request.

[fig-0004 - original figure evidence](../diagrams/fig-0004.md)

