---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Financing top-up — two parties"
flow_id: "flow-settlement-reconciliation-financing-top-up-two-parties"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P421", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[421]"}, {"source_id": "src-000196", "paragraph_id": "P422", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[422]"}, {"source_id": "src-000196", "paragraph_id": "P423", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[423]"}, {"source_id": "src-000196", "paragraph_id": "P424", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[424]"}, {"source_id": "src-000196", "paragraph_id": "P425", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[425]"}, {"source_id": "src-000196", "paragraph_id": "P426", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[426]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.025.001.13", "sese.034.001.11"]
participant_ids: ["participant-settlement-reconciliation-financing-instructing-party", "participant-settlement-reconciliation-financing-servicing-settlement-executing-party"]
diagram_ids: ["fig-0048"]
updated: "2026-11-09"
limitations: ["The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---





# Financing top-up — two parties

## Purpose, trigger and boundaries

The source-defined scenario is **Financing top-up — two parties**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Financing top-up — two parties](../diagrams/settlement-sequences/fig-0048.md)

src-000196 P421–P428.

### Participants in this source sequence

- A — Securities Financing Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-instructing-party.md)
- B — Securities Financing Servicing Party/Settlement Executing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-servicing-settlement-executing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P421** — B – Top Up

**src-000196 P422** — The securities financing instructing party (a broker) sends a SecuritiesSettlementTransactionInstruction (deliver free) to the securities financing servicing party/settlement executing party (a sub-custodian) to increase the quantity of securities that serves as collateral.

**src-000196 P423** — The securities financing servicing party/settlement executing party may send a status on the delivery to the securities financing instructing party with a SecuritiesSettlementTransactionStatusAdvice.

**src-000196 P424** — When the top up is completed, the securities financing servicing party/settlement executing party sends a

**src-000196 P425** — SecuritiesSettlementTransactionConfirmation for the delivery to the securities financing instructing party with a SecuritiesSettlementTransactionConfirmation.

**src-000196 P426** — The securities financing servicing party/settlement executing party will also send a SecuritiesFinancingStatusAdvice to the securities financing instructing party to advise of the position change impacting the securities financing transaction.

<!-- SETTLEMENT-SEQUENCE-END -->
