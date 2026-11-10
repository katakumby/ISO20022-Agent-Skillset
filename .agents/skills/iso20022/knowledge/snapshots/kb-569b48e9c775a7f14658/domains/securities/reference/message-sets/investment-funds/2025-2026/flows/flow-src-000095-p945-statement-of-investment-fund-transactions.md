---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p945-statement-of-investment-fund-transactions"
title: "Investment fund transaction statement"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P916", "heading_path": ["BusinessTransactions", "Statements"], "xml_path": "/w:document/w:body/w:p[916]"}, {"source_id": "src-000095", "paragraph_id": "P917", "heading_path": ["BusinessTransactions", "Statements"], "xml_path": "/w:document/w:body/w:p[917]"}, {"source_id": "src-000095", "paragraph_id": "P918", "heading_path": ["BusinessTransactions", "Statements"], "xml_path": "/w:document/w:body/w:p[918]"}, {"source_id": "src-000095", "paragraph_id": "P946", "heading_path": ["BusinessTransactions", "Statements", "Transaction Statement ", "Statement of Investment Fund Transactions"], "xml_path": "/w:document/w:body/w:p[946]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P947", "heading_path": ["BusinessTransactions", "Statements", "Transaction Statement ", "Statement of Investment Fund Transactions"], "xml_path": "/w:document/w:body/w:p[947]", "figure_id": "fig-0139"}]
participants: []
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Statement"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[6]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000096", "locator": "file page 408; 22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02"}]
message_ids: ["semt.006.001.02"]
message_families: ["semt.006"]
search_terms: ["Statement of Investment Fund Transactions", "semt.006"]
limitations: ["The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-account-owner", "participant-src-000095-account-servicer", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0139.md"]
updated: "2026-11-09"
---

# Investment fund transaction statement

## Purpose, trigger and outcome

Provide the account owner with an investment fund transaction statement.

**Trigger:** Statement delivery is typically governed by the parties’ SLA.

**Source-defined outcome:** The account servicer sends StatementOfInvestmentFundTransactions.

These statements are grounded in src-000095 P946–P946. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md)
- [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Account Servicer | Account Owner | StatementOfInvestmentFundTransactions |


## Ordered narrative, conditions and alternatives

**src-000095 P946** — An account servicer sends an StatementOfInvestmentFundTransactions message to the account owner.

### Common source context

**src-000095 P916** — This message flow section illustrates the use of the statement messages in typical message sequencing scenarios. The statement messages are sent by an account servicer to the account owner. 

**src-000095 P917** — Typically, a statement is sent according to the Service Level Agreement (SLA) held between the account servicer and the account owner. This SLA sets the parameters around the frequency at which the statement message is sent, for example, daily, weekly, intra-day.

**src-000095 P918** — The account owner is, for example, an investment manager or its authorised representative. The account servicer is, for example, a transfer agent.

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| StatementOfInvestmentFundTransactions | [semt.006.001.02](../../../../messages/semt.006.001.02/index.md) | src-000096 file page 408; 22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0139.md)

- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
