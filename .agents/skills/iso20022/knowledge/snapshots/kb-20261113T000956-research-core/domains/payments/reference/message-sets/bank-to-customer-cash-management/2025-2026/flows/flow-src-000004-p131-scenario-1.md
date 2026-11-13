---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
flow_id: "flow-src-000004-p131-scenario-1"
title: "Scenario 1"
source_locations: [{"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting", "Scenario 1"], "locator": "/w:document/w:body/w:p[131]", "paragraph_id": "P131", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting", "Scenario 1"], "locator": "/w:document/w:body/w:p[132]", "paragraph_id": "P132", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting", "Scenario 1"], "locator": "/w:document/w:body/w:p[133]", "paragraph_id": "P133", "table_id": null}]
participants: ["participant-src-000004-account-owner", "participant-src-000004-account-servicer"]
message_mapping_evidence: [{"source_id": "src-000004", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Reporting "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000004", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Reporting "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["camt.052.001.14", "camt.053.001.14"]
message_families: ["camt.052", "camt.053"]
search_terms: ["Scenario 1", "Account Servicer", "Account Owner", "camt.052", "camt.053"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Business conditions and source contradictions are separate from XML validation."]
manual_curated: true
review_date: "2026-11-09"
source_flow_review: "pass"
---





# Scenario 1

Source context: Bank-to-Customer Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P132** The following service has been agreed between account owner and account servicer: During the day, the account servicer sends one or more BankToCustomerAccountReport messages to inform the account owner of any intraday movements (booked and pending) on the account. At the end of the business day, the account servicer summarises all booked entries in the BankToCustomerStatement and provides booked and available balance information.

Source diagram evidence: [fig-0011](../documents/src-000004/diagrams/fig-0011.md). Canonical source reconstruction and actual review evidence are linked below.

## Messages and alternative paths

Source-supported message family mentions: `camt.052`, `camt.053`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000004](../../../../../../../evidence/omitted/52f543e2b58f688bc16fa140.md). Heading path: BusinessTransactions / Reporting / Scenario 1.

## Curated source flow

Under the agreed service, one or more intraday reports provide booked and pending movements; at end of business day the statement summarises all booked entries and provides booked and available balances. Both arrows run Account Servicer to Account Owner. Source names are resolved to the four exact definitions listed in this edition and companion Part2; no version comparison is inferred.

[Complete source diagram](../diagrams/curated/fig-0011.md).

### Adjacent source narrative

**P132** The following service has been agreed between account owner and account servicer: During the day, the account servicer sends one or more BankToCustomerAccountReport messages to inform the account owner of any intraday movements (booked and pending) on the account. At the end of the business day, the account servicer summarises all booked entries in the BankToCustomerStatement and provides booked and available balance information.

Scoped participants: [account owner](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md), [account servicer](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md).

[Complete business conditions and source examples](../business-rules.md). Source-defined trigger/preconditions, activities, responsibilities and alternatives compared with the linked table/narrative and complete source figure on2026-11-09. Unstated conditions remain unstated.
