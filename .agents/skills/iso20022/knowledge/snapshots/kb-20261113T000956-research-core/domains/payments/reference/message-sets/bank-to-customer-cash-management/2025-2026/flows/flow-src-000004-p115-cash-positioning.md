---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
flow_id: "flow-src-000004-p115-cash-positioning"
title: "Cash Positioning"
source_locations: [{"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:p[115]", "paragraph_id": "P115", "table_id": null}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:p[116]", "paragraph_id": "P116", "table_id": null}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[14]", "paragraph_id": null, "table_id": "T14"}]
participants: ["participant-src-000004-account-owner", "participant-src-000004-account-servicer", "participant-src-000004-cash-position-evaluation-position", "participant-src-000004-cash-position-evaluation-system", "participant-src-000004-liquidity-system", "participant-src-000004-position-system", "participant-src-000004-reconciliation-system", "participant-src-000004-treasury-system"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Cash Positioning", "Cash Position Evaluation Position", "Cash Position Evaluation System", "Reconciliation System", "Account Servicer", "Liquidity System", "Position System", "Treasury System"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Business conditions and source contradictions are separate from XML validation."]
manual_curated: true
review_date: "2026-11-09"
source_flow_review: "pass"
---





# Cash Positioning

Source context: Bank-to-Customer Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Cash Position Evaluation Position | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-cash-position-evaluation-position.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Cash Position Evaluation System | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-cash-position-evaluation-system.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Reconciliation System | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-reconciliation-system.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Liquidity System | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-liquidity-system.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Position System | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-position-system.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Treasury System | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-treasury-system.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0007](../documents/src-000004/diagrams/fig-0007.md). Canonical source reconstruction and actual review evidence are linked below.

Source table [T14](../documents/src-000004/tables/tbl-0014.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Consolidated data | A number of different sources of actual and forecast information data are collected. | Cash Position Evaluation System  |
| Adjust prior position to actual | Prior position is updated with the information collected: new closing ledger, available and forward balance positions are set. | Cash Position Evaluation Position |
| Set new positions | Prior position is updated with the information collected: new closing ledger, available and forward balance positions are set. | Cash Position Evaluation System  |
| Provide updated balance information | Final balance positions are provided to the investment/liquidity management department. | Cash Position Evaluation Position |
| Collect available funds for investing/funding | All available liquidity is collected throughout the different systems. | Liquidity System |
| Provide investment/funding final amount | Available liquidity is made available to the cash position system. | Liquidity System |
| Provide balance information  | New actual balance information is received from the bank. This includes information on the booked (ledger) balance (closing balance at end of previous day, opening booked balance at start of current day, available and forward available balances. Note: the different balance types that need to be reported on are further discussed in the data requirements chapter. | Account Servicer |
| Provide transaction information | If intraday reporting occurs, additional information on transactions posted to the account is received from the account servicing bank during the day. Intraday balances may be provided, even though intraday balance reconciliation is usually not done. | Account Servicer |
| Provide prior position  | Prior balance position forecast information is received from the position system. | Position System |
| Provide todays reconciled balance | Forecasted balance is reconciled with actual balance information received from the bank. | Reconciliation System |
| Forecast transactions | Expected transaction information is collected. This can be a repetitive activity. | Treasury System |
| Close balance positions | Process terminates once all cash transaction activity ceases for the day, or once funding/investment options are no longer available due to market close. | Cash Position Evaluation System |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000004](../../../../../../../evidence/omitted/52f543e2b58f688bc16fa140.md). Heading path: Description of BusinessActivities.

## Curated source flow

Six lanes and every source information/control arrow are retained. The evaluation system combines five input streams, adjusts positions, provides updated balances to liquidity collection, receives the funding final amount and closes positions. T14 specifies ledger, available and forward balances; intraday transaction reporting may include balances although intraday reconciliation usually is not done. Forecasts may repeat. Closure occurs when cash activity ceases or market close removes funding/investment options. The two literal Cash Position Evaluation Position initiator cells differ from the System lane and other rows; both labels remain scoped under issue-000060, without an unsupported alias merge.

[Complete source diagram](../diagrams/curated/fig-0007.md).

Scoped participants: [account owner](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md), [account servicer](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md), [treasury system](../../../../../../../shared/reference/participants/participant-src-000004-treasury-system.md), [liquidity system](../../../../../../../shared/reference/participants/participant-src-000004-liquidity-system.md), [reconciliation system](../../../../../../../shared/reference/participants/participant-src-000004-reconciliation-system.md), [position system](../../../../../../../shared/reference/participants/participant-src-000004-position-system.md), [cash position evaluation system](../../../../../../../shared/reference/participants/participant-src-000004-cash-position-evaluation-system.md), [cash position evaluation position](../../../../../../../shared/reference/participants/participant-src-000004-cash-position-evaluation-position.md).

[Complete business conditions and source examples](../business-rules.md). Source-defined trigger/preconditions, activities, responsibilities and alternatives compared with the linked table/narrative and complete source figure on2026-11-09. Unstated conditions remain unstated.
