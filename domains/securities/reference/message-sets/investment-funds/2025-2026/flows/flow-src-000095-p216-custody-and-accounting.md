---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p216-custody-and-accounting"
title: "Custody and Accounting"
source_locations: [{"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reconciliation (Statements)", "Custody and Accounting"], "locator": "/w:document/w:body/w:p[216]", "paragraph_id": "P216", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reconciliation (Statements)", "Custody and Accounting"], "locator": "/w:document/w:body/w:p[217]", "paragraph_id": "P217", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reconciliation (Statements)", "Custody and Accounting"], "locator": "/w:document/w:body/w:tbl[41]", "paragraph_id": null, "table_id": "T41"}]
participants: ["participant-src-000095-requesting-party", "participant-src-000095-reporting-party", "participant-src-000095-requesting-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Custody and Accounting", "Requesting Party", "Reporting Party"]
limitations: ["Grey shading surrounds the optional pull request/status path; not all institutions support it. Push reporting enters at Send Statement (T41). The picture prints Yes on the connector between Send Statement and Correction Required? and draws no replacement loop; T41 separately specifies a new statement for incorrect information.", "Unlabelled plain source connectors are retained as undirected lines; business direction established by the activity table is described separately. Blank start/end and control symbols remain blank. Mermaid swimlanes preserve responsibility labels but not the exact source geometry."]
manual_curated: true
participant_ids: ["participant-src-000095-requesting-party", "participant-src-000095-reporting-party", "participant-src-000095-requesting-party"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0013.md"]
updated: "2026-11-09"
diagram_review: {"status": "pass", "date": "2026-11-09", "reviewer": "shared-evidence agent", "scope": "Original extracted picture and complete Word-rendered source page compared with rendered Mermaid PNG; checked actor occurrences, source labels, endpoints, arrowheads/plain lines, lane/control boundaries and alternatives. Complete-page composition checked in contact sheets; original pictures inspected at readable size.", "source_page": 31, "result_notes": ["All source edges and labels compared; plain-line connectors not promoted to inferred direction."]}
issue_ids: []
---



# Statement Flow

[src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx); Description of BusinessActivities / Reconciliation (Statements) / Custody and Accounting; direct-body paragraph P217; T41.

## Purpose, trigger and conditions

[Source business-process conditions T33](../documents/src-000095/tables/tbl-0033.md)

| Item | Description |
| --- | --- |
| Definition | Records (shares and cash) and account details on the books of a party are compared/matched and brought into conformity with the records and account details on the books of another party, through the identification of discrepancies, determination of the correct value for any item where a discrepancy exists, and modification of the books of one or both parties to result in the correct value enabling full reconciliation of both parties.<br>Custody reporting<br>Accounting reporting<br>Transactions reporting<br>Transparency of holdings reporting: provides transparency and the breakdown structure of the underlying holdings through a chain of custodians of one or several financial instruments. |
| Trigger | time period as defined in SLA<br>time period as defined by regulator<br>on request<br>completion of any transaction that affects account balances<br>corporate event |
| Pre-conditions | both parties involved maintain records for an account that is recognisably the same account<br>both parties agree on the reconciliation process |
| Post-conditions | parties agree (verbally, in writing) as to account details and balances, otherwise repeat process<br>reconciliation is completed |
| Role | Account servicer, account servicer |


## Participants and responsibilities

- [requesting party](../../../../../../../shared/reference/participants/participant-src-000095-requesting-party.md)
- [reporting party](../../../../../../../shared/reference/participants/participant-src-000095-reporting-party.md)
- [requesting party](../../../../../../../shared/reference/participants/participant-src-000095-requesting-party.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Request Statement | The requesting party (where the "pull" scenario is supported), sends a request for a statement. | Requesting Party |
| Status Received | If the request is not accepted by the reporting party, it sends a status message to the requesting party rejecting the request and specifying the reason for the rejection. | Reporting Party |
| Send Statement | If the request is accepted by the reporting party, it sends a statement report to the requesting party in response to the request. In the "push" scenario, the reporting party sends a statement to the receiving party at the agreed frequency. | Reporting Party |
| Send Cancellation | If the statement is found to have been issued in error or contains incorrect information, a statement cancellation message is sent by the reporting party to the requesting/receiving party specifying the reason for cancellation. | Reporting Party |
| Send Statement | If the cancellation is because the statement contained incorrect information, the reporting party sends a new statement to the requesting/receiving party. | Reporting Party |


## Ordered paths, messages and alternatives

[Complete source reconstruction, connector list and decision paths](../diagrams/funds-processes/fig-0013.md)

Follow the source graph for connected activities; the source table lists responsibilities rather than a universal execution order. Source-labelled exchange types are retained; this high-level activity view does not establish exact message versions.

## Source qualifications and omissions

- Grey shading surrounds the optional pull request/status path; not all institutions support it. Push reporting enters at Send Statement (T41). The picture prints Yes on the connector between Send Statement and Correction Required? and draws no replacement loop; T41 separately specifies a new statement for incorrect information.
- Unlabelled plain source connectors are retained as undirected lines; business direction established by the activity table is described separately. Blank start/end and control symbols remain blank. Mermaid swimlanes preserve responsibility labels but not the exact source geometry.
