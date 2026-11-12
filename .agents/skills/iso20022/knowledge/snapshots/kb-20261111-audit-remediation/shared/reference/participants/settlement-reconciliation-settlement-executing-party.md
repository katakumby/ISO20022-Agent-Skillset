---
template: false
document_kind: "participant"
review_status: "needs-review"
participant_id: "participant-settlement-reconciliation-settlement-executing-party"
title: "Settlement Executing Party"
domain: "securities"
domains: ["securities"]
source_ids: ["src-000196"]
source_labels: ["Settlement Executing Party"]
aliases: []
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P348", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[348]"}, {"source_id": "src-000196", "paragraph_id": "P351", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[351]"}, {"source_id": "src-000196", "paragraph_id": "P352", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[352]"}, {"source_id": "src-000196", "paragraph_id": "P353", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[353]"}, {"source_id": "src-000196", "paragraph_id": "P354", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[354]"}, {"source_id": "src-000196", "paragraph_id": "P355", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[355]"}, {"source_id": "src-000196", "paragraph_id": "P356", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[356]"}, {"source_id": "src-000196", "paragraph_id": "P358", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[358]"}, {"source_id": "src-000196", "paragraph_id": "P359", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[359]"}, {"source_id": "src-000196", "paragraph_id": "P374", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[374]"}, {"source_id": "src-000196", "paragraph_id": "P375", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[375]"}]
message_ids: ["sese.020.001.09", "sese.023.001.13", "sese.024.001.14", "sese.025.001.13", "sese.033.001.13", "sese.034.001.11", "sese.036.001.10"]
flow_ids: ["flow-settlement-reconciliation-financing-instruction-three-parties", "flow-settlement-reconciliation-financing-modification-three-parties", "flow-settlement-reconciliation-financing-substitution-three-parties", "flow-settlement-reconciliation-financing-top-up-three-parties", "flow-settlement-reconciliation-financing-withdrawal-three-parties"]
role_kind: "functional participant role"
updated: "2026-11-09"
limitations: ["This definition is scoped to the cited scenarios. Institution examples do not define or fix the role.", "No identifier scheme is specified in these source paragraphs."]
source_editions: ["March 2026"]
---

# Settlement Executing Party

## Definition and context

Functional participant that receives settlement-leg instructions and supplies their status and confirmation to the securities financing servicing party.

[src-000196](../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md); P348, P351, P352, P353, P354, P355, P356, P358, P359, P374, P375.

## Responsibilities, relationships and evidence

**src-000196 P348** — This diagram shows the messages flow between the securities financing instructing party, the securities financing servicing party and the settlement executing party.

**src-000196 P351** — The securities financing servicing party in turn sends a SecuritiesSettlementTransactionInstruction for the opening leg to the settlement executing party.

**src-000196 P352** — The settlement executing party may send a processing and/or a matching or settlement status with a

**src-000196 P353** — SecuritiesSettlementTransactionStatusAdvice to the securities financing servicing party for the opening leg.

**src-000196 P354** — The securities financing servicing party then sends a SecuritiesSettlementTransactionInstruction for the closing leg to the settlement executing party.

**src-000196 P355** — The settlement executing party may send a processing and/or a matching or settlement status with a

**src-000196 P356** — SecuritiesSettlementTransactionStatusAdvice to the securities financing servicing party for the closing leg.

**src-000196 P358** — When the opening leg settles, the settlement executing party sends a SecuritiesSettlementTransactionConfirmation to the securities financing servicing party. The securities financing servicing party then sends a SecuritiesFinancingConfirmation to the securities financing instructing party.

**src-000196 P359** — When the closing leg settles, the settlement executing party sends a SecuritiesSettlementTransactionConfirmation to the securities financing servicing party. The securities financing servicing party then sends a SecuritiesFinancingConfirmation to the securities financing instructing party.

**src-000196 P374** — The securities financing servicing party in turn sends a SecuritiesTransactionCancellationRequest to the settlement executing party (a CSD) and a new SecuritiesSettlementTransactionInstructing for the closing leg with the new rate.

**src-000196 P375** — The settlement executing party may send a processing and/or settlement or matching status to the securities financing servicing party with a SecuritiesSettlementStatusAdvice.

## Applicable flows

- [Securities financing — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-instruction-three-parties.md)
- [Financing modification without position change — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-modification-three-parties.md)
- [Financing substitution — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-substitution-three-parties.md)
- [Financing top-up — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-top-up-three-parties.md)
- [Financing withdrawal — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-withdrawal-three-parties.md)

## Identifier schemes and ambiguity

No identifier scheme is specified in the cited role narrative. The source examples do not make this role identical to a particular institution. A compound participant in a two-party scenario does not merge the separate three-party role definitions.

<!-- SETTLEMENT-FLOW-LINKS-START -->
## Additional source-scoped settlement flows

- [Securities financing — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-instruction-three-parties.md)
- [Financing modification without position change — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-modification-three-parties.md)
- [Financing substitution — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-substitution-three-parties.md)
- [Financing top-up — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-top-up-three-parties.md)
- [Financing withdrawal — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-withdrawal-three-parties.md)
<!-- SETTLEMENT-FLOW-LINKS-END -->








<!-- SOURCE196-DIAGRAM-13-START -->
[Financing instruction activity — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0013.md) — src-000196 direct-body paragraph P210.
<!-- SOURCE196-DIAGRAM-13-END -->

<!-- SOURCE196-DIAGRAM-15-START -->
[Financing modification activity — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0015.md) — src-000196 direct-body paragraph P228.
<!-- SOURCE196-DIAGRAM-15-END -->

<!-- SOURCE196-DIAGRAM-40-START -->
[Securities financing — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0040.md) — src-000196 direct-body paragraph P360.
<!-- SOURCE196-DIAGRAM-40-END -->

<!-- SOURCE196-DIAGRAM-42-START -->
[Financing modification without position change — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0042.md) — src-000196 direct-body paragraph P377.
<!-- SOURCE196-DIAGRAM-42-END -->

<!-- SOURCE196-DIAGRAM-44-START -->
[Financing substitution — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0044.md) — src-000196 direct-body paragraph P394.
<!-- SOURCE196-DIAGRAM-44-END -->

<!-- SOURCE196-DIAGRAM-45-START -->
[Financing top-up — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0045.md) — src-000196 direct-body paragraph P403.
<!-- SOURCE196-DIAGRAM-45-END -->

<!-- SOURCE196-DIAGRAM-46-START -->
[Financing withdrawal — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0046.md) — src-000196 direct-body paragraph P414.
<!-- SOURCE196-DIAGRAM-46-END -->
