---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000356"]
source_editions: ["march-2024"]
message_sets: ["t2s-collateral-reporting"]
flow_id: "flow-src-000356-p138-query-management-process"
title: "Collateral-value query management"
source_locations: [{"source_id": "src-000356", "heading_path": ["Description of BusinessActivities", "Query Management Process"], "locator": "/w:document/w:body/w:p[138]", "paragraph_id": "P138", "table_id": null}, {"source_id": "src-000356", "heading_path": ["Description of BusinessActivities", "Query Management Process"], "locator": "/w:document/w:body/w:p[139]", "paragraph_id": "P139", "table_id": null}, {"source_id": "src-000356", "heading_path": ["Description of BusinessActivities", "Query Management Process"], "locator": "/w:document/w:body/w:p[140]", "paragraph_id": "P140", "table_id": null}, {"source_id": "src-000356", "heading_path": ["Description of BusinessActivities", "Query Management Process"], "locator": "/w:document/w:body/w:p[141]", "paragraph_id": "P141", "table_id": null}, {"source_id": "src-000356", "heading_path": ["Description of BusinessActivities", "Query Management Process"], "locator": "/w:document/w:body/w:p[142]", "paragraph_id": "P142", "table_id": null}, {"source_id": "src-000356", "heading_path": ["Description of BusinessActivities", "Query Management Process"], "locator": "/w:document/w:body/w:tbl[9]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000356", "heading_path": ["Description of BusinessActivities", "Query Management Process"], "locator": "/w:document/w:body/w:p[143]", "paragraph_id": "P143", "table_id": null}]
participants: ["participant-src-000356-central-securities-depositories-csd", "participant-src-000356-central-system", "participant-src-000356-executing-servicing-party", "participant-src-000356-instructing-party", "participant-src-000356-national-central-bank-ncb", "participant-src-000356-payment-bank", "participant-src-000356-settlement-infrastructure", "participant-src-000356-settlement-infrastructure-direct-participant", "participant-src-000356-system-member", "participant-src-000356-system-transaction-administrator"]
message_mapping_evidence: [{"source_id": "src-000356", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Collateral Reporting"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["colr.001.001.02", "colr.002.001.02"]
message_families: ["colr.001", "colr.002"]
search_terms: ["Query Management Process", "System Transaction Administrator", "Settlement Infrastructure", "Instructing Party", "System Member", "Payment Bank", "colr.001", "total collateral value", "cash account", "security collateral value", "intraday credit", "access rights", "error rejection"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence.", "Diagram review and table-cell review have separate evidence.", "Diagram review and table-cell review have separate evidence.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
---











# Query Management Process

Source context: T2S CollateralReporting. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| System Transaction Administrator | [Participant](../../../../../../../shared/reference/participants/participant-src-000356-system-transaction-administrator.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Settlement Infrastructure | [Participant](../../../../../../../shared/reference/participants/participant-src-000356-settlement-infrastructure.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000356-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| System Member | [Participant](../../../../../../../shared/reference/participants/participant-src-000356-system-member.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Payment Bank | [Participant](../../../../../../../shared/reference/participants/participant-src-000356-payment-bank.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P140** Notes: In the frame of Central System flow, instructing party corresponds to the direct participant, payment bank or CSD, the servicing/executing party or the receiving party is the settlement infrastructure who achieves the report query request.

Source diagram evidence: [fig-0008](../documents/src-000356/diagrams/fig-0008.md). A canonical source reconstruction and actual review evidence are linked below.

Source table [T9](../documents/src-000356/tables/tbl-0009.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Query<br> | Request for Information concerning collateral values on a specific account | System Member |
| Rejection | Informs the instruction party (by error and description) in case if the instruction of a collateral value query was not valid for processing.<br>There could be three different reasons for a rejection message:<br>plausibility check not successful<br>permission check not successful<br>extracting process not successful | System Transaction Administrator |
| Response | Delivers the requested data, if available, to the infrastructure of the requesting system member Party of the completeness of this instruction. | System Transaction Administrator |

## Messages and alternative paths

Source-supported message family mentions: `colr.001`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000356](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralReporting_2023_2024_v2.docx`. Heading path: Description of BusinessActivities / Query Management Process.

## Curated source flow

The interface submits a collateral-value-of-securities query into Query Management. Plausibility, permission and extraction run in order. Each Not ok route merges into Error data queries; successive ok routes reach Queried data. Both outputs return to the interface. The SD and DD data stores connect to a common trunk supplying all three processing steps; the artwork does not assign one store exclusively to one check. The SD/DD acronyms are retained without unsupported expansion because the supplied glossary does not define them. Three repeated query object boxes are kept as separate occurrences. Boundary and object-underlining presentation remain fully available in the original.

[Complete source diagram](../diagrams/curated/fig-0003.md).

Scoped participants: [system member](../../../../../../../shared/reference/participants/participant-src-000356-system-member.md), [system transaction administrator](../../../../../../../shared/reference/participants/participant-src-000356-system-transaction-administrator.md), [central system](../../../../../../../shared/reference/participants/participant-src-000356-central-system.md), [settlement infrastructure](../../../../../../../shared/reference/participants/participant-src-000356-settlement-infrastructure.md).

## Curated source flow

System Member sends the query to System Transaction Administrator. Failure of plausibility, permission or extraction leads to Deliver Error Message and a member end point. All successful checks lead to Deliver Queried Data Response Message and a distinct member end point. The Yes label on the ExtractDataForQuery-to-decision arrow is retained exactly as drawn, in addition to the decision Yes/No labels. T9 lists the same three rejection reasons. P140 maps the instructing party context to direct participant/payment bank/CSD and the executing/receiving role to settlement infrastructure.

[Complete source diagram](../diagrams/curated/fig-0008.md).

Scoped participants: [system member](../../../../../../../shared/reference/participants/participant-src-000356-system-member.md), [system transaction administrator](../../../../../../../shared/reference/participants/participant-src-000356-system-transaction-administrator.md), [instructing party](../../../../../../../shared/reference/participants/participant-src-000356-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000356-executing-servicing-party.md), [settlement infrastructure](../../../../../../../shared/reference/participants/participant-src-000356-settlement-infrastructure.md), [settlement infrastructure direct participant](../../../../../../../shared/reference/participants/participant-src-000356-settlement-infrastructure-direct-participant.md), [payment bank](../../../../../../../shared/reference/participants/participant-src-000356-payment-bank.md), [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000356-central-securities-depositories-csd.md).

## Curated source flow

An NCB, CSD or directly connected Central System party queries the Central System for current securities collateral value. The source picture shows both error and value response arrows; P148 explicitly says they are mutually exclusive. No sequential error-then-success requirement is inferred. P148 describes the value as the intraday-credit amount a party may receive by collateralising its securities. P83 requires the actual selection timestamp and balance snapshot time/types in the response context. This is collateral-value reporting, not securities movement reversal or a collateral creation instruction.

[Complete source diagram](../diagrams/curated/fig-0009.md).

### Adjacent source narrative

**P148** As outlined above, an NCB, CSD or directly connected Central System party sends a Collateral Value Query to the Central System (e.g. T2S platform) to request information on the current available value of securities for auto collateralisation. The value will represent the amount of intraday credit that a party may receive through collateralising of their securities. Error Response or Collateral Value Response are both exclusive.

Scoped participants: [system member](../../../../../../../shared/reference/participants/participant-src-000356-system-member.md), [system transaction administrator](../../../../../../../shared/reference/participants/participant-src-000356-system-transaction-administrator.md), [national central bank ncb](../../../../../../../shared/reference/participants/participant-src-000356-national-central-bank-ncb.md), [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000356-central-securities-depositories-csd.md), [settlement infrastructure direct participant](../../../../../../../shared/reference/participants/participant-src-000356-settlement-infrastructure-direct-participant.md), [central system](../../../../../../../shared/reference/participants/participant-src-000356-central-system.md).

## Curated source flow

System Member sends CollateralValueQuery to System Transaction Administrator. The source has two separately drawn alternative frames: alt1 Rejection returns CollateralValueReport with a rejection reason; alt2 Execution returns CollateralValueReport. A single native Mermaid alt/else expresses the explicit exclusivity stated by P148; the original preserves the two separate frame boxes. The ERROR RESPONSE MESSAGE in the preceding overview is therefore a rejection-bearing CollateralValueReport, not an invented distinct ISO message.

[Complete source diagram](../diagrams/curated/fig-0010.md).

Scoped participants: [system member](../../../../../../../shared/reference/participants/participant-src-000356-system-member.md), [system transaction administrator](../../../../../../../shared/reference/participants/participant-src-000356-system-transaction-administrator.md).

## Purpose, trigger, conditions and outcomes

P81-P96 defines three usages: total current collateral value of earmarked available securities per cash account; collateral value per cash account and security; and value of a specified security in each linked securities account. A System Member query triggers the process (T9). Actor privileges and data access rights restrict execution and returned data (P121/P125/P129); no additional formal precondition is invented. Successful processing returns data with the selection timestamp, securities balance type and balance snapshot time (P83). Failed plausibility, permission or extraction returns a rejection reason (T9). P148 makes error and value responses mutually exclusive.

The source role mapping and T5/T6 distinctions are contextual. One institution may occur as CSD and NCB simultaneously (P110); neither functional participant role is equated with a named institution.
