---
template: false
document_kind: "participant"
review_status: "needs-review"
title: "Executing/servicing party"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
participant_id: "participant-settlement-reconciliation-executing-servicing-party"
role_kind: "functional participant role"
source_labels: ["Executing Servicing Party", "Executing/Servicing Party", "Executing Party", "servicing/executing party"]
aliases: ["Executing Servicing Party", "Executing/Servicing Party", "Executing Party", "servicing/executing party"]
domains: ["securities"]
message_ids: ["sese.023.001.13"]
flow_ids: ["flow-settlement-reconciliation-allegement", "flow-settlement-reconciliation-bilateral-splitting", "flow-settlement-reconciliation-cancellation-advice", "flow-settlement-reconciliation-cancellation-request", "flow-settlement-reconciliation-hold-release", "flow-settlement-reconciliation-instruction-confirmation", "flow-settlement-reconciliation-intra-position-instruction", "flow-settlement-reconciliation-modification-after-settlement", "flow-settlement-reconciliation-modification-before-settlement", "flow-settlement-reconciliation-pair-off", "flow-settlement-reconciliation-partial-settlement", "flow-settlement-reconciliation-portfolio-transfer", "flow-settlement-reconciliation-processing-change-multiple-transactions", "flow-settlement-reconciliation-processing-change-one-transaction", "flow-settlement-reconciliation-released-held-released", "flow-settlement-reconciliation-reporting-pull", "flow-settlement-reconciliation-reporting-push", "flow-settlement-reconciliation-reversal-advice", "flow-settlement-reconciliation-transaction-generation", "flow-settlement-reconciliation-unilateral-splitting"]
limitations: ["Formal §3.1 table14 definition is truncated to “Party that manages”. This record uses explicit activities and preserves the incomplete definition as a source defect."]
---

# Executing/servicing party

## Definition and context

Receives and validates instructions, performs matching and settlement, returns status information and confirmations, and processes cancellation requests. These responsibilities are established by the activity and transaction descriptions.

**Evidence:** src-000196 §5.1 table28; §6.1 paragraphs324–327; §5.12 table45; §6.12 paragraphs607–612. Original: [src-000196](../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md).

## Responsibilities and relationships

Responsibilities and message directions are specific to each linked flow. A role in one relationship does not establish the same role in another.

- [instruction confirmation](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/instruction-confirmation.md)
- [partial settlement](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/partial-settlement.md)
- [cancellation request](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/cancellation-request.md)
- [cancellation advice](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/cancellation-advice.md)
- [reversal advice](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/reversal-advice.md)
- [reporting push](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-push.md)
- [reporting pull](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-pull.md)
- [portfolio transfer](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/portfolio-transfer.md)
- [transaction generation](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/transaction-generation.md)

## Source labels and identifier schemes

Source labels: `Executing Servicing Party`, `Executing/Servicing Party`, `Executing Party`, `servicing/executing party`. The role definition does not mandate a universal identifier scheme. Consult the exact message component for its permitted identification choices.

## Limitations

Formal §3.1 table14 definition is truncated to “Party that manages”. This record uses explicit activities and preserves the incomplete definition as a source defect.

[Message-set participants](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/participants.md) · [sese.023.001.13 context](../../../domains/securities/reference/messages/sese.023.001.13/business.md)

Tracked issues: [issue-000006](../../../tracking/issues.md).

<!-- SETTLEMENT-FLOW-LINKS-START -->
## Additional source-scoped settlement flows

- [Allegement and counterparty response](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/allegement.md)
- [Bilateral splitting](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/bilateral-splitting.md)
- [Release an instruction originally on hold](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/hold-release.md)
- [Intra-position instruction and confirmation](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/intra-position-instruction.md)
- [Modification after settlement](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/modification-after-settlement.md)
- [Modification before settlement with counterparty response](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/modification-before-settlement.md)
- [Pair-off instruction sequence](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/pair-off.md)
- [Portfolio transfer settlement details](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/portfolio-transfer.md)
- [Processing change for two transactions](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/processing-change-multiple-transactions.md)
- [Processing change for one transaction](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/processing-change-one-transaction.md)
- [Hold then release an instruction](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/released-held-released.md)
- [Reporting pull mode with third party](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-pull.md)
- [Reporting push mode with third party](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-push.md)
- [Unilateral splitting](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/unilateral-splitting.md)
<!-- SETTLEMENT-FLOW-LINKS-END -->










































