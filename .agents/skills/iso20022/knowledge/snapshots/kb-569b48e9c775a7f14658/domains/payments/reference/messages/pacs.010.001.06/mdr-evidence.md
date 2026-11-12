---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "pacs.010.001.06"
message_family: "pacs.010"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06"
source_ids: ["src-000163"]
source_locations: [{"source_id": "src-000163", "heading": "8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "file_pages": [1016, 1048]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# pacs.010.001.06 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000163 — 8 pacs.010.001.06 FinancialInstitutionDirectDebitV06

[src-000163](../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md); file pp1016–1048; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000163, 8 pacs.010.001.06 FinancialInstitutionDirectDebitV06, Functionality, file p1016.**

Scope:
The FinancialInstitutionDirectDebit message is sent by an exchange or clearing house, or a financial
institution, directly or through another agent, to the DebtorAgent. It is used to instruct the DebtorAgent
to move funds from one or more debtor(s) account(s) to one or more creditor(s), where both debtor and
creditor are financial institutions.
Usage:
The FinancialInstitutionDirectDebit message is exchanged between agents and can contain one or
more financial institution direct debit instruction(s) for one or more creditor(s). The
FinancialInstitutionDirectDebit message can be used in domestic and cross-border scenarios.
Outline
The FinancialInstitutionDirectDebitV06 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. GroupHeader
Common characteristics for all individual transactions included in the message.
B. CreditInstruction
Characteristics that apply to the credit side of the payment transaction(s) included in the message.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1016 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00757.md) | 1016–1016 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.2 Structure](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00758.md) | 1017–1017 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.3 Constraints](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00759.md) | 1018–1019 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00760.md) | 1020–1020 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.1 GroupHeader &lt;GrpHdr&gt; / 8.4.1.1 MessageIdentification &lt;MsgId&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00761.md) | 1021–1021 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.1 GroupHeader &lt;GrpHdr&gt; / 8.4.1.6 InstructedAgent &lt;InstdAgt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00762.md) | 1022–1022 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00763.md) | 1023–1026 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.1 CreditIdentification &lt;CdtId&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00764.md) | 1027–1027 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.5 InterbankSettlementDate &lt;IntrBkSttlmDt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00765.md) | 1028–1028 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.7 InstructingAgent &lt;InstgAgt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00766.md) | 1029–1029 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.9 IntermediaryAgent1 &lt;IntrmyAgt1&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00767.md) | 1030–1030 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.10 IntermediaryAgent1Account &lt;IntrmyAgt1Acct&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00768.md) | 1031–1031 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.11 IntermediaryAgent2 &lt;IntrmyAgt2&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00769.md) | 1032–1032 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.13 IntermediaryAgent3 &lt;IntrmyAgt3&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00770.md) | 1033–1033 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.14 IntermediaryAgent3Account &lt;IntrmyAgt3Acct&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00771.md) | 1034–1034 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.15 CreditorAgent &lt;CdtrAgt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00772.md) | 1035–1035 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.17 Creditor &lt;Cdtr&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00773.md) | 1036–1036 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.18 CreditorAccount &lt;CdtrAcct&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00774.md) | 1037–1037 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.19 UltimateCreditor &lt;UltmtCdtr&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00775.md) | 1038–1038 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.21 DirectDebitTransactionInformation &lt;DrctDbtTxInf&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00776.md) | 1039–1039 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.21 DirectDebitTransactionInformation &lt;DrctDbtTxInf&gt; / 8.4.2.21.1 PaymentIdentification &lt;PmtId&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00777.md) | 1040–1040 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.21 DirectDebitTransactionInformation &lt;DrctDbtTxInf&gt; / 8.4.2.21.3 InterbankSettlementAmount &lt;IntrBkSttlmAmt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00778.md) | 1041–1041 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.21 DirectDebitTransactionInformation &lt;DrctDbtTxInf&gt; / 8.4.2.21.5 SettlementPriority &lt;SttlmPrty&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00779.md) | 1042–1042 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.21 DirectDebitTransactionInformation &lt;DrctDbtTxInf&gt; / 8.4.2.21.8 UltimateDebtor &lt;UltmtDbtr&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00780.md) | 1043–1043 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.21 DirectDebitTransactionInformation &lt;DrctDbtTxInf&gt; / 8.4.2.21.10 DebtorAccount &lt;DbtrAcct&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00781.md) | 1044–1044 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.21 DirectDebitTransactionInformation &lt;DrctDbtTxInf&gt; / 8.4.2.21.11 DebtorAgent &lt;DbtrAgt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00782.md) | 1045–1045 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.21 DirectDebitTransactionInformation &lt;DrctDbtTxInf&gt; / 8.4.2.21.13 InstructionForDebtorAgent &lt;InstrForDbtrAgt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00783.md) | 1046–1046 |
| [8 pacs.010.001.06 FinancialInstitutionDirectDebitV06 / 8.4 Message Building Blocks / 8.4.2 CreditInstruction &lt;CdtInstr&gt; / 8.4.2.21 DirectDebitTransactionInformation &lt;DrctDbtTxInf&gt; / 8.4.2.21.15 RemittanceInformation &lt;RmtInf&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00784.md) | 1047–1048 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Account Owner](../../../../../shared/reference/participants/participant-src-000162-account-owner.md) | participant | src-000162 |
| [Account Servicer](../../../../../shared/reference/participants/participant-src-000162-account-servicer.md) | participant | src-000162 |
| [ACH](../../../../../shared/reference/participants/participant-src-000162-ach.md) | participant | src-000162 |
| [Clearing System](../../../../../shared/reference/participants/participant-src-000162-clearing-system.md) | participant | src-000162 |
| [Creditor Agent or Creditor](../../../../../shared/reference/participants/participant-src-000162-creditor-agent-or-creditor.md) | participant | src-000162 |
| [Creditor Agent](../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | participant | src-000162 |
| [Creditor](../../../../../shared/reference/participants/participant-src-000162-creditor.md) | participant | src-000162 |
| [Debtor agent](../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | participant | src-000162 |
| [Debtor](../../../../../shared/reference/participants/participant-src-000162-debtor.md) | participant | src-000162 |
| [Financial Institution](../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | participant | src-000162 |
| [Forwarding Agent](../../../../../shared/reference/participants/participant-src-000162-forwarding-agent.md) | participant | src-000162 |
| [Initiating Party](../../../../../shared/reference/participants/participant-src-000162-initiating-party.md) | participant | src-000162 |
| [Instructed Agent/ACH](../../../../../shared/reference/participants/participant-src-000162-instructed-agent-ach.md) | participant | src-000162 |
| [Intermediary Agent](../../../../../shared/reference/participants/participant-src-000162-intermediary-agent.md) | participant | src-000162 |
| [Party](../../../../../shared/reference/participants/participant-src-000162-party.md) | participant | src-000162 |
| [PaymentClearingAgent A](../../../../../shared/reference/participants/participant-src-000162-payment-clearing-agent-a.md) | participant | src-000162 |
| [PaymentClearingAgent B](../../../../../shared/reference/participants/participant-src-000162-payment-clearing-agent-b.md) | participant | src-000162 |
| [Payment Clearing Agent (Instructing Agent)](../../../../../shared/reference/participants/participant-src-000162-payment-clearing-agent-instructing-agent.md) | participant | src-000162 |
| [Payment Clearing Agent](../../../../../shared/reference/participants/participant-src-000162-payment-clearing-agent.md) | participant | src-000162 |
| [Payment Settlement Agent (Instructed Agent)](../../../../../shared/reference/participants/participant-src-000162-payment-settlement-agent-instructed-agent.md) | participant | src-000162 |
| [PaymentSettlementAgent](../../../../../shared/reference/participants/participant-src-000162-payment-settlement-agent.md) | participant | src-000162 |
| [Settlement Agent](../../../../../shared/reference/participants/participant-src-000162-settlement-agent.md) | participant | src-000162 |
| [Ultimate Creditor](../../../../../shared/reference/participants/participant-src-000162-ultimate-creditor.md) | participant | src-000162 |
| [Ultimate Debtor](../../../../../shared/reference/participants/participant-src-000162-ultimate-debtor.md) | participant | src-000162 |
| [Accept Inter-Bank Payment](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p114-accept-inter-bank-payment.md) | business-flow | src-000162 |
| [Asses Interbank Payment Risk](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p115-asses-interbank-payment-risk.md) | business-flow | src-000162 |
| [Validate Interbank Payment](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p116-validate-interbank-payment.md) | business-flow | src-000162 |
| [Authorise Interbank Payment](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p117-authorise-interbank-payment.md) | business-flow | src-000162 |
| [Clear Interbank Payment](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p118-clear-interbank-payment.md) | business-flow | src-000162 |
| [Sort Interbank Payment](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p119-sort-interbank-payment.md) | business-flow | src-000162 |
| [Calculate the Settlement Positions](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p120-calculate-the-settlement-positions.md) | business-flow | src-000162 |
| [Prepare Onward Interbank Payment](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p121-prepare-onward-interbank-payment.md) | business-flow | src-000162 |
| [Settle Interbank Payment](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p122-settle-interbank-payment.md) | business-flow | src-000162 |
| [Generate Regulatory Reporting Information](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p123-generate-regulatory-reporting-information.md) | business-flow | src-000162 |
| [Process direct debit](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p127-process-direct-debit.md) | business-flow | src-000162 |
| [Process Reject](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p128-process-reject.md) | business-flow | src-000162 |
| [Process Return/Request for Refund](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p129-process-return-request-for-refund.md) | business-flow | src-000162 |
| [Process Reversal](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p130-process-reversal.md) | business-flow | src-000162 |
| [Credit Transfer](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p138-credit-transfer.md) | business-flow | src-000162 |
| [Direct debit instruction](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p154-direct-debit-instruction.md) | business-flow | src-000162 |
| [Direct Debit Reversal](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p161-direct-debit-reversal.md) | business-flow | src-000162 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
