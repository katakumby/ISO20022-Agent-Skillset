---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Bilateral splitting"
flow_id: "flow-settlement-reconciliation-bilateral-splitting"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P527", "heading_path": ["BusinessTransactions", "Split Settlement"], "xml_path": "/w:document/w:body/w:p[527]"}, {"source_id": "src-000196", "paragraph_id": "P528", "heading_path": ["BusinessTransactions", "Split Settlement"], "xml_path": "/w:document/w:body/w:p[528]"}, {"source_id": "src-000196", "paragraph_id": "P529", "heading_path": ["BusinessTransactions", "Split Settlement", "Bilateral Splitting"], "xml_path": "/w:document/w:body/w:p[529]"}, {"source_id": "src-000196", "paragraph_id": "P530", "heading_path": ["BusinessTransactions", "Split Settlement", "Bilateral Splitting"], "xml_path": "/w:document/w:body/w:p[530]"}, {"source_id": "src-000196", "paragraph_id": "P531", "heading_path": ["BusinessTransactions", "Split Settlement", "Bilateral Splitting"], "xml_path": "/w:document/w:body/w:p[531]"}, {"source_id": "src-000196", "paragraph_id": "P532", "heading_path": ["BusinessTransactions", "Split Settlement", "Bilateral Splitting"], "xml_path": "/w:document/w:body/w:p[532]"}, {"source_id": "src-000196", "paragraph_id": "P533", "heading_path": ["BusinessTransactions", "Split Settlement", "Bilateral Splitting"], "xml_path": "/w:document/w:body/w:p[533]"}, {"source_id": "src-000196", "paragraph_id": "P534", "heading_path": ["BusinessTransactions", "Split Settlement", "Bilateral Splitting"], "xml_path": "/w:document/w:body/w:p[534]"}, {"source_id": "src-000196", "paragraph_id": "P535", "heading_path": ["BusinessTransactions", "Split Settlement", "Bilateral Splitting"], "xml_path": "/w:document/w:body/w:p[535]"}, {"source_id": "src-000196", "paragraph_id": "P536", "heading_path": ["BusinessTransactions", "Split Settlement", "Bilateral Splitting"], "xml_path": "/w:document/w:body/w:p[536]"}, {"source_id": "src-000196", "paragraph_id": "P537", "heading_path": ["BusinessTransactions", "Split Settlement", "Bilateral Splitting"], "xml_path": "/w:document/w:body/w:p[537]"}]
message_ids: ["sese.020.001.09", "sese.023.001.13", "sese.024.001.14", "sese.025.001.13", "sese.027.001.09"]
participant_ids: ["participant-settlement-reconciliation-executing-servicing-party", "participant-settlement-reconciliation-instructing-party", "participant-settlement-reconciliation-instructing-splitting-party", "participant-settlement-reconciliation-split-settlement-client"]
diagram_ids: ["fig-0029", "fig-0058", "fig-0059", "fig-0060", "fig-0061"]
updated: "2026-11-09"
limitations: ["The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This is part 1 of the four source pictures for bilateral splitting; the original “Flow continues on next page” note is retained. Abbreviated message labels are preserved.", "This is part 2 of the bilateral-splitting source sequence. Instruction1 and Instruction2 are distinct replacements, not versions of a message definition.", "This is part 3 of the bilateral-splitting source sequence. Eight separate optional status arrows are retained; similar labels are not deduplicated.", "This is part 4 of the bilateral-splitting source sequence. Both replacement transactions produce confirmations on both counterparties’ client chains.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---

# Bilateral splitting

## Purpose, trigger and boundaries

The source-defined scenario is **Bilateral splitting**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Bilateral splitting — original instructions and cancellation](../diagrams/settlement-sequences/fig-0058.md)
- [Bilateral splitting — two replacement instructions](../diagrams/settlement-sequences/fig-0059.md)
- [Bilateral splitting — status propagation](../diagrams/settlement-sequences/fig-0060.md)
- [Bilateral splitting — settlement confirmations](../diagrams/settlement-sequences/fig-0061.md)

src-000196 P527–P543.

### Participants in this source sequence

- A — Client: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-split-settlement-client.md)
- B — Instructing/Splitting Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-splitting-party.md)
- C — Executing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)
- D — Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- E — Client: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-split-settlement-client.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P527** — Split Settlement

**src-000196 P528** — The split settlement consists (for an instructing/splitting party) in requesting the replacement of an existing instruction by two or more instructions. This is typically done by CSD Participants (unilaterally or bilaterally) to for example, enable the settlement of a client instruction that is short. Unilateral splitting is when only one party instructs the split. This happens for example in the UK.

**src-000196 P529** — Bilateral Splitting

**src-000196 P530** — Bilateral splitting is when both parties to a trade must instruct and match for a split to take place. This happens for example in Switzerland.

**src-000196 P531** — This diagram shows the messages flow between the client, the instructing splitting party, the executing/servicing party in addition to the counterparty's client and instructing party.

**src-000196 P532** — A client sends a SecuritiesSettlementTransactionInstruction to the instructing/splitting party (for example a global custodian) which in turn sends the instruction to the executing/servicing party (a CSD). The same flow takes place on the counterparty's side.

**src-000196 P533** — The executing/servicing party may send back to the instructing party and in turn the client, a processing status and/or a settlement/matching status referring to the state of the transaction. The same flow takes place on the counterparty's side.

**src-000196 P534** — The instructing/splitting party sends a cancellation request to the executing/servicing party (and optionally advise their client on the status of this request) and replaces it with two new instructions. Again, the instructing party may advise the client of the status of the new instructions. The same flow takes place on the counterparty's side.

**src-000196 P535** — The executing/servicing party may send back to the instructing party and in turn the client a processing status and/or a settlement/matching status referring to the state for both transactions. The same flow takes place on the counterparty's side.

**src-000196 P536** — When the transactions settle at the executing/servicing party, this latter sends two

**src-000196 P537** — SecuritiesSettlementTransactionConfirmation to advise the instructing party and then in turn the client that the settlement has taken place. The same flow takes place on the counterparty's side.

### Source activity responsibilities

[Activity table T41 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0041.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

### Source-specific qualifications

- This is part 1 of the four source pictures for bilateral splitting; the original “Flow continues on next page” note is retained. Abbreviated message labels are preserved.
- This is part 2 of the bilateral-splitting source sequence. Instruction1 and Instruction2 are distinct replacements, not versions of a message definition.
- This is part 3 of the bilateral-splitting source sequence. Eight separate optional status arrows are retained; similar labels are not deduplicated.
- This is part 4 of the bilateral-splitting source sequence. Both replacement transactions produce confirmations on both counterparties’ client chains.

<!-- SETTLEMENT-SEQUENCE-END -->


<!-- SOURCE-ACTIVITY-0029-START -->
[Split settlement activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0029.md)
<!-- SOURCE-ACTIVITY-0029-END -->
