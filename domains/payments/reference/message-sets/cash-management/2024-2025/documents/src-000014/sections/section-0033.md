---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Liquidity Management", "Liquidity Credit Transfer"]
content_origin: "source-transcription"
---

# Liquidity Credit Transfer

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / Liquidity Management / Liquidity Credit Transfer.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P173** Liquidity Credit Transfer

**P174** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with the ability to manage their liquidity.

**P175** At any time during the operating hours of the system, a member can request the transaction administrator to execute the transfer of funds between two accounts that the transaction administrator maintains for the member. For this, the member can send a LiquidityCreditTransfer message to the transaction administrator. In this message, the member will identify the accounts involved in the transfer. The transaction administrator process the request and reply with a Receipt message that may contain the status of the request.

[fig-0003 - original figure evidence](../diagrams/fig-0003.md)

