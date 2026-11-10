---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p491-scenarios-for-confirmations-when-multiple-orders-specified-in-a-single"
title: "Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message"], "locator": "/w:document/w:body/w:p[491]", "paragraph_id": "P491", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message"], "locator": "/w:document/w:body/w:p[492]", "paragraph_id": "P492", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message"], "locator": "/w:document/w:body/w:p[493]", "paragraph_id": "P493", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message"], "locator": "/w:document/w:body/w:p[494]", "paragraph_id": "P494", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message"], "locator": "/w:document/w:body/w:p[495]", "paragraph_id": "P495", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message"], "locator": "/w:document/w:body/w:p[496]", "paragraph_id": "P496", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message"], "locator": "/w:document/w:body/w:p[497]", "paragraph_id": "P497", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message"], "locator": "/w:document/w:body/w:p[498]", "paragraph_id": "P498", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message"], "locator": "/w:document/w:body/w:p[499]", "paragraph_id": "P499", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message"], "locator": "/w:document/w:body/w:p[500]", "paragraph_id": "P500", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message"], "locator": "/w:document/w:body/w:p[501]", "paragraph_id": "P501", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message"], "locator": "/w:document/w:body/w:p[502]", "paragraph_id": "P502", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message"], "locator": "/w:document/w:body/w:p[503]", "paragraph_id": "P503", "table_id": null}]
participants: ["participant-src-000095-executing-party", "participant-src-000095-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[5]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2101; 44 setr.004.001.05 RedemptionOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[7]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2310; 46 setr.006.001.06 RedemptionOrderConfirmationV06"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[11]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3001; 50 setr.010.001.05 SubscriptionOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[13]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3248; 52 setr.012.001.06 SubscriptionOrderConfirmationV06"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[2]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4109; 56 setr.016.001.05 OrderInstructionStatusReportV05"}]
message_ids: []
message_families: ["setr.004", "setr.006", "setr.010", "setr.012", "setr.016"]
search_terms: ["Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message", "Executing Party", "setr.004", "setr.006", "setr.010", "setr.012", "setr.016"]
limitations: ["Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.", "P498 intentionally omits OrderInstructionStatusReport. P499 says waiting for all executions can delay confirmation of earlier trade dates. Source colours: Order1 green, Order2 cyan, Order3 red.", "Part1 message names/families do not establish exact versions; use maintained Part2/schema references.", "Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition.", "Source colours distinguish Order1 green, Order2 cyan and Order3 red; explicit textual identities are retained.", "Source left icon is unlabelled; its displayed explanatory label is not source text. The instructing role comes from enclosing narrative. Dates are illustrative source dates without a year. P502 intentionally omits OrderInstructionStatusReport. Source order colours1–6: green, cyan, red, blue, brown, purple."]
manual_curated: true
participant_ids: ["participant-src-000095-executing-party", "participant-src-000095-instructing-party"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0069.md", "domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0070.md", "domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0071.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Complete source-delimited narrative and literal diagram messages/directions checked; institutional examples retained separately."}
---

# Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message

[src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx); source heading P491, direct-body paragraph P495, direct-body paragraph P497, direct-body paragraph P501.

## Purpose, trigger and common conditions

**P492** The SubscriptionOrder (setr.010), RedemptionOrder (setr.004), SubscriptionOrderConfirmation (setr.012) and RedemptionOrderConfirmation (setr.006) messages all allow the specification of one or more individual orders or order executions for the same investment account.

**P493** The following section shows the various possibilities.

The source-specific trigger, acceptance conditions, outcomes and optional/failure paths are preserved in the ordered narrative below. A separate formal precondition/postcondition is asserted only where the source supplies one.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [executing party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | Explicit figure sender/receiver; see step table. |
| [instructing party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | Explicit figure sender/receiver; see step table. |


## Ordered activities and source-defined alternatives

**P492** The SubscriptionOrder (setr.010), RedemptionOrder (setr.004), SubscriptionOrderConfirmation (setr.012) and RedemptionOrderConfirmation (setr.006) messages all allow the specification of one or more individual orders or order executions for the same investment account.

**P493** The following section shows the various possibilities.

**P494** [1]	Some institutions send more than one individual order per message. Most institutions, on receipt of a ‘multiple’ order will respond with individual status and confirmation messages:

**P496** [2]	Some institutions send more than one individual order per message. Some institutions will send back a single confirmation message with all the executions for the order:

**P498** The OrderInstructionStatusReport (setr.016) message is not shown on the diagram.

**P499** This means the ‘order executing party' will wait until all orders are executed and then send a single SubscriptionOrderConfirmation (setr.012) message with the three individual executions. Because the trade dates may be different this could mean a delay for those orders that are executed on an earlier trade date.

**P500** [3]	Some institutions offer full flexibility and will, for example, send a ‘combination’ depending on the trade date cycles of the investment funds in the order message.

**P502** The OrderInstructionStatusReport (setr.016) message is not shown on the diagram.

**P503** An institution could decide ‘it’s always single a confirmation message per order’ or the institution could offer flexibility.

### fig-0069

[Literal source sequence and visual review](../diagrams/funds-processes/fig-0069.md) (Word file page 67).

| Step | Sender | Receiver | Source message label |
| --- | --- | --- | --- |
| 1 | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | SubscriptionOrder with Order1, Order2, and Order3 |
| 2 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | OrderInstructionStatusReport for Order1 |
| 3 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | OrderInstructionStatusReport for Order2 |
| 4 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | OrderInstructionStatusReport for Order3 |
| 5 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | SubscriptionOrderConfirmation for Order1 |
| 6 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | SubscriptionOrderConfirmation for Order2 |
| 7 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | SubscriptionOrderConfirmation for Order3 |


### fig-0070

[Literal source sequence and visual review](../diagrams/funds-processes/fig-0070.md) (Word file page 67).

| Step | Sender | Receiver | Source message label |
| --- | --- | --- | --- |
| 1 | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | SubscriptionOrder with Order1, Order2, and Order3 |
| 2 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | SubscriptionOrderConfirmation for Order1, Order2, and Order3 |


### fig-0071

[Literal source sequence and visual review](../diagrams/funds-processes/fig-0071.md) (Word file page 68).

| Step | Sender | Receiver | Source message label |
| --- | --- | --- | --- |
| 1 | [Unlabelled left participant](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | SubscriptionOrder with Order1, Order2, Order3, Order4, Order5 and Order6 |
| 2 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Unlabelled left participant](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | SubscriptionOrderConfirmation 27 July for Order3 |
| 3 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Unlabelled left participant](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | SubscriptionOrderConfirmation 30 July for Order4 and Order5 |
| 4 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Unlabelled left participant](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | SubscriptionOrderConfirmation 3 August for Order1, Order2 and Order6 |



## Message definitions and related paths

| Family | Supplied exact definition | Scope |
| --- | --- | --- |
| setr.004 | [setr.004.001.05](../../../../messages/setr.004.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.006 | [setr.006.001.06](../../../../messages/setr.006.001.06/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.010 | [setr.010.001.05](../../../../messages/setr.010.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.012 | [setr.012.001.06](../../../../messages/setr.012.001.06/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.016 | [setr.016.001.05](../../../../messages/setr.016.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |


## Outcomes and source qualifications

- Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.
- P498 intentionally omits OrderInstructionStatusReport. P499 says waiting for all executions can delay confirmation of earlier trade dates. Source colours: Order1 green, Order2 cyan, Order3 red.
- Part1 message names/families do not establish exact versions; use maintained Part2/schema references.
- Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition.
- Source colours distinguish Order1 green, Order2 cyan and Order3 red; explicit textual identities are retained.
- Source left icon is unlabelled; its displayed explanatory label is not source text. The instructing role comes from enclosing narrative. Dates are illustrative source dates without a year. P502 intentionally omits OrderInstructionStatusReport. Source order colours1–6: green, cyan, red, blue, brown, purple.

The narrative gives each outcome: execution confirmation, accepted/pending status, reporting/replacement, rejection or cancellation as applicable. These outcomes are not interchanged. For cancellation, CAND concerns completion of the requested cancellation; order acceptance (PACK) does not assert execution.

## Review

Source narrative, participant roles and every depicted message direction were compared with the original picture and Word-rendered page on 2026-11-09. The bounded flow scope is reviewed; referenced schemas and tables retain their own statuses.
