---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_sets: ["t2s-billing"]
flow_id: "flow-src-000347-p142-negative-scenario"
title: "Negative Scenario"
source_locations: [{"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Negative Scenario"], "locator": "/w:document/w:body/w:p[142]", "paragraph_id": "P142", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Negative Scenario"], "locator": "/w:document/w:body/w:p[143]", "paragraph_id": "P143", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Negative Scenario"], "locator": "/w:document/w:body/w:p[144]", "paragraph_id": "P144", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Negative Scenario"], "locator": "/w:document/w:body/w:p[145]", "paragraph_id": "P145", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Negative Scenario"], "locator": "/w:document/w:body/w:p[146]", "paragraph_id": "P146", "table_id": null}]
participants: ["participant-src-000347-executing-servicing-party", "participant-src-000347-instructing-party", "participant-src-000347-system-member", "participant-src-000347-system-transaction-administrator"]
message_mapping_evidence: [{"source_id": "src-000347", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Billing"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000347", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Billing"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["camt.076.001.01", "camt.077.001.01"]
message_families: ["camt.076", "camt.077"]
search_terms: ["Negative Scenario", "Executing / Servicing Party", "Instructing Party", "camt.076", "camt.077"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Flow interpretation checked against its linked source diagram; table review is recorded separately."]
manual_curated: true
---



# Negative Scenario

Source context: T2S Billing. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000347-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000347-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P143** Applies when the query sent by the Instructing Party is rejected by the Executing/Servicing Party.

**P145** Query ProcessBilling Report (camt.077): REJECTEDCumulative/Itemised Billing Report Request (camt.076)Query ProcessBilling Report (camt.077): REJECTEDCumulative/Itemised Billing Report Request (camt.076)

Source diagram evidence: [fig-0010](../documents/src-000347/diagrams/fig-0010.md). Dedicated source reconstruction and actual review evidence are linked below.

## Messages and alternative paths

Source-supported message family mentions: `camt.076`, `camt.077`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000347](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`. Heading path: BusinessTransactions / Query Billing Information / Negative Scenario.

## Curated source process

The Instructing Party requests cumulative or itemised billing data, specifying invoice, period and (for itemised queries) securities account, cash account or participant. The Executing/Servicing Party returns REJECTED and the business or operational error causing the rejection. The report is not a settlement reversal or invoice-cancellation instruction.

[Complete source diagram reconstruction](../diagrams/curated/fig-0010.md).

### Complete adjacent scenario narrative

**P143** Applies when the query sent by the Instructing Party is rejected by the Executing/Servicing Party.

**P147** Billing Report Request

**P148** The Instructing Party sends the query to the Executing/Servicing Party to obtain information about:

**P149** Cumulative Billing Data

**P150** Itemised Billing Data

**P152** This query contains information that clearly identifies a certain invoice, billing period or, in case of itemised queries, specific securities account, cash account or participant.

**P153** The Executing/Servicing Party informs the Instructing party that the Billing Report Query has been rejected (REJECTED). The Executing/Servicing Party present to the Instructing Party the business or operational error which caused the rejection.

| Participant | Source-specific responsibility |
| --- | --- |
| [instructing party](../../../../../../../shared/reference/participants/participant-src-000347-instructing-party.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000347-executing-servicing-party.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [system member](../../../../../../../shared/reference/participants/participant-src-000347-system-member.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [system transaction administrator](../../../../../../../shared/reference/participants/participant-src-000347-system-transaction-administrator.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |


