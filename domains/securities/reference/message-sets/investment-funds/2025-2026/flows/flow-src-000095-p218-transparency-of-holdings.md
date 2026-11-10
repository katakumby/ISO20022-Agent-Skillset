---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p218-transparency-of-holdings"
title: "Transparency of Holdings"
source_locations: [{"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reconciliation (Statements)", "Transparency of Holdings"], "locator": "/w:document/w:body/w:p[218]", "paragraph_id": "P218", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reconciliation (Statements)", "Transparency of Holdings"], "locator": "/w:document/w:body/w:p[219]", "paragraph_id": "P219", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reconciliation (Statements)", "Transparency of Holdings"], "locator": "/w:document/w:body/w:p[220]", "paragraph_id": "P220", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reconciliation (Statements)", "Transparency of Holdings"], "locator": "/w:document/w:body/w:tbl[42]", "paragraph_id": null, "table_id": "T42"}]
participants: ["participant-src-000095-reporting-party", "participant-src-000095-receiving-party-all-levels"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Statement"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[2]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000096", "locator": "file page 375; 18 semt.002.001.02 CustodyStatementOfHoldingsV02"}]
message_ids: []
message_families: ["semt.002"]
search_terms: ["Transparency of Holdings", "Receiving Party (all levels)", "Reporting Party", "Transfer Agent", "Custodian", "semt.002"]
limitations: ["Two receiving occurrences represent distinct custody-chain levels. The right edge has an outgoing arrow and an incoming continuation without named external actors; explicit boundary nodes in this reconstruction are explanatory labels, not new source participants. Parallel bars and both return paths are retained.", "Unlabelled plain source connectors are retained as undirected lines; business direction established by the activity table is described separately. Blank start/end and control symbols remain blank. Mermaid swimlanes preserve responsibility labels but not the exact source geometry."]
manual_curated: true
participant_ids: ["participant-src-000095-reporting-party", "participant-src-000095-receiving-party-all-levels"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0014.md"]
updated: "2026-11-09"
diagram_review: {"status": "pass", "date": "2026-11-09", "reviewer": "shared-evidence agent", "scope": "Original extracted picture and complete Word-rendered source page compared with rendered Mermaid PNG; checked actor occurrences, source labels, endpoints, arrowheads/plain lines, lane/control boundaries and alternatives. Complete-page composition checked in contact sheets; original pictures inspected at readable size.", "source_page": 32, "result_notes": ["All source edges and labels compared; plain-line connectors not promoted to inferred direction."]}
issue_ids: []
---



# Report Transparency of Holdings

[src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx); Description of BusinessActivities / Reconciliation (Statements) / Transparency of Holdings; direct-body paragraph P219; T42.

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

- [reporting party](../../../../../../../shared/reference/participants/participant-src-000095-reporting-party.md)
- [receiving party all levels](../../../../../../../shared/reference/participants/participant-src-000095-receiving-party-all-levels.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Generate Transparency Statement | The reporting party generates a statement of the holdings containing all holdings reported <br>from customers to their custodian, “downstream” in the custody chain, providing transparency of holdings of customers of the customers and compiled with the customers’ inbound statements “upstream” in the custody chain, like a regular custody statement of holdings, from a custodian to their customers, aggregated with the inbound statements received from the respective customers and enriched with the same customer data as is reported to the fund company/transfer agent.<br>The purposes that the transparency of holdings statement has been designed for include:<br>Disclosure of information about customers of customers<br>Verify/validate claims for retrocessions, rebates and commissions<br>Check compliance with laws, regulations and general terms and conditions.<br>Perform data analysis throughout custody chains, to identify geographic distribution patterns, measure the effects of targeted advertisement initiatives, and so on. | Reporting Party |
| Aggregate Holdings | Upon receipt of the Transparency of Holdings statement, the receiver combines data from its own books with the information received in the statement, and identifies any discrepancies to be reported as “account differences”. | Receiving Party (all levels) |
| Reconcile Aggregated Holdings | The receiver books all required updates in its own accounts for alignment. | Receiving Party (all levels) |


## Ordered paths, messages and alternatives

[Complete source reconstruction, connector list and decision paths](../diagrams/funds-processes/fig-0014.md)

Follow the source graph for connected activities; the source table lists responsibilities rather than a universal execution order. Source-labelled exchange types are retained; this high-level activity view does not establish exact message versions.

## Source qualifications and omissions

- Two receiving occurrences represent distinct custody-chain levels. The right edge has an outgoing arrow and an incoming continuation without named external actors; explicit boundary nodes in this reconstruction are explanatory labels, not new source participants. Parallel bars and both return paths are retained.
- Unlabelled plain source connectors are retained as undirected lines; business direction established by the activity table is described separately. Blank start/end and control symbols remain blank. Mermaid swimlanes preserve responsibility labels but not the exact source geometry.
