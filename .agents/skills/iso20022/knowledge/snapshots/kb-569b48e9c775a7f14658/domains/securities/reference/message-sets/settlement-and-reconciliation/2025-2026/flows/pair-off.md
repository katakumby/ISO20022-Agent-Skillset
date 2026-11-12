---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Pair-off instruction sequence"
flow_id: "flow-settlement-reconciliation-pair-off"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P435", "heading_path": ["BusinessTransactions", "Pair-Off Instruction"], "xml_path": "/w:document/w:body/w:p[435]"}, {"source_id": "src-000196", "paragraph_id": "P436", "heading_path": ["BusinessTransactions", "Pair-Off Instruction"], "xml_path": "/w:document/w:body/w:p[436]"}, {"source_id": "src-000196", "paragraph_id": "P437", "heading_path": ["BusinessTransactions", "Pair-Off Instruction"], "xml_path": "/w:document/w:body/w:p[437]"}, {"source_id": "src-000196", "paragraph_id": "P438", "heading_path": ["BusinessTransactions", "Pair-Off Instruction"], "xml_path": "/w:document/w:body/w:p[438]"}, {"source_id": "src-000196", "paragraph_id": "P439", "heading_path": ["BusinessTransactions", "Pair-Off Instruction"], "xml_path": "/w:document/w:body/w:p[439]"}, {"source_id": "src-000196", "paragraph_id": "P440", "heading_path": ["BusinessTransactions", "Pair-Off Instruction"], "xml_path": "/w:document/w:body/w:p[440]"}, {"source_id": "src-000196", "paragraph_id": "P441", "heading_path": ["BusinessTransactions", "Pair-Off Instruction"], "xml_path": "/w:document/w:body/w:p[441]"}, {"source_id": "src-000196", "paragraph_id": "P442", "heading_path": ["BusinessTransactions", "Pair-Off Instruction"], "xml_path": "/w:document/w:body/w:p[442]"}, {"source_id": "src-000196", "paragraph_id": "P443", "heading_path": ["BusinessTransactions", "Pair-Off Instruction"], "xml_path": "/w:document/w:body/w:p[443]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14"]
participant_ids: ["participant-settlement-reconciliation-executing-servicing-party", "participant-settlement-reconciliation-instructing-party"]
diagram_ids: ["fig-0017", "fig-0050"]
updated: "2026-11-09"
limitations: ["The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative.", "“See payment messages” is a source cross-reference, not an exact supplied payment-message identifier. The narrative conditions the cash-difference step on successful cancellation and describes both payment directions; the picture shows only one generic arrow."]
---

# Pair-off instruction sequence

## Purpose, trigger and boundaries

The source-defined scenario is **Pair-off instruction sequence**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Pair-off instruction sequence](../diagrams/settlement-sequences/fig-0050.md)

src-000196 P435–P444.

### Participants in this source sequence

- A — Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- B — Executing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P435** — Pair-Off Instruction

**src-000196 P436** — This diagram shows the messages flow between the instructing party and the executing/servicing party.

**src-000196 P437** — A pair-off consists of a buyback to offset and effectively liquidate a prior sale of securities or a sellback to offset and effectively liquidate a prior buy of securities.

**src-000196 P438** — An instructing party (for example and investment manager or a broker) sends a SecuritiesSettlementTransactionInstruction to the executing/servicing party (a global custodian).

**src-000196 P439** — The executing/servicing party may send back to the instructing party a processing status and/or a settlement status referring to the state of the transaction.

**src-000196 P440** — The instructing party sends the pair-off instruction for the previously sent instruction.

**src-000196 P441** — The executing/servicing party may send back to the instructing party a processing status and/or a settlement status referring to the state of the pair-off transaction.

**src-000196 P442** — The next potential step can be to cancel the paired-off instruction. This is linked to the matching/settlement process as the capacity to cancel or not will depend on the matching and the settlement status of the transactions to be cancelled.

**src-000196 P443** — Providing it was possible to cancel the transaction to be paired-off, the executing/servicing party will wire the cash difference (if net loss) or wait for the cash difference to be wired by the counterparty (in case of net gain).

### Source activity responsibilities

[Activity table T35 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0035.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

### Source-specific qualifications

- “See payment messages” is a source cross-reference, not an exact supplied payment-message identifier. The narrative conditions the cash-difference step on successful cancellation and describes both payment directions; the picture shows only one generic arrow.

<!-- SETTLEMENT-SEQUENCE-END -->




<!-- SOURCE-ACTIVITY-0017-START -->
[Pair-off activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0017.md)
<!-- SOURCE-ACTIVITY-0017-END -->
