---
template: false
document_kind: "participant"
review_status: "needs-review"
title: "CSD / ICSD"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
participant_id: "participant-settlement-reconciliation-csd-icsd"
role_kind: "business role"
source_labels: ["CSD / ICSD"]
aliases: ["CSD / ICSD"]
domains: ["securities"]
message_ids: []
flow_ids: []
limitations: ["Table16 account-role headers differ from functional labels in table14. Preserve the source mapping without reversing or repairing it."]
---

# CSD / ICSD

## Definition and context

Infrastructure that, holds or controls, the holding of physical or dematerialised financial instruments belonging to all, or a large portion of, the investors in a securities market. It effects the centralised transfer of ownership of such securities by entries on its books and records. The depository may delegate custody to another entity (custodian).

**Evidence:** src-000196 §3.1 Business Roles table15, row9. Original: [src-000196](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx>).

## Responsibilities and relationships

The source role overview and mapping table are linked from [the participant index](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/participants.md>). Assignment to a flow requires that flow’s evidence.

## Source labels and identifier schemes

Source labels: `CSD / ICSD`. The role definition does not mandate a universal identifier scheme. Consult the exact message component for its permitted identification choices.

## Limitations

Table16 account-role headers differ from functional labels in table14. Preserve the source mapping without reversing or repairing it.

[Message-set participants](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/participants.md>) · [sese.023.001.13 context](<../../../domains/securities/reference/messages/sese.023.001.13/business.md>)



<!-- SOURCE196-DIAGRAM-1-START -->
[Settlement communication scope and account relationships](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0001.md) — src-000196 direct-body paragraph P145.
<!-- SOURCE196-DIAGRAM-1-END -->

<!-- SOURCE196-DIAGRAM-36-START -->
[Portfolio transfer activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0036.md) — src-000196 direct-body paragraph P312.
<!-- SOURCE196-DIAGRAM-36-END -->
