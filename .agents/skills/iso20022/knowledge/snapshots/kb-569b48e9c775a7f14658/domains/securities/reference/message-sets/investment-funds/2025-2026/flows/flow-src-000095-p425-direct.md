---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p425-direct"
title: "Order Instruction Status Reporting / Subscription / Direct"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Instruction Status Reporting", "Subscription", "Direct"], "locator": "/w:document/w:body/w:p[425]", "paragraph_id": "P425", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Instruction Status Reporting", "Subscription", "Direct"], "locator": "/w:document/w:body/w:p[426]", "paragraph_id": "P426", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Instruction Status Reporting", "Subscription", "Direct"], "locator": "/w:document/w:body/w:p[427]", "paragraph_id": "P427", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Instruction Status Reporting", "Subscription", "Direct"], "locator": "/w:document/w:body/w:p[428]", "paragraph_id": "P428", "table_id": null}]
participants: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[11]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3001; 50 setr.010.001.05 SubscriptionOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[2]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4109; 56 setr.016.001.05 OrderInstructionStatusReportV05"}]
message_ids: []
message_families: ["setr.010", "setr.016"]
search_terms: ["Direct", "Instructing Party", "Executing Party", "setr.010", "setr.016"]
limitations: ["Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.", "P427: conditional acceptance awaits enough cash to execute the subscription.", "Part1 message names/families do not establish exact versions; use maintained Part2/schema references.", "Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition."]
manual_curated: true
participant_ids: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0058.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Complete source-delimited narrative and literal diagram messages/directions checked; institutional examples retained separately."}
---

# Order Instruction Status Reporting / Subscription / Direct

[src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md); source heading P425, direct-body paragraph P428.

## Purpose, trigger and common conditions

**P416** This message flow section illustrates the use of the OrderInstructionStatusReport message in typical message sequencing scenarios. The OrderInstructionStatusReport message is sent by the executing party to the instructing party. It is used to inform the instructing party of the status of its order/s or order message.

**P417** There may be one or more intermediaries in the transaction chain.

**P418** Different message flows may exist depending on the service level agreement (SLA). These include:

**P419** how frequently an order instruction status message must be sent,

**P420** when, and if, an order instruction status message must be sent at a pre-defined time (at cut-off time or once a day) or upon request,

**P421** which statuses will be sent, for example, 'rejected only', 'received and rejected only’, ‘sent to next party’ and accepted only’.

**P422** The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent.

**P423** The intermediary party is, for example, a distributor.

The source-specific trigger, acceptance conditions, outcomes and optional/failure paths are preserved in the ordered narrative below. A separate formal precondition/postcondition is asserted only where the source supplies one.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [distributor](../../../../../../../shared/reference/participants/participant-src-000095-distributor.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [executing party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | Explicit figure sender/receiver; see step table. |
| [instructing party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | Explicit figure sender/receiver; see step table. |
| [investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [transfer agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |


## Ordered activities and source-defined alternatives

**P426** The instructing party sends a SubscriptionOrder message to the executing party.

**P427** As the execution of the order in the SubscriptionOrder message is pending until there is enough cash in the account to pay for the subscription, the executing party responds with an OrderInstructionStatusReport message, with the status ConditionallyAccepted, and awaiting money.

### fig-0058

[Literal source sequence and visual review](../diagrams/funds-processes/fig-0058.md) (Word file page 60).

| Step | Sender | Receiver | Source message label |
| --- | --- | --- | --- |
| 1 | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | SubscriptionOrder |
| 2 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | OrderInstructionStatusReport &lt;CndlyAccptd&gt; |



## Message definitions and related paths

| Family | Supplied exact definition | Scope |
| --- | --- | --- |
| setr.010 | [setr.010.001.05](../../../../messages/setr.010.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.016 | [setr.016.001.05](../../../../messages/setr.016.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |


## Outcomes and source qualifications

- Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.
- P427: conditional acceptance awaits enough cash to execute the subscription.
- Part1 message names/families do not establish exact versions; use maintained Part2/schema references.
- Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition.

The narrative gives each outcome: execution confirmation, accepted/pending status, reporting/replacement, rejection or cancellation as applicable. These outcomes are not interchanged. For cancellation, CAND concerns completion of the requested cancellation; order acceptance (PACK) does not assert execution.

## Review

Source narrative, participant roles and every depicted message direction were compared with the original picture and Word-rendered page on 2026-11-09. The bounded flow scope is reviewed; referenced schemas and tables retain their own statuses.
