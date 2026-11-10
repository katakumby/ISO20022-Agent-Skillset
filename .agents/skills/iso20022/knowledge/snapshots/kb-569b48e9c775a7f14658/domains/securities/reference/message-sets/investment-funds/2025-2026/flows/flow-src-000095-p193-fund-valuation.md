---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p193-fund-valuation"
title: "Fund Valuation"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[193]", "paragraph_id": "P193", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[29]", "paragraph_id": null, "table_id": "T29"}]
participants: ["participant-src-000095-fund-accountant"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Fund Valuation", "Fund Accountant"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Fund Valuation

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The fund accountant calculates the value of assets, liabilities, expenses, income, buy/sell orders etc. of the fund and calculates the total net asset value, the NAV per fund unit, the dealing and unit price(s).

Evidence: [T29](../documents/src-000095/tables/tbl-0029.md), source row 2.

### Trigger

date and time of calculation is reached
fund dependent

Evidence: [T29](../documents/src-000095/tables/tbl-0029.md), source row 3.

### Pre-conditions

calculation method and accounting principles are known from the prospectus
number of units is known
portfolio evaluation is done
quantities and Prices (mid or buy/sell) for all fund assets are know
number of existing units of each class in the fund is known
income and expenses are known
reconciliation completed as required

Evidence: [T29](../documents/src-000095/tables/tbl-0029.md), source row 4.

### Post-conditions

Net Asset Value (NAV) per unit and dealing price are determined

Evidence: [T29](../documents/src-000095/tables/tbl-0029.md), source row 5.

### Role

Fund accountant

Evidence: [T29](../documents/src-000095/tables/tbl-0029.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Fund Accountant | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-fund-accountant.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T29](../documents/src-000095/tables/tbl-0029.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Heading path: BusinessProcess Description.
