---
template: false
document_kind: "participant"
review_status: "needs-review"
participant_id: "participant-settlement-reconciliation-portfolio-settlement-third-party"
title: "Third Party — portfolio settlement diagram"
domain: "securities"
domains: ["securities"]
source_ids: ["src-000196"]
source_labels: ["Third Party"]
aliases: []
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P627", "heading_path": ["BusinessTransactions", "Portfolio Transfer"], "xml_path": "/w:document/w:body/w:p[627]"}, {"source_id": "src-000196", "paragraph_id": "P628", "heading_path": ["BusinessTransactions", "Portfolio Transfer"], "xml_path": "/w:document/w:body/w:p[628]"}, {"source_id": "src-000196", "paragraph_id": "P629", "heading_path": ["BusinessTransactions", "Portfolio Transfer"], "xml_path": "/w:document/w:body/w:p[629]"}, {"source_id": "src-000196", "paragraph_id": "P630", "heading_path": ["BusinessTransactions", "Portfolio Transfer"], "xml_path": "/w:document/w:body/w:p[630]"}]
message_ids: []
flow_ids: ["flow-settlement-reconciliation-portfolio-transfer"]
role_kind: "functional participant role"
updated: "2026-11-09"
limitations: ["This definition is scoped to the cited scenarios. Institution examples do not define or fix the role.", "No identifier scheme is specified in these source paragraphs."]
source_editions: ["March 2026"]
---

# Third Party — portfolio settlement diagram

## Definition and context

Source diagram fig-0072 identifies a Third Party receiving Delivery free and Receipt free settlement instructions. The figure supplies no independent definition or identifier scheme for this label.

[src-000196](../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md); P627, P628, P629, P630.

## Responsibilities, relationships and evidence

**src-000196 P627** — Portfolio Transfer

**src-000196 P628** — This diagram shows the messages flow between two executing/servicing parties that exchange settlement details information during a retail or institutional client portfolio transfer.

**src-000196 P629** — By exchange of transfer settlement details, it is understood the providing of, by the delivering account servicer to the receiving account servicer, the settlement details (for example, trade date, settlement date, delivering settlement chain, quantities) of the individual transfers that will take place during a full or partial portfolio transfer.

**src-000196 P630** — This delivering account servicer message may also include, for validation, the receiving settlement chain as provided by the client. In case the receiving settlement chain is not available to the delivering account servicer, the receiving account servicer may in return provide to the delivering account servicer the receiving settlement chain using the same message.

## Applicable flows

- [Portfolio transfer settlement details](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/portfolio-transfer.md)

## Identifier schemes and ambiguity

No identifier scheme is specified in the cited role narrative. The source examples do not make this role identical to a particular institution. A compound participant in a two-party scenario does not merge the separate three-party role definitions.

The middle diagram lifeline is not equated with the portfolio client or the reporting Third Party. The activity narrative separately names the client and CSD; the figure itself only supplies the label Third Party.

<!-- SETTLEMENT-FLOW-LINKS-START -->
## Additional source-scoped settlement flows

- [Portfolio transfer settlement details](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/portfolio-transfer.md)
<!-- SETTLEMENT-FLOW-LINKS-END -->


<!-- SOURCE196-DIAGRAM-72-START -->
[Portfolio transfer settlement details](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/fig-0072.md) — src-000196 direct-body paragraph P631.
<!-- SOURCE196-DIAGRAM-72-END -->
