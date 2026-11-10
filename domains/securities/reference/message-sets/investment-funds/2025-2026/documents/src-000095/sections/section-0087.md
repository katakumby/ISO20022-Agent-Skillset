---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Instruction Status Reporting", "Subscription", "Intermediary"]
content_origin: "source-transcription"
---

# Intermediary

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Instruction Status Reporting / Subscription / Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P429** Intermediary

**P430** The instructing party sends a SubscriptionOrder message to the intermediary party. There may be more than one intermediary party in the transaction chain. 

**P431** The intermediary party sends a SubscriptionOrder message to the executing party.

**P432** The intermediary sends an OrderInstructionStatusReport message, with the status SentToNextParty (STNP) or Received (RECE), to the instructing party. 

**P433** As the intermediary party and the executing party have a service level agreement (SLA) that states the executing party will always send a status, the executing party responds to the SubscriptionOrder message by sending an OrderInstructionStatusReport message, with the status Accepted (PACK), to the intermediary.

**P434** Likewise, the intermediary party sends a OrderInstructionStatusReport message, with the status Accepted (PACK), to the instructing party.

[fig-0059 - original figure evidence](../diagrams/fig-0059.md)

