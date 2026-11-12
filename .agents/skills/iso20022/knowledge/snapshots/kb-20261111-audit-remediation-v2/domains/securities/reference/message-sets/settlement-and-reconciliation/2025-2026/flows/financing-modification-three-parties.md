---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Financing modification without position change — three parties"
flow_id: "flow-settlement-reconciliation-financing-modification-three-parties"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P369", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[369]"}, {"source_id": "src-000196", "paragraph_id": "P370", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[370]"}, {"source_id": "src-000196", "paragraph_id": "P371", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[371]"}, {"source_id": "src-000196", "paragraph_id": "P372", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[372]"}, {"source_id": "src-000196", "paragraph_id": "P373", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[373]"}, {"source_id": "src-000196", "paragraph_id": "P374", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[374]"}, {"source_id": "src-000196", "paragraph_id": "P375", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[375]"}, {"source_id": "src-000196", "paragraph_id": "P376", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "], "xml_path": "/w:document/w:body/w:p[376]"}]
message_ids: ["sese.020.001.09", "sese.023.001.13", "sese.024.001.14", "sese.034.001.11", "sese.036.001.10"]
participant_ids: ["participant-settlement-reconciliation-financing-instructing-party", "participant-settlement-reconciliation-financing-servicing-party", "participant-settlement-reconciliation-settlement-executing-party"]
diagram_ids: ["fig-0015", "fig-0042"]
updated: "2026-11-09"
limitations: ["The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---

# Financing modification without position change — three parties

## Purpose, trigger and boundaries

The source-defined scenario is **Financing modification without position change — three parties**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Financing modification without position change — three parties](../diagrams/settlement-sequences/fig-0042.md)

src-000196 P369–P377.

### Participants in this source sequence

- A — Securities Financing Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-instructing-party.md)
- B — Securities Financing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-servicing-party.md)
- C — Settlement Executing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-settlement-executing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P369** — Changes That Do Not Impact the Securities Position 

**src-000196 P370** — This scenario applies to rate, date, amount, price closing leg changes not impacting the securities position, for example, repo call, repo rollover, repo rate change, securities lending return date change , etc... It illustrates the exchanges of messages between the Securities Financing Instruction Party, the Securities Financing Servicing Party and optionally the Settlement Executing party.

**src-000196 P371** — Three Parties

**src-000196 P372** — This diagram report the messages flow between the securities financing instructing party, the securities financing servicing party and the settlement executing party.

**src-000196 P373** — The securities financing Instructing party (a broker for example) sends a SecuritiesFinancingModificationInstruction to the securities financing servicing party (a custodian) to modify the rate of a repo for instance, on the closing leg.

**src-000196 P374** — The securities financing servicing party in turn sends a SecuritiesTransactionCancellationRequest to the settlement executing party (a CSD) and a new SecuritiesSettlementTransactionInstructing for the closing leg with the new rate.

**src-000196 P375** — The settlement executing party may send a processing and/or settlement or matching status to the securities financing servicing party with a SecuritiesSettlementStatusAdvice.

**src-000196 P376** — The securities financing servicing party may in turn send a processing and/or matching/settlement status to the securities financing instructing party with a SecuritiesFinancingStatusAdvice.

### Source activity responsibilities

[Activity table T33 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0033.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

<!-- SETTLEMENT-SEQUENCE-END -->




<!-- SOURCE-ACTIVITY-0015-START -->
[Financing modification activity — three parties — source activity/communication diagram](../diagrams/settlement-activities/fig-0015.md)
<!-- SOURCE-ACTIVITY-0015-END -->
