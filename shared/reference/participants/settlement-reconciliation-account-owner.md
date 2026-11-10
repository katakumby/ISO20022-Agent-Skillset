---
template: false
document_kind: "participant"
review_status: "needs-review"
title: "Account owner"
domain: "securities"
source_ids: ["src-000196", "src-000197", "src-000198"]
source_editions: ["2025-2026", "March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
participant_id: "participant-settlement-reconciliation-account-owner"
role_kind: "functional account role"
source_labels: ["AccountOwnerRole"]
aliases: ["AccountOwnerRole"]
domains: ["securities"]
message_ids: ["sese.023.001.13"]
flow_ids: ["flow-settlement-reconciliation-instruction-confirmation", "flow-settlement-reconciliation-partial-settlement", "flow-settlement-reconciliation-cancellation-request", "flow-settlement-reconciliation-reversal-advice", "flow-settlement-reconciliation-reporting-push", "flow-settlement-reconciliation-reporting-pull"]
limitations: ["Institutional examples do not define this functional role."]
---

# Account owner

## Definition and context

Party that legally owns the account. In this message context, the account owner sends a settlement instruction to the account servicer. Account ownership and an authority to instruct are not automatically identical.

**Evidence:** src-000198 FullBusinessModel!A89:F89; src-000197 file/printed p491, §17.1 Scope. Original: [src-000198](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart3_SettlementAndReconciliation_2025_2026_v1.xlsx>).

## Responsibilities and relationships

Responsibilities and message directions are specific to each linked flow. A role in one relationship does not establish the same role in another.

- [instruction confirmation](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/instruction-confirmation.md>)
- [partial settlement](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/partial-settlement.md>)
- [cancellation request](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/cancellation-request.md>)
- [reversal advice](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/reversal-advice.md>)
- [reporting push](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-push.md>)
- [reporting pull](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-pull.md>)

## Source labels and identifier schemes

Source labels: `AccountOwnerRole`. The role definition does not mandate a universal identifier scheme. Consult the exact message component for its permitted identification choices.

## Limitations

Institutional examples do not define this functional role.

[Message-set participants](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/participants.md>) · [sese.023.001.13 context](<../../../domains/securities/reference/messages/sese.023.001.13/business.md>)

## Same-source conceptual record

[AccountOwnerRole](<../business-components/bc-b2f06e2fe55728412fe2.md>) preserves the complete FullBusinessModel rows cited by this participant record. This link is based on the explicit source component name, not a general equivalence between similarly labelled roles.




<!-- SOURCE196-DIAGRAM-1-START -->
[Settlement communication scope and account relationships](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0001.md) — src-000196 direct-body paragraph P145.
<!-- SOURCE196-DIAGRAM-1-END -->

<!-- SOURCE196-DIAGRAM-2-START -->
[Reporting communication overview](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0002.md) — src-000196 direct-body paragraph P147.
<!-- SOURCE196-DIAGRAM-2-END -->

<!-- SOURCE196-DIAGRAM-3-START -->
[Intra-position communication overview](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0003.md) — src-000196 direct-body paragraph P149.
<!-- SOURCE196-DIAGRAM-3-END -->
