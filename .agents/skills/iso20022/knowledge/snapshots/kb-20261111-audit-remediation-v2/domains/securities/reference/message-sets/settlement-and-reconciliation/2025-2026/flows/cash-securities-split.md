---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Cash/securities split instruction and confirmation"
flow_id: "flow-settlement-reconciliation-cash-securities-split"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P445", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[445]"}, {"source_id": "src-000196", "paragraph_id": "P446", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[446]"}, {"source_id": "src-000196", "paragraph_id": "P447", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[447]"}, {"source_id": "src-000196", "paragraph_id": "P448", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[448]"}, {"source_id": "src-000196", "paragraph_id": "P449", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[449]"}, {"source_id": "src-000196", "paragraph_id": "P450", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[450]"}, {"source_id": "src-000196", "paragraph_id": "P451", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[451]"}, {"source_id": "src-000196", "paragraph_id": "P452", "heading_path": ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[452]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.025.001.13"]
participant_ids: ["participant-settlement-reconciliation-cash-leg-executing-party", "participant-settlement-reconciliation-cash-securities-split-servicing-party", "participant-settlement-reconciliation-instructing-party", "participant-settlement-reconciliation-securities-leg-executing-party"]
diagram_ids: ["fig-0018", "fig-0051"]
updated: "2026-11-09"
limitations: ["CashTransfer/CashAdvice, ConfirmCashTransfer and ConfirmCash are retained as source labels. No particular payment schema is inferred from them.", "The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---

# Cash/securities split instruction and confirmation

## Purpose, trigger and boundaries

The source-defined scenario is **Cash/securities split instruction and confirmation**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Cash/securities split instruction and confirmation](../diagrams/settlement-sequences/fig-0051.md)

src-000196 P445–P453.

### Participants in this source sequence

- A — Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- B — Securities/Cash Instruction Executing/Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-cash-securities-split-servicing-party.md)
- C — Securities Leg Executing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-securities-leg-executing-party.md)
- D — Cash Leg Executing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-cash-leg-executing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P445** — Cash/Securities Split Instruction and Confirmation

**src-000196 P446** — This sequence diagram reports the messages flow between the instructing party, the securities/cash instruction executing/servicing party, the securities leg executing party and the cash leg executing party.

**src-000196 P447** — An instructing party (for example an investment manager), sends a SecuritiesSettlementTransactionInstruction (receive or delivery versus payment) to the securities/cash instruction executing/servicing party (a Global Custodian).

**src-000196 P448** — The securities/cash instruction executing/servicing party in turn sends a SecuritiesSettlementTransactionInstruction (receive or deliver free) to the securities leg executing party and a cash transfer to the cash leg executing party.

**src-000196 P449** — The securities leg executing party may send to the securities/cash instruction executing/servicing party a processing status and/or a settlement status referring to the state of the transaction. The later will then pass the information on to the instructing party.

**src-000196 P450** — When the transaction settles at the securities leg executing party, then this latter sends a

**src-000196 P451** — SecuritiesSettlementTransactionConfirmation to advise the securities/cash instruction executing/servicing party that the settlement has taken place. The securities/cash instruction executing/servicing party will then relay the information to the instructing party.

**src-000196 P452** — When the cash transfer takes place at the cash leg executing party, then this latter sends a security cash transfer confirmation to advise the securities/cash instruction executing/servicing party that the cash is transferred. The securities/cash instruction executing/servicing party will then relay the information to the instructing party.

### Source activity responsibilities

[Activity table T36 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0036.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

### Source-specific qualifications

- CashTransfer/CashAdvice, ConfirmCashTransfer and ConfirmCash are retained as source labels. No particular payment schema is inferred from them.

<!-- SETTLEMENT-SEQUENCE-END -->




<!-- SOURCE-ACTIVITY-0018-START -->
[Cash/securities split activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0018.md)
<!-- SOURCE-ACTIVITY-0018-END -->
