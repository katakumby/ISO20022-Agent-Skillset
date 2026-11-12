---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p940-transparency-of-holdings-statement"
title: "Transparency holdings statement aggregation and status"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P916", "heading_path": ["BusinessTransactions", "Statements"], "xml_path": "/w:document/w:body/w:p[916]"}, {"source_id": "src-000095", "paragraph_id": "P917", "heading_path": ["BusinessTransactions", "Statements"], "xml_path": "/w:document/w:body/w:p[917]"}, {"source_id": "src-000095", "paragraph_id": "P918", "heading_path": ["BusinessTransactions", "Statements"], "xml_path": "/w:document/w:body/w:p[918]"}, {"source_id": "src-000095", "paragraph_id": "P941", "heading_path": ["BusinessTransactions", "Statements", "Transparency of Holdings Statement "], "xml_path": "/w:document/w:body/w:p[941]"}, {"source_id": "src-000095", "paragraph_id": "P942", "heading_path": ["BusinessTransactions", "Statements", "Transparency of Holdings Statement "], "xml_path": "/w:document/w:body/w:p[942]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P943", "heading_path": ["BusinessTransactions", "Statements", "Transparency of Holdings Statement "], "xml_path": "/w:document/w:body/w:p[943]", "figure_id": "fig-0138"}]
participants: ["participant-src-000095-custodian"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Statement"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[8]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Statement"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[9]", "paragraph_id": null, "table_id": "T16"}]
message_ids: []
message_families: ["semt.041", "semt.042"]
search_terms: ["Transparency of Holdings Statement", "Custodian", "semt.041", "semt.042"]
limitations: ["The picture explicitly names Sub-Level Account Owner, Omnibus Account Owner and Omnibus Account Servicer. P941 describes the initial sender as an account servicer such as a custodian. These contextual labels are preserved without assigning one institution a permanent owner/servicer role.", "The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-account-owner", "participant-src-000095-account-servicer", "participant-src-000095-custodian", "participant-src-000095-investment-manager", "participant-src-000095-omnibus-account-owner", "participant-src-000095-omnibus-account-servicer", "participant-src-000095-sub-level-account-owner", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0138.md"]
updated: "2026-11-09"
---

# Transparency holdings statement aggregation and status

## Purpose, trigger and outcome

Pass and optionally enrich an aggregated holdings statement along the custody chain, with acceptance or rejection status at each receiver.

**Trigger:** A participant sends SecuritiesBalanceTransparencyReport; the receiver may enrich it with its own data and forward the aggregated report.

**Source-defined outcome:** Each receiver responds with SecuritiesBalanceTransparencyReportStatusAdvice accepting or rejecting the holdings as presented.

These statements are grounded in src-000095 P941–P942. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Sub-Level Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-sub-level-account-owner.md)
- [Omnibus Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-omnibus-account-owner.md)
- [Omnibus Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-omnibus-account-servicer.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Sub-Level Account Owner | Omnibus Account Owner | SecuritiesBalanceTransparencyReport |
| 2 | Omnibus Account Owner | Sub-Level Account Owner | SecuritiesBalanceTransparencyReportStatusAdvice |
| 3 | Omnibus Account Owner | Omnibus Account Servicer | SecuritiesBalanceTransparencyReport |
| 4 | Omnibus Account Servicer | Omnibus Account Owner | SecuritiesBalanceTransparencyReportStatusAdvice |


## Ordered narrative, conditions and alternatives

**src-000095 P941** — An account servicer, such as a custodian, sends the SecuritiesBalanceTransparencyReport statement message to a receiver, who in turn, may enrich it with data of its own and send the aggregated statement onward in the custody chain. 

**src-000095 P942** — The receiver of the message responds with the SecuritiesBalanceTransparencyReportStatusAdvice message to accept or reject the statement of holdings as presented in the aggregated statement.

### Common source context

**src-000095 P916** — This message flow section illustrates the use of the statement messages in typical message sequencing scenarios. The statement messages are sent by an account servicer to the account owner. 

**src-000095 P917** — Typically, a statement is sent according to the Service Level Agreement (SLA) held between the account servicer and the account owner. This SLA sets the parameters around the frequency at which the statement message is sent, for example, daily, weekly, intra-day.

**src-000095 P918** — The account owner is, for example, an investment manager or its authorised representative. The account servicer is, for example, a transfer agent.

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0138.md)

- The picture explicitly names Sub-Level Account Owner, Omnibus Account Owner and Omnibus Account Servicer. P941 describes the initial sender as an account servicer such as a custodian. These contextual labels are preserved without assigning one institution a permanent owner/servicer role.
- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md)
- [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md)
- [Custodian](../../../../../../../shared/reference/participants/participant-src-000095-custodian.md)
- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
