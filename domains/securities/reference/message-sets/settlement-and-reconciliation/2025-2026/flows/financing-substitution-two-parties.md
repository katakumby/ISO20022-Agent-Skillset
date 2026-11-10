---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Financing substitution — two parties"
flow_id: "flow-settlement-reconciliation-financing-substitution-two-parties"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P415", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[415]"}, {"source_id": "src-000196", "paragraph_id": "P416", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[416]"}, {"source_id": "src-000196", "paragraph_id": "P417", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[417]"}, {"source_id": "src-000196", "paragraph_id": "P418", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[418]"}, {"source_id": "src-000196", "paragraph_id": "P419", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[419]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.025.001.13", "sese.034.001.11"]
participant_ids: ["participant-settlement-reconciliation-financing-instructing-party", "participant-settlement-reconciliation-financing-servicing-settlement-executing-party"]
diagram_ids: ["fig-0047"]
updated: "2026-11-09"
limitations: ["The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---





# Financing substitution — two parties

## Purpose, trigger and boundaries

The source-defined scenario is **Financing substitution — two parties**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Financing substitution — two parties](../diagrams/settlement-sequences/fig-0047.md)

src-000196 P415–P420.

### Participants in this source sequence

- A — Securities Financing Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-instructing-party.md)
- B — Securities Financing Servicing Party/Settlement Executing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-servicing-settlement-executing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P415** — Two Parties

**src-000196 P416** — A – Substitution

**src-000196 P417** — The securities financing instructing party (a broker) sends two SecuritiesSettlementTransactionInstruction (receipt free and deliver free) to the securities financing servicing party/settlement executing party (a sub custodian) to substitute the a quantity of securities. The securities financing servicing party/settlement executing party may send a status on the receipt and the delivery to the securities financing instructing party with two SecuritiesSettlementTransactionStatusAdvice.

**src-000196 P418** — When the substitution is completed, the securities financing servicing party/settlement executing party sends two SecuritiesSettlementTransactionConfirmation for the receipt and the delivery to the securities financing instructing party.

**src-000196 P419** — The securities financing servicing party/settlement executing party will also send a SecuritiesFinancingStatusAdvice to the securities financing instructing party to advise of the position change impacting the securities financing transaction.

<!-- SETTLEMENT-SEQUENCE-END -->
