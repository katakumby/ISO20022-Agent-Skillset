---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Trade Leg Notification BusinessTransaction"]
content_origin: "source-transcription"
---

# Trade Leg Notification BusinessTransaction

Source: [src-000052](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Trade Leg Notification BusinessTransaction.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P217** Trade Leg Notification BusinessTransaction

**P218** The TradeLegNotification message is sent by the central counterparty (CCP) to a clearing member to report the trade that has been executed by the trading platform. Through novation the original contract between the buyer and seller is extinguished and replaced by two new contracts, one between the CCP and the buyer and one between the CCP and the seller. The CCP reports both sides of the trade from the clearing member perspective. 

**P219** At the end of the day (or during the day depending on each CCP’s internal process), the CCP reports a summary of all trades that occurred for a specific period in that day, that is, the CCP sends the TradeLegStatement message to the clearing member.

[fig-0012 - original figure evidence](../diagrams/fig-0012.md)

