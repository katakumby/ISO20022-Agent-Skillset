---
template: false
document_kind: "participant"
review_status: "needs-review"
title: "Account servicer"
domain: "securities"
source_ids: ["src-000196", "src-000197", "src-000198"]
source_editions: ["2025-2026", "March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
participant_id: "participant-settlement-reconciliation-account-servicer"
role_kind: "functional account role"
source_labels: ["AccountServicerRole", "another account servicer", "delivering account servicer", "receiving account servicer"]
aliases: ["AccountServicerRole"]
domains: ["securities"]
message_ids: ["sese.023.001.13", "sese.037.001.09"]
flow_ids: ["flow-settlement-reconciliation-instruction-confirmation", "flow-settlement-reconciliation-partial-settlement", "flow-settlement-reconciliation-cancellation-request", "flow-settlement-reconciliation-reversal-advice", "flow-settlement-reconciliation-reporting-push", "flow-settlement-reconciliation-reporting-pull"]
limitations: ["Custodians, CSDs and settlement market infrastructures can service accounts in the relationships described in §17.1; this is not a fixed institution mapping."]
source_locations: [{"source_id": "src-000197", "heading": "31 sese.037.001.09 PortfolioTransferNotificationV09", "file_pages": [1094], "evidence_id": "src-000197-sese.037.001.09-p1094-c001"}, {"source_id": "src-000197", "heading": "31 sese.037.001.09 PortfolioTransferNotificationV09", "file_pages": [1094], "evidence_id": "src-000197-sese.037.001.09-p1094-c003"}, {"source_id": "src-000197", "heading": "31 sese.037.001.09 PortfolioTransferNotificationV09", "file_pages": [1094], "evidence_id": "src-000197-sese.037.001.09-p1094-c004"}, {"source_id": "src-000197", "heading": "31 sese.037.001.09 PortfolioTransferNotificationV09", "file_pages": [1094], "evidence_id": "src-000197-sese.037.001.09-p1094-c005"}]
message_families: ["sese.023", "sese.037"]
---







# Account servicer

## Definition and context

Party that manages the account on behalf of its owner: registration and booking of entries, calculating balances, and providing account information. In this message context it receives the account owner’s settlement instruction.

**Evidence:** src-000198 FullBusinessModel!A108:F108; src-000197 file/printed p491, §17.1 Scope. Original: [src-000198](../../../evidence/omitted/c6a84c22fb63cab3b848bd88.md).

## Responsibilities and relationships

Responsibilities and message directions are specific to each linked flow. A role in one relationship does not establish the same role in another.

- [instruction confirmation](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/instruction-confirmation.md)
- [partial settlement](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/partial-settlement.md)
- [cancellation request](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/cancellation-request.md)
- [reversal advice](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/reversal-advice.md)
- [reporting push](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-push.md)
- [reporting pull](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-pull.md)

## Source labels and identifier schemes

Source labels: `AccountServicerRole`. The role definition does not mandate a universal identifier scheme. Consult the exact message component for its permitted identification choices.

## Limitations

Custodians, CSDs and settlement market infrastructures can service accounts in the relationships described in §17.1; this is not a fixed institution mapping.

[Message-set participants](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/participants.md) · [sese.023.001.13 context](../../../domains/securities/reference/messages/sese.023.001.13/business.md)

## Same-source conceptual record

[AccountServicerRole](../business-components/bc-11b811aa7b53717bee35.md) preserves the complete FullBusinessModel rows cited by this participant record. This link is based on the explicit source component name, not a general equivalence between similarly labelled roles.




<!-- SOURCE196-DIAGRAM-1-START -->
[Settlement communication scope and account relationships](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0001.md) — src-000196 direct-body paragraph P145.
<!-- SOURCE196-DIAGRAM-1-END -->

<!-- SOURCE196-DIAGRAM-2-START -->
[Reporting communication overview](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0002.md) — src-000196 direct-body paragraph P147.
<!-- SOURCE196-DIAGRAM-2-END -->

<!-- SOURCE196-DIAGRAM-3-START -->
[Intra-position communication overview](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0003.md) — src-000196 direct-body paragraph P149.
<!-- SOURCE196-DIAGRAM-3-END -->



<!-- FUNCTIONALITY-ALIASES-src-000197 -->
## Additional literal publication labels

The source assigns delivering and receiving positions to two account-servicer instances in the portfolio-transfer exchange. They reuse the functional account-servicer definition; the source directions and distinct instance labels remain explicit.

| Source label | Source context |
| --- | --- |
| delivering account servicer | src-000197-sese.037.001.09-p1094-c003; src-000197-sese.037.001.09-p1094-c004; src-000197-sese.037.001.09-p1094-c005 |
| receiving account servicer | src-000197-sese.037.001.09-p1094-c003; src-000197-sese.037.001.09-p1094-c005 |


> The exchange of transfer settlement details is the provision, by the delivering account servicer to the receiving account servicer, of the settlement data (such as trade date, settlement date, delivering settlement chain, quantities) of the individual transfers that will take place during a full or partial portfolio transfer.

src-000197, file pages1094; 31 sese.037.001.09 PortfolioTransferNotificationV09.

> This delivering account servicer message may also include, for validation, the receiving settlement chain as provided by the client.

src-000197, file pages1094; 31 sese.037.001.09 PortfolioTransferNotificationV09.

> In case the receiving settlement chain is not available to the delivering account servicer, the receiving account servicer may in return provide to the delivering account servicer the receiving settlement chain using the same message.

src-000197, file pages1094; 31 sese.037.001.09 PortfolioTransferNotificationV09.

<!-- /FUNCTIONALITY-ALIASES-src-000197 -->
