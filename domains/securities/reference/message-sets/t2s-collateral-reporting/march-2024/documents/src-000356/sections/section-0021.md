---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000356"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessTransactions"]
content_origin: "source-transcription"
---

# BusinessTransactions

Source: [src-000356](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralReporting_2023_2024_v2.docx`. Locator: heading path BusinessTransactions.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P144** BusinessTransactions

**P145** This section describes the message flows based on the activity diagrams documented above. It shows the typical exchanges of information in the context of a BusinessTransaction.

[fig-0009 - original figure evidence](../diagrams/fig-0009.md)

**P148** As outlined above, an NCB, CSD or directly connected Central System party sends a Collateral Value Query to the Central System (e.g. T2S platform) to request information on the current available value of securities for auto collateralisation. The value will represent the amount of intraday credit that a party may receive through collateralising of their securities. Error Response or Collateral Value Response are both exclusive.

**P150** An overview of the communication flow and sequence diagram can be found below:

[fig-0010 - original figure evidence](../diagrams/fig-0010.md)

