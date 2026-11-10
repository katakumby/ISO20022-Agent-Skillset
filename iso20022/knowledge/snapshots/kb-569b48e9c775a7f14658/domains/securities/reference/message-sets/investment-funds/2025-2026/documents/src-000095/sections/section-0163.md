---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Direct – Double Leg"]
content_origin: "source-transcription"
---

# Two Account Owners – Direct – Double Leg

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Individual Asset Transfer / Two Account Owners – Direct – Double Leg.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P816** Two Account Owners – Direct – Double Leg

**P817** Instructing party 1 sends a TransferOutInstruction message to the executing party.

**P818** The message requests the executing party to withdraw a quantity of financial instrument from the instructing party's account and deliver the financial instrument to instructing party 2, which also has its account at the executing party.

**P819** At the same time, instructing party 2 sends a TransferInInstruction message to the executing party, requesting the executing party to receive the financial instrument from instructing party 1. 

**P820** The executing party sends a TransferOutConfirmation message to instructing party 1 to confirm the delivery and a TransferInConfirmation message to instructing party 2, to confirm the receipt of the financial instrument.

[fig-0115 - original figure evidence](../diagrams/fig-0115.md)

