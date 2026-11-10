---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Duplex Type Scenarios", "Duplex Type"]
content_origin: "source-transcription"
---

# Duplex Type

Source: [src-000180](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx). Locator: heading path BusinessTransactions / BusinessTransactions - Local Matching Scenarios / Duplex Type Scenarios / Duplex Type.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P214** Duplex Type

**P215** The Underwriter sends a trade confirmation to the CMU. The CMU forwards the confirmation received from the Underwriter to the Transfer Agent. Should the trade detail on the confirmation agree with that of the Transfer Agent, it sends an affirmation message to the CMU. Upon receipt of the affirmation message from the Transfer Agent, the CMU forwards the confirmation received from the Underwriter to the Cash Settlement Agent. Should the trade detail on the confirmation agree with that of the Cash Settlement Agent, it sends an affirmation message to the CMU. The message will bind the parties to the trade details of the confirmation being affirmed. The CMU sends an affirmation status message to the Underwriter and the trade can move into the settlement process.

[fig-0018 - original figure evidence](../diagrams/fig-0018.md)

**P217**   


