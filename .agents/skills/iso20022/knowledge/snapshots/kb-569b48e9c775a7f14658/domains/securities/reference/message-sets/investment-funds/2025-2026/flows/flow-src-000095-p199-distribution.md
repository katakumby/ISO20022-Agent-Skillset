---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p199-distribution"
title: "Distribution"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[199]", "paragraph_id": "P199", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[34]", "paragraph_id": null, "table_id": "T34"}]
participants: ["participant-src-000095-fund-accountant", "participant-src-000095-transfer-agent", "participant-src-000095-intermediary"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Distribution", "Fund Accountant", "Transfer Agent", "Intermediary"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Distribution

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The fund accountant calculates the benefits payable to the unit holders in the fund and announces it accordingly. The transfer agent/registrar/intermediary calculates at shareholder level the amount of distribution. The shareholder has instructed or will instruct to have the distribution paid in cash or reinvested. 

Evidence: [T34](../documents/src-000095/tables/tbl-0034.md), source row 2.

### Trigger

Entitlement date reached

Evidence: [T34](../documents/src-000095/tables/tbl-0034.md), source row 3.

### Pre-conditions

fund exists
prospectus dependent
decision by the fund company during the AGM to have a distribution

Evidence: [T34](../documents/src-000095/tables/tbl-0034.md), source row 4.

### Post-conditions

distribution is processed
payment of cash dividend and/or execution of the dividend reinvestment are initiated
tax reporting is initiated

Evidence: [T34](../documents/src-000095/tables/tbl-0034.md), source row 5.

### Role

Account servicer

Evidence: [T34](../documents/src-000095/tables/tbl-0034.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Fund Accountant | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-fund-accountant.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Intermediary | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T34](../documents/src-000095/tables/tbl-0034.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Heading path: BusinessProcess Description.
