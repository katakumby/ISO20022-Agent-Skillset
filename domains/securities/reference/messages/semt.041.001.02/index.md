---
template: false
document_kind: "message-index"
review_status: "needs-review"
manual_curated: true
title: "SecuritiesBalanceTransparencyReport"
message_id: "semt.041.001.02"
message_family: "semt.041"
business_area: "semt"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
documentation_status: "business-examples-only"
schema_status: "not-supplied"
namespace: null
source_locations: [{"source_id": "src-000095", "paragraph_id": "P941", "heading_path": ["BusinessTransactions", "Statements", "Transparency of Holdings Statement "], "xml_path": "/w:document/w:body/w:p[941]"}, {"source_id": "src-000095", "paragraph_id": "P942", "heading_path": ["BusinessTransactions", "Statements", "Transparency of Holdings Statement "], "xml_path": "/w:document/w:body/w:p[942]"}, {"source_id": "src-000095", "paragraph_id": "P5806", "heading_path": ["Business Examples", "Transparency Of Holdings"], "xml_path": "/w:document/w:body/w:p[5806]"}, {"source_id": "src-000095", "paragraph_id": "P5807", "heading_path": ["Business Examples", "Transparency Of Holdings"], "xml_path": "/w:document/w:body/w:p[5807]"}, {"source_id": "src-000095", "paragraph_id": "P5808", "heading_path": ["Business Examples", "Transparency Of Holdings"], "xml_path": "/w:document/w:body/w:p[5808]"}, {"source_id": "src-000095", "paragraph_id": "P5809", "heading_path": ["Business Examples", "Transparency Of Holdings"], "xml_path": "/w:document/w:body/w:p[5809]"}, {"source_id": "src-000095", "paragraph_id": "P5810", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 - 1"], "xml_path": "/w:document/w:body/w:p[5810]"}, {"source_id": "src-000095", "paragraph_id": "P5811", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 - 1"], "xml_path": "/w:document/w:body/w:p[5811]"}, {"source_id": "src-000095", "paragraph_id": "P5812", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 - 1"], "xml_path": "/w:document/w:body/w:p[5812]"}]
limitations: ["The supplied Part1 explicitly prints this exact identifier, but no corresponding supplied XSD or Part2 definition has been located. See issue-000042.", "Source examples establish specific illustrated content and directions; they do not establish complete schema structure or all business rules."]
updated: "2026-11-09"
participant_ids: ["participant-src-000095-account-servicer", "participant-src-000095-receiving-party-all-levels", "participant-src-000095-example-cusa", "participant-src-000095-example-cusb", "participant-src-000095-example-cusc", "participant-src-000095-example-icsd", "participant-src-000095-example-trag"]
flow_ids: ["flow-src-000095-transparency-example-1", "flow-src-000095-transparency-example-2"]
---

# SecuritiesBalanceTransparencyReport — semt.041.001.02

This exact identifier is explicitly documented in the supplied Investment Funds Part1 business-example headings. **No matching supplied XSD or exact Part2 definition is available.** This reference therefore preserves business-example evidence without claiming complete schema coverage.

## Purpose, roles and usage evidence

**src-000095 P941** — An account servicer, such as a custodian, sends the SecuritiesBalanceTransparencyReport statement message to a receiver, who in turn, may enrich it with data of its own and send the aggregated statement onward in the custody chain. 

**src-000095 P942** — The receiver of the message responds with the SecuritiesBalanceTransparencyReportStatusAdvice message to accept or reject the statement of holdings as presented in the aggregated statement.

**src-000095 P5806** — Transparency Of Holdings

**src-000095 P5807** — This diagram shows a structural overview of the Securities Balance Transparency Report message:

**src-000095 P5810** — SecuritiesBalanceTransparencyReport semt.041.001.02 - 1

**src-000095 P5811** — This diagram shows the flow of messages for the scenario illustrated by the business examples:

## Complete source instance tables

- [T61 — preserved message data and comments](../../message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0061.md)
- [T62 — preserved message data and comments](../../message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0062.md)
- [T63 — preserved message data and comments](../../message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0063.md)
- [T64 — preserved message data and comments](../../message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0064.md)

## Flows and diagrams

[Transparency reporting and acceptance/rejection sequence](../../message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0138.md)

- [Business example 1](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-transparency-example-1.md)
- [Business example 2](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-transparency-example-2.md)

[Structural overview and example diagrams](../../message-sets/investment-funds/2025-2026/diagrams/funds-transparency/index.md)

## Availability and unresolved gaps

Namespace, complete field/type references, validation facets and normative rule coverage cannot be established from these business examples alone. [issue-000042 — missing schema and exact Part2 definition](../../../../../tracking/issues.md); [issue-000040 — transparency example contradictions](../../../../../tracking/issues.md).

## Original source and canonical participants

[src-000095](../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx)

- [Account Servicer](../../../../../shared/reference/participants/participant-src-000095-account-servicer.md)
- [Receiving Party (all levels)](../../../../../shared/reference/participants/participant-src-000095-receiving-party-all-levels.md)
- [CUSA — transparency business example](../../../../../shared/reference/participants/participant-src-000095-example-cusa.md)
- [CUSB — transparency business example](../../../../../shared/reference/participants/participant-src-000095-example-cusb.md)
- [CUSC — transparency business example](../../../../../shared/reference/participants/participant-src-000095-example-cusc.md)
- [ICSD — transparency business example](../../../../../shared/reference/participants/participant-src-000095-example-icsd.md)
- [TRAG — transparency business example](../../../../../shared/reference/participants/participant-src-000095-example-trag.md)

- [Transparency of holdings — supplied business example 1](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-transparency-example-1.md)
- [Transparency of holdings — supplied business example 2](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-transparency-example-2.md)
