---
template: false
document_kind: "participant"
review_status: "needs-review"
title: "Portfolio transfer client"
domain: "securities"
source_ids: ["src-000196", "src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
participant_id: "participant-settlement-reconciliation-portfolio-transfer-client"
role_kind: "functional participant role"
source_labels: ["Client", "customer"]
aliases: ["Client", "customer"]
domains: ["securities"]
message_ids: []
flow_ids: ["flow-settlement-reconciliation-portfolio-transfer"]
limitations: ["Narrative and activity-table participant remains included although the message sequence shows only two custodians."]
source_locations: [{"source_id": "src-000197", "file_pages": [1094], "heading": "31 sese.037.001.09 PortfolioTransferNotificationV09", "evidence_id": "src-000197-sese.037.001.09-p1094-c001"}, {"source_id": "src-000197", "file_pages": [1094], "heading": "31 sese.037.001.09 PortfolioTransferNotificationV09", "evidence_id": "src-000197-sese.037.001.09-p1094-c002"}, {"source_id": "src-000197", "file_pages": [1094], "heading": "31 sese.037.001.09 PortfolioTransferNotificationV09", "evidence_id": "src-000197-sese.037.001.09-p1094-c004"}]
---



# Portfolio transfer client

## Definition and context

Client informs delivering and receiving custodians of a move of some or all positions, investigates breaks with them, and may advise an updated move of positions.

**Evidence:** src-000196 §5.15 Portfolio Transfer Process table48 rows2,9. Original: [src-000196](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx>).

## Responsibilities and relationships

Responsibilities and message directions are specific to each linked flow. A role in one relationship does not establish the same role in another.

- [portfolio transfer](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/portfolio-transfer.md>)

## Source labels and identifier schemes

Source labels: `Client`, `customer`. The role definition does not mandate a universal identifier scheme. Consult the exact message component for its permitted identification choices.

## Limitations

Narrative and activity-table participant remains included although the message sequence shows only two custodians.

[Message-set participants](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/participants.md>) · [sese.023.001.13 context](<../../../domains/securities/reference/messages/sese.023.001.13/business.md>)


<!-- SOURCE196-DIAGRAM-36-START -->
[Portfolio transfer activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0036.md) — src-000196 direct-body paragraph P312.
<!-- SOURCE196-DIAGRAM-36-END -->

## Exact PortfolioTransferNotification context

Source197 sese.037.001.09 Functionality explicitly describes retail or institutional client portfolio transfer, the account-servicer exchange and the client-provided receiving settlement chain. These are the paired Part1 portfolio-transfer responsibilities; an allegement or split-settlement context is not inferred.
