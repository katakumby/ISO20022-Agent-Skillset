---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Financing withdrawal — two parties"
flow_id: "flow-settlement-reconciliation-financing-withdrawal-two-parties"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P429", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[429]"}, {"source_id": "src-000196", "paragraph_id": "P430", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[430]"}, {"source_id": "src-000196", "paragraph_id": "P431", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[431]"}, {"source_id": "src-000196", "paragraph_id": "P432", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[432]"}, {"source_id": "src-000196", "paragraph_id": "P433", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[433]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.025.001.13", "sese.034.001.11"]
participant_ids: ["participant-settlement-reconciliation-financing-instructing-party", "participant-settlement-reconciliation-financing-servicing-settlement-executing-party"]
diagram_ids: ["fig-0049"]
updated: "2026-11-09"
limitations: ["The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---





# Financing withdrawal — two parties

## Purpose, trigger and boundaries

The source-defined scenario is **Financing withdrawal — two parties**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Financing withdrawal — two parties](../diagrams/settlement-sequences/fig-0049.md)

src-000196 P429–P434.

### Participants in this source sequence

- A — Securities Financing Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-instructing-party.md)
- B — Securities Financing Servicing Party/Settlement Executing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-servicing-settlement-executing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P429** — C – Withdrawal

**src-000196 P430** — The securities financing instructing party (a broker) sends a SecuritiesSettlementTransactionInstruction (receipt free) to the securities financing servicing party/settlement executing party (a sub-custodian) to decrease the quantity of securities that serve as collateral.

**src-000196 P431** — The securities financing servicing party/settlement executing party may send a status on the receipt to the securities financing instructing party with a SecuritiesSettlementTransactionStatusAdvice.

**src-000196 P432** — When the withdrawal is completed, the securities financing servicing party/settlement executing party sends a SecuritiesSettlementTransactionConfirmation for the receipt, to the securities financing instructing party.

**src-000196 P433** — The securities financing servicing party/settlement executing party will also send a SecuritiesFinancingStatusAdvice to the securities financing instructing party to advise of the position change impacting the securities financing transaction.

<!-- SETTLEMENT-SEQUENCE-END -->
