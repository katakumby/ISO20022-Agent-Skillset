---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p351-fund-reference-data-report-solicited-requested"
title: "Fund Reference Data Reporting / Fund Reference Data Report – Solicited (requested)"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Reference Data Reporting", "Fund Reference Data Report – Solicited (requested)"], "locator": "/w:document/w:body/w:p[351]", "paragraph_id": "P351", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Reference Data Reporting", "Fund Reference Data Report – Solicited (requested)"], "locator": "/w:document/w:body/w:p[352]", "paragraph_id": "P352", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Reference Data Reporting", "Fund Reference Data Report – Solicited (requested)"], "locator": "/w:document/w:body/w:p[353]", "paragraph_id": "P353", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Reference Data Reporting", "Fund Reference Data Report – Solicited (requested)"], "locator": "/w:document/w:body/w:p[354]", "paragraph_id": "P354", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Reference Data Reporting", "Fund Reference Data Report – Solicited (requested)"], "locator": "/w:document/w:body/w:p[355]", "paragraph_id": "P355", "table_id": null}]
participants: ["participant-src-000095-distributor", "participant-src-000095-fund-management-company", "participant-src-000095-fund-promoter", "participant-src-000095-market-data-provider", "participant-src-000095-other-interested-party", "participant-src-000095-professional-investor", "participant-src-000095-regulator", "participant-src-000095-reporting-party", "participant-src-000095-requesting-party", "participant-src-000095-transfer-agent"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Fund Reference Data"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[2]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000096", "locator": "file page 291; 15 reda.004.001.07 FundReferenceDataReportV07"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Fund Reference Data"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[3]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000096", "locator": "file page 365; 16 reda.005.001.03 InvestmentFundReportRequestV03"}]
message_ids: []
message_families: ["reda.004", "reda.005"]
search_terms: ["Fund Reference Data Report – Solicited (requested)", "reda.004", "reda.005"]
limitations: ["Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.", "P352–354: request is for reference data for a specific instrument.", "Part1 message names/families do not establish exact versions; use maintained Part2/schema references.", "Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition."]
manual_curated: true
participant_ids: ["participant-src-000095-distributor", "participant-src-000095-fund-management-company", "participant-src-000095-fund-promoter", "participant-src-000095-market-data-provider", "participant-src-000095-other-interested-party", "participant-src-000095-professional-investor", "participant-src-000095-regulator", "participant-src-000095-reporting-party", "participant-src-000095-requesting-party", "participant-src-000095-transfer-agent"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0044.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Complete source-delimited narrative and literal diagram messages/directions checked; institutional examples retained separately."}
---

# Fund Reference Data Reporting / Fund Reference Data Report – Solicited (requested)

[src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx); source heading P351, direct-body paragraph P355.

## Purpose, trigger and common conditions

**P349** This message flow section illustrates the use of the fund reference data messages in typical message sequencing scenarios. The fund reference data reports are exchanged between a report provider and the report user.

**P350** The report provider is, for example, a fund promoter, fund management company, transfer agent or market data provider. The report user is, for example, a professional investor, investment fund distributor, market data provider, regulator or other interested party.

The source-specific trigger, acceptance conditions, outcomes and optional/failure paths are preserved in the ordered narrative below. A separate formal precondition/postcondition is asserted only where the source supplies one.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [distributor](../../../../../../../shared/reference/participants/participant-src-000095-distributor.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [fund management company](../../../../../../../shared/reference/participants/participant-src-000095-fund-management-company.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [fund promoter](../../../../../../../shared/reference/participants/participant-src-000095-fund-promoter.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [market data provider](../../../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [other interested party](../../../../../../../shared/reference/participants/participant-src-000095-other-interested-party.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [professional investor](../../../../../../../shared/reference/participants/participant-src-000095-professional-investor.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [regulator](../../../../../../../shared/reference/participants/participant-src-000095-regulator.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [reporting party](../../../../../../../shared/reference/participants/participant-src-000095-reporting-party.md) | Explicit figure sender/receiver; see step table. |
| [requesting party](../../../../../../../shared/reference/participants/participant-src-000095-requesting-party.md) | Explicit figure sender/receiver; see step table. |
| [transfer agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |


## Ordered activities and source-defined alternatives

**P352** The report user sends an InvestmentFundReportRequest message to the report provider.

**P353** In this scenario, the InvestmentFundReportRequest message is used to request a FundReferenceDataReport for a specific financial instrument.

**P354** Subsequently, the report provider responds by sending a FundReferenceDataReport message.

### fig-0044

[Literal source sequence and visual review](../diagrams/funds-processes/fig-0044.md) (Word file page 53).

| Step | Sender | Receiver | Source message label |
| --- | --- | --- | --- |
| 1 | [Report User](../../../../../../../shared/reference/participants/participant-src-000095-requesting-party.md) | [Report Provider](../../../../../../../shared/reference/participants/participant-src-000095-reporting-party.md) | InvestmentFundReportRequest |
| 2 | [Report Provider](../../../../../../../shared/reference/participants/participant-src-000095-reporting-party.md) | [Report User](../../../../../../../shared/reference/participants/participant-src-000095-requesting-party.md) | FundReferenceDataReport |



## Message definitions and related paths

| Family | Supplied exact definition | Scope |
| --- | --- | --- |
| reda.004 | [reda.004.001.07](../../../../messages/reda.004.001.07/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| reda.005 | [reda.005.001.03](../../../../messages/reda.005.001.03/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |


## Outcomes and source qualifications

- Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.
- P352–354: request is for reference data for a specific instrument.
- Part1 message names/families do not establish exact versions; use maintained Part2/schema references.
- Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition.

The narrative gives each outcome: execution confirmation, accepted/pending status, reporting/replacement, rejection or cancellation as applicable. These outcomes are not interchanged. For cancellation, CAND concerns completion of the requested cancellation; order acceptance (PACK) does not assert execution.

## Review

Source narrative, participant roles and every depicted message direction were compared with the original picture and Word-rendered page on 2026-11-09. The bounded flow scope is reviewed; referenced schemas and tables retain their own statuses.
