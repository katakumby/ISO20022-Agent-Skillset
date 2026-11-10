---
template: false
document_kind: "flow-context"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p296-financial-institution-credit-transfer"
title: "FinancialInstitutionCreditTransfer"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "], "locator": "/w:document/w:body/w:p[296]", "paragraph_id": "P296", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "], "locator": "/w:document/w:body/w:p[297]", "paragraph_id": "P297", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "], "locator": "/w:document/w:body/w:p[298]", "paragraph_id": "P298", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "], "locator": "/w:document/w:body/w:p[299]", "paragraph_id": "P299", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "], "locator": "/w:document/w:body/w:p[300]", "paragraph_id": "P300", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "], "locator": "/w:document/w:body/w:p[301]", "paragraph_id": "P301", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "], "locator": "/w:document/w:body/w:p[302]", "paragraph_id": "P302", "table_id": null}]
participants: ["participant-src-000162-financial-institution", "participant-src-000162-intermediary-agent", "participant-src-000162-settlement-agent", "participant-src-000162-creditor-agent", "participant-src-000162-debtor-agent", "participant-src-000162-creditor", "participant-src-000162-debtor", "participant-src-000162-party"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["pacs.009"]
search_terms: ["FinancialInstitutionCreditTransfer", "Financial Institution", "Intermediary Agent", "Settlement Agent", "Creditor Agent", "Debtor agent", "Creditor", "Debtor", "Party", "pacs.009"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "This source-delimited heading/context is not an additional independent flow. Follow linked canonical flows for ordered responsibilities and message directions."]
manual_curated: true
issue_ids: []
related_flows: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p303-debtor-and-creditor-are-correspondents.md", "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p310-debtor-and-creditor-agent-are-correspondents.md", "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p317-debtor-agent-and-creditor-are-correspondents.md", "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p327-debtor-agent-and-creditor-agent-are-correspondents.md", "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p335-debtor-agent-and-creditor-agent-are-not-correspondents.md"]
context_review_date: "2026-11-09"
---





# FinancialInstitutionCreditTransfer

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Financial Institution | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Intermediary Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-intermediary-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Settlement Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-settlement-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Creditor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Creditor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P297** A FinancialInstitutionCreditTransfer message is the inter-bank movement of an amount from a party bank account (the debtor) to a beneficiary party (the creditor) where all parties are financial institutions.

**P298** FinancialInstitutionCreditTransfer messages result in cash transfers between debtors and creditors through correspondent banks or infrastructures. They may be exchanged as single instructions or grouped following certain common characteristics and, for convenience or efficiency reasons, exchanged in a batch mode. The processing of credit transfers may differ from country to country and system to system.

**P299** Depending on the scenario, there might be an agent between the debtor agent and the creditor agent. This agent can be an intermediary agent or a reimbursement agent. The narrative will describe more in detail the agent role.

**P300** In scenarios where the receiving agent services an account for the sending agent, the scenario also includes the case where the sending agent has an account with a branch/head office of the receiving agent and will indicate that the receiving agent can reimburse itself at this institution. The sending agent has to be aware of an intra-group agreement allowing this.

**P301** A payment clearing and settlement system could occur between debtor agent and creditor agent (or between any other agents). The clearing process where the clearing agent after being informed on the transaction prepares and sends the payment information to the settlement agent (if different) is out of scope and will not be described. This process includes the calculation of the settlement positions and transmission of files to the settlement agent. The settlement agent transfers the funds from the debtor agent to the creditor agent in accordance with the settlement cycle and based on the settlement report provided by the clearing agent.

**P302** Only the messages in the scope of interbank credit transfer are illustrated in the BusinessTransactions (sequence diagrams). The original contracts between the debtor and the creditor, for example, forex, inter-bank loans, and securities transactions, are out of scope and are not included in the diagrams.

## Messages and alternative paths

Source-supported message family mentions: `pacs.009`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Heading path: BusinessTransactions / Credit Transfer / FinancialInstitutionCreditTransfer .

<!-- CLEARING-CONTEXT -->
[Curated full process context, participants, alternatives and source evidence](flow-src-000162-p303-debtor-and-creditor-are-correspondents.md)
<!-- /CLEARING-CONTEXT -->

## Reviewed flow context

The source-delimited content above was checked with its complete process narrative, original picture and Word figure context. It is a contextual section, not a separate message exchange.

- [Debtor and Creditor are Correspondents](flow-src-000162-p303-debtor-and-creditor-are-correspondents.md)
- [Debtor and Creditor Agent are Correspondents](flow-src-000162-p310-debtor-and-creditor-agent-are-correspondents.md)
- [Debtor Agent and Creditor are Correspondents](flow-src-000162-p317-debtor-agent-and-creditor-are-correspondents.md)
- [Debtor Agent and Creditor Agent are Correspondents](flow-src-000162-p327-debtor-agent-and-creditor-agent-are-correspondents.md)
- [Debtor Agent and Creditor Agent are Not Correspondents](flow-src-000162-p335-debtor-agent-and-creditor-agent-are-not-correspondents.md)
