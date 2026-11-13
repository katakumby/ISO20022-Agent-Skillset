---
template: false
document_kind: "participant"
review_status: "needs-review"
participant_id: "participant-settlement-reconciliation-cash-securities-split-servicing-party"
title: "Securities/Cash Instruction Executing/Servicing Party"
domain: "securities"
domains: ["securities"]
source_ids: ["src-000196"]
source_labels: ["Securities/Cash Instruction Executing/Servicing Party", "Securities/Cash instruction Executing/Servicing Party"]
aliases: []
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P446", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[446]"}, {"source_id": "src-000196", "paragraph_id": "P447", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[447]"}, {"source_id": "src-000196", "paragraph_id": "P448", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[448]"}, {"source_id": "src-000196", "paragraph_id": "P449", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[449]"}, {"source_id": "src-000196", "paragraph_id": "P450", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[450]"}, {"source_id": "src-000196", "paragraph_id": "P451", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[451]"}, {"source_id": "src-000196", "paragraph_id": "P452", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[452]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.025.001.13"]
flow_ids: ["flow-settlement-reconciliation-cash-securities-split"]
role_kind: "functional participant role"
updated: "2026-11-09"
limitations: ["This definition is scoped to the cited scenarios. Institution examples do not define or fix the role.", "No identifier scheme is specified in these source paragraphs."]
source_editions: ["March 2026"]
---

# Securities/Cash Instruction Executing/Servicing Party

## Definition and context

Receives a versus-payment settlement instruction, separates it into securities and cash legs, and relays status and completion information from the leg executing parties.

[src-000196](../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md); P446, P447, P448, P449, P450, P451, P452.

## Responsibilities, relationships and evidence

**src-000196 P446** — This sequence diagram reports the messages flow between the instructing party, the securities/cash instruction executing/servicing party, the securities leg executing party and the cash leg executing party.

**src-000196 P447** — An instructing party (for example an investment manager), sends a SecuritiesSettlementTransactionInstruction (receive or delivery versus payment) to the securities/cash instruction executing/servicing party (a Global Custodian).

**src-000196 P448** — The securities/cash instruction executing/servicing party in turn sends a SecuritiesSettlementTransactionInstruction (receive or deliver free) to the securities leg executing party and a cash transfer to the cash leg executing party.

**src-000196 P449** — The securities leg executing party may send to the securities/cash instruction executing/servicing party a processing status and/or a settlement status referring to the state of the transaction. The later will then pass the information on to the instructing party.

**src-000196 P450** — When the transaction settles at the securities leg executing party, then this latter sends a

**src-000196 P451** — SecuritiesSettlementTransactionConfirmation to advise the securities/cash instruction executing/servicing party that the settlement has taken place. The securities/cash instruction executing/servicing party will then relay the information to the instructing party.

**src-000196 P452** — When the cash transfer takes place at the cash leg executing party, then this latter sends a security cash transfer confirmation to advise the securities/cash instruction executing/servicing party that the cash is transferred. The securities/cash instruction executing/servicing party will then relay the information to the instructing party.

## Applicable flows

- [Cash/securities split instruction and confirmation](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/cash-securities-split.md)

## Identifier schemes and ambiguity

No identifier scheme is specified in the cited role narrative. The source examples do not make this role identical to a particular institution. A compound participant in a two-party scenario does not merge the separate three-party role definitions.

<!-- SETTLEMENT-FLOW-LINKS-START -->
## Additional source-scoped settlement flows

- [Cash/securities split instruction and confirmation](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/cash-securities-split.md)
<!-- SETTLEMENT-FLOW-LINKS-END -->



<!-- SOURCE196-DIAGRAM-18-START -->
[Cash/securities split activity](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0018.md) — src-000196 direct-body paragraph P242.
<!-- SOURCE196-DIAGRAM-18-END -->

<!-- SOURCE196-DIAGRAM-51-START -->
[Cash/securities split instruction and confirmation](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0051.md) — src-000196 direct-body paragraph P453.
<!-- SOURCE196-DIAGRAM-51-END -->
