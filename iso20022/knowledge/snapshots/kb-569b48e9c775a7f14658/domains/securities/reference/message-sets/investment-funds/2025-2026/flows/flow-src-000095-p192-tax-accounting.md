---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p192-tax-accounting"
title: "Tax Accounting"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[192]", "paragraph_id": "P192", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[28]", "paragraph_id": null, "table_id": "T28"}]
participants: ["participant-src-000095-fund-accountant", "participant-src-000095-transfer-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Tax Accounting", "Fund Accountant", "Transfer Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Tax Accounting

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Calculation and identification of taxable income, taxable profits and losses pursuant to liquidation of an investment, determination of the allocation of net proceeds into categories such as taxable, tax-exempt, tax-deferred; determination of the holding period of an investment and calculation of whether it qualifies for preferential treatment due to long-term holdings.

Evidence: [T28](../documents/src-000095/tables/tbl-0028.md), source row 2.

### Trigger

annual, on request, per service level agreement (SLA) 
upon completion of a transaction
regulatory deadline to declare taxes is reached

Evidence: [T28](../documents/src-000095/tables/tbl-0028.md), source row 3.

### Pre-conditions

historical information is available
taxation authority has been identified
tax position is known
holding or transaction exists

Evidence: [T28](../documents/src-000095/tables/tbl-0028.md), source row 4.

### Post-conditions

Tax liability is known

Evidence: [T28](../documents/src-000095/tables/tbl-0028.md), source row 5.

### Role

Fund accountant/transfer agent

Evidence: [T28](../documents/src-000095/tables/tbl-0028.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Fund Accountant | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-fund-accountant.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T28](../documents/src-000095/tables/tbl-0028.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Heading path: BusinessProcess Description.
