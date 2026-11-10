---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000343"]
source_editions: ["march-2024"]
message_sets: ["t2s-administration"]
flow_id: "flow-src-000343-p136-resent-request-process"
title: "Resent Request Process"
source_locations: [{"source_id": "src-000343", "heading_path": ["BusinessProcess Description", "Resend Request"], "locator": "/w:document/w:body/w:p[136]", "paragraph_id": "P136", "table_id": null}, {"source_id": "src-000343", "heading_path": ["BusinessProcess Description", "Resend Request"], "locator": "/w:document/w:body/w:tbl[9]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000343", "heading_path": ["BusinessProcess Description", "Resend Request"], "locator": "/w:document/w:body/w:p[137]", "paragraph_id": "P137", "table_id": null}]
participants: ["participant-src-000343-system-member"]
message_mapping_evidence: [{"source_id": "src-000343", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Administration"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["admi.006"]
search_terms: ["Resent Request Process", "System Member", "admi.006"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Resent Request Process

Source context: T2S Administration. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The Resend request enables directly connected CSDs, CBs or any parties authorized by them to request the resending of a message or a file (duplicate of the original message/file) supported by Central System. To instruct Central System for the resend of a message the technical address of the receiving party must be specified.  

Evidence: [T9](../documents/src-000343/tables/tbl-0009.md), source row 2.

### Trigger

The process is triggered when a CB, CSD or any party authorised by them to use the Resend by defining specific criteria, e. g.  Business Date (optional field), Sequence number or Original Message Reference can be used to further specify the request: If no Business Date is specified the current Business Date is assumed 

Evidence: [T9](../documents/src-000343/tables/tbl-0009.md), source row 3.

### Pre-conditions

The System User has the respective privilege to obtain the requested report. The corresponding business data (T2S outbound messages or files) are already produced and accessible 

Evidence: [T9](../documents/src-000343/tables/tbl-0009.md), source row 4.

### Post-conditions

In response to the Resend Request message, Central System sends first a positive “Validation Result Resend” after the successful permission check. In parallel, the duplicate of the original message/file is sent. If an error occurs resulting from the processing of the Resend Request an error information is sent.

Evidence: [T9](../documents/src-000343/tables/tbl-0009.md), source row 5.

### Role

System Member

Evidence: [T9](../documents/src-000343/tables/tbl-0009.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| System Member | [Participant](../../../../participants/participant-src-000343-system-member.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T9](../documents/src-000343/tables/tbl-0009.md).

## Messages and alternative paths

Source-supported message family mentions: `admi.006`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000343](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart1_Target2Securities_Administration_2023_2024_v2.docx`. Heading path: BusinessProcess Description / Resend Request.
