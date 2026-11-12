---
template: false
document_kind: "participant"
review_status: "needs-review"
participant_id: "participant-settlement-reconciliation-financing-instructing-party"
title: "Securities Financing Instructing Party"
domain: "securities"
domains: ["securities"]
source_ids: ["src-000196"]
source_labels: ["Securities Financing Instructing Party"]
aliases: []
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P346", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[346]"}, {"source_id": "src-000196", "paragraph_id": "P349", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[349]"}, {"source_id": "src-000196", "paragraph_id": "P350", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[350]"}, {"source_id": "src-000196", "paragraph_id": "P357", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[357]"}, {"source_id": "src-000196", "paragraph_id": "P358", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[358]"}, {"source_id": "src-000196", "paragraph_id": "P359", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[359]"}, {"source_id": "src-000196", "paragraph_id": "P362", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Two Parties"], "xml_path": "/w:document/w:body/w:p[362]"}, {"source_id": "src-000196", "paragraph_id": "P363", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Two Parties"], "xml_path": "/w:document/w:body/w:p[363]"}, {"source_id": "src-000196", "paragraph_id": "P366", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Two Parties"], "xml_path": "/w:document/w:body/w:p[366]"}, {"source_id": "src-000196", "paragraph_id": "P373", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[373]"}, {"source_id": "src-000196", "paragraph_id": "P376", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[376]"}, {"source_id": "src-000196", "paragraph_id": "P380", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[380]"}, {"source_id": "src-000196", "paragraph_id": "P381", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[381]"}]
message_ids: ["sese.020.001.09", "sese.023.001.13", "sese.024.001.14", "sese.025.001.13", "sese.033.001.13", "sese.034.001.11", "sese.035.001.13", "sese.036.001.10"]
flow_ids: ["flow-settlement-reconciliation-financing-instruction-three-parties", "flow-settlement-reconciliation-financing-instruction-two-parties", "flow-settlement-reconciliation-financing-modification-three-parties", "flow-settlement-reconciliation-financing-modification-two-parties", "flow-settlement-reconciliation-financing-substitution-three-parties", "flow-settlement-reconciliation-financing-substitution-two-parties", "flow-settlement-reconciliation-financing-top-up-three-parties", "flow-settlement-reconciliation-financing-top-up-two-parties", "flow-settlement-reconciliation-financing-withdrawal-three-parties", "flow-settlement-reconciliation-financing-withdrawal-two-parties"]
role_kind: "functional participant role"
updated: "2026-11-09"
limitations: ["This definition is scoped to the cited scenarios. Institution examples do not define or fix the role.", "No identifier scheme is specified in these source paragraphs."]
source_editions: ["March 2026"]
---

# Securities Financing Instructing Party

## Definition and context

Functional participant that sends the financing instruction or modification and receives financing status/confirmation in the financing scenarios.

[src-000196](../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md); P346, P349, P350, P357, P358, P359, P362, P363, P366, P373, P376, P380, P381.

## Responsibilities, relationships and evidence

**src-000196 P346** — This section illustrates the instruction, status and confirmation of the opening and closing leg of a securities financing transaction and the relevant messages exchanged between the securities financing instructing party, the securities financing servicing party and the settlement executing party. The pure settlement of the opening and closing leg, when no securities financing information is required, would still be handled using regular settlement messages. The flows apply to repo/reverse repo, securities lending, securities borrowing, collateral in and collateral out (managed by a securities financing servicing party).

**src-000196 P349** — The securities financing instructing party sends a SecuritiesFinancingInstruction to the securities financing servicing party.

**src-000196 P350** — The securities financing servicing party may send a processing and/or a settlement or matching status with a SecuritiesFinancingStatusAdvice to the securities financing instructing party for the opening leg.

**src-000196 P357** — The securities financing servicing party may send a processing and/or a settlement or matching status with a SecuritiesFinancingStatusAdvice to the securities financing instructing party for the closing leg.

**src-000196 P358** — When the opening leg settles, the settlement executing party sends a SecuritiesSettlementTransactionConfirmation to the securities financing servicing party. The securities financing servicing party then sends a SecuritiesFinancingConfirmation to the securities financing instructing party.

**src-000196 P359** — When the closing leg settles, the settlement executing party sends a SecuritiesSettlementTransactionConfirmation to the securities financing servicing party. The securities financing servicing party then sends a SecuritiesFinancingConfirmation to the securities financing instructing party.

**src-000196 P362** — This diagram report the messages flow between the securities financing instructing party (a broker for example) and the securities financing servicing party/settlement executing party (a global custodian for instance).

**src-000196 P363** — The securities financing instructing party sends a SecuritiesFinancingInstruction to the securities financing servicing party/settlement executing party.

**src-000196 P366** — When the opening and closing legs settle, the securities financing servicing party/settlement executing party sends a SecuritiesFinancingConfirmation to the securities financing instructing party.

**src-000196 P373** — The securities financing Instructing party (a broker for example) sends a SecuritiesFinancingModificationInstruction to the securities financing servicing party (a custodian) to modify the rate of a repo for instance, on the closing leg.

