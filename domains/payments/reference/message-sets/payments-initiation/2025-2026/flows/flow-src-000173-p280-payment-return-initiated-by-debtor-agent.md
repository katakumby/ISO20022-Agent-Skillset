---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p280-payment-return-initiated-by-debtor-agent"
title: "PaymentReturn Initiated by Debtor Agent"
source_locations: [{"source_id": "src-000173", "locator": "/w:document/w:body/w:p[278]", "paragraph_id": "P278", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[279]", "paragraph_id": "P279", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[280]", "paragraph_id": "P280", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[281]", "paragraph_id": "P281", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[282]", "paragraph_id": "P282", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[283]", "paragraph_id": "P283", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[284]", "paragraph_id": "P284", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[285]", "paragraph_id": "P285", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[286]", "paragraph_id": "P286", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[287]", "paragraph_id": "P287", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[288]", "paragraph_id": "P288", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[289]", "paragraph_id": "P289", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[290]", "paragraph_id": "P290", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[291]", "paragraph_id": "P291", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[292]", "paragraph_id": "P292", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[293]", "paragraph_id": "P293", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[294]", "paragraph_id": "P294", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[295]", "paragraph_id": "P295", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[296]", "paragraph_id": "P296", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "Refund by the Debtor"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[297]", "paragraph_id": "P297", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "Refund by the Debtor"]}]
participants: ["participant-src-000173-clearing-agent", "participant-src-000173-clearing-and-settlement-agent", "participant-src-000173-credit-party", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debit-party", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-initiating-party", "participant-src-000173-settlement-agent"]
message_mapping_evidence: [{"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["camt.052", "camt.053", "pacs.002", "pacs.003", "pacs.004", "pain.002", "pain.008"]
search_terms: ["PaymentReturn Initiated by Debtor Agent", "Creditor Agent", "Debtor Agent", "Creditor", "Debtor", "Party", "pain.002", "pain.008"]
limitations: ["Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.", "P279/P283/P297: return may be initiated by debtor agent or triggered by debtor refund request; refund request is assumed non-automated and outside message scope. Source picture includes RefundRequest despite heading debtor-agent-initiated return. P294 separate settlement and P295 customer information are narrative-only.", "Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling."]
manual_curated: true
participant_ids: ["participant-src-000173-clearing-agent", "participant-src-000173-clearing-and-settlement-agent", "participant-src-000173-credit-party", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debit-party", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-initiating-party", "participant-src-000173-settlement-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/diagrams/initiation/fig-0024.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and rendered page context compared; tables retain independent review status."}
message_reference_scope: "Family/name-level Part1 flows; supplied exact definitions linked separately."
---



# PaymentReturn Initiated by Debtor Agent

[src-000173](../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx)

## Purpose and trigger

Return a collected direct debit, including a debtor-requested refund.

P279: debit cannot be executed for administrative/banking reasons; refund request can also trigger return.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [clearing agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-agent.md) | Narrative-only participant/example; omitted as a separate figure lifeline. |
| [clearing and settlement agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [credit party](../../../../../../../shared/reference/participants/participant-src-000173-credit-party.md) | Narrative-only participant/example; omitted as a separate figure lifeline. |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debit party](../../../../../../../shared/reference/participants/participant-src-000173-debit-party.md) | Narrative-only participant/example; omitted as a separate figure lifeline. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [initiating party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Source figure occurrence; exact action/message direction is shown below. |
| [settlement agent](../../../../../../../shared/reference/participants/participant-src-000173-settlement-agent.md) | Narrative-only participant/example; omitted as a separate figure lifeline. |


## Source-defined conditions and activities

**P279** A PaymentReturn message is initiated by the debtor agent and sent to the previous party in the payment chain when a debit cannot be executed due to an administrative reason (such as non-existing/closed account) or due to a banking reason (such as insufficient funds). The PaymentReturn message is also the message to be used by the debtor agent following the receipt of a refund request by the debtor as it is assumed that the refund request will be done through a non-automated tool (such as phone/fax) and is not part of the scope. In this case, the PaymentReturn message will contain a code to indicate that it is triggered by a request for refund by the debtor.

**P281** A PaymentReturn message is initiated by the debtor agent (only the messages that are part of the scope of the direct debit are illustrated in the diagram):

**P283** With respect to the RefundRequest, the payment return process can be triggered by a RefundRequest by the debtor or initiated by the debtor agent.

**P284** If the booking of the original instruction on the creditor's account has already taken place, the return of the funds will be notified to the creditor through return information included in a BankToCustomerNotification message and/or a BankToCustomerAccountReport or a BankToCustomerStatement message.

**P285** The creditor sends the CustomerDirectDebitInitiation message to its Agent (the creditor agent).

**P286** The creditor agent confirms the processability of the CustomerDirectDebitInitiation instruction by sending a positive CustomerPaymentStatusReport to the creditor.

**P287** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

**P288** The clearing and settlement agent confirms the processability of the FIToFICustomerDirectDebit instruction by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P289** The clearing and settlement agent sends an FIToFICustomerDirectDebit message, optionally with the Mandate Related Reference (MRI) to the debtor agent immediately for information purposes only.

**P290** The debtor agent sends a positive FIToFIPaymentStatusReport message to the clearing and settlement agent.

**P291** If the debtor agent is unable to make the collection from the debtor Account for one or several reasons (for example, insufficient funds, customer deceased), the debtor agent will initiate a PaymentReturn message, and route it through the clearing and settlement agent to the creditor agent, giving the reason for the Return.

**P292** The clearing and settlement agent optionally confirms the receipt of the PaymentReturn message by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P293** The clearing and settlement agent forwards the PaymentReturn message to the creditor agent.

**P294** If the clearing and settlement agent are two parties the Clearing Agent prepares the (returned) payment information for the Settlement Agent (the net position to be debited, the party to be debited, the net position to be credited, the party to be credited and the value date) in accordance with the agreed and published settlement cycle. The Settlement Agent performs the transfer of cash from the credit party to the debit party (in accordance with the agreed published settlement cycle). (Out of scope and not illustrated).

**P295** The creditor agent will optionally confirm receipt of the PaymentReturn message to the clearing and settlement agent. Depending on agreements between the creditor and the creditor agent, the creditor may be informed either through a negative CustomerPaymentStatusReport message, or through a CustomerToBankDebitCreditNotification message ('notification') or through a BankToCustomerAccountReport and/or BankToCustomerStatement message ('statement') about the funds return and thus the debit on his account.

**P297** This scenario is similar to the previous scenario, except that the PaymentReturn message by the debtor agent to the clearing and settlement agent is triggered by a Refund Request by the debtor to his agent, the debtor agent (in a non-automated manner). In this case, the PaymentReturn message will contain a code indicating that it was triggered by a request for refund by the debtor.

### fig-0024

[Source reconstruction and review](../diagrams/initiation/fig-0024.md); direct-body paragraph P282; Word file page37.

| Step | Sender and roles | Receiver and roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | CustomerDirectDebitInitiation |
| 2 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | CustomerPaymentStatusReport |
| 3 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | FIToFICustomerDirectDebit |
| 4 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | FIToFIPaymentStatusReport |
| 5 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | FIToFICustomerDirectDebit |
| 6 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | FIToFIPaymentStatusReport |
| 7 | [Debtor / debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | RefundRequest |
| 8 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | PaymentReturn |
| 9 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | FIToFIPaymentStatusReport |
| 10 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | PaymentReturn |
| 11 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | FIToFIPaymentStatusReport |



## Outcomes, alternatives and related processes

Return includes reason; refund-triggered return has indicating code. Separate settlement and customer account information are narrative-only, not absent (P294–297).

- Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.
- P279/P283/P297: return may be initiated by debtor agent or triggered by debtor refund request; refund request is assumed non-automated and outside message scope. Source picture includes RefundRequest despite heading debtor-agent-initiated return. P294 separate settlement and P295 customer information are narrative-only.
- Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.

| Process | Reference |
| --- | --- |
| Direct-debit return activity | [Direct-debit return activity](flow-src-000173-p149-return-direct-debit.md) |
| Debtor refund request | [Debtor refund request](flow-src-000173-p151-request-refund-of-direct-debit.md) |
| PaymentReturn exchange | [PaymentReturn exchange](flow-src-000173-p280-payment-return-initiated-by-debtor-agent.md) |
| Post-settlement CustomerPaymentReversal | [Post-settlement CustomerPaymentReversal](flow-src-000173-p298-customer-payment-reversal-with-direct-debit.md) |


## Supplied message definitions

| Family | Exact supplied reference | Scope |
| --- | --- | --- |
| camt.052 | [camt.052.001.14](../../../../messages/camt.052.001.14/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| camt.053 | [camt.053.001.14](../../../../messages/camt.053.001.14/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pacs.002 | [pacs.002.001.16](../../../../messages/pacs.002.001.16/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pacs.003 | [pacs.003.001.12](../../../../messages/pacs.003.001.12/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pacs.004 | [pacs.004.001.15](../../../../messages/pacs.004.001.15/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pain.002 | [pain.002.001.15](../../../../messages/pain.002.001.15/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pain.008 | [pain.008.001.12](../../../../messages/pain.008.001.12/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |



## Review

Compared source narrative, picture labels/directions and complete figure page context on 2026-11-09. This bounded flow evidence has been reviewed; participant classification/schema/table references keep their own review status.
