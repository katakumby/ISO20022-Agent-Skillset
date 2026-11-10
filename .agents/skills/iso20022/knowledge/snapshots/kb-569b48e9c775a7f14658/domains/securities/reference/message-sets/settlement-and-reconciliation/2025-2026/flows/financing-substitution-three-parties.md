---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Financing substitution — three parties"
flow_id: "flow-settlement-reconciliation-financing-substitution-three-parties"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P383", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[383]"}, {"source_id": "src-000196", "paragraph_id": "P384", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[384]"}, {"source_id": "src-000196", "paragraph_id": "P385", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[385]"}, {"source_id": "src-000196", "paragraph_id": "P386", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[386]"}, {"source_id": "src-000196", "paragraph_id": "P387", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[387]"}, {"source_id": "src-000196", "paragraph_id": "P388", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[388]"}, {"source_id": "src-000196", "paragraph_id": "P389", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[389]"}, {"source_id": "src-000196", "paragraph_id": "P390", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[390]"}, {"source_id": "src-000196", "paragraph_id": "P391", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[391]"}, {"source_id": "src-000196", "paragraph_id": "P392", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[392]"}, {"source_id": "src-000196", "paragraph_id": "P393", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[393]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.025.001.13", "sese.034.001.11"]
participant_ids: ["participant-settlement-reconciliation-financing-instructing-party", "participant-settlement-reconciliation-financing-servicing-party", "participant-settlement-reconciliation-settlement-executing-party"]
diagram_ids: ["fig-0044"]
updated: "2026-11-09"
limitations: ["The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---





# Financing substitution — three parties

## Purpose, trigger and boundaries

The source-defined scenario is **Financing substitution — three parties**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Financing substitution — three parties](../diagrams/settlement-sequences/fig-0044.md)

src-000196 P383–P394.

### Participants in this source sequence

- A — Securities Financing Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-instructing-party.md)
- B — Securities Financing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-servicing-party.md)
- C — Settlement Executing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-settlement-executing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P383** — Changes That Do Impact the Securities Position

**src-000196 P384** — This refers to the substitution, top up and withdrawal flows that per SMPG current market practice are considered as simple position movements for which settlement instructions are used. Despite the scenarios will cover pure settlement movements, upon settlement of the change of positions not only a SecuritiesSettlementTransactionConfirmation will be sent out but also a Securities Financing Status Advice to advise of the position change impacting the securities financing transaction.

**src-000196 P385** — Three Parties

**src-000196 P386** — A – Substitution

**src-000196 P387** — The securities financing instructing party (a broker) sends two SecuritiesSettlementTransactionInstruction (receipt free and deliver free) to the Securities Financing servicing party (a custodian) to substitute the quantity of securities A with securities B.

**src-000196 P388** — The securities financing servicing party in turn sends two SecuritiesSettlementTransactionInstruction (receipt free and deliver free) to the settlement executing party (a CSD).

**src-000196 P389** — The settlement executing party may send a status on the receipt and the delivery to the securities financing servicing party with two SecuritiesSettlementTransactionStatusAdvice.

**src-000196 P390** — The securities financing servicing party may in turn send a status on the receipt and the delivery to the securities financing instructing party with two SecuritiesSettlementTransactionStatusAdvice.

**src-000196 P391** — When the substitution is completed, the settlement executing party sends two SecuritiesSettlementTransactionConfirmation for the receipt and the delivery to the securities financing servicing party.

**src-000196 P392** — The securities financing servicing party in turn sends two SecuritiesSettlementTransactionConfirmation for the receipt and the delivery to the securities financing instructing party .

**src-000196 P393** — The securities financing servicing party will also send a SecuritiesFinancingStatusAdvice to the securities financing instructing party to advise of the position change impacting the securities financing transaction.

<!-- SETTLEMENT-SEQUENCE-END -->
