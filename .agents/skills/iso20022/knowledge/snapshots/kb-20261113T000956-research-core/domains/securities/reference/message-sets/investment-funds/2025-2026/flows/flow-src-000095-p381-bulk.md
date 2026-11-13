---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p381-bulk"
title: "Order and Confirmation / Subscription  / Bulk"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation", "Subscription ", "Bulk"], "locator": "/w:document/w:body/w:p[381]", "paragraph_id": "P381", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation", "Subscription ", "Bulk"], "locator": "/w:document/w:body/w:p[382]", "paragraph_id": "P382", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation", "Subscription ", "Bulk"], "locator": "/w:document/w:body/w:p[383]", "paragraph_id": "P383", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation", "Subscription ", "Bulk"], "locator": "/w:document/w:body/w:p[384]", "paragraph_id": "P384", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation", "Subscription ", "Bulk"], "locator": "/w:document/w:body/w:p[385]", "paragraph_id": "P385", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation", "Subscription ", "Bulk"], "locator": "/w:document/w:body/w:p[386]", "paragraph_id": "P386", "table_id": null}]
participants: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[8]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2523; 47 setr.007.001.05 SubscriptionBulkOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[10]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2766; 49 setr.009.001.05 SubscriptionBulkOrderConfirmationV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[11]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3001; 50 setr.010.001.05 SubscriptionOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[13]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3248; 52 setr.012.001.06 SubscriptionOrderConfirmationV06"}]
message_ids: []
message_families: ["setr.007", "setr.009", "setr.010", "setr.012"]
search_terms: ["Bulk", "Instructing Party", "Executing Party", "Transfer Agent", "Intermediary", "setr.007", "setr.009", "setr.010", "setr.012"]
limitations: ["Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.", "Part1 message names/families do not establish exact versions; use maintained Part2/schema references.", "Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition."]
manual_curated: true
participant_ids: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0050.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Complete source-delimited narrative and literal diagram messages/directions checked; institutional examples retained separately."}
---

# Order and Confirmation / Subscription  / Bulk

[src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md); source heading P381, direct-body paragraph P386.

## Purpose, trigger and common conditions

**P361** This message flow section illustrates the use of the order and confirmation messages in typical message sequencing scenarios. The different order instructions are sent by the instructing party to the executing party to instruct either a subscription, a redemption or a switch.

**P362** The order confirmation messages are sent by the executing party to the instructing party to the confirm the execution of a subscription or a redemption or a switch.

**P363** The order status messages are sent by the executing party to the instructing party to the provide the status of the order instructions. Use of this optional message is shown in the next section.

**P364** There may be one or more intermediaries in the transaction chain.

**P365** The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent.

**P366** The intermediary party is, for example, a distributor.

The source-specific trigger, acceptance conditions, outcomes and optional/failure paths are preserved in the ordered narrative below. A separate formal precondition/postcondition is asserted only where the source supplies one.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [distributor](../../../../../../../shared/reference/participants/participant-src-000095-distributor.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [executing party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | Explicit figure sender/receiver; see step table. |
| [instructing party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | Explicit figure sender/receiver; see step table. |
| [intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | Explicit figure sender/receiver; see step table. |
| [investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [transfer agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |


## Ordered activities and source-defined alternatives

**P382** Instructing party 1 sends a SubscriptionOrder to the intermediary party. Instructing party 2 sends a SubscriptionOrder to the intermediary party.

**P383** The intermediary party collects the individual orders. As the orders sent by instructing parties 1 and 2 are for the same financial instrument, the orders are grouped together and the intermediary sends a SubscriptionBulkOrder to the transfer agent.

**P384** The executing party sends a SubscriptionBulkOrderConfirmation to the intermediary party.

**P385** The intermediary party splits up the confirmation according to the originating chain of instructions and sends a SubscriptionOrderConfirmation to instructing party 1 and a SubscriptionOrderConfirmation to instructing party 2.

### fig-0050

[Literal source sequence and visual review](../diagrams/funds-processes/fig-0050.md) (Word file page 56).

| Step | Sender | Receiver | Source message label |
| --- | --- | --- | --- |
| 1 | [Instructing Party 1](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | SubscriptionOrder |
| 2 | [Instructing Party 2](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | SubscriptionOrder |
| 3 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | SubscriptionBulkOrder |
| 4 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | SubscriptionBulkOrderConfirmation |
| 5 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Instructing Party 2](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | SubscriptionOrderConfirmation |
| 6 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Instructing Party 1](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | SubscriptionOrderConfirmation |



## Message definitions and related paths

| Family | Supplied exact definition | Scope |
| --- | --- | --- |
| setr.007 | [setr.007.001.05](../../../../messages/setr.007.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.009 | [setr.009.001.05](../../../../messages/setr.009.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.010 | [setr.010.001.05](../../../../messages/setr.010.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.012 | [setr.012.001.06](../../../../messages/setr.012.001.06/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |


## Outcomes and source qualifications

- Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.
- Part1 message names/families do not establish exact versions; use maintained Part2/schema references.
- Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition.

The narrative gives each outcome: execution confirmation, accepted/pending status, reporting/replacement, rejection or cancellation as applicable. These outcomes are not interchanged. For cancellation, CAND concerns completion of the requested cancellation; order acceptance (PACK) does not assert execution.

## Review

Source narrative, participant roles and every depicted message direction were compared with the original picture and Word-rendered page on 2026-11-09. The bounded flow scope is reviewed; referenced schemas and tables retain their own statuses.
