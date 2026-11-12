---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p374-intermediary"
title: "Order and Confirmation / Subscription  / Intermediary"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation", "Subscription ", "Intermediary"], "locator": "/w:document/w:body/w:p[374]", "paragraph_id": "P374", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation", "Subscription ", "Intermediary"], "locator": "/w:document/w:body/w:p[375]", "paragraph_id": "P375", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation", "Subscription ", "Intermediary"], "locator": "/w:document/w:body/w:p[376]", "paragraph_id": "P376", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation", "Subscription ", "Intermediary"], "locator": "/w:document/w:body/w:p[377]", "paragraph_id": "P377", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation", "Subscription ", "Intermediary"], "locator": "/w:document/w:body/w:p[378]", "paragraph_id": "P378", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation", "Subscription ", "Intermediary"], "locator": "/w:document/w:body/w:p[379]", "paragraph_id": "P379", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation", "Subscription ", "Intermediary"], "locator": "/w:document/w:body/w:p[380]", "paragraph_id": "P380", "table_id": null}]
participants: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[11]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3001; 50 setr.010.001.05 SubscriptionOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[13]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3248; 52 setr.012.001.06 SubscriptionOrderConfirmationV06"}]
message_ids: []
message_families: ["setr.010", "setr.012"]
search_terms: ["Intermediary", "Instructing Party", "Executing Party", "Intermediary", "setr.010", "setr.012"]
limitations: ["Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.", "Part1 message names/families do not establish exact versions; use maintained Part2/schema references.", "Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition."]
manual_curated: true
participant_ids: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0048.md", "domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0049.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Complete source-delimited narrative and literal diagram messages/directions checked; institutional examples retained separately."}
---

# Order and Confirmation / Subscription  / Intermediary

[src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md); source heading P374, direct-body paragraph P378, direct-body paragraph P380.

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

**P375** An instructing party sends a SubscriptionOrder message to the intermediary party. The intermediary party sends a SubscriptionOrder message to the executing party.

**P376** To confirm execution of the order, the executing party sends a SubscriptionOrderConfirmation message to the intermediary party. In turn, the intermediary party sends a SubscriptionOrderConfirmation message to the instructing party.

**P377** When more than one order is sent within the same order message, the response to the SubscriptionOrder message may be more than one SubscriptionOrderConfirmation message, as the valuation cycle of the financial instruments of each individual order may be different.

**P379** When more than one order is sent within the same order message, the response to the SubscriptionOrder message may be more than one SubscriptionOrderConfirmation message, as the valuation cycle of the financial instruments of each individual order may be different.

### fig-0048

[Literal source sequence and visual review](../diagrams/funds-processes/fig-0048.md) (Word file page 55).

| Step | Sender | Receiver | Source message label |
| --- | --- | --- | --- |
| 1 | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | SubscriptionOrder |
| 2 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | SubscriptionOrder |
| 3 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | SubscriptionOrderConfirmation |
| 4 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | SubscriptionOrderConfirmation |


### fig-0049

[Literal source sequence and visual review](../diagrams/funds-processes/fig-0049.md) (Word file page 55).

| Step | Sender | Receiver | Source message label |
| --- | --- | --- | --- |
| 1 | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | SubscriptionOrder (2 ISINs) |
| 2 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | SubscriptionOrder (2 ISINs) |
| 3 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | SubscriptionOrderConfirmation (1st ISIN) |
| 4 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | SubscriptionOrderConfirmation (1st ISIN) |
| 5 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | SubscriptionOrderConfirmation (2nd ISIN) |
| 6 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | SubscriptionOrderConfirmation (2nd ISIN) |



## Message definitions and related paths

| Family | Supplied exact definition | Scope |
| --- | --- | --- |
| setr.010 | [setr.010.001.05](../../../../messages/setr.010.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.012 | [setr.012.001.06](../../../../messages/setr.012.001.06/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |


## Outcomes and source qualifications

- Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.
- Part1 message names/families do not establish exact versions; use maintained Part2/schema references.
- Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition.

The narrative gives each outcome: execution confirmation, accepted/pending status, reporting/replacement, rejection or cancellation as applicable. These outcomes are not interchanged. For cancellation, CAND concerns completion of the requested cancellation; order acceptance (PACK) does not assert execution.

## Review

Source narrative, participant roles and every depicted message direction were compared with the original picture and Word-rendered page on 2026-11-09. The bounded flow scope is reviewed; referenced schemas and tables retain their own statuses.
