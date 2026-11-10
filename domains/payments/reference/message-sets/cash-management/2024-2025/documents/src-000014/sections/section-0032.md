---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Liquidity Management"]
content_origin: "source-transcription"
---

# Liquidity Management

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / Liquidity Management.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P170** Liquidity Management

**P171** Transfers are processed only when the balance in the account to be debited is sufficient to pass the liquidity transfer instruction and remain positive. Based on the criteria received within the LiquidityCreditTransfer message, the transaction administrator will execute or reject the requested transfer through the Receipt (camt.025) message.

**P172** In principle, the transaction administrator may send a Receipt message as a reply to the liquidity transfer request. To verify the outcome of the request, the member may submit a request to query on the status of the transaction and / or the account message with the appropriate search criteria.

