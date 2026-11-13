---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
flow_id: "flow-src-000004-p137-scenario-3"
title: "Scenario 3"
source_locations: [{"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting", "Scenario 3"], "locator": "/w:document/w:body/w:p[137]", "paragraph_id": "P137", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting", "Scenario 3"], "locator": "/w:document/w:body/w:p[138]", "paragraph_id": "P138", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting", "Scenario 3"], "locator": "/w:document/w:body/w:p[139]", "paragraph_id": "P139", "table_id": null}]
participants: ["participant-src-000004-account-owner", "participant-src-000004-account-servicer", "participant-src-000004-recipient"]
message_mapping_evidence: []
message_ids: ["camt.053.001.14", "camt.054.001.14"]
message_families: ["camt.053", "camt.054"]
search_terms: ["Scenario 3", "Account Owner", "Recipient"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Business conditions and source contradictions are separate from XML validation."]
manual_curated: true
review_date: "2026-11-09"
source_flow_review: "pass"
---





# Scenario 3

Source context: Bank-to-Customer Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Recipient | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-recipient.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P138** This scenario shows that the Bank to Customer Cash Management messages can also be delivered to a party authorised by the account owner to receive the account information (that is, the Message Recipient).

Source diagram evidence: [fig-0013](../documents/src-000004/diagrams/fig-0013.md). Canonical source reconstruction and actual review evidence are linked below.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000004](../../../../../../../evidence/omitted/52f543e2b58f688bc16fa140.md). Heading path: BusinessTransactions / Reporting / Scenario 3.

## Curated source flow

The account owner authorises the Recipient to receive account information. The source explicitly allows an internal message for the Recipient-to-Owner legs, so those legs are not guaranteed ISO 20022 exchanges. The diagram contains notification and statement only; no account-report arrow is added. Recipient is not equated with Forwarding Agent.

[Complete source diagram](../diagrams/curated/fig-0013.md).

### Adjacent source narrative

**P138** This scenario shows that the Bank to Customer Cash Management messages can also be delivered to a party authorised by the account owner to receive the account information (that is, the Message Recipient).

Scoped participants: [account owner](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md), [account servicer](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md), [recipient](../../../../../../../shared/reference/participants/participant-src-000004-recipient.md).

[Complete business conditions and source examples](../business-rules.md). Source-defined trigger/preconditions, activities, responsibilities and alternatives compared with the linked table/narrative and complete source figure on2026-11-09. Unstated conditions remain unstated.
