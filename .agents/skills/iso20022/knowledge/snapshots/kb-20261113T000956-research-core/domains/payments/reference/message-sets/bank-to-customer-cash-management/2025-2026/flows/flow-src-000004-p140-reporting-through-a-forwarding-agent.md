---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
flow_id: "flow-src-000004-p140-reporting-through-a-forwarding-agent"
title: "Reporting through a Forwarding Agent"
source_locations: [{"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting through a Forwarding Agent "], "locator": "/w:document/w:body/w:p[140]", "paragraph_id": "P140", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting through a Forwarding Agent "], "locator": "/w:document/w:body/w:p[141]", "paragraph_id": "P141", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting through a Forwarding Agent "], "locator": "/w:document/w:body/w:p[142]", "paragraph_id": "P142", "table_id": null}]
participants: ["participant-src-000004-account-owner", "participant-src-000004-account-servicer", "participant-src-000004-forwarding-agent", "participant-src-000004-recipient"]
message_mapping_evidence: []
message_ids: ["camt.052.001.14", "camt.053.001.14"]
message_families: ["camt.052", "camt.053"]
search_terms: ["Reporting through a Forwarding Agent", "Account Servicer", "Forwarding Agent", "Account Owner", "Recipient"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Business conditions and source contradictions are separate from XML validation."]
manual_curated: true
review_date: "2026-11-09"
source_flow_review: "pass"
---





# Reporting through a Forwarding Agent

Source context: Bank-to-Customer Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Forwarding Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-forwarding-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Recipient | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-recipient.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P141** The Bank-to-Customer Cash Management messages are sent from the account servicer through a Forwarding Agent (who plays the role of 'concentrating institution' for the account owner) to the account owner, or a party authorised by the account owner to receive the account information (that is, the Message Recipient). Which messages will be sent will be agreed between the three parties.

Source diagram evidence: [fig-0014](../documents/src-000004/diagrams/fig-0014.md). Canonical source reconstruction and actual review evidence are linked below.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000004](../../../../../../../evidence/omitted/52f543e2b58f688bc16fa140.md). Heading path: BusinessTransactions / Reporting through a Forwarding Agent .

## Curated source flow

The Forwarding Agent is a concentrating institution for the Account Owner. The three parties agree which reporting messages are sent. P141 also allows the final recipient to be a party authorised by the owner; this Recipient role is narrative context not drawn as a fourth actor. Both OR alternatives remain alternatives rather than a mandatory pair.

[Complete source diagram](../diagrams/curated/fig-0014.md).

### Adjacent source narrative

**P141** The Bank-to-Customer Cash Management messages are sent from the account servicer through a Forwarding Agent (who plays the role of 'concentrating institution' for the account owner) to the account owner, or a party authorised by the account owner to receive the account information (that is, the Message Recipient). Which messages will be sent will be agreed between the three parties.

Scoped participants: [account owner](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md), [account servicer](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md), [forwarding agent](../../../../../../../shared/reference/participants/participant-src-000004-forwarding-agent.md), [recipient](../../../../../../../shared/reference/participants/participant-src-000004-recipient.md).

[Complete business conditions and source examples](../business-rules.md). Source-defined trigger/preconditions, activities, responsibilities and alternatives compared with the linked table/narrative and complete source figure on2026-11-09. Unstated conditions remain unstated.
