---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Amendment ", "Switch ", "Intermediary"]
content_origin: "source-transcription"
---

# Intermediary

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Confirmation Amendment  / Switch  / Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P664** Intermediary

**P665** The instructing party sends a SwitchOrder message to the intermediary party. In turn, the intermediary party sends the SwitchOrder message to the executing party. 

**P666** The executing party sends the SwitchOrderConfirmation message to the intermediary party. The intermediary party sends the SwitchOrderConfirmation message to the instructing party. 

**P667** As an amendment has to be made to the SwitchOrderConfirmation message details, another SwitchOrderConfirmation message is sent by the executing party to inform the intermediary about the amended details, with the AmendmentIndicator set to 'true' or '1'. 

**P668** In turn, the intermediary party sends a SwitchOrderConfirmation message to the instructing party, with the AmendmentIndicator set to 'true' or '1'. 

[fig-0094 - original figure evidence](../diagrams/fig-0094.md)

