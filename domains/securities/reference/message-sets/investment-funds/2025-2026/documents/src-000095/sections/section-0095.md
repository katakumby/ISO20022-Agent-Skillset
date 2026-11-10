---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Instruction Status Reporting", "Switch", "Intermediary"]
content_origin: "source-transcription"
---

# Intermediary

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Instruction Status Reporting / Switch / Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P469** Intermediary

**P470** The instructing party sends a SwitchOrder message to the intermediary party. There may be more than one intermediary party in the transaction chain. 

**P471** The intermediary party sends a SwitchOrder message to the executing party. 

**P472** The intermediary sends an OrderInstructionStatusReport message, with the status SentToNextParty (STNP) or Received (RECE), to the instructing party. 

**P473** As the switch order has been accepted, but not yet executed, the executing party responds to the SwitchOrder by sending a an OrderInstructionStatusReport message, with the status Accepted (PACK), to the intermediary party. In turn, the intermediary party sends an OrderInstructionStatusReport message, with the status Accepted (PACK), to the instructing party.

[fig-0065 - original figure evidence](../diagrams/fig-0065.md)

