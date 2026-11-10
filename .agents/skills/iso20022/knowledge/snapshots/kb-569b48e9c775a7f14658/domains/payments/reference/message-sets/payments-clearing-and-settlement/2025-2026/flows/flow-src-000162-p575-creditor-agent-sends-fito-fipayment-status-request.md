---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p575-creditor-agent-sends-fito-fipayment-status-request"
title: "Creditor Agent sends FIToFIPaymentStatusRequest"
source_locations: [{"source_id": "src-000162", "locator": "/w:document/w:body/w:p[575]", "paragraph_id": "P575", "heading_path": ["BusinessTransactions", "Direct Debit", "Creditor Agent sends FIToFIPaymentStatusRequest"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[576]", "paragraph_id": "P576", "heading_path": ["BusinessTransactions", "Direct Debit", "Creditor Agent sends FIToFIPaymentStatusRequest"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[577]", "paragraph_id": "P577", "heading_path": ["BusinessTransactions", "Direct Debit", "Creditor Agent sends FIToFIPaymentStatusRequest"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[578]", "paragraph_id": "P578", "heading_path": ["BusinessTransactions", "Direct Debit", "Creditor Agent sends FIToFIPaymentStatusRequest"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[579]", "paragraph_id": "P579", "heading_path": ["BusinessTransactions", "Direct Debit", "Creditor Agent sends FIToFIPaymentStatusRequest"]}]
participants: ["participant-src-000162-clearing-and-settlement-agent", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[4]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[5]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pacs.002", "pacs.003", "pacs.009", "pacs.028"]
search_terms: ["Creditor Agent sends FIToFIPaymentStatusRequest", "Financial Institution", "Creditor Agent", "pacs.002", "pacs.003", "pacs.009", "pacs.028"]
limitations: ["Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.", "P576 requires status response referring to original; no response arrow is drawn. P578 literally refers to FinancialInstitutionCreditTransfer despite DD section/figure (issue-000054).", "Source message names establish family-level flow context; supplied exact schema versions are separately identified.", "Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible."]
manual_curated: true
participant_ids: ["participant-src-000162-clearing-and-settlement-agent", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/diagrams/clearing/fig-0043.md"]
issue_ids: ["issue-000054"]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and whole Word figure pages compared; source tables retain independent review."}
message_reference_scope: "Part1 name/family flow; no exact version inferred from picture."
---

# Creditor Agent sends FIToFIPaymentStatusRequest

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and preconditions

Request a missing processability status for the original payment.

Expected status has not arrived within required scheme timeframe, with no final status yet.

## Participants and responsibilities

| Scoped participant | Evidence role |
| --- | --- |
| [clearing and settlement agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-and-settlement-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |


## Source-defined activities and conditions

**P576** In the previous scenarios, the (optional) possibility of confirming the processability of the FIToFICustomerDirectDebit via a FIToFIPaymentStatusReport was always mentioned/included. In some payment schemes, especially referring to real-time payments, the receipt of this FIToFIPaymentStatusReport is crucial within a certain timeframe. In this case, if the FIToFIPaymentStatusReport is not received within the required timeframe, a reminder shall be launched by sending an FIToFIPaymentStatusRequest. The reply message to the FIToFIPaymentStatusRequest shall be a FIToFIPaymentStatusReport referring to the original payment instruction.

**P578** Sending an FIToFIPaymentStatusRequest is possible in all FinancialInstitutionCreditTransfer scenarios described before (section 6.2.2, 6.2.3, 6.2.4, 6.2.5), if no 'final' status is received yet in a FIToFIPaymentStatusReport message.

### fig-0043

[Source reconstruction and actual review](../diagrams/clearing/fig-0043.md); direct-body paragraph P577; Word page57.

| Step | Sender and depicted roles | Receiver and depicted roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-and-settlement-agent.md) | FIToFICustomerDirectDebit |
| 2 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-and-settlement-agent.md) | FIToFIPaymentStatusRequest |



### Narrative-only message path

[clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-and-settlement-agent.md) → [creditor-agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md): FIToFIPaymentStatusReport (P576). Reply to the request, referring to original instruction; intentionally absent from drawn response arrows.

## Outcomes, optional paths and source limitations

Source-defined optional acknowledgements, repair/resubmission, account reporting, rejection/return and settlement conditions are retained below. Positive processability status is not by itself settlement.

- Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.
- P576 requires status response referring to original; no response arrow is drawn. P578 literally refers to FinancialInstitutionCreditTransfer despite DD section/figure (issue-000054).
- Source message names establish family-level flow context; supplied exact schema versions are separately identified.
- Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible.

## Supplied exact message references

| Family | Exact supplied definition | Scope |
| --- | --- | --- |
| pacs.002 | [pacs.002.001.16](../../../../messages/pacs.002.001.16/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.003 | [pacs.003.001.12](../../../../messages/pacs.003.001.12/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.009 | [pacs.009.001.13](../../../../messages/pacs.009.001.13/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.028 | [pacs.028.001.07](../../../../messages/pacs.028.001.07/index.md) | Retrieval name match; schema definition version remains separately scoped. |


## Review

Source text, original image and complete Word-rendered figure context checked on 2026-11-09. Source issues: issue-000054. Activity tables and schemas retain their own review status.
