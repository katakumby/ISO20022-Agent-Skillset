---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
flow_id: "flow-src-000371-p238-securities-account-status-advice"
title: "Securities Account Status Advice"
source_locations: [{"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[238]", "paragraph_id": "P238", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[239]", "paragraph_id": "P239", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[240]", "paragraph_id": "P240", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[241]", "paragraph_id": "P241", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[242]", "paragraph_id": "P242", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[243]", "paragraph_id": "P243", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[244]", "paragraph_id": "P244", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[245]", "paragraph_id": "P245", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[246]", "paragraph_id": "P246", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[247]", "paragraph_id": "P247", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[248]", "paragraph_id": "P248", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[249]", "paragraph_id": "P249", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[250]", "paragraph_id": "P250", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[251]", "paragraph_id": "P251", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[252]", "paragraph_id": "P252", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[253]", "paragraph_id": "P253", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[254]", "paragraph_id": "P254", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[255]", "paragraph_id": "P255", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[256]", "paragraph_id": "P256", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[257]", "paragraph_id": "P257", "table_id": null}]
participants: ["participant-src-000371-executing-servicing-party", "participant-src-000371-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["reda.020"]
search_terms: ["Securities Account Status Advice", "Executing/Servicing Party", "Instructing Party", "reda.020"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Securities Account Status Advice

Source context: T2S SecuritiesAccountReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000371-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000371-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P239** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P241** Rejected

**P242** The instruction did not pass validation, some reasons could be:

**P243** the mandatory information is not present or incorrect,

**P244** the data cannot be updated,

**P245** the instruction has already been received and is being processed 

**P246** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status

**P247** .

**P248** Queued

**P249** The Executing/Servicing Party might inform the Instructing party that the processing of the Modify Securities Account instruction has been delayed. In case of e.g. a night-time cycle is running.

**P251** Rejected

**P252** After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P253** the mandatory information is not present or incorrect,

**P254** the data cannot be updated,

**P255** the Instructing Party does not have the right to block/unblock security account,

**P256** the instruction has already been received and is being processed. 

**P257** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

## Messages and alternative paths

Source-supported message family mentions: `reda.020`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000371](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Heading path: BusinessTransactions / Modification Process / Rejection Scenario.
