---
template: false
document_kind: "business-flow"
review_status: "needs-review"
manual_curated: true
flow_id: "flow-src-000095-transparency-status-advice-example"
title: "Transparency status advice — accepted with exception example"
source_ids: ["src-000095"]
domain: "securities"
message_sets: ["investment-funds"]
message_ids: ["semt.042.001.01"]
participant_ids: ["participant-src-000095-example-icsd", "participant-src-000095-example-cusa"]
source_locations: [{"source_id": "src-000095", "paragraph_id": "P5920", "xml_path": "/w:document/w:body/w:p[5920]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReportStatusAdvice semt.042.001.01"]}, {"source_id": "src-000095", "paragraph_id": "P5921", "xml_path": "/w:document/w:body/w:p[5921]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReportStatusAdvice semt.042.001.01"]}, {"source_id": "src-000095", "paragraph_id": "P5922", "xml_path": "/w:document/w:body/w:p[5922]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReportStatusAdvice semt.042.001.01"]}, {"source_id": "src-000095", "paragraph_id": "P5923", "xml_path": "/w:document/w:body/w:p[5923]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReportStatusAdvice semt.042.001.01"]}, {"source_id": "src-000095", "paragraph_id": "P5924", "xml_path": "/w:document/w:body/w:p[5924]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReportStatusAdvice semt.042.001.01"]}, {"source_id": "src-000095", "paragraph_id": "P5925", "xml_path": "/w:document/w:body/w:p[5925]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReportStatusAdvice semt.042.001.01"]}]
limitations: ["No source diagram specifically tied to this exact status-advice version is supplied.", "The referenced report is named by family semt.041 in this status example; its identifier is not printed here as a full version."]
updated: "2026-11-09"
source_editions: ["March 2025"]
---

# Transparency status advice — accepted with exception example

## Purpose, trigger and outcome

After receiving and processing a SecuritiesBalanceTransparencyReport from CUSA, ICSD responds with a status advice. In this source example the three holdings referenced by statement OH_1023 are rejected for an invalid ISIN while the general details remain valid: the result is accepted with exception. Evidence: src-000095 P5922–P5925.

## Participants and ordered actions

| Step | Responsible participant / sender | Receiver | Action |
| --- | --- | --- | --- |
| 1 | [CUSA](../../../../../../../shared/reference/participants/participant-src-000095-example-cusa.md) | [ICSD](../../../../../../../shared/reference/participants/participant-src-000095-example-icsd.md) | Send/receive the report (family semt.041). |
| 2 | [ICSD](../../../../../../../shared/reference/participants/participant-src-000095-example-icsd.md) | [CUSA](../../../../../../../shared/reference/participants/participant-src-000095-example-cusa.md) | After processing, send semt.042.001.01 status advice; reject holdings for invalid ISIN while accepting valid general details with exception. |


## Complete evidence

**src-000095 P5920** — SecuritiesBalanceTransparencyReportStatusAdvice semt.042.001.01

**src-000095 P5921** — Description

**src-000095 P5922** — ICSD (ICSDLULL) receives a SecuritiesBalanceTransparencyReport (semt.041) message from CUSA (CUSALULL). 

**src-000095 P5923** — Following processing, ICSD responds with a Securities Balance Transparency Report Status Advice (semt.042). 

**src-000095 P5924** — This status message provides details on the acceptance of a SecuritiesBalanceTransparencyReport message with statement identification OH_1023 which provide details of three holdings.

**src-000095 P5925** — The status message specifies that the holdings in the original SecuritiesBalanceTransparencyReport message are rejected because the ISIN of the financial instrument is invalid. The general details are still valid, so the status is accepted with exception.

[T65 — complete source instance and comments](../documents/src-000095/tables/tbl-0065.md)

The source does not specify a retry, correction, deadline or additional failure branch in this example. No further conditions are inferred.
