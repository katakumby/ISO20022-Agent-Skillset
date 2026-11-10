---
template: false
document_kind: "participant"
review_status: "needs-review"
participant_id: "participant-settlement-reconciliation-securities-leg-executing-party"
title: "Securities Leg Executing Party"
domain: "securities"
domains: ["securities"]
source_ids: ["src-000196"]
source_labels: ["Securities Leg Executing Party"]
aliases: []
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P446", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[446]"}, {"source_id": "src-000196", "paragraph_id": "P448", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[448]"}, {"source_id": "src-000196", "paragraph_id": "P449", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[449]"}, {"source_id": "src-000196", "paragraph_id": "P450", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[450]"}, {"source_id": "src-000196", "paragraph_id": "P451", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[451]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.025.001.13"]
flow_ids: ["flow-settlement-reconciliation-cash-securities-split"]
role_kind: "functional participant role"
updated: "2026-11-09"
limitations: ["This definition is scoped to the cited scenarios. Institution examples do not define or fix the role.", "No identifier scheme is specified in these source paragraphs."]
source_editions: ["March 2026"]
---

# Securities Leg Executing Party

## Definition and context

Executes the securities leg in the cash/securities split scenario and provides status and settlement confirmation to the participant that split the instruction.

[src-000196](../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx); P446, P448, P449, P450, P451.

## Responsibilities, relationships and evidence

**src-000196 P446** — This sequence diagram reports the messages flow between the instructing party, the securities/cash instruction executing/servicing party, the securities leg executing party and the cash leg executing party.

**src-000196 P448** — The securities/cash instruction executing/servicing party in turn sends a SecuritiesSettlementTransactionInstruction (receive or deliver free) to the securities leg executing party and a cash transfer to the cash leg executing party.

**src-000196 P449** — The securities leg executing party may send to the securities/cash instruction executing/servicing party a processing status and/or a settlement status referring to the state of the transaction. The later will then pass the information on to the instructing party.

**src-000196 P450** — When the transaction settles at the securities leg executing party, then this latter sends a

**src-000196 P451** — SecuritiesSettlementTransactionConfirmation to advise the securities/cash instruction executing/servicing party that the settlement has taken place. The securities/cash instruction executing/servicing party will then relay the information to the instructing party.

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
