---
template: false
document_kind: "participant"
review_status: "needs-review"
participant_id: "participant-settlement-reconciliation-financing-servicing-settlement-executing-party"
title: "Securities Financing Servicing Party / Settlement Executing Party"
domain: "securities"
domains: ["securities"]
source_ids: ["src-000196"]
source_labels: ["Securities Financing Servicing Party/Settlement Executing Party", "Securities Financing Servicing Party / Settlement Executing Party"]
aliases: []
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P362", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Two Parties"], "xml_path": "/w:document/w:body/w:p[362]"}, {"source_id": "src-000196", "paragraph_id": "P363", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Two Parties"], "xml_path": "/w:document/w:body/w:p[363]"}, {"source_id": "src-000196", "paragraph_id": "P364", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Two Parties"], "xml_path": "/w:document/w:body/w:p[364]"}, {"source_id": "src-000196", "paragraph_id": "P365", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Two Parties"], "xml_path": "/w:document/w:body/w:p[365]"}, {"source_id": "src-000196", "paragraph_id": "P366", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Two Parties"], "xml_path": "/w:document/w:body/w:p[366]"}, {"source_id": "src-000196", "paragraph_id": "P379", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[379]"}, {"source_id": "src-000196", "paragraph_id": "P380", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[380]"}, {"source_id": "src-000196", "paragraph_id": "P381", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[381]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.025.001.13", "sese.033.001.13", "sese.034.001.11", "sese.035.001.13", "sese.036.001.10"]
flow_ids: ["flow-settlement-reconciliation-financing-instruction-two-parties", "flow-settlement-reconciliation-financing-modification-two-parties", "flow-settlement-reconciliation-financing-substitution-two-parties", "flow-settlement-reconciliation-financing-top-up-two-parties", "flow-settlement-reconciliation-financing-withdrawal-two-parties"]
role_kind: "functional participant role"
updated: "2026-11-09"
limitations: ["This definition is scoped to the cited scenarios. Institution examples do not define or fix the role.", "No identifier scheme is specified in these source paragraphs."]
source_editions: ["March 2026"]
---

# Securities Financing Servicing Party / Settlement Executing Party

## Definition and context

The two-party financing scenario explicitly combines financing servicing and settlement execution in the same participant. The participant creates and manages the two settlement legs and returns their financing statuses and confirmations.

[src-000196](../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md); P362, P363, P364, P365, P366, P379, P380, P381.

## Responsibilities, relationships and evidence

**src-000196 P362** — This diagram report the messages flow between the securities financing instructing party (a broker for example) and the securities financing servicing party/settlement executing party (a global custodian for instance).

**src-000196 P363** — The securities financing instructing party sends a SecuritiesFinancingInstruction to the securities financing servicing party/settlement executing party.

**src-000196 P364** — The securities financing servicing party/settlement executing party sets up both the closing and the opening leg of the securities financing.

**src-000196 P365** — The securities financing servicing party/settlement executing party may send a processing and/or a matching or settlement status to the securities financing instructing party for the opening and the closing legs.

**src-000196 P366** — When the opening and closing legs settle, the securities financing servicing party/settlement executing party sends a SecuritiesFinancingConfirmation to the securities financing instructing party.

**src-000196 P379** — This diagram shows the messages flow between the securities financing instructing party and the securities financing servicing party/settlement executing party.

**src-000196 P380** — The Securities Financing Instructing party (a broker for example) sends a SecuritiesFinancingModificationInstruction to the securities financing servicing party/settlement executing party (a sub-custodian) to modify the rate of a repo for instance on the closing leg.

**src-000196 P381** — The securities financing servicing party/settlement executing party may send a processing and/or settlement or matching status for the instruction to the securities financing instructing party with a SecuritiesFinancingStatusAdvice.

## Applicable flows

- [Securities financing — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-instruction-two-parties.md)
- [Financing modification without position change — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-modification-two-parties.md)
- [Financing substitution — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-substitution-two-parties.md)
- [Financing top-up — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-top-up-two-parties.md)
- [Financing withdrawal — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-withdrawal-two-parties.md)

## Identifier schemes and ambiguity

No identifier scheme is specified in the cited role narrative. The source examples do not make this role identical to a particular institution. A compound participant in a two-party scenario does not merge the separate three-party role definitions.

<!-- SETTLEMENT-FLOW-LINKS-START -->
## Additional source-scoped settlement flows

- [Securities financing — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-instruction-two-parties.md)
- [Financing modification without position change — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-modification-two-parties.md)
- [Financing substitution — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-substitution-two-parties.md)
- [Financing top-up — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-top-up-two-parties.md)
- [Financing withdrawal — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-withdrawal-two-parties.md)
<!-- SETTLEMENT-FLOW-LINKS-END -->








<!-- SOURCE196-DIAGRAM-14-START -->
[Financing instruction activity — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0014.md) — src-000196 direct-body paragraph P213.
<!-- SOURCE196-DIAGRAM-14-END -->

<!-- SOURCE196-DIAGRAM-16-START -->
[Financing modification activity — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0016.md) — src-000196 direct-body paragraph P231.
<!-- SOURCE196-DIAGRAM-16-END -->

<!-- SOURCE196-DIAGRAM-41-START -->
[Securities financing — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0041.md) — src-000196 direct-body paragraph P367.
<!-- SOURCE196-DIAGRAM-41-END -->

<!-- SOURCE196-DIAGRAM-43-START -->
[Financing modification without position change — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0043.md) — src-000196 direct-body paragraph P382.
<!-- SOURCE196-DIAGRAM-43-END -->

<!-- SOURCE196-DIAGRAM-47-START -->
[Financing substitution — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0047.md) — src-000196 direct-body paragraph P420.
<!-- SOURCE196-DIAGRAM-47-END -->

<!-- SOURCE196-DIAGRAM-48-START -->
[Financing top-up — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0048.md) — src-000196 direct-body paragraph P428.
<!-- SOURCE196-DIAGRAM-48-END -->

<!-- SOURCE196-DIAGRAM-49-START -->
[Financing withdrawal — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0049.md) — src-000196 direct-body paragraph P434.
<!-- SOURCE196-DIAGRAM-49-END -->
