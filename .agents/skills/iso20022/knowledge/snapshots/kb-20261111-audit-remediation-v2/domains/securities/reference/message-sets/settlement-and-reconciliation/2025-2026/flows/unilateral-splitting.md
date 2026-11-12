---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Unilateral splitting"
flow_id: "flow-settlement-reconciliation-unilateral-splitting"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P544", "heading_path": ["BusinessTransactions", "Split Settlement", "Unilateral Splitting"], "xml_path": "/w:document/w:body/w:p[544]"}, {"source_id": "src-000196", "paragraph_id": "P545", "heading_path": ["BusinessTransactions", "Split Settlement", "Unilateral Splitting"], "xml_path": "/w:document/w:body/w:p[545]"}, {"source_id": "src-000196", "paragraph_id": "P546", "heading_path": ["BusinessTransactions", "Split Settlement", "Unilateral Splitting"], "xml_path": "/w:document/w:body/w:p[546]"}, {"source_id": "src-000196", "paragraph_id": "P547", "heading_path": ["BusinessTransactions", "Split Settlement", "Unilateral Splitting"], "xml_path": "/w:document/w:body/w:p[547]"}, {"source_id": "src-000196", "paragraph_id": "P548", "heading_path": ["BusinessTransactions", "Split Settlement", "Unilateral Splitting"], "xml_path": "/w:document/w:body/w:p[548]"}, {"source_id": "src-000196", "paragraph_id": "P549", "heading_path": ["BusinessTransactions", "Split Settlement", "Unilateral Splitting"], "xml_path": "/w:document/w:body/w:p[549]"}, {"source_id": "src-000196", "paragraph_id": "P550", "heading_path": ["BusinessTransactions", "Split Settlement", "Unilateral Splitting"], "xml_path": "/w:document/w:body/w:p[550]"}, {"source_id": "src-000196", "paragraph_id": "P551", "heading_path": ["BusinessTransactions", "Split Settlement", "Unilateral Splitting"], "xml_path": "/w:document/w:body/w:p[551]"}, {"source_id": "src-000196", "paragraph_id": "P552", "heading_path": ["BusinessTransactions", "Split Settlement", "Unilateral Splitting"], "xml_path": "/w:document/w:body/w:p[552]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.025.001.13", "sese.027.001.09", "sese.030.001.10"]
participant_ids: ["participant-settlement-reconciliation-executing-servicing-party", "participant-settlement-reconciliation-instructing-party", "participant-settlement-reconciliation-instructing-splitting-party", "participant-settlement-reconciliation-split-settlement-client"]
diagram_ids: ["fig-0029", "fig-0062", "fig-0063", "fig-0064", "fig-0065"]
updated: "2026-11-09"
limitations: ["The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This is part 1 of the four source pictures for unilateral splitting. The condition-modification request and ensuing cancellation-request-status labels are retained as drawn; no replacement request is invented.", "This is part 2 of the unilateral-splitting source sequence. The eight arrows and optional frames are preserved in their picture order.", "This is part 3 of the unilateral-splitting source sequence. The similar preceding picture is not byte-identical; this picture has different vertical ordering of the last status arrows and remains separate.", "This is part 4 of the unilateral-splitting source sequence. Confirmation order follows this picture, independently of the bilateral scenario.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---

# Unilateral splitting

## Purpose, trigger and boundaries

The source-defined scenario is **Unilateral splitting**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Unilateral splitting — instruction and split request](../diagrams/settlement-sequences/fig-0062.md)
- [Unilateral splitting — status propagation, first picture](../diagrams/settlement-sequences/fig-0063.md)
- [Unilateral splitting — status propagation, second picture](../diagrams/settlement-sequences/fig-0064.md)
- [Unilateral splitting — settlement confirmations](../diagrams/settlement-sequences/fig-0065.md)

src-000196 P544–P563.

### Participants in this source sequence

- A — Client: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-split-settlement-client.md)
- B — Instructing/Splitting Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-splitting-party.md)
- C — Executing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)
- D — Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- E — Client: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-split-settlement-client.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P544** — Unilateral Splitting

**src-000196 P545** — Unilateral splitting is when only one party instructs the split. This happens, for example, in the UK and the US.

**src-000196 P546** — This diagram shows the messages flow between the client, the instructing splitting party, the executing/servicing party in addition to the counterparty's client and instructing party.

**src-000196 P547** — A client sends a SecuritiesSettlementTransactionInstruction to the instructing/splitting party (for example a global custodian) which in turn send the instruction to the executing/servicing party (a CSD). The same flow takes place on the counterparty's side.

**src-000196 P548** — The executing/servicing party may send back to the instructing party and in turn the client, a processing status and/or a settlement status referring to the state of the transaction. The same flow takes place on the counterparty's side.

**src-000196 P549** — The instructing/splitting party sends a SecuritieSettlementConditionModificationRequest to the executing/servicing party to request the splitting of the instruction in two. This can happen when the client sends an instruction for US government bonds with a quantity greater than 50 million which is not allowed on the US market.

**src-000196 P550** — The executing/servicing party then cancels the counterparty's transaction and replaces it with two new transactions.

**src-000196 P551** — The executing/servicing party may send back to the instructing party and in turn the client a processing status and/or a settlement/matching status referring to the state of the transaction. The same flow takes place on the counterparty's side.

**src-000196 P552** — When the transactions settle at the executing/servicing party, this latter sends two Security SettlementTransactionConfirmation to advise the instructing party and then in turn the client that the settlement has taken place. The same flow takes place on the counterparty's side.

### Source activity responsibilities

[Activity table T41 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0041.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

### Source-specific qualifications

- This is part 1 of the four source pictures for unilateral splitting. The condition-modification request and ensuing cancellation-request-status labels are retained as drawn; no replacement request is invented.
- This is part 2 of the unilateral-splitting source sequence. The eight arrows and optional frames are preserved in their picture order.
- This is part 3 of the unilateral-splitting source sequence. The similar preceding picture is not byte-identical; this picture has different vertical ordering of the last status arrows and remains separate.
- This is part 4 of the unilateral-splitting source sequence. Confirmation order follows this picture, independently of the bilateral scenario.

<!-- SETTLEMENT-SEQUENCE-END -->


<!-- SOURCE-ACTIVITY-0029-START -->
[Split settlement activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0029.md)
<!-- SOURCE-ACTIVITY-0029-END -->
