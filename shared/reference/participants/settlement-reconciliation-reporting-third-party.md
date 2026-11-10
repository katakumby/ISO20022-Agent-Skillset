---
template: false
document_kind: "participant"
review_status: "needs-review"
title: "Third party in securities reporting"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
participant_id: "participant-settlement-reconciliation-reporting-third-party"
role_kind: "functional participant role"
source_labels: ["third party"]
aliases: ["third party"]
domains: ["securities"]
message_ids: []
flow_ids: ["flow-settlement-reconciliation-reporting-pull", "flow-settlement-reconciliation-reporting-push"]
limitations: ["Scoped to reporting; not equated with every third-party copy recipient supported by BAH."]
---

# Third party in securities reporting

## Definition and context

A third party, for example a CSD, may receive or request an audit trail for an individual pending securities transaction. The report covers status, modification, replacement and cancellation history.

**Evidence:** src-000196 §5.11 paragraphs283,298–300; §6.11 paragraphs602–604. Original: [src-000196](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx>).

## Responsibilities and relationships

Responsibilities and message directions are specific to each linked flow. A role in one relationship does not establish the same role in another.

- [reporting push](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-push.md>)
- [reporting pull](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-pull.md>)

## Source labels and identifier schemes

Source labels: `third party`. The role definition does not mandate a universal identifier scheme. Consult the exact message component for its permitted identification choices.

## Limitations

Scoped to reporting; not equated with every third-party copy recipient supported by BAH.

[Message-set participants](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/participants.md>) · [sese.023.001.13 context](<../../../domains/securities/reference/messages/sese.023.001.13/business.md>)

<!-- SETTLEMENT-FLOW-LINKS-START -->
## Additional source-scoped settlement flows

- [Reporting pull mode with third party](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-pull.md)
- [Reporting push mode with third party](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-push.md)
<!-- SETTLEMENT-FLOW-LINKS-END -->





<!-- SOURCE196-DIAGRAM-67-START -->
[Reporting push mode with third party](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0067.md) — src-000196 direct-body paragraph P590.
<!-- SOURCE196-DIAGRAM-67-END -->

<!-- SOURCE196-DIAGRAM-68-START -->
[Reporting pull mode with third party](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0068.md) — src-000196 direct-body paragraph P605.
<!-- SOURCE196-DIAGRAM-68-END -->

<!-- SOURCE196-DIAGRAM-31-START -->
[Reporting push activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0031.md) — src-000196 direct-body paragraph P284.
<!-- SOURCE196-DIAGRAM-31-END -->

<!-- SOURCE196-DIAGRAM-32-START -->
[Reporting pull activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0032.md) — src-000196 direct-body paragraph P301.
<!-- SOURCE196-DIAGRAM-32-END -->
