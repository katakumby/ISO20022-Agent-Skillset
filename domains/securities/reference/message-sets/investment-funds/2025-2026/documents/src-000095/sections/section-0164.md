---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Direct – Single Leg"]
content_origin: "source-transcription"
---

# Two Account Owners – Direct – Single Leg

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Individual Asset Transfer / Two Account Owners – Direct – Single Leg.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P822** Two Account Owners – Direct – Single Leg

**P823** Instructing party 1 sends a TransferOutInstruction message to the executing party. 

**P824** The message requests the executing party to withdraw a quantity of financial instrument from the instructing party's account and deliver the financial instrument to instructing party 2, which also has its account at the executing party. 

**P825** The Service Level Agreement (SLA) in place between the executing party and instructing party 2, specifies that the executing party does not need to receive a corresponding TransferInInstruction message from instructing party 2 in order to act upon the TransferOutInstruction message. 

**P826** The executing party sends a TransferOutConfirmation message to instructing party 1 to confirm the delivery and a TransferInConfirmation message to instructing party 2, to confirm the receipt of the financial instrument.

[fig-0116 - original figure evidence](../diagrams/fig-0116.md)

