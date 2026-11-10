---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Amendment "]
content_origin: "source-transcription"
---

# Order Confirmation Amendment 

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Confirmation Amendment .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P612** Order Confirmation Amendment 

**P613** This message flow section illustrates the use of the messages for the amendment of an order confirmation in typical message sequencing scenarios.

**P614** More than one message detail can be amended. The order confirmation, when sent as an amendment (AmendmentIndicator set to 'true' or '1'), might follow an order confirmation cancellation instruction message, if, in the order confirmation cancellation instruction message, the AmendmentIndicator is set to 'true' or '1' (see sequence diagrams related to order confirmation cancellation instruction messages).

**P615** The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**P616** The intermediary party is, for example, a distributor.

**P617** There may be one or more intermediaries in the transaction chain

