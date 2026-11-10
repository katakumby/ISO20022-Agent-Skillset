---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p904-price-report"
title: "Price report"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P901", "heading_path": ["BusinessTransactions", "Price Reporting"], "xml_path": "/w:document/w:body/w:p[901]"}, {"source_id": "src-000095", "paragraph_id": "P902", "heading_path": ["BusinessTransactions", "Price Reporting"], "xml_path": "/w:document/w:body/w:p[902]"}, {"source_id": "src-000095", "paragraph_id": "P903", "heading_path": ["BusinessTransactions", "Price Reporting"], "xml_path": "/w:document/w:body/w:p[903]"}, {"source_id": "src-000095", "paragraph_id": "P905", "heading_path": ["BusinessTransactions", "Price Reporting", "Price Report"], "xml_path": "/w:document/w:body/w:p[905]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P906", "heading_path": ["BusinessTransactions", "Price Reporting", "Price Report"], "xml_path": "/w:document/w:body/w:p[906]", "figure_id": "fig-0129"}]
participants: []
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Price Report "], "locator": "/w:document/w:body/w:tbl[14]/w:tr[2]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000096", "locator": "file page 159; 13 reda.001.001.05 PriceReportV05"}]
message_ids: ["reda.001.001.05"]
message_families: ["reda.001"]
search_terms: ["Price Report", "reda.001"]
limitations: ["The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-fund-accountant", "participant-src-000095-fund-management-company", "participant-src-000095-market-data-provider", "participant-src-000095-reporting-party", "participant-src-000095-requesting-party", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0129.md"]
updated: "2026-11-09"
---

# Price report

## Purpose, trigger and outcome

Provide a new price report to a report user.

**Trigger:** The report provider sends a PriceReport with Function NewPriceReport (NEWP).

**Source-defined outcome:** The report user receives the report and may forward it onward, although that next recipient is not drawn.

These statements are grounded in src-000095 P905–P905. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Report Provider](../../../../../../../shared/reference/participants/participant-src-000095-reporting-party.md)
- [Report User](../../../../../../../shared/reference/participants/participant-src-000095-requesting-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Report Provider | Report User | PriceReport |


## Ordered narrative, conditions and alternatives

**src-000095 P905** — A report provider sends a PriceReport message to the report user. The report user may, in turn, forward the PriceReport message. (Function is NewPriceReport, code NEWP.)

### Common source context

**src-000095 P901** — This message flow section illustrates the use of the price report messages in typical message sequencing scenarios. The price report messages are sent by a report provider to the report user.

**src-000095 P902** — The report provider is, for example, a fund accountant, transfer agent, market data provider, or any other interested party.

**src-000095 P903** — The report user is, for example, a fund management company, a transfer agent, market data provider, regulator or any other interested party.

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| PriceReport | [reda.001.001.05](../../../../messages/reda.001.001.05/index.md) | src-000096 file page 159; 13 reda.001.001.05 PriceReportV05 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0129.md)

- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Fund Accountant](../../../../../../../shared/reference/participants/participant-src-000095-fund-accountant.md)
- [Fund Management Company](../../../../../../../shared/reference/participants/participant-src-000095-fund-management-company.md)
- [Market Data Provider](../../../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
