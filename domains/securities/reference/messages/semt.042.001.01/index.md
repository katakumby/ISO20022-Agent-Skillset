---
template: false
document_kind: "message-index"
review_status: "needs-review"
manual_curated: true
title: "SecuritiesBalanceTransparencyReportStatusAdvice"
message_id: "semt.042.001.01"
message_family: "semt.042"
business_area: "semt"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
documentation_status: "business-examples-only"
schema_status: "not-supplied"
namespace: null
source_locations: [{"source_id": "src-000095", "paragraph_id": "P5920", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReportStatusAdvice semt.042.001.01"], "xml_path": "/w:document/w:body/w:p[5920]"}, {"source_id": "src-000095", "paragraph_id": "P5921", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReportStatusAdvice semt.042.001.01"], "xml_path": "/w:document/w:body/w:p[5921]"}, {"source_id": "src-000095", "paragraph_id": "P5922", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReportStatusAdvice semt.042.001.01"], "xml_path": "/w:document/w:body/w:p[5922]"}, {"source_id": "src-000095", "paragraph_id": "P5923", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReportStatusAdvice semt.042.001.01"], "xml_path": "/w:document/w:body/w:p[5923]"}, {"source_id": "src-000095", "paragraph_id": "P5924", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReportStatusAdvice semt.042.001.01"], "xml_path": "/w:document/w:body/w:p[5924]"}, {"source_id": "src-000095", "paragraph_id": "P5925", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReportStatusAdvice semt.042.001.01"], "xml_path": "/w:document/w:body/w:p[5925]"}]
limitations: ["The supplied Part1 explicitly prints this exact identifier, but no corresponding supplied XSD or Part2 definition has been located. See issue-000042.", "Source examples establish specific illustrated content and directions; they do not establish complete schema structure or all business rules."]
updated: "2026-11-09"
participant_ids: ["participant-src-000095-example-icsd", "participant-src-000095-example-cusa"]
flow_ids: ["flow-src-000095-transparency-status-advice-example"]
---

# SecuritiesBalanceTransparencyReportStatusAdvice — semt.042.001.01

This exact identifier is explicitly documented in the supplied Investment Funds Part1 business-example headings. **No matching supplied XSD or exact Part2 definition is available.** This reference therefore preserves business-example evidence without claiming complete schema coverage.

## Purpose, roles and usage evidence

**src-000095 P5920** — SecuritiesBalanceTransparencyReportStatusAdvice semt.042.001.01

**src-000095 P5921** — Description

**src-000095 P5922** — ICSD (ICSDLULL) receives a SecuritiesBalanceTransparencyReport (semt.041) message from CUSA (CUSALULL). 

**src-000095 P5923** — Following processing, ICSD responds with a Securities Balance Transparency Report Status Advice (semt.042). 

**src-000095 P5924** — This status message provides details on the acceptance of a SecuritiesBalanceTransparencyReport message with statement identification OH_1023 which provide details of three holdings.

**src-000095 P5925** — The status message specifies that the holdings in the original SecuritiesBalanceTransparencyReport message are rejected because the ISIN of the financial instrument is invalid. The general details are still valid, so the status is accepted with exception.

## Complete source instance tables

- [T65 — preserved message data and comments](../../message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0065.md)
- [T66 — preserved message data and comments](../../message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0066.md)

## Flows and diagrams

[Transparency reporting and acceptance/rejection sequence](../../message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0138.md)

In the supplied example, ICSD receives the report from CUSA and responds with status. The holdings are rejected for an invalid ISIN while general details remain valid, giving accepted with exception (P5922–P5925). No source diagram specifically tied to this exact status-advice version is supplied.

## Availability and unresolved gaps

Namespace, complete field/type references, validation facets and normative rule coverage cannot be established from these business examples alone. [issue-000042 — missing schema and exact Part2 definition](../../../../../tracking/issues.md); [issue-000040 — transparency example contradictions](../../../../../tracking/issues.md).

## Original source and canonical participants

[src-000095](../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx)

- [ICSD — transparency business example](../../../../../shared/reference/participants/participant-src-000095-example-icsd.md)
- [CUSA — transparency business example](../../../../../shared/reference/participants/participant-src-000095-example-cusa.md)

- [Transparency status advice — accepted with exception example](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-transparency-status-advice-example.md)
