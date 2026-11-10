---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
flow_id: "flow-src-000004-p134-scenario-2"
title: "Scenario 2"
source_locations: [{"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting", "Scenario 2"], "locator": "/w:document/w:body/w:p[134]", "paragraph_id": "P134", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting", "Scenario 2"], "locator": "/w:document/w:body/w:p[135]", "paragraph_id": "P135", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting", "Scenario 2"], "locator": "/w:document/w:body/w:p[136]", "paragraph_id": "P136", "table_id": null}]
participants: ["participant-src-000004-account-owner", "participant-src-000004-account-servicer"]
message_mapping_evidence: [{"source_id": "src-000004", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Reporting "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000004", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Reporting "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000004", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Reporting "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["camt.052.001.14", "camt.053.001.14", "camt.054.001.14"]
message_families: ["camt.052", "camt.053", "camt.054"]
search_terms: ["Scenario 2", "Account Servicer", "Account Owner", "camt.052", "camt.053", "camt.054"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Business conditions and source contradictions are separate from XML validation."]
manual_curated: true
review_date: "2026-11-09"
source_flow_review: "pass"
---





# Scenario 2

Source context: Bank-to-Customer Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P135** The following service has been agreed between account owner and account servicer: During the day, the account servicer will send a BankToCustomerDebitCreditNotification for any incoming credits above a certain threshold. At a pre-agreed time during the day, the account servicer will also provide an intraday BankToCustomerAccountReport, summarising all movements (booked and pending) which have been posted to the account since the start of the business day. The account servicer will also include balance information (booked and expected) in the message. At the end of the business day, the account servicer summarises all booked entries in the BankToCustomerStatement and provides booked and available balance information.

Source diagram evidence: [fig-0012](../documents/src-000004/diagrams/fig-0012.md). Canonical source reconstruction and actual review evidence are linked below.

## Messages and alternative paths

Source-supported message family mentions: `camt.052`, `camt.053`, `camt.054`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000004](../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart1_BankToCustomerCashManagement_2025_2026_v2.docx). Heading path: BusinessTransactions / Reporting / Scenario 2.

## Curated source flow

The agreed service sends notifications for incoming credits above a threshold, an intraday report at a pre-agreed time with all booked/pending movements since business-day start and booked/expected balances, then an end-of-day statement of booked entries with booked/available balances. The threshold is not supplied numerically and is not invented.

[Complete source diagram](../diagrams/curated/fig-0012.md).

### Adjacent source narrative

**P135** The following service has been agreed between account owner and account servicer: During the day, the account servicer will send a BankToCustomerDebitCreditNotification for any incoming credits above a certain threshold. At a pre-agreed time during the day, the account servicer will also provide an intraday BankToCustomerAccountReport, summarising all movements (booked and pending) which have been posted to the account since the start of the business day. The account servicer will also include balance information (booked and expected) in the message. At the end of the business day, the account servicer summarises all booked entries in the BankToCustomerStatement and provides booked and available balance information.

Scoped participants: [account owner](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md), [account servicer](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md).

[Complete business conditions and source examples](../business-rules.md). Source-defined trigger/preconditions, activities, responsibilities and alternatives compared with the linked table/narrative and complete source figure on2026-11-09. Unstated conditions remain unstated.