<!-- SOURCE196-DIAGRAM-67-START -->
[Reporting push mode with third party](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0067.md) — src-000196 direct-body paragraph P590.
<!-- SOURCE196-DIAGRAM-67-END -->

<!-- SOURCE196-DIAGRAM-68-START -->
[Reporting pull mode with third party](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0068.md) — src-000196 direct-body paragraph P605.
<!-- SOURCE196-DIAGRAM-68-END -->

<!-- SOURCE196-DIAGRAM-72-START -->
[Portfolio transfer settlement details](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0072.md) — src-000196 direct-body paragraph P631.
<!-- SOURCE196-DIAGRAM-72-END -->

<!-- SOURCE196-DIAGRAM-30-START -->
[Allegement activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0030.md) — src-000196 direct-body paragraph P272.
<!-- SOURCE196-DIAGRAM-30-END -->

<!-- SOURCE196-DIAGRAM-31-START -->
[Reporting push activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0031.md) — src-000196 direct-body paragraph P284.
<!-- SOURCE196-DIAGRAM-31-END -->

<!-- SOURCE196-DIAGRAM-32-START -->
[Reporting pull activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0032.md) — src-000196 direct-body paragraph P301.
<!-- SOURCE196-DIAGRAM-32-END -->

<!-- SOURCE196-DIAGRAM-29-START -->
[Split settlement activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0029.md) — src-000196 direct-body paragraph P270.
<!-- SOURCE196-DIAGRAM-29-END -->

<!-- SOURCE196-DIAGRAM-28-START -->
[Modification after settlement activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0028.md) — src-000196 direct-body paragraph P268.
<!-- SOURCE196-DIAGRAM-28-END -->

<!-- SOURCE196-DIAGRAM-38-START -->
[Intra-position instruction and confirmation](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0038.md) — src-000196 direct-body paragraph P334.
<!-- SOURCE196-DIAGRAM-38-END -->

<!-- SOURCE196-DIAGRAM-61-START -->
[Bilateral splitting — settlement confirmations](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0061.md) — src-000196 direct-body paragraph P543.
<!-- SOURCE196-DIAGRAM-61-END -->

<!-- SOURCE196-DIAGRAM-11-START -->
[Intra-position instruction activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0011.md) — src-000196 direct-body paragraph P200.
<!-- SOURCE196-DIAGRAM-11-END -->

<!-- SOURCE196-DIAGRAM-12-START -->
[Partial settlement activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0012.md) — src-000196 direct-body paragraph P202.
<!-- SOURCE196-DIAGRAM-12-END -->

<!-- SOURCE196-DIAGRAM-17-START -->
[Pair-off activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0017.md) — src-000196 direct-body paragraph P240.
<!-- SOURCE196-DIAGRAM-17-END -->

<!-- SOURCE196-DIAGRAM-19-START -->
[Settlement instruction status processes](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0019.md) — src-000196 direct-body paragraph P247.
<!-- SOURCE196-DIAGRAM-19-END -->

<!-- SOURCE196-DIAGRAM-20-START -->
[Cancellation-request status processes](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0020.md) — src-000196 direct-body paragraph P249.
<!-- SOURCE196-DIAGRAM-20-END -->

<!-- SOURCE196-DIAGRAM-21-START -->
[Cancellation status and reason](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0021.md) — src-000196 direct-body paragraph P252.
<!-- SOURCE196-DIAGRAM-21-END -->

<!-- SOURCE196-DIAGRAM-22-START -->
[Intra-position instruction status processes](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0022.md) — src-000196 direct-body paragraph P254.
<!-- SOURCE196-DIAGRAM-22-END -->

<!-- SOURCE196-DIAGRAM-23-START -->
[Statement or status query validation](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0023.md) — src-000196 direct-body paragraph P256.
<!-- SOURCE196-DIAGRAM-23-END -->

<!-- SOURCE196-DIAGRAM-24-START -->
[Modification-request status processes](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0024.md) — src-000196 direct-body paragraph P258.
<!-- SOURCE196-DIAGRAM-24-END -->

<!-- SOURCE196-DIAGRAM-25-START -->
[Hold and release activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0025.md) — src-000196 direct-body paragraph P261.
<!-- SOURCE196-DIAGRAM-25-END -->

<!-- SOURCE196-DIAGRAM-26-START -->
[Other processing-change activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0026.md) — src-000196 direct-body paragraph P263.
<!-- SOURCE196-DIAGRAM-26-END -->

