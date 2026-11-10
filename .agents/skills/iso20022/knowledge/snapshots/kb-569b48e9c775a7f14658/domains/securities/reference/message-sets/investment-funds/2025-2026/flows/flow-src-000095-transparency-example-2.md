---
template: false
document_kind: "business-flow"
review_status: "needs-review"
manual_curated: true
flow_id: "flow-src-000095-transparency-example-2"
title: "Transparency of holdings — supplied business example 2"
domain: "securities"
source_ids: ["src-000095"]
message_sets: ["investment-funds"]
message_ids: ["semt.041.001.02"]
participant_ids: ["participant-src-000095-example-icsd", "participant-src-000095-example-trag", "participant-src-000095-example-cusc", "participant-src-000095-example-ccxx", "participant-src-000095-example-ccyy"]
source_locations: [{"source_id": "src-000095", "paragraph_id": "P5905", "xml_path": "/w:document/w:body/w:p[5905]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1"]}, {"source_id": "src-000095", "paragraph_id": "P5906", "xml_path": "/w:document/w:body/w:p[5906]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1"]}, {"source_id": "src-000095", "paragraph_id": "P5907", "xml_path": "/w:document/w:body/w:p[5907]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1"]}, {"source_id": "src-000095", "paragraph_id": "P5908", "xml_path": "/w:document/w:body/w:p[5908]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1"]}, {"source_id": "src-000095", "paragraph_id": "P5909", "xml_path": "/w:document/w:body/w:p[5909]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1"]}, {"source_id": "src-000095", "paragraph_id": "P5910", "xml_path": "/w:document/w:body/w:p[5910]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1"]}, {"source_id": "src-000095", "paragraph_id": "P5911", "xml_path": "/w:document/w:body/w:p[5911]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1"]}, {"source_id": "src-000095", "paragraph_id": "P5912", "xml_path": "/w:document/w:body/w:p[5912]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1"]}, {"source_id": "src-000095", "paragraph_id": "P5913", "xml_path": "/w:document/w:body/w:p[5913]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1"]}, {"source_id": "src-000095", "paragraph_id": "P5914", "xml_path": "/w:document/w:body/w:p[5914]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1"]}, {"source_id": "src-000095", "paragraph_id": "P5915", "xml_path": "/w:document/w:body/w:p[5915]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1"]}, {"source_id": "src-000095", "paragraph_id": "P5916", "xml_path": "/w:document/w:body/w:p[5916]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1"]}, {"source_id": "src-000095", "paragraph_id": "P5917", "xml_path": "/w:document/w:body/w:p[5917]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1"]}, {"source_id": "src-000095", "paragraph_id": "P5918", "xml_path": "/w:document/w:body/w:p[5918]", "heading_path": ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1"]}]
limitations: ["The supplied business example contains conflicting labels and account/party identifiers; issue-000040 preserves them separately.", "This flow has no source-defined rejection or cancellation branch; no additional preconditions or SLA deadline is inferred."]
updated: "2026-11-09"
source_editions: ["March 2025"]
---

# Transparency of holdings — supplied business example 2

## Purpose, trigger and outcome

Communicate transparent holdings through a custody chain. The customer-side custodian sends a breakdown of its account into underlying client accounts; ICSD can enrich and echo the data, then pass the aggregated information to the transfer agent. The numbered messages below are the source example order; each step’s context remains in the complete narrative. No timing prerequisite beyond receipt of the relevant report is inferred.

## Participants and relationship-specific roles

- [ICSD](../../../../../../../shared/reference/participants/participant-src-000095-example-icsd.md) — International Central Securities Depository; Account Owner to TRAG; Account Servicer to CUSC
- [TRAG](../../../../../../../shared/reference/participants/participant-src-000095-example-trag.md) — Transfer Agent; Account Servicer to ICSD
- [CUSC](../../../../../../../shared/reference/participants/participant-src-000095-example-cusc.md) — Custodian; Account Owner to ICSD; Account Servicer to CCXX, CCYY
- [CCXX](../../../../../../../shared/reference/participants/participant-src-000095-example-ccxx.md) — (client 1); Account Owner
- [CCYY](../../../../../../../shared/reference/participants/participant-src-000095-example-ccyy.md) — (client 2); Account Owner

## Numbered messages and responsibilities

| Sender / responsible participant | Receiver | Source number and message |
| --- | --- | --- |
| CUSC | ICSD | [1] Securities Balance Transparency Report semt.041 |
| ICSD | CUSC | [2] Securities Balance Transparency Report semt.041 |
| ICSD | TRAG | [3] Securities Balance Transparency Report semt.041 |


## Source narrative, alternatives and values

**src-000095 P5905** — Description

**src-000095 P5906** — CUSC (CUSCLULL) sends a SecuritiesBalanceTransparencyReport message to ICSD (ICSDLULL) with a breakdown of the account that ICSD services for CUSC, account CUSC3333. (In the message, this account specified at the safekeeping account level.)

**src-000095 P5907** — For this account, CUSC specifies the holdings of two accounts of its clients.

**src-000095 P5908** — CUSC’s two clients account and holdings 

**src-000095 P5909** — [1.1]	Client CCXX (CCXXLULL), account CCXX-c1. For ISIN LU1234567890, the aggregated settled balance is 1500 units, the aggregated traded balance is 1700 units. (In the message, this is specified at account sub level 1 repetition 1.)

**src-000095 P5910** — The following balance breakdowns are specified:

**src-000095 P5911** — 150 units are traded and pending settlement (PNET).

**src-000095 P5912** — 50 units are traded and pending settlement is overdue (OPNT).

**src-000095 P5913** — [1.2]	Client CCYY (CCYYLULL), account CCYY-c2. For ISIN LU1234567890, the aggregated settled balance is 4700 units, the aggregated traded balance is 5000 units. (In the message, this is specified at account sub level 1 repetition 2.)

**src-000095 P5914** — The following balance breakdowns are specified:

**src-000095 P5915** — 260 units are traded and pending settlement (PNET).

**src-000095 P5916** — 40 units are traded and pending settlement is overdue (OPNT).

**src-000095 P5918** — The other messages in this scenario are not illustrated with XML message instances.

## Source diagrams and complete instance tables

- [Transparency of holdings — custody-chain example 2](../diagrams/funds-transparency/fig-0148.md)

- [Source T64: complete XML example and comments](../documents/src-000095/tables/tbl-0064.md)

## Limits

[issue-000040 — literal example inconsistencies](../../../../../../../tracking/issues.md); [Exact documented message and unavailable schema/Part2 evidence](../../../../messages/semt.041.001.02/index.md). Source XML examples are retained as tables; these are not claimed to be schema validation tests.
