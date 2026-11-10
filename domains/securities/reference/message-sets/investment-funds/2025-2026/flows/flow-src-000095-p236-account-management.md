---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p236-account-management"
title: "Account Management"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management"], "locator": "/w:document/w:body/w:p[236]", "paragraph_id": "P236", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management"], "locator": "/w:document/w:body/w:p[237]", "paragraph_id": "P237", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management"], "locator": "/w:document/w:body/w:p[238]", "paragraph_id": "P238", "table_id": null}]
participants: ["participant-src-000095-transfer-agent", "participant-src-000095-custodian"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Account Management", "Transfer Agent", "Custodian"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Account Management

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Custodian | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-custodian.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P237** This message flow section illustrates the use of the account management messages in typical message sequencing scenarios. The account management messages are exchanged between an account owner and an account servicer. There may be one or more intermediaries between the account owner and the account servicer.

**P238** The account owner is, for example, an investor or its designated agent. The account servicer is, for example, a registrar, transfer agent or custodian.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Heading path: BusinessTransactions / Account Management.
