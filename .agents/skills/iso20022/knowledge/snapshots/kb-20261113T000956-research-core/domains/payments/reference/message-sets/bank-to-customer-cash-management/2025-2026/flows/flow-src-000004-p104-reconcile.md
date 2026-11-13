---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
flow_id: "flow-src-000004-p104-reconcile"
title: "Reconcile"
source_locations: [{"source_id": "src-000004", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[104]", "paragraph_id": "P104", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[105]", "paragraph_id": "P105", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[106]", "paragraph_id": "P106", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[10]", "paragraph_id": null, "table_id": "T10"}]
participants: ["participant-src-000004-account-owner", "participant-src-000004-account-servicer", "participant-src-000004-creditor", "participant-src-000004-creditor-agent", "participant-src-000004-debtor", "participant-src-000004-debtor-agent", "participant-src-000004-final-agent", "participant-src-000004-first-agent", "participant-src-000004-forwarding-agent", "participant-src-000004-initiating-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Reconcile", "Account Owner", "Creditor", "Debtor"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Business conditions and source contradictions are separate from XML validation."]
manual_curated: true
review_date: "2026-11-09"
source_flow_review: "pass"
---





# Reconcile

Source context: Bank-to-Customer Cash Management. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The process includes the financial impact reporting, the reporting on the payment transaction status and the reconciliation process. Further descriptions of these sub-processes are included below.

Evidence: [T10](../documents/src-000004/tables/tbl-0010.md), source row 2.

### Trigger

Payment process is completed. 

Evidence: [T10](../documents/src-000004/tables/tbl-0010.md), source row 3.

### Pre-conditions

An agreement exists between the reporting party and the reported party to do a specific type of reporting, in order to meet legal requirements and business requirements agreed between the reporting and reported party.

Evidence: [T10](../documents/src-000004/tables/tbl-0010.md), source row 4.

### Post-conditions

The payment transaction is reported on.

Evidence: [T10](../documents/src-000004/tables/tbl-0010.md), source row 5.

### Role

Account Owner (debtor or creditor).

Evidence: [T10](../documents/src-000004/tables/tbl-0010.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Creditor | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-creditor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P105** Reporting applies both to interbank reporting, for example, nostro account reporting, and bank-to-customer reporting. The definitions below apply to the bank-to-customer reporting.

**P106** Regulatory reporting is described as a separate process. 

Source table [T10](../documents/src-000004/tables/tbl-0010.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000004](../../../../../../../evidence/omitted/52f543e2b58f688bc16fa140.md). Heading path: BusinessProcess Description.

## Curated source flow

The source has five BusinessActor figures and four BusinessProcess ovals, connected by undirected plain lines. Actor labels carry the source namespace note from DICO_BusinessActorsAndRoles. There is no drawn boundary, inheritance, include or extend arrow. Native use-case notation retains that actor/process topology. T9-T12 and P102-P110 supply the four process definitions, triggers and conditions; status-chain roles First Agent and Final Agent are narrative participants absent from this overview. The generic status process has no specified exact message and is not assigned a camt reporting definition.

[Complete source diagram](../diagrams/curated/fig-0002.md).

Scoped participants: [account owner](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md), [account servicer](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md), [debtor](../../../../../../../shared/reference/participants/participant-src-000004-debtor.md), [debtor agent](../../../../../../../shared/reference/participants/participant-src-000004-debtor-agent.md), [creditor](../../../../../../../shared/reference/participants/participant-src-000004-creditor.md), [creditor agent](../../../../../../../shared/reference/participants/participant-src-000004-creditor-agent.md), [initiating party](../../../../../../../shared/reference/participants/participant-src-000004-initiating-party.md), [forwarding agent](../../../../../../../shared/reference/participants/participant-src-000004-forwarding-agent.md), [first agent](../../../../../../../shared/reference/participants/participant-src-000004-first-agent.md), [final agent](../../../../../../../shared/reference/participants/participant-src-000004-final-agent.md).

[Complete business conditions and source examples](../business-rules.md). Source-defined trigger/preconditions, activities, responsibilities and alternatives compared with the linked table/narrative and complete source figure on2026-11-09. Unstated conditions remain unstated.
