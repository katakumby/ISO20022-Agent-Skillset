---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
flow_id: "flow-src-000004-p144-direct-scenario"
title: "Direct Scenario"
source_locations: [{"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting Request to Account Servicer", "Direct Scenario"], "locator": "/w:document/w:body/w:p[144]", "paragraph_id": "P144", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting Request to Account Servicer", "Direct Scenario"], "locator": "/w:document/w:body/w:p[145]", "paragraph_id": "P145", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting Request to Account Servicer", "Direct Scenario"], "locator": "/w:document/w:body/w:p[146]", "paragraph_id": "P146", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting Request to Account Servicer", "Direct Scenario"], "locator": "/w:document/w:body/w:p[147]", "paragraph_id": "P147", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting Request to Account Servicer", "Direct Scenario"], "locator": "/w:document/w:body/w:p[148]", "paragraph_id": "P148", "table_id": null}]
participants: ["participant-src-000004-account-owner", "participant-src-000004-account-servicer"]
message_mapping_evidence: [{"source_id": "src-000004", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Request "], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}]
message_ids: ["camt.052.001.14", "camt.053.001.14", "camt.054.001.14", "camt.060.001.07"]
message_families: ["camt.052", "camt.053", "camt.054", "camt.060"]
search_terms: ["Direct Scenario", "Account Owner", "camt.060"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Business conditions and source contradictions are separate from XML validation."]
manual_curated: true
review_date: "2026-11-09"
source_flow_review: "pass"
---





# Direct Scenario

Source context: Bank-to-Customer Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P145** In this scenario, an account owner requests a statement directly from its account servicing institution.

**P146** The account owner sends the AccountReportingRequest directly to its account serving institution.

**P147** The account servicing institution sends the requested message to the account owner.

Source diagram evidence: [fig-0015](../documents/src-000004/diagrams/fig-0015.md). Canonical source reconstruction and actual review evidence are linked below.

## Messages and alternative paths

Source-supported message family mentions: `camt.060`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000004](../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart1_BankToCustomerCashManagement_2025_2026_v2.docx). Heading path: BusinessTransactions / Reporting Request to Account Servicer / Direct Scenario.

## Curated source flow

The owner requests reporting directly; the servicer sends the requested definition to the owner. The three drawn return arrows enumerate available message definitions; the annotation makes selection dependent on the request. They are not a source requirement to send all three. The order and annotation are retained without inventing explicit alt frames absent from the original.

[Complete source diagram](../diagrams/curated/fig-0015.md).

### Adjacent source narrative

**P145** In this scenario, an account owner requests a statement directly from its account servicing institution.

**P146** The account owner sends the AccountReportingRequest directly to its account serving institution.

**P147** The account servicing institution sends the requested message to the account owner.

Scoped participants: [account owner](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md), [account servicer](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md).

[Complete business conditions and source examples](../business-rules.md). Source-defined trigger/preconditions, activities, responsibilities and alternatives compared with the linked table/narrative and complete source figure on2026-11-09. Unstated conditions remain unstated.
