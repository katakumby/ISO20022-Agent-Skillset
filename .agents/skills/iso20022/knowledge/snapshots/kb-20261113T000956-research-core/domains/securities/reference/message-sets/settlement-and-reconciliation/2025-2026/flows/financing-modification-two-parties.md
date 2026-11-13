---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Financing modification without position change — two parties"
flow_id: "flow-settlement-reconciliation-financing-modification-two-parties"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P378", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[378]"}, {"source_id": "src-000196", "paragraph_id": "P379", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[379]"}, {"source_id": "src-000196", "paragraph_id": "P380", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[380]"}, {"source_id": "src-000196", "paragraph_id": "P381", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[381]"}]
message_ids: ["sese.034.001.11", "sese.036.001.10"]
participant_ids: ["participant-settlement-reconciliation-financing-instructing-party", "participant-settlement-reconciliation-financing-servicing-settlement-executing-party"]
diagram_ids: ["fig-0016", "fig-0043"]
updated: "2026-11-09"
limitations: ["The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---

# Financing modification without position change — two parties

## Purpose, trigger and boundaries

The source-defined scenario is **Financing modification without position change — two parties**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Financing modification without position change — two parties](../diagrams/settlement-sequences/fig-0043.md)

src-000196 P378–P382.

### Participants in this source sequence

- A — Securities Financing Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-instructing-party.md)
- B — Securities Financing Servicing Party/Settlement Executing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-servicing-settlement-executing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P378** — Two Parties

**src-000196 P379** — This diagram shows the messages flow between the securities financing instructing party and the securities financing servicing party/settlement executing party.

**src-000196 P380** — The Securities Financing Instructing party (a broker for example) sends a SecuritiesFinancingModificationInstruction to the securities financing servicing party/settlement executing party (a sub-custodian) to modify the rate of a repo for instance on the closing leg.

**src-000196 P381** — The securities financing servicing party/settlement executing party may send a processing and/or settlement or matching status for the instruction to the securities financing instructing party with a SecuritiesFinancingStatusAdvice.

### Source activity responsibilities

[Activity table T34 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0034.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

<!-- SETTLEMENT-SEQUENCE-END -->




<!-- SOURCE-ACTIVITY-0016-START -->
[Financing modification activity — two parties — source activity/communication diagram](../diagrams/settlement-activities/fig-0016.md)
<!-- SOURCE-ACTIVITY-0016-END -->
