---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Default Fund Contribution BusinessTransaction"]
content_origin: "source-transcription"
---

# Default Fund Contribution BusinessTransaction

Source: [src-000052](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Default Fund Contribution BusinessTransaction.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P240** Default Fund Contribution BusinessTransaction

**P241** Central counterparties require participants to post assets in a clearing fund that can be used in the event of a default by a participant to compensate non-defaulting participants for losses they suffer due to this default. Contributions are linked to the riskiness of a participant's activity as measured by margin posted, by size of position or sometimes by stress-testing results. 

**P242** The DefaultFundContributionReport message is sent by a central counterparty (CCP) to the clearing member to report on the calculation of the default fund contribution and the potential net excess or deficit.

**P243** Optional flow:

**P244** Depending on the CCP’s internal rules, the CCP may send a MarginCallRequest message for the deficit amount required to cover the default fund.

**P245** Note that this flow is not part of the scope of this project and will not be described in this document. It is only shown for the sake of completeness. For more information please refer to the Collateral Management project.

[fig-0016 - original figure evidence](../diagrams/fig-0016.md)

