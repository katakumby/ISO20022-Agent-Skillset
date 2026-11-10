---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Portfolio transfer"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
flow_id: "flow-settlement-reconciliation-portfolio-transfer"
participant_ids: ["participant-settlement-reconciliation-executing-servicing-party", "participant-settlement-reconciliation-portfolio-settlement-third-party", "participant-settlement-reconciliation-portfolio-transfer-client"]
message_ids: ["sese.023.001.13", "sese.037.001.09"]
limitations: ["The source uses generic PortfolioTransfer and SecuritiesSettlementInstruction labels. It does not label the middle Third Party as the client; the client is separately required by the activity narrative. The delivering/receiving detail labels and settlement directions are retained exactly rather than inferred from the left/right lifeline position.", "Unreviewed source reconstructions and full source coverage remain visible in the coverage inventory."]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P627", "heading_path": ["BusinessTransactions", "Portfolio Transfer"], "xml_path": "/w:document/w:body/w:p[627]"}, {"source_id": "src-000196", "paragraph_id": "P628", "heading_path": ["BusinessTransactions", "Portfolio Transfer"], "xml_path": "/w:document/w:body/w:p[628]"}, {"source_id": "src-000196", "paragraph_id": "P629", "heading_path": ["BusinessTransactions", "Portfolio Transfer"], "xml_path": "/w:document/w:body/w:p[629]"}, {"source_id": "src-000196", "paragraph_id": "P630", "heading_path": ["BusinessTransactions", "Portfolio Transfer"], "xml_path": "/w:document/w:body/w:p[630]"}]
diagram_ids: ["fig-0036", "fig-0072"]
---

# Portfolio transfer

## Purpose and boundaries

Exchange settlement details for full or partial client portfolio transfer.

**Trigger:** Client intends to move some or all positions to another custodian.

**Preconditions:** No formal precondition list is stated in §5.15/§6.15.

**Outcome/postconditions:** After reconciliation without breaks, receiving custodian instructs receives-free and delivering custodian instructs deliveries-free to CSD.

**Evidence:** [src-000196](<../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx>), §5.15 table48; §6.15 paragraphs628–630.

## Participants

- [portfolio transfer client](<../../../../../../../shared/reference/participants/settlement-reconciliation-portfolio-transfer-client.md>)
- [executing servicing party](<../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md>)

## Activities, decisions and alternatives

Client advises both custodians. Custodians process request, exchange details and reconcile them. Breaks lead to client investigation and potentially an updated move. Sequence highlights only two servicing parties; narrative/table also include client and instructions to CSD. Delivering custodian may include a receiving settlement chain for validation; if unavailable, receiving custodian can return it in same message type.

- [Complete source table 48](<../documents/src-000196/tables/tbl-0048.md>) — §5.15 table48; §6.15 paragraphs628–630.

## Messages and navigation

- [sese.037.001.09](<../../../../messages/sese.037.001.09/index.md>)
- [sese.023.001.13](<../../../../messages/sese.023.001.13/index.md>)

[Participant index](<../participants.md>) · [Flow index](<index.md>)

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Portfolio transfer settlement details](../diagrams/settlement-sequences/fig-0072.md)

src-000196 P627–P631.

### Participants in this source sequence

- A — Executing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)
- B — Third Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-portfolio-settlement-third-party.md)
- C — Executing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P627** — Portfolio Transfer

**src-000196 P628** — This diagram shows the messages flow between two executing/servicing parties that exchange settlement details information during a retail or institutional client portfolio transfer.

**src-000196 P629** — By exchange of transfer settlement details, it is understood the providing of, by the delivering account servicer to the receiving account servicer, the settlement details (for example, trade date, settlement date, delivering settlement chain, quantities) of the individual transfers that will take place during a full or partial portfolio transfer.

**src-000196 P630** — This delivering account servicer message may also include, for validation, the receiving settlement chain as provided by the client. In case the receiving settlement chain is not available to the delivering account servicer, the receiving account servicer may in return provide to the delivering account servicer the receiving settlement chain using the same message.

### Source activity responsibilities

[Activity table T48 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0048.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

### Source-specific qualifications

- The source uses generic PortfolioTransfer and SecuritiesSettlementInstruction labels. It does not label the middle Third Party as the client; the client is separately required by the activity narrative. The delivering/receiving detail labels and settlement directions are retained exactly rather than inferred from the left/right lifeline position.

<!-- SETTLEMENT-SEQUENCE-END -->


<!-- SOURCE-ACTIVITY-0036-START -->
[Portfolio transfer activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0036.md)
<!-- SOURCE-ACTIVITY-0036-END -->
