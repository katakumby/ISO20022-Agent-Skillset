---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Cancellation ", "Switch ", "Intermediary"]
content_origin: "source-transcription"
---

# Intermediary

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Confirmation Cancellation  / Switch  / Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P720** Intermediary

**P721** The instructing party sends a SwitchOrder message to the intermediary party. 

**P722** The intermediary party sends the SwitchOrder message to the executing party. 

**P723** The executing party sends the SwitchOrderConfirmation message to the intermediary party. The intermediary party sends the SwitchOrderConfirmation message to the instructing party. 

**P724** As the confirmation needs to be cancelled, a SwitchOrderConfirmationCancellationInstruction message is sent by the executing party to inform the intermediary. In turn, the intermediary party sends a SwitchOrderConfirmationCancellationInstruction message to the instructing party. 

[fig-0102 - original figure evidence](../diagrams/fig-0102.md)

