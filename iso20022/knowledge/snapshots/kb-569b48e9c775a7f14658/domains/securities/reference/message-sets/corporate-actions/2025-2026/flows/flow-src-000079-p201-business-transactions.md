---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p201-business-transactions"
title: "BusinessTransactions"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[201]", "paragraph_id": "P201", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[202]", "paragraph_id": "P202", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[203]", "paragraph_id": "P203", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[204]", "paragraph_id": "P204", "table_id": null}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner", "participant-src-000079-issuer-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["BusinessTransactions", "Account Servicer", "Account Owner", "Issuer Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# BusinessTransactions

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Issuer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-issuer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P202** This section describes the message flows based on the activity diagrams documented above. It shows the typical exchanges of information in the context of a BusinessTransaction.

**P203** The corporate action messages are exchanged between business actors acting either as an account servicer, for example, ICSDs, CSDs, global custodians or clearing agents, or as an account owner, for example, fund managers or institutional investors. 

**P204** If there are intermediaries in the corporate action processing chain between the issuer (agent) and the end investor, some of the business actors, for example, ICSDs, CSDs, global custodians or sub-custodians, will play the account servicer role in one part of the message flow and then, in the next part of the message flow, play the account owner role. In order to keep the generic nature of the message flows described hereafter, only the roles account servicer and account owner will be used.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: BusinessTransactions.
