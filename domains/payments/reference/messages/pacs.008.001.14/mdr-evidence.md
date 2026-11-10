---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "pacs.008.001.14"
message_family: "pacs.008"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14"
source_ids: ["src-000163"]
source_locations: [{"source_id": "src-000163", "heading": "6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "file_pages": [702, 829]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# pacs.008.001.14 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000163 — 6 pacs.008.001.14 FIToFICustomerCreditTransferV14

[src-000163](../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf); file pp702–829; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000163, 6 pacs.008.001.14 FIToFICustomerCreditTransferV14, Functionality, file p702.**

Scope
The FinancialInstitutionToFinancialInstitutionCustomerCreditTransfer message is sent by the debtor
agent to the creditor agent, directly or through other agents and/or a payment clearing and settlement
system. It is used to move funds from a debtor account to a creditor.
Usage
The FIToFICustomerCreditTransfer message is exchanged between agents and can contain one or
more customer credit transfer instructions.
The FIToFICustomerCreditTransfer message does not allow for grouping: a
CreditTransferTransactionInformation block must be present for each credit transfer transaction.
The FIToFICustomerCreditTransfer message can be used in different ways:
- If the instructing agent and the instructed agent wish to use their direct account relationship in the
currency of the transfer then the message contains both the funds for the customer transfer(s) as well
as the payment details;
- If the instructing agent and the instructed agent have no direct account relationship in the currency of
the transfer, or do not wish to use their account relationship, then other (reimbursement) agents will be
involved to cover for the customer transfer(s). The FIToFICustomerCreditTransfer contains only the
payment details and the instructing agent must cover the customer transfer by sending a
FinancialInstitutionCreditTransfer to a reimbursement agent. This payment method is called the Cover
method;
- If more than two financial institutions are involved in the payment chain and if the
FIToFICustomerCreditTransfer is sent from one financial institution to the next financial institution in the
payment chain, then the payment method is called the Serial method.
The FIToFICustomerCreditTransfer message can be used in domestic and cross-border scenarios.
Outline
The FIToFICustomerCreditTransferV14 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. GroupHeader
Set of characteristics shared by all individual transactions included in the message.
B. CreditTransferTransactionInformation
Set of elements providing information specific to the individual credit transfer(s).
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
702 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00520.md) | 702–702 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.2 Structure](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00521.md) | 703–710 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.3 Constraints](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00522.md) | 711–715 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00523.md) | 716–717 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.1.1 MessageIdentification &lt;MsgId&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00524.md) | 718–718 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.1.6 ControlSum &lt;CtrlSum&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00525.md) | 719–720 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.1.9 SettlementInformation &lt;SttlmInf&gt; / 6.4.1.9.1 SettlementMethod &lt;SttlmMtd&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00526.md) | 721–721 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.1.9 SettlementInformation &lt;SttlmInf&gt; / 6.4.1.9.2 SettlementAccount &lt;SttlmAcct&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00527.md) | 722–722 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.1.9 SettlementInformation &lt;SttlmInf&gt; / 6.4.1.9.3 ClearingSystem &lt;ClrSys&gt; / 6.4.1.9.3.1 Code &lt;Cd&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00528.md) | 723–723 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.1.9 SettlementInformation &lt;SttlmInf&gt; / 6.4.1.9.5 InstructingReimbursementAgentAccount &lt;InstgRmbrsmntAgtAcct&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00529.md) | 724–724 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.1.9 SettlementInformation &lt;SttlmInf&gt; / 6.4.1.9.7 InstructedReimbursementAgentAccount &lt;InstdRmbrsmntAgtAcct&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00530.md) | 725–725 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.1.9 SettlementInformation &lt;SttlmInf&gt; / 6.4.1.9.8 ThirdReimbursementAgent &lt;ThrdRmbrsmntAgt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00531.md) | 726–726 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.1.10 PaymentTypeInformation &lt;PmtTpInf&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00532.md) | 727–727 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.1.11 InstructingAgent &lt;InstgAgt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00533.md) | 728–728 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.1.12 InstructedAgent &lt;InstdAgt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00534.md) | 729–738 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.1 PaymentIdentification &lt;PmtId&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00535.md) | 739–739 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.2 PaymentTypeInformation &lt;PmtTpInf&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00536.md) | 740–740 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.4 InterbankSettlementDate &lt;IntrBkSttlmDt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00537.md) | 741–741 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.6 SettlementTimeIndication &lt;SttlmTmIndctn&gt; / 6.4.2.6.1 DebitDateTime &lt;DbtDtTm&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00538.md) | 742–742 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.8 AdditionalDateTime &lt;AddtlDtTm&gt; / 6.4.2.8.1 AcceptanceDateTime &lt;AccptncDtTm&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00539.md) | 743–743 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.10 ExchangeRate &lt;XchgRate&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00540.md) | 744–744 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.11 AgreedRate &lt;AgrdRate&gt; / 6.4.2.11.3 PreAgreedExchangeRate &lt;PreAgrdXchgRate&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00541.md) | 745–745 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.12 ChargeBearer &lt;ChrgBr&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00542.md) | 746–746 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.13 ChargesInformation &lt;ChrgsInf&gt; / 6.4.2.13.1 Amount &lt;Amt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00543.md) | 747–747 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.13 ChargesInformation &lt;ChrgsInf&gt; / 6.4.2.13.3 Type &lt;Tp&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00544.md) | 748–748 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.14 MandateRelatedInformation &lt;MndtRltdInf&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00545.md) | 749–749 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.15 PaymentSignature &lt;PmtSgntr&gt; / 6.4.2.15.1 ILPV4 &lt;ILPV4&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00546.md) | 750–750 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.18 PreviousInstructingAgent2 &lt;PrvsInstgAgt2&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00547.md) | 751–751 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.19 PreviousInstructingAgent2Account &lt;PrvsInstgAgt2Acct&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00548.md) | 752–752 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.20 PreviousInstructingAgent3 &lt;PrvsInstgAgt3&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00549.md) | 753–753 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.22 InstructingAgent &lt;InstgAgt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00550.md) | 754–754 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.23 InstructedAgent &lt;InstdAgt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00551.md) | 755–755 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.24 IntermediaryAgent1 &lt;IntrmyAgt1&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00552.md) | 756–756 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.25 IntermediaryAgent1Account &lt;IntrmyAgt1Acct&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00553.md) | 757–757 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.26 IntermediaryAgent2 &lt;IntrmyAgt2&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00554.md) | 758–758 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.28 IntermediaryAgent3 &lt;IntrmyAgt3&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00555.md) | 759–759 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.29 IntermediaryAgent3Account &lt;IntrmyAgt3Acct&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00556.md) | 760–760 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.30 UltimateDebtor &lt;UltmtDbtr&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00557.md) | 761–761 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.31 InitiatingParty &lt;InitgPty&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00558.md) | 762–762 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.32 Debtor &lt;Dbtr&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00559.md) | 763–763 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.33 DebtorAccount &lt;DbtrAcct&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00560.md) | 764–764 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.34 DebtorAgent &lt;DbtrAgt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00561.md) | 765–765 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.35 DebtorAgentAccount &lt;DbtrAgtAcct&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00562.md) | 766–766 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.36 CreditorAgent &lt;CdtrAgt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00563.md) | 767–767 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.38 Creditor &lt;Cdtr&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00564.md) | 768–768 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.39 CreditorAccount &lt;CdtrAcct&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00565.md) | 769–769 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.40 UltimateCreditor &lt;UltmtCdtr&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00566.md) | 770–770 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.41 InstructionForCreditorAgent &lt;InstrForCdtrAgt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00567.md) | 771–771 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.42 InstructionForNextAgent &lt;InstrForNxtAgt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00568.md) | 772–772 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.44 RegulatoryReporting &lt;RgltryRptg&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00569.md) | 773–774 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.45 Tax &lt;Tax&gt; / 6.4.2.45.1 Creditor &lt;Cdtr&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00570.md) | 775–775 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.45 Tax &lt;Tax&gt; / 6.4.2.45.4 AdministrationZone &lt;AdmstnZone&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00571.md) | 776–776 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.45 Tax &lt;Tax&gt; / 6.4.2.45.8 TotalTaxAmount &lt;TtlTaxAmt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00572.md) | 777–777 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.45 Tax &lt;Tax&gt; / 6.4.2.45.11 Record &lt;Rcrd&gt; / 6.4.2.45.11.1 Type &lt;Tp&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00573.md) | 778–778 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.45 Tax &lt;Tax&gt; / 6.4.2.45.11 Record &lt;Rcrd&gt; / 6.4.2.45.11.4 DebtorStatus &lt;DbtrSts&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00574.md) | 779–779 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.45 Tax &lt;Tax&gt; / 6.4.2.45.11 Record &lt;Rcrd&gt; / 6.4.2.45.11.7 Period &lt;Prd&gt; / 6.4.2.45.11.7.3 FromToDate &lt;FrToDt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00575.md) | 780–780 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.45 Tax &lt;Tax&gt; / 6.4.2.45.11 Record &lt;Rcrd&gt; / 6.4.2.45.11.8 TaxAmount &lt;TaxAmt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00576.md) | 781–781 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.45 Tax &lt;Tax&gt; / 6.4.2.45.11 Record &lt;Rcrd&gt; / 6.4.2.45.11.8 TaxAmount &lt;TaxAmt&gt; / 6.4.2.45.11.8.4 Details &lt;Dtls&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00577.md) | 782–782 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.45 Tax &lt;Tax&gt; / 6.4.2.45.11 Record &lt;Rcrd&gt; / 6.4.2.45.11.8 TaxAmount &lt;TaxAmt&gt; / 6.4.2.45.11.8.4 Details &lt;Dtls&gt; / 6.4.2.45.11.8.4.1 Period &lt;Prd&gt; / 6.4.2.45.11.8.4.1.2 Type &lt;Tp&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00578.md) | 783–783 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.45 Tax &lt;Tax&gt; / 6.4.2.45.11 Record &lt;Rcrd&gt; / 6.4.2.45.11.8 TaxAmount &lt;TaxAmt&gt; / 6.4.2.45.11.8.4 Details &lt;Dtls&gt; / 6.4.2.45.11.8.4.2 Amount &lt;Amt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00579.md) | 784–784 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.46 RelatedRemittanceInformation &lt;RltdRmtInf&gt; / 6.4.2.46.1 RemittanceIdentification &lt;RmtId&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00580.md) | 785–785 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.46 RelatedRemittanceInformation &lt;RltdRmtInf&gt; / 6.4.2.46.2 RemittanceLocationDetails &lt;RmtLctnDtls&gt; / 6.4.2.46.2.2 ElectronicAddress &lt;ElctrncAdr&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00581.md) | 786–786 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00582.md) | 787–790 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.1 Unstructured &lt;Ustrd&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00583.md) | 791–794 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.1 ReferredDocumentInformation &lt;RfrdDocInf&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00584.md) | 795–796 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.1 ReferredDocumentInformation &lt;RfrdDocInf&gt; / 6.4.2.47.2.1.1 Type &lt;Tp&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00585.md) | 797–797 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.1 ReferredDocumentInformation &lt;RfrdDocInf&gt; / 6.4.2.47.2.1.2 Number &lt;Nb&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00586.md) | 798–798 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.1 ReferredDocumentInformation &lt;RfrdDocInf&gt; / 6.4.2.47.2.1.4 LineDetails &lt;LineDtls&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00587.md) | 799–799 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.1 ReferredDocumentInformation &lt;RfrdDocInf&gt; / 6.4.2.47.2.1.4 LineDetails &lt;LineDtls&gt; / 6.4.2.47.2.1.4.1 Identification &lt;Id&gt; / 6.4.2.47.2.1.4.1.1 Type &lt;Tp&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00588.md) | 800–800 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.1 ReferredDocumentInformation &lt;RfrdDocInf&gt; / 6.4.2.47.2.1.4 LineDetails &lt;LineDtls&gt; / 6.4.2.47.2.1.4.1 Identification &lt;Id&gt; / 6.4.2.47.2.1.4.1.1 Type &lt;Tp&gt; / 6.4.2.47.2.1.4.1.1.2 Issuer &lt;Issr&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00589.md) | 801–801 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.1 ReferredDocumentInformation &lt;RfrdDocInf&gt; / 6.4.2.47.2.1.4 LineDetails &lt;LineDtls&gt; / 6.4.2.47.2.1.4.3 Amount &lt;Amt&gt; / 6.4.2.47.2.1.4.3.1 RemittanceAmountAndType &lt;RmtAmtAndTp&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00590.md) | 802–802 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.1 ReferredDocumentInformation &lt;RfrdDocInf&gt; / 6.4.2.47.2.1.4 LineDetails &lt;LineDtls&gt; / 6.4.2.47.2.1.4.3 Amount &lt;Amt&gt; / 6.4.2.47.2.1.4.3.1 RemittanceAmountAndType &lt;RmtAmtAndTp&gt; / 6.4.2.47.2.1.4.3.1.1 Type &lt;Tp&gt; / 6.4.2.47.2.1.4.3.1.1.1 Code &lt;Cd&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00591.md) | 803–803 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.1 ReferredDocumentInformation &lt;RfrdDocInf&gt; / 6.4.2.47.2.1.4 LineDetails &lt;LineDtls&gt; / 6.4.2.47.2.1.4.3 Amount &lt;Amt&gt; / 6.4.2.47.2.1.4.3.2 AdjustmentAmountAndReason &lt;AdjstmntAmtAndRsn&gt; / 6.4.2.47.2.1.4.3.2.2 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00592.md) | 804–804 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.2 ReferredDocumentAmount &lt;RfrdDocAmt&gt; / 6.4.2.47.2.2.1 RemittanceAmountAndType &lt;RmtAmtAndTp&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00593.md) | 805–805 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.2 ReferredDocumentAmount &lt;RfrdDocAmt&gt; / 6.4.2.47.2.2.1 RemittanceAmountAndType &lt;RmtAmtAndTp&gt; / 6.4.2.47.2.2.1.1 Type &lt;Tp&gt; / 6.4.2.47.2.2.1.1.1 Code &lt;Cd&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00594.md) | 806–806 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.2 ReferredDocumentAmount &lt;RfrdDocAmt&gt; / 6.4.2.47.2.2.2 AdjustmentAmountAndReason &lt;AdjstmntAmtAndRsn&gt; / 6.4.2.47.2.2.2.2 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00595.md) | 807–807 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.3 CreditorReferenceInformation &lt;CdtrRefInf&gt; / 6.4.2.47.2.3.1 Type &lt;Tp&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00596.md) | 808–808 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.3 CreditorReferenceInformation &lt;CdtrRefInf&gt; / 6.4.2.47.2.3.1 Type &lt;Tp&gt; / 6.4.2.47.2.3.1.2 Issuer &lt;Issr&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00597.md) | 809–809 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.5 Invoicee &lt;Invcee&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00598.md) | 810–810 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.6 TaxRemittance &lt;TaxRmt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00599.md) | 811–812 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.6 TaxRemittance &lt;TaxRmt&gt; / 6.4.2.47.2.6.1 Creditor &lt;Cdtr&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00600.md) | 813–813 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.6 TaxRemittance &lt;TaxRmt&gt; / 6.4.2.47.2.6.4 AdministrationZone &lt;AdmstnZone&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00601.md) | 814–814 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.6 TaxRemittance &lt;TaxRmt&gt; / 6.4.2.47.2.6.8 TotalTaxAmount &lt;TtlTaxAmt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00602.md) | 815–815 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.6 TaxRemittance &lt;TaxRmt&gt; / 6.4.2.47.2.6.11 Record &lt;Rcrd&gt; / 6.4.2.47.2.6.11.1 Type &lt;Tp&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00603.md) | 816–816 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.6 TaxRemittance &lt;TaxRmt&gt; / 6.4.2.47.2.6.11 Record &lt;Rcrd&gt; / 6.4.2.47.2.6.11.4 DebtorStatus &lt;DbtrSts&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00604.md) | 817–817 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.6 TaxRemittance &lt;TaxRmt&gt; / 6.4.2.47.2.6.11 Record &lt;Rcrd&gt; / 6.4.2.47.2.6.11.7 Period &lt;Prd&gt; / 6.4.2.47.2.6.11.7.3 FromToDate &lt;FrToDt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00605.md) | 818–818 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.6 TaxRemittance &lt;TaxRmt&gt; / 6.4.2.47.2.6.11 Record &lt;Rcrd&gt; / 6.4.2.47.2.6.11.8 TaxAmount &lt;TaxAmt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00606.md) | 819–819 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.6 TaxRemittance &lt;TaxRmt&gt; / 6.4.2.47.2.6.11 Record &lt;Rcrd&gt; / 6.4.2.47.2.6.11.8 TaxAmount &lt;TaxAmt&gt; / 6.4.2.47.2.6.11.8.4 Details &lt;Dtls&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00607.md) | 820–820 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.6 TaxRemittance &lt;TaxRmt&gt; / 6.4.2.47.2.6.11 Record &lt;Rcrd&gt; / 6.4.2.47.2.6.11.8 TaxAmount &lt;TaxAmt&gt; / 6.4.2.47.2.6.11.8.4 Details &lt;Dtls&gt; / 6.4.2.47.2.6.11.8.4.1 Period &lt;Prd&gt; / 6.4.2.47.2.6.11.8.4.1.2 Type &lt;Tp&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00608.md) | 821–821 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.6 TaxRemittance &lt;TaxRmt&gt; / 6.4.2.47.2.6.11 Record &lt;Rcrd&gt; / 6.4.2.47.2.6.11.8 TaxAmount &lt;TaxAmt&gt; / 6.4.2.47.2.6.11.8.4 Details &lt;Dtls&gt; / 6.4.2.47.2.6.11.8.4.2 Amount &lt;Amt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00609.md) | 822–822 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.7 GarnishmentRemittance &lt;GrnshmtRmt&gt; / 6.4.2.47.2.7.1 Type &lt;Tp&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00610.md) | 823–823 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.7 GarnishmentRemittance &lt;GrnshmtRmt&gt; / 6.4.2.47.2.7.1 Type &lt;Tp&gt; / 6.4.2.47.2.7.1.1 CodeOrProprietary &lt;CdOrPrtry&gt; / 6.4.2.47.2.7.1.1.1 Code &lt;Cd&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00611.md) | 824–824 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.7 GarnishmentRemittance &lt;GrnshmtRmt&gt; / 6.4.2.47.2.7.3 GarnishmentAdministrator &lt;GrnshmtAdmstr&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00612.md) | 825–825 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.7 GarnishmentRemittance &lt;GrnshmtRmt&gt; / 6.4.2.47.2.7.4 ReferenceNumber &lt;RefNb&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00613.md) | 826–826 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.7 GarnishmentRemittance &lt;GrnshmtRmt&gt; / 6.4.2.47.2.7.5 Date &lt;Dt&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00614.md) | 827–827 |
| [6 pacs.008.001.14 FIToFICustomerCreditTransferV14 / 6.4 Message Building Blocks / 6.4.2.47 RemittanceInformation &lt;RmtInf&gt; / 6.4.2.47.2 Structured &lt;Strd&gt; / 6.4.2.47.2.8 SecuritiesData &lt;SctiesData&gt; / 6.4.2.47.2.8.1 UniqueTransactionIdentifier &lt;UnqTxIdr&gt;](../../message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00615.md) | 828–829 |

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
