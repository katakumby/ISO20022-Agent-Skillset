---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Intra-position instruction and confirmation"
flow_id: "flow-settlement-reconciliation-intra-position-instruction"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P329", "heading_path": ["BusinessTransactions", "Intra-Position Instruction"], "xml_path": "/w:document/w:body/w:p[329]"}, {"source_id": "src-000196", "paragraph_id": "P330", "heading_path": ["BusinessTransactions", "Intra-Position Instruction"], "xml_path": "/w:document/w:body/w:p[330]"}, {"source_id": "src-000196", "paragraph_id": "P331", "heading_path": ["BusinessTransactions", "Intra-Position Instruction"], "xml_path": "/w:document/w:body/w:p[331]"}, {"source_id": "src-000196", "paragraph_id": "P332", "heading_path": ["BusinessTransactions", "Intra-Position Instruction"], "xml_path": "/w:document/w:body/w:p[332]"}, {"source_id": "src-000196", "paragraph_id": "P333", "heading_path": ["BusinessTransactions", "Intra-Position Instruction"], "xml_path": "/w:document/w:body/w:p[333]"}]
message_ids: ["semt.013.001.07", "semt.014.001.09", "semt.015.001.10"]
participant_ids: ["participant-settlement-reconciliation-executing-servicing-party", "participant-settlement-reconciliation-instructing-party"]
diagram_ids: ["fig-0003", "fig-0011", "fig-0022", "fig-0038"]
updated: "2026-11-09"
limitations: ["The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---

# Intra-position instruction and confirmation

## Purpose, trigger and boundaries

The source-defined scenario is **Intra-position instruction and confirmation**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Intra-position instruction and confirmation](../diagrams/settlement-sequences/fig-0038.md)

src-000196 P329–P334.

### Participants in this source sequence

- A — Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- B — Executing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P329** — Intra-Position Instruction

**src-000196 P330** — This diagram shows the messages flow between the instructing party and the executing/servicing party.

**src-000196 P331** — An instructing party (for example a CSD participant), sends a IntraPositionMovementInstruction to the executing/servicing party (a CSD) to move some securities from one sub-balance to another or from one balance status to another.

**src-000196 P332** — The executing/servicing party may send back to the instructing party a processing status and/or a settlement status referring to the state of the intra-position movement.

**src-000196 P333** — When the intra-position movement is finalised at the executing/servicing party, this latter sends a IntraPositionMovementConfirmation to advise the instructing party that the movement of securities has taken place.

### Source activity responsibilities

[Activity table T29 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0029.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

<!-- SETTLEMENT-SEQUENCE-END -->






















<!-- SOURCE-ACTIVITY-0003-START -->
[Intra-position communication overview — source activity/communication diagram](../diagrams/settlement-activities/fig-0003.md)
<!-- SOURCE-ACTIVITY-0003-END -->

<!-- SOURCE-ACTIVITY-0011-START -->
[Intra-position instruction activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0011.md)
<!-- SOURCE-ACTIVITY-0011-END -->

<!-- SOURCE-ACTIVITY-0022-START -->
[Intra-position instruction status processes — source activity/communication diagram](../diagrams/settlement-activities/fig-0022.md)
<!-- SOURCE-ACTIVITY-0022-END -->
