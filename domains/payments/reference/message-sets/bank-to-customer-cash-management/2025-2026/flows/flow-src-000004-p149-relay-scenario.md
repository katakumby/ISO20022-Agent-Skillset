---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
flow_id: "flow-src-000004-p149-relay-scenario"
title: "Relay Scenario"
source_locations: [{"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting Request to Account Servicer", "Relay Scenario"], "locator": "/w:document/w:body/w:p[149]", "paragraph_id": "P149", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting Request to Account Servicer", "Relay Scenario"], "locator": "/w:document/w:body/w:p[150]", "paragraph_id": "P150", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting Request to Account Servicer", "Relay Scenario"], "locator": "/w:document/w:body/w:p[151]", "paragraph_id": "P151", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting Request to Account Servicer", "Relay Scenario"], "locator": "/w:document/w:body/w:p[152]", "paragraph_id": "P152", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting Request to Account Servicer", "Relay Scenario"], "locator": "/w:document/w:body/w:p[153]", "paragraph_id": "P153", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting Request to Account Servicer", "Relay Scenario"], "locator": "/w:document/w:body/w:p[154]", "paragraph_id": "P154", "table_id": null}]
participants: ["participant-src-000004-account-owner", "participant-src-000004-account-servicer", "participant-src-000004-forwarding-agent"]
message_mapping_evidence: [{"source_id": "src-000004", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Request "], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}]
message_ids: ["camt.052.001.14", "camt.053.001.14", "camt.054.001.14", "camt.060.001.07"]
message_families: ["camt.052", "camt.053", "camt.054", "camt.060"]
search_terms: ["Relay Scenario", "Forwarding Agent", "Account Owner", "camt.060"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Business conditions and source contradictions are separate from XML validation."]
manual_curated: true
review_date: "2026-11-09"
source_flow_review: "pass"
---





# Relay Scenario

Source context: Bank-to-Customer Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Forwarding Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-forwarding-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P150** An account owner wishes to request its account servicing institution to send a statement of the account owner's account however, the account owner uses a forwarding agent for all its communication with the account servicing institution.

**P151** The account owner sends the AccountReportingRequest to the forwarding agent or requests a forwarding agent to issue an AccountReportingRequest.

**P152** The forwarding agent forwards the AccountReportingRequest to the account servicing institution.

**P153** The account servicing institution sends the requested message to the forwarding agent- The forwarding agent forwards the message to the account owner.

Source diagram evidence: [fig-0016](../documents/src-000004/diagrams/fig-0016.md). Canonical source reconstruction and actual review evidence are linked below.

## Messages and alternative paths

Source-supported message family mentions: `camt.060`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000004](../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart1_BankToCustomerCashManagement_2025_2026_v2.docx). Heading path: BusinessTransactions / Reporting Request to Account Servicer / Relay Scenario.

## Curated source flow

The owner communicates with the servicer through a Forwarding Agent. P151 permits the owner either to send an AccountReportingRequest to that agent or request the agent to issue one; the latter request is not assigned an invented XML format. The forwarded request reaches the servicer, which responds through the agent. The same principle applies to statements and debit/credit notifications, as the source note states.

[Complete source diagram](../diagrams/curated/fig-0016.md).

### Adjacent source narrative

**P150** An account owner wishes to request its account servicing institution to send a statement of the account owner's account however, the account owner uses a forwarding agent for all its communication with the account servicing institution.

**P151** The account owner sends the AccountReportingRequest to the forwarding agent or requests a forwarding agent to issue an AccountReportingRequest.

**P152** The forwarding agent forwards the AccountReportingRequest to the account servicing institution.

**P153** The account servicing institution sends the requested message to the forwarding agent- The forwarding agent forwards the message to the account owner.

Scoped participants: [account owner](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md), [account servicer](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md), [forwarding agent](../../../../../../../shared/reference/participants/participant-src-000004-forwarding-agent.md).

[Complete business conditions and source examples](../business-rules.md). Source-defined trigger/preconditions, activities, responsibilities and alternatives compared with the linked table/narrative and complete source figure on2026-11-09. Unstated conditions remain unstated.
