---
template: false
document_kind: "participant"
review_status: "needs-review"
participant_id: "participant-settlement-reconciliation-split-settlement-client"
title: "Client — split settlement"
domain: "securities"
domains: ["securities"]
source_ids: ["src-000196"]
source_labels: ["Client"]
aliases: []
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P531", "heading_path": ["BusinessTransactions", "Split Settlement", "Bilateral Splitting"], "xml_path": "/w:document/w:body/w:p[531]"}, {"source_id": "src-000196", "paragraph_id": "P532", "heading_path": ["BusinessTransactions", "Split Settlement", "Bilateral Splitting"], "xml_path": "/w:document/w:body/w:p[532]"}, {"source_id": "src-000196", "paragraph_id": "P533", "heading_path": ["BusinessTransactions", "Split Settlement", "Bilateral Splitting"], "xml_path": "/w:document/w:body/w:p[533]"}, {"source_id": "src-000196", "paragraph_id": "P534", "heading_path": ["BusinessTransactions", "Split Settlement", "Bilateral Splitting"], "xml_path": "/w:document/w:body/w:p[534]"}, {"source_id": "src-000196", "paragraph_id": "P535", "heading_path": ["BusinessTransactions", "Split Settlement", "Bilateral Splitting"], "xml_path": "/w:document/w:body/w:p[535]"}, {"source_id": "src-000196", "paragraph_id": "P537", "heading_path": ["BusinessTransactions", "Split Settlement", "Bilateral Splitting"], "xml_path": "/w:document/w:body/w:p[537]"}, {"source_id": "src-000196", "paragraph_id": "P546", "heading_path": ["BusinessTransactions", "Split Settlement", "Unilateral Splitting"], "xml_path": "/w:document/w:body/w:p[546]"}, {"source_id": "src-000196", "paragraph_id": "P547", "heading_path": ["BusinessTransactions", "Split Settlement", "Unilateral Splitting"], "xml_path": "/w:document/w:body/w:p[547]"}, {"source_id": "src-000196", "paragraph_id": "P548", "heading_path": ["BusinessTransactions", "Split Settlement", "Unilateral Splitting"], "xml_path": "/w:document/w:body/w:p[548]"}, {"source_id": "src-000196", "paragraph_id": "P549", "heading_path": ["BusinessTransactions", "Split Settlement", "Unilateral Splitting"], "xml_path": "/w:document/w:body/w:p[549]"}, {"source_id": "src-000196", "paragraph_id": "P551", "heading_path": ["BusinessTransactions", "Split Settlement", "Unilateral Splitting"], "xml_path": "/w:document/w:body/w:p[551]"}, {"source_id": "src-000196", "paragraph_id": "P552", "heading_path": ["BusinessTransactions", "Split Settlement", "Unilateral Splitting"], "xml_path": "/w:document/w:body/w:p[552]"}]
message_ids: ["sese.020.001.09", "sese.023.001.13", "sese.024.001.14", "sese.025.001.13", "sese.027.001.09", "sese.030.001.10"]
flow_ids: ["flow-settlement-reconciliation-bilateral-splitting", "flow-settlement-reconciliation-unilateral-splitting"]
role_kind: "functional participant role"
updated: "2026-11-09"
limitations: ["This definition is scoped to the cited scenarios. Institution examples do not define or fix the role.", "No identifier scheme is specified in these source paragraphs."]
source_editions: ["March 2026"]
---

# Client — split settlement

## Definition and context

A client sends the original settlement instruction through its instructing/splitting party or instructing party and receives relayed statuses and confirmations. Each side of the trade has a separately depicted client instance.

[src-000196](../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md); P531, P532, P533, P534, P535, P537, P546, P547, P548, P549, P551, P552.

## Responsibilities, relationships and evidence

**src-000196 P531** — This diagram shows the messages flow between the client, the instructing splitting party, the executing/servicing party in addition to the counterparty's client and instructing party.

**src-000196 P532** — A client sends a SecuritiesSettlementTransactionInstruction to the instructing/splitting party (for example a global custodian) which in turn sends the instruction to the executing/servicing party (a CSD). The same flow takes place on the counterparty's side.

**src-000196 P533** — The executing/servicing party may send back to the instructing party and in turn the client, a processing status and/or a settlement/matching status referring to the state of the transaction. The same flow takes place on the counterparty's side.

**src-000196 P534** — The instructing/splitting party sends a cancellation request to the executing/servicing party (and optionally advise their client on the status of this request) and replaces it with two new instructions. Again, the instructing party may advise the client of the status of the new instructions. The same flow takes place on the counterparty's side.

**src-000196 P535** — The executing/servicing party may send back to the instructing party and in turn the client a processing status and/or a settlement/matching status referring to the state for both transactions. The same flow takes place on the counterparty's side.

**src-000196 P537** — SecuritiesSettlementTransactionConfirmation to advise the instructing party and then in turn the client that the settlement has taken place. The same flow takes place on the counterparty's side.

**src-000196 P546** — This diagram shows the messages flow between the client, the instructing splitting party, the executing/servicing party in addition to the counterparty's client and instructing party.

**src-000196 P547** — A client sends a SecuritiesSettlementTransactionInstruction to the instructing/splitting party (for example a global custodian) which in turn send the instruction to the executing/servicing party (a CSD). The same flow takes place on the counterparty's side.

**src-000196 P548** — The executing/servicing party may send back to the instructing party and in turn the client, a processing status and/or a settlement status referring to the state of the transaction. The same flow takes place on the counterparty's side.

**src-000196 P549** — The instructing/splitting party sends a SecuritieSettlementConditionModificationRequest to the executing/servicing party to request the splitting of the instruction in two. This can happen when the client sends an instruction for US government bonds with a quantity greater than 50 million which is not allowed on the US market.

**src-000196 P551** — The executing/servicing party may send back to the instructing party and in turn the client a processing status and/or a settlement/matching status referring to the state of the transaction. The same flow takes place on the counterparty's side.

**src-000196 P552** — When the transactions settle at the executing/servicing party, this latter sends two Security SettlementTransactionConfirmation to advise the instructing party and then in turn the client that the settlement has taken place. The same flow takes place on the counterparty's side.

## Applicable flows

- [Bilateral splitting](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/bilateral-splitting.md)
- [Unilateral splitting](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/unilateral-splitting.md)

## Identifier schemes and ambiguity

No identifier scheme is specified in the cited role narrative. The source examples do not make this role identical to a particular institution. A compound participant in a two-party scenario does not merge the separate three-party role definitions.

<!-- SETTLEMENT-FLOW-LINKS-START -->
## Additional source-scoped settlement flows

- [Bilateral splitting](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/bilateral-splitting.md)
- [Unilateral splitting](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/unilateral-splitting.md)
<!-- SETTLEMENT-FLOW-LINKS-END -->










<!-- SOURCE196-DIAGRAM-29-START -->
[Split settlement activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0029.md) — src-000196 direct-body paragraph P270.
<!-- SOURCE196-DIAGRAM-29-END -->

<!-- SOURCE196-DIAGRAM-61-START -->
[Bilateral splitting — settlement confirmations](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0061.md) — src-000196 direct-body paragraph P543.
<!-- SOURCE196-DIAGRAM-61-END -->

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
