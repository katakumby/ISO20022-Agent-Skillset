---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p915-statements"
title: "Statements"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Statements"], "locator": "/w:document/w:body/w:p[915]", "paragraph_id": "P915", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Statements"], "locator": "/w:document/w:body/w:p[916]", "paragraph_id": "P916", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Statements"], "locator": "/w:document/w:body/w:p[917]", "paragraph_id": "P917", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Statements"], "locator": "/w:document/w:body/w:p[918]", "paragraph_id": "P918", "table_id": null}]
participants: ["participant-src-000095-transfer-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Statements", "Transfer Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Statements

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P916** This message flow section illustrates the use of the statement messages in typical message sequencing scenarios. The statement messages are sent by an account servicer to the account owner. 

**P917** Typically, a statement is sent according to the Service Level Agreement (SLA) held between the account servicer and the account owner. This SLA sets the parameters around the frequency at which the statement message is sent, for example, daily, weekly, intra-day.

**P918** The account owner is, for example, an investment manager or its authorised representative. The account servicer is, for example, a transfer agent.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Heading path: BusinessTransactions / Statements.