<!-- SOURCE196-DIAGRAM-27-START -->
[Modification before settlement activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0027.md) — src-000196 direct-body paragraph P266.
<!-- SOURCE196-DIAGRAM-27-END -->

<!-- SOURCE196-DIAGRAM-33-START -->
[Cancellation-request activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0033.md) — src-000196 direct-body paragraph P303.
<!-- SOURCE196-DIAGRAM-33-END -->

<!-- SOURCE196-DIAGRAM-34-START -->
[Cancellation-advice activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0034.md) — src-000196 direct-body paragraph P305.
<!-- SOURCE196-DIAGRAM-34-END -->

<!-- SOURCE196-DIAGRAM-35-START -->
[Settlement reversal-advice activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0035.md) — src-000196 direct-body paragraph P310.
<!-- SOURCE196-DIAGRAM-35-END -->

<!-- SOURCE196-DIAGRAM-36-START -->
[Portfolio transfer activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0036.md) — src-000196 direct-body paragraph P312.
<!-- SOURCE196-DIAGRAM-36-END -->

<!-- SOURCE196-DIAGRAM-50-START -->
[Pair-off instruction sequence](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0050.md) — src-000196 direct-body paragraph P444.
<!-- SOURCE196-DIAGRAM-50-END -->

<!-- SOURCE196-DIAGRAM-52-START -->
[Release an instruction originally on hold](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0052.md) — src-000196 direct-body paragraph P476.
<!-- SOURCE196-DIAGRAM-52-END -->

<!-- SOURCE196-DIAGRAM-53-START -->
[Hold then release an instruction](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0053.md) — src-000196 direct-body paragraph P487.
<!-- SOURCE196-DIAGRAM-53-END -->

<!-- SOURCE196-DIAGRAM-54-START -->
[Processing change for one transaction](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0054.md) — src-000196 direct-body paragraph P496.
<!-- SOURCE196-DIAGRAM-54-END -->

<!-- SOURCE196-DIAGRAM-55-START -->
[Processing change for two transactions](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0055.md) — src-000196 direct-body paragraph P502.
<!-- SOURCE196-DIAGRAM-55-END -->

<!-- SOURCE196-DIAGRAM-56-START -->
[Modification before settlement with counterparty response](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0056.md) — src-000196 direct-body paragraph P517.
<!-- SOURCE196-DIAGRAM-56-END -->

<!-- SOURCE196-DIAGRAM-57-START -->
[Modification after settlement](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0057.md) — src-000196 direct-body paragraph P526.
<!-- SOURCE196-DIAGRAM-57-END -->

<!-- SOURCE196-DIAGRAM-58-START -->
[Bilateral splitting — original instructions and cancellation](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0058.md) — src-000196 direct-body paragraph P538.
<!-- SOURCE196-DIAGRAM-58-END -->

<!-- SOURCE196-DIAGRAM-59-START -->
[Bilateral splitting — two replacement instructions](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0059.md) — src-000196 direct-body paragraph P540.
<!-- SOURCE196-DIAGRAM-59-END -->

<!-- SOURCE196-DIAGRAM-60-START -->
[Bilateral splitting — status propagation](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0060.md) — src-000196 direct-body paragraph P541.
<!-- SOURCE196-DIAGRAM-60-END -->

<!-- SOURCE196-DIAGRAM-62-START -->
[Unilateral splitting — instruction and split request](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0062.md) — src-000196 direct-body paragraph P555.
<!-- SOURCE196-DIAGRAM-62-END -->

<!-- SOURCE196-DIAGRAM-63-START -->
[Unilateral splitting — status propagation, first picture](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0063.md) — src-000196 direct-body paragraph P557.
<!-- SOURCE196-DIAGRAM-63-END -->

<!-- SOURCE196-DIAGRAM-64-START -->
[Unilateral splitting — status propagation, second picture](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0064.md) — src-000196 direct-body paragraph P562.
<!-- SOURCE196-DIAGRAM-64-END -->

<!-- SOURCE196-DIAGRAM-65-START -->
[Unilateral splitting — settlement confirmations](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0065.md) — src-000196 direct-body paragraph P563.
<!-- SOURCE196-DIAGRAM-65-END -->

<!-- SOURCE196-DIAGRAM-66-START -->
[Allegement and counterparty response](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0066.md) — src-000196 direct-body paragraph P571.
<!-- SOURCE196-DIAGRAM-66-END -->
