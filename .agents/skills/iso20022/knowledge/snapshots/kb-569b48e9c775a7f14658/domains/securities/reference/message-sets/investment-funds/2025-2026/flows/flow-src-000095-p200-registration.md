---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p200-registration"
title: "Registration"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[200]", "paragraph_id": "P200", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[35]", "paragraph_id": null, "table_id": "T35"}]
participants: ["participant-src-000095-transfer-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Registration", "Transfer Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Registration

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Process by which units are allocated/removed to/from the registrar. Process by which the legal status of the ownership is defined.

Evidence: [T35](../documents/src-000095/tables/tbl-0035.md), source row 2.

### Trigger

Confirmation of a deal that is executed

Evidence: [T35](../documents/src-000095/tables/tbl-0035.md), source row 3.

### Pre-conditions

deal is executed
payment is received
an account is opened and all required legal documents are received

Evidence: [T35](../documents/src-000095/tables/tbl-0035.md), source row 4.

### Post-conditions

units are fully registered on the shareholder register
units are added or removed to or from the existing shareholder register

Evidence: [T35](../documents/src-000095/tables/tbl-0035.md), source row 5.

### Role

Transfer agent

Evidence: [T35](../documents/src-000095/tables/tbl-0035.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T35](../documents/src-000095/tables/tbl-0035.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Heading path: BusinessProcess Description.