**src-000196 P376** — The securities financing servicing party may in turn send a processing and/or matching/settlement status to the securities financing instructing party with a SecuritiesFinancingStatusAdvice.

**src-000196 P380** — The Securities Financing Instructing party (a broker for example) sends a SecuritiesFinancingModificationInstruction to the securities financing servicing party/settlement executing party (a sub-custodian) to modify the rate of a repo for instance on the closing leg.

**src-000196 P381** — The securities financing servicing party/settlement executing party may send a processing and/or settlement or matching status for the instruction to the securities financing instructing party with a SecuritiesFinancingStatusAdvice.

## Applicable flows

- [Securities financing — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-instruction-three-parties.md)
- [Securities financing — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-instruction-two-parties.md)
- [Financing modification without position change — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-modification-three-parties.md)
- [Financing modification without position change — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-modification-two-parties.md)
- [Financing substitution — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-substitution-three-parties.md)
- [Financing top-up — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-top-up-three-parties.md)
- [Financing withdrawal — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-withdrawal-three-parties.md)
- [Financing substitution — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-substitution-two-parties.md)
- [Financing top-up — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-top-up-two-parties.md)
- [Financing withdrawal — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-withdrawal-two-parties.md)

## Identifier schemes and ambiguity

No identifier scheme is specified in the cited role narrative. The source examples do not make this role identical to a particular institution. A compound participant in a two-party scenario does not merge the separate three-party role definitions.

<!-- SETTLEMENT-FLOW-LINKS-START -->
## Additional source-scoped settlement flows

- [Securities financing — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-instruction-three-parties.md)
- [Securities financing — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-instruction-two-parties.md)
- [Financing modification without position change — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-modification-three-parties.md)
- [Financing modification without position change — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-modification-two-parties.md)
- [Financing substitution — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-substitution-three-parties.md)
- [Financing substitution — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-substitution-two-parties.md)
- [Financing top-up — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-top-up-three-parties.md)
- [Financing top-up — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-top-up-two-parties.md)
- [Financing withdrawal — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-withdrawal-three-parties.md)
- [Financing withdrawal — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/financing-withdrawal-two-parties.md)
<!-- SETTLEMENT-FLOW-LINKS-END -->















<!-- SOURCE196-DIAGRAM-13-START -->
[Financing instruction activity — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0013.md) — src-000196 direct-body paragraph P210.
<!-- SOURCE196-DIAGRAM-13-END -->

<!-- SOURCE196-DIAGRAM-14-START -->
[Financing instruction activity — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0014.md) — src-000196 direct-body paragraph P213.
<!-- SOURCE196-DIAGRAM-14-END -->

<!-- SOURCE196-DIAGRAM-15-START -->
[Financing modification activity — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0015.md) — src-000196 direct-body paragraph P228.
<!-- SOURCE196-DIAGRAM-15-END -->

<!-- SOURCE196-DIAGRAM-16-START -->
[Financing modification activity — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0016.md) — src-000196 direct-body paragraph P231.
<!-- SOURCE196-DIAGRAM-16-END -->

<!-- SOURCE196-DIAGRAM-40-START -->
[Securities financing — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0040.md) — src-000196 direct-body paragraph P360.
<!-- SOURCE196-DIAGRAM-40-END -->

<!-- SOURCE196-DIAGRAM-41-START -->
[Securities financing — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0041.md) — src-000196 direct-body paragraph P367.
<!-- SOURCE196-DIAGRAM-41-END -->

<!-- SOURCE196-DIAGRAM-42-START -->
[Financing modification without position change — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0042.md) — src-000196 direct-body paragraph P377.
<!-- SOURCE196-DIAGRAM-42-END -->

<!-- SOURCE196-DIAGRAM-43-START -->
[Financing modification without position change — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0043.md) — src-000196 direct-body paragraph P382.
<!-- SOURCE196-DIAGRAM-43-END -->

<!-- SOURCE196-DIAGRAM-44-START -->
[Financing substitution — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0044.md) — src-000196 direct-body paragraph P394.
<!-- SOURCE196-DIAGRAM-44-END -->

<!-- SOURCE196-DIAGRAM-45-START -->
[Financing top-up — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0045.md) — src-000196 direct-body paragraph P403.
<!-- SOURCE196-DIAGRAM-45-END -->

<!-- SOURCE196-DIAGRAM-46-START -->
[Financing withdrawal — three parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0046.md) — src-000196 direct-body paragraph P414.
<!-- SOURCE196-DIAGRAM-46-END -->

<!-- SOURCE196-DIAGRAM-47-START -->
[Financing substitution — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0047.md) — src-000196 direct-body paragraph P420.
<!-- SOURCE196-DIAGRAM-47-END -->

<!-- SOURCE196-DIAGRAM-48-START -->
[Financing top-up — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0048.md) — src-000196 direct-body paragraph P428.
<!-- SOURCE196-DIAGRAM-48-END -->

<!-- SOURCE196-DIAGRAM-49-START -->
[Financing withdrawal — two parties](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0049.md) — src-000196 direct-body paragraph P434.
<!-- SOURCE196-DIAGRAM-49-END -->
