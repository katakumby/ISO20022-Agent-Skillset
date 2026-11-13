---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Financing withdrawal — three parties"
flow_id: "flow-settlement-reconciliation-financing-withdrawal-three-parties"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P404", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[404]"}, {"source_id": "src-000196", "paragraph_id": "P405", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[405]"}, {"source_id": "src-000196", "paragraph_id": "P406", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[406]"}, {"source_id": "src-000196", "paragraph_id": "P407", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[407]"}, {"source_id": "src-000196", "paragraph_id": "P408", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[408]"}, {"source_id": "src-000196", "paragraph_id": "P409", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[409]"}, {"source_id": "src-000196", "paragraph_id": "P410", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[410]"}, {"source_id": "src-000196", "paragraph_id": "P411", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[411]"}, {"source_id": "src-000196", "paragraph_id": "P412", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[412]"}, {"source_id": "src-000196", "paragraph_id": "P413", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"], "xml_path": "/w:document/w:body/w:p[413]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.025.001.13", "sese.034.001.11"]
participant_ids: ["participant-settlement-reconciliation-financing-instructing-party", "participant-settlement-reconciliation-financing-servicing-party", "participant-settlement-reconciliation-settlement-executing-party"]
diagram_ids: ["fig-0046"]
updated: "2026-11-09"
limitations: ["The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---





# Financing withdrawal — three parties

## Purpose, trigger and boundaries

The source-defined scenario is **Financing withdrawal — three parties**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Financing withdrawal — three parties](../diagrams/settlement-sequences/fig-0046.md)

src-000196 P404–P414.

### Participants in this source sequence

- A — Securities Financing Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-instructing-party.md)
- B — Securities Financing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-servicing-party.md)
- C — Settlement Executing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-settlement-executing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P404** — C – Withdrawal

**src-000196 P405** — The securities financing instructing party (a broker) sends a SecuritiesSettlementTransactionInstruction (receipt free) to the securities financing servicing party (a custodian) to decrease the quantity of securities that serves as collateral.

**src-000196 P406** — The securities financing servicing party in turn sends a SecuritiesSettlementTransactionInstruction (receipt free) to the settlement executing party (a CSD).

**src-000196 P407** — The settlement executing party may send a status on the receipt to the Securities Financing servicing party with a

**src-000196 P408** — SecuritiesSettlementTransactionStatusAdvice.

**src-000196 P409** — The securities financing servicing party may in turn send a status on the receipt to the securities financing instructing party with a SecuritiesSettlementTransactionStatusAdvice.

**src-000196 P410** — When the withdrawal is completed, the settlement executing party sends a

**src-000196 P411** — SecuritiesSettlementTransactionConfirmation for the receipt to the securities financing servicing party.

**src-000196 P412** — The securities financing servicing party in turn sends a SecuritiesSettlementTransactionConfirmation for the receipt to the securities financing instructing party.

**src-000196 P413** — The securities financing servicing party will also send a SecuritiesFinancingStatusAdvice to the securities financing instructing party to advise of the position change impacting the securities financing transaction.

<!-- SETTLEMENT-SEQUENCE-END -->
