---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000362"]
source_editions: ["february-2025"]
message_sets: ["t2s-limit-utilisation-journal"]
flow_id: "flow-src-000362-p132-query-report-process"
title: "Query Report Process"
source_locations: [{"source_id": "src-000362", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[132]", "paragraph_id": "P132", "table_id": null}, {"source_id": "src-000362", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[8]", "paragraph_id": null, "table_id": "T8"}, {"source_id": "src-000362", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[133]", "paragraph_id": "P133", "table_id": null}]
participants: ["participant-src-000362-central-counterparty", "participant-src-000362-central-securities-depositories-csd", "participant-src-000362-csd-participant", "participant-src-000362-direct-connected-participant-dcp", "participant-src-000362-executing-servicing-party", "participant-src-000362-instructing-party", "participant-src-000362-national-central-bank-ncb", "participant-src-000362-payment-agent", "participant-src-000362-payment-bank", "participant-src-000362-system-application"]
message_mapping_evidence: []
message_ids: ["camt.064.001.01", "camt.065.001.01"]
message_families: ["camt.064", "camt.065"]
search_terms: ["Query Report Process", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
flow_scope: "parent process with two modes"
---









# Query Report Process

Source context: T2S LimitUtilisationJournal. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The instructing party requests a journaling of limit utilisation with selected criteria, from the executing party who replies with the limit activity within the settlement domain corresponding to the query criteria. 

Evidence: [T8](../documents/src-000362/tables/tbl-0008.md), source row 2.

### Trigger

The process is triggered either by the system through a scheduled event at the end of day or the sending of a query request by the Instructing Party.

Evidence: [T8](../documents/src-000362/tables/tbl-0008.md), source row 3.

### Pre-conditions

Limits must exist to query within the scope of the Instructing Party.

Evidence: [T8](../documents/src-000362/tables/tbl-0008.md), source row 4.

### Post-conditions

none

Evidence: [T8](../documents/src-000362/tables/tbl-0008.md), source row 5.

### Role

• Instructing Party for the Query.
• Executing/Servicing Party for the Report.

Evidence: [T8](../documents/src-000362/tables/tbl-0008.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000362-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000362-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T8](../documents/src-000362/tables/tbl-0008.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000362](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`. Heading path: BusinessProcess Description.

## Curated source flow

Native use-case notation preserves the six actor symbols, source stereotypes, directed LimitProcess-to-actor associations and plain links from the business area and to three process ellipses. No include, extend or inheritance semantics are supplied or invented. Only LimitReporting is green and in the supplied message-set scope; LimitManagement and LimitJournaling are source context (P97/P109). This exact artwork occurs at P96 and P111 and is reconstructed once. The source business-area label SettlementAndReconciliation does not reroute this T2S child set or classify it merely by its camt prefix.

[Complete source diagram](../diagrams/curated/fig-0002.md).

Scoped participants: [csd participant](../../../../../../../shared/reference/participants/participant-src-000362-csd-participant.md), [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000362-central-securities-depositories-csd.md), [payment agent](../../../../../../../shared/reference/participants/participant-src-000362-payment-agent.md), [central counterparty](../../../../../../../shared/reference/participants/participant-src-000362-central-counterparty.md), [national central bank ncb](../../../../../../../shared/reference/participants/participant-src-000362-national-central-bank-ncb.md), [system application](../../../../../../../shared/reference/participants/participant-src-000362-system-application.md).

## Curated source flow

Queries branch into A2A/U2A and a shared actor/category taxonomy. The source includes a dashed A2A–U2A connector without a defined meaning, retained as dashed and not interpreted as a message. CSDs, CSD Participants (DCP), Payment Banks and NCBs feed six query categories. Cash accounts has fourteen query/response pairs, with forward solid and return dashed links; only the Limit Utilisation Journal pair is green/in scope. The complete source and two focused detail reconstructions preserve all28 leaf labels and28 message-type link labels. The reconstruction adds a clearly labelled detail-navigation box, not a source process. Other query types are context and are not assigned camt.064/065.

[Complete source diagram](../diagrams/curated/fig-0005.md).

Scoped participants: [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000362-central-securities-depositories-csd.md), [direct connected participant dcp](../../../../../../../shared/reference/participants/participant-src-000362-direct-connected-participant-dcp.md), [csd participant](../../../../../../../shared/reference/participants/participant-src-000362-csd-participant.md), [payment bank](../../../../../../../shared/reference/participants/participant-src-000362-payment-bank.md), [national central bank ncb](../../../../../../../shared/reference/participants/participant-src-000362-national-central-bank-ncb.md).

## Source-defined conditions and direction

T8 requires limits to exist within the scope of the Instructing Party and states postconditions as none. Its two triggers are a participant query or a scheduled system event at end of day. This is the parent query/report process; the pull and push mode records provide the distinct ordered activities.

Linked modes: [pull mode](flow-src-000362-p137-pull-mode.md), [push mode](flow-src-000362-p143-push-mode.md).

## Query business attributes and report content

P63–P72 business-required query attributes are credit-consumer party identification, responsible-party identification (NCB as parent/credit provider or CSD as parent of client), and journal-activity date. Dedicated cash account and limit type are optional. Source limit-type choices are Auto Collateralisation, External Guarantee and Unsecured Credit. These narrative rules remain distinct from the exact XSD constraints.

P78–P89 report outputs are party identification, responsible party identification, date, dedicated cash account, limit type, debit/credit indicator, limit currency, initial limit amount, utilised amount, remaining available headroom and transaction reference.

Supplied examples: [business result](../examples/business-report.md); [operational error Q065](../examples/operational-error.md).
