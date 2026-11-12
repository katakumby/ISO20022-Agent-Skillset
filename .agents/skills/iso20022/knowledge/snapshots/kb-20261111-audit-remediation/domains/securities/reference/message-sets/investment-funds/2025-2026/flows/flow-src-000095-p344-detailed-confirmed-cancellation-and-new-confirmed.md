---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p344-detailed-confirmed-cancellation-and-new-confirmed"
title: "Fund Cash Forecast Reporting / Cancellation and New / Detailed Confirmed, Cancellation and New Confirmed "
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Cash Forecast Reporting", "Cancellation and New", "Detailed Confirmed, Cancellation and New Confirmed "], "locator": "/w:document/w:body/w:p[344]", "paragraph_id": "P344", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Cash Forecast Reporting", "Cancellation and New", "Detailed Confirmed, Cancellation and New Confirmed "], "locator": "/w:document/w:body/w:p[345]", "paragraph_id": "P345", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Cash Forecast Reporting", "Cancellation and New", "Detailed Confirmed, Cancellation and New Confirmed "], "locator": "/w:document/w:body/w:p[346]", "paragraph_id": "P346", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Cash Forecast Reporting", "Cancellation and New", "Detailed Confirmed, Cancellation and New Confirmed "], "locator": "/w:document/w:body/w:p[347]", "paragraph_id": "P347", "table_id": null}]
participants: ["participant-src-000095-fund-accountant", "participant-src-000095-fund-management-company", "participant-src-000095-market-data-provider", "participant-src-000095-other-interested-party", "participant-src-000095-regulator", "participant-src-000095-reporting-party", "participant-src-000095-requesting-party", "participant-src-000095-transfer-agent"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Fund Cash Forecast Reporting"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[5]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000096", "locator": "file page 126; 10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Fund Cash Forecast Reporting"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[6]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000096", "locator": "file page 153; 12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03"}]
message_ids: []
message_families: ["camt.043", "camt.045"]
search_terms: ["Detailed Confirmed, Cancellation and New Confirmed", "camt.043", "camt.045"]
limitations: ["Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.", "P345–346: detailed confirmed cancellation/amendment uses cancellation then new report.", "Part1 message names/families do not establish exact versions; use maintained Part2/schema references.", "Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition."]
manual_curated: true
participant_ids: ["participant-src-000095-fund-accountant", "participant-src-000095-fund-management-company", "participant-src-000095-market-data-provider", "participant-src-000095-other-interested-party", "participant-src-000095-regulator", "participant-src-000095-reporting-party", "participant-src-000095-requesting-party", "participant-src-000095-transfer-agent"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0043.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Complete source-delimited narrative and literal diagram messages/directions checked; institutional examples retained separately."}
---

# Fund Cash Forecast Reporting / Cancellation and New / Detailed Confirmed, Cancellation and New Confirmed 

[src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md); source heading P344, direct-body paragraph P347.

## Purpose, trigger and common conditions

**P316** This message flow section illustrates the use of the fund cash forecast messages in typical message sequencing scenarios. The fund cash forecast messages are sent by a report provider to the report user.

**P317** The report provider is, for example, a fund accountant, transfer agent, market data provider, or any other interested party.

**P318** The report user is, for example, a fund management company, a transfer agent, market data provider, regulator or any other interested party.

**P319** The difference between estimated and confirmed cash forecast reports is that estimated reports are sent before the cut-off time and/or the price valuation, whereas confirmed cash forecast reports contain definitive prices.

**P320** The difference between detailed and non-detailed cash forecast reports is in the level of information that can be provided. In the detailed reports, the cash flow amounts can be sorted according to pre-defined or user-defined criteria and it is possible to breakdown cash forecast amounts by, for example, investment fund transaction types.

The source-specific trigger, acceptance conditions, outcomes and optional/failure paths are preserved in the ordered narrative below. A separate formal precondition/postcondition is asserted only where the source supplies one.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [fund accountant](../../../../../../../shared/reference/participants/participant-src-000095-fund-accountant.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [fund management company](../../../../../../../shared/reference/participants/participant-src-000095-fund-management-company.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [market data provider](../../../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [other interested party](../../../../../../../shared/reference/participants/participant-src-000095-other-interested-party.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [regulator](../../../../../../../shared/reference/participants/participant-src-000095-regulator.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [reporting party](../../../../../../../shared/reference/participants/participant-src-000095-reporting-party.md) | Explicit figure sender/receiver; see step table. |
| [requesting party](../../../../../../../shared/reference/participants/participant-src-000095-requesting-party.md) | Explicit figure sender/receiver; see step table. |
| [transfer agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |


## Ordered activities and source-defined alternatives

**P345** After the cut-off time and/or the price valuation of the fund, the report provider sends a FundDetailedConfirmedCashForecastReport message to the report user to inform the report user of the definitive cash flow movements for a specific financial instrument on a specific trade date.

**P346** As the FundDetailedConfirmedCashForecastReport message needs to be cancelled or amended, the report provider sends a FundDetailedConfirmedCashForecastReportCancellation message to the report user. Subsequently, the report provider sends a new FundDetailedConfirmedCashForecastReport message to the report user.

### fig-0043

[Literal source sequence and visual review](../diagrams/funds-processes/fig-0043.md) (Word file page 52).

| Step | Sender | Receiver | Source message label |
| --- | --- | --- | --- |
| 1 | [Report Provider](../../../../../../../shared/reference/participants/participant-src-000095-reporting-party.md) | [Report User](../../../../../../../shared/reference/participants/participant-src-000095-requesting-party.md) | FundDetailedConfirmedCashForecastReport |
| 2 | [Report Provider](../../../../../../../shared/reference/participants/participant-src-000095-reporting-party.md) | [Report User](../../../../../../../shared/reference/participants/participant-src-000095-requesting-party.md) | FundDetailedConfirmedCashForecastReportCancellation |
| 3 | [Report Provider](../../../../../../../shared/reference/participants/participant-src-000095-reporting-party.md) | [Report User](../../../../../../../shared/reference/participants/participant-src-000095-requesting-party.md) | FundDetailedConfirmedCashForecastReport |



## Message definitions and related paths

| Family | Supplied exact definition | Scope |
| --- | --- | --- |
| camt.043 | [camt.043.001.04](../../../../messages/camt.043.001.04/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| camt.045 | [camt.045.001.03](../../../../messages/camt.045.001.03/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |


## Outcomes and source qualifications

- Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.
- P345–346: detailed confirmed cancellation/amendment uses cancellation then new report.
- Part1 message names/families do not establish exact versions; use maintained Part2/schema references.
- Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition.

The narrative gives each outcome: execution confirmation, accepted/pending status, reporting/replacement, rejection or cancellation as applicable. These outcomes are not interchanged. For cancellation, CAND concerns completion of the requested cancellation; order acceptance (PACK) does not assert execution.

## Review

Source narrative, participant roles and every depicted message direction were compared with the original picture and Word-rendered page on 2026-11-09. The bounded flow scope is reviewed; referenced schemas and tables retain their own statuses.
