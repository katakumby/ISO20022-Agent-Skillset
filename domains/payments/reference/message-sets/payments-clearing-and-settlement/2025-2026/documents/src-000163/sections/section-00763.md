---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "8.4 Message Building Blocks", "8.4.2 CreditInstruction <CdtInstr>"]
file_pages: [1023, 1024, 1025, 1026]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.010.001.06"]
---

# 8.4.2 CreditInstruction <CdtInstr>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1023 to 1026.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1023

```text
InstructedAgent <InstdAgt> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 1173 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  1174
     BICFI <BICFI> [0..1] IdentifierSet C5 1174
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1175
     LEI <LEI> [0..1] IdentifierSet 1175
     Name <Nm> [0..1] Text 1175
     PostalAddress <PstlAdr> [0..1] ± 1175
     Other <Othr> [0..1] ± 1176
   BranchIdentification <BrnchId> [0..1]  1177
     Identification <Id> [0..1] Text 1177
     LEI <LEI> [0..1] IdentifierSet 1177
     Name <Nm> [0..1] Text 1177
     PostalAddress <PstlAdr> [0..1] ± 1177
8.4.2 CreditInstruction <CdtInstr>
Presence: [1..*]
Definition: Characteristics that apply to the credit side of the payment transaction(s) included in the
message.
Impacted by: C5 "CreditorAgentAccountRule", C10 "InterbankSettlementDateRule", C11
"IntermediaryAgent1AccountRule", C12 "IntermediaryAgent1Rule", C13
"IntermediaryAgent2AccountRule", C14 "IntermediaryAgent2Rule", C15
"IntermediaryAgent3AccountRule", C16 "IntermediaryAgent3Rule", C17
"PaymentTypeInformationRule", C20 "TotalInterbankSettlementAmountAndSumRule", C21
"TotalInterbankSettlementAmountRule", C23 "UltimateCreditorGuideline"
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1023 March 2026
```

## File page 1024

```text
CreditInstruction <CdtInstr> contains the following CreditTransferTransaction66 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CreditIdentification <CdtId> [1..1] Text 1027
   BatchBooking <BtchBookg> [0..1] Indicator 1027
   PaymentTypeInformation <PmtTpInf> [0..1] ± 1027
   TotalInterbankSettlementAmount <TtlIntrBkSttlmAmt> [0..1] Amount C1, C6 1027
   InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 1028
   SettlementTimeIndication <SttlmTmIndctn> [0..1]  1028
     DebitDateTime <DbtDtTm> [0..1] DateTime 1028
     CreditDateTime <CdtDtTm> [0..1] DateTime 1028
   InstructingAgent <InstgAgt> [0..1] ± 1029
   InstructedAgent <InstdAgt> [0..1] ± 1029
   IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 1030
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C9, C8 1031
   IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 1032
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1] ± C9, C8 1032
   IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 1033
   IntermediaryAgent3Account <IntrmyAgt3Acct> [0..1] ± C9, C8 1034
   CreditorAgent <CdtrAgt> [0..1] ± 1035
   CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C9, C8 1035
   Creditor <Cdtr> [1..1] ± 1036
   CreditorAccount <CdtrAcct> [0..1] ± C9, C8 1037
   UltimateCreditor <UltmtCdtr> [0..1] ± 1038
   InstructionForCreditorAgent <InstrForCdtrAgt> [0..*] ± 1038
   DirectDebitTransactionInformation <DrctDbtTxInf> [1..*]  C24 1039
     PaymentIdentification <PmtId> [1..1] ± C22 1040
     PaymentTypeInformation <PmtTpInf> [0..1] ± 1040
     InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount C1, C6 1041
     InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 1041
     SettlementPriority <SttlmPrty> [0..1] CodeSet 1042
     SettlementTimeIndication <SttlmTmIndctn> [0..1]  1042
       DebitDateTime <DbtDtTm> [0..1] DateTime 1042
       CreditDateTime <CdtDtTm> [0..1] DateTime 1042
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1024 March 2026
```

## File page 1025

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     SettlementTimeRequest <SttlmTmReq> [0..1] ± 1042
     UltimateDebtor <UltmtDbtr> [0..1] ± 1043
     Debtor <Dbtr> [1..1] ± 1043
     DebtorAccount <DbtrAcct> [0..1] ± C9, C8 1044
     DebtorAgent <DbtrAgt> [0..1] ± 1045
     DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C9, C8 1045
     InstructionForDebtorAgent <InstrForDbtrAgt> [0..1] Text 1046
     Purpose <Purp> [0..1] ± 1046
     RemittanceInformation <RmtInf> [0..1] ± 1047
   SupplementaryData <SplmtryData> [0..*] ± C19 1047
Constraints
• CreditorAgentAccountRule
If CreditorAgentAccount is present, then CreditorAgent must be present.
On Condition
    /CreditorAgent is absent
Following Must be True
    /CreditorAgentAccount Must be absent
• InterbankSettlementDateRule
If InterbankSettlementDate is present, then DirectDebitTransactionInformation/
InterbankSettlementDate is not allowed.
On Condition
    /InterbankSettlementDate is present
Following Must be True
    /DirectDebitTransactionInformation[*]/InterbankSettlementDate Must be absent
• IntermediaryAgent1AccountRule
If IntermediaryAgent1Account is present, then IntermediaryAgent1 must be present.
On Condition
    /IntermediaryAgent1 is absent
Following Must be True
    /IntermediaryAgent1Account Must be absent
• IntermediaryAgent1Rule
If IntermediaryAgent1 is present, then CreditorAgent must be present.
On Condition
    /IntermediaryAgent1 is present
Following Must be True
    /CreditorAgent Must be present
• IntermediaryAgent2AccountRule
If IntermediaryAgent2Account is present, then IntermediaryAgent2 must be present.
On Condition
    /IntermediaryAgent2 is absent
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1025 March 2026
```

## File page 1026

```text
Following Must be True
    /IntermediaryAgent2Account Must be absent
• IntermediaryAgent2Rule
If IntermediaryAgent2 is present, then IntermediaryAgent1 must be present.
On Condition
    /IntermediaryAgent2 is present
Following Must be True
    /IntermediaryAgent1 Must be present
• IntermediaryAgent3AccountRule
If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present.
On Condition
    /IntermediaryAgent3 is absent
Following Must be True
    /IntermediaryAgent3Account Must be absent
• IntermediaryAgent3Rule
If IntermediaryAgent3 is present, then IntermediaryAgent2 must be present.
On Condition
    /IntermediaryAgent3 is present
Following Must be True
    /IntermediaryAgent2 Must be present
• PaymentTypeInformationRule
If PaymentTypeInformation is present, then DirectDebitTransactionInformation/
PaymentTypeInformation is not allowed.
On Condition
    /PaymentTypeInformation is present
Following Must be True
    /DirectDebitTransactionInformation[*]/PaymentTypeInformation Must be absent
• TotalInterbankSettlementAmountAndSumRule
If TotalInterbankSettlementAmount is present, then it must equal the sum of all occurrences of
DirectDebitTransactionInformation/InterbankSettlementAmount.
On Condition
    /TotalInterbankSettlementAmount is present
Following Must be True
    /TotalInterbankSettlementAmount Must be equal to value 'sum of /
DirectDebitTransactionInformation[*]/InterbankSettlementAmount'
• TotalInterbankSettlementAmountRule
If CreditInformation/TotalInterbankSettlementAmount is present, then all occurrences of
DirectDebitTransactionInformation/InterbankSettlementAmount must have the same currency as the
currency of CreditInformation/TotalInterbankSettlementAmount.
On Condition
    /TotalInterbankSettlementAmount is present
Following Must be True
    /DirectDebitTransactionInformation[*]/InterbankSettlementAmount/
attribute::Currency Must be equal to /TotalInterbankSettlementAmount/
attribute::Currency
• UltimateCreditorGuideline
UltimateCreditor may only be present if different from Creditor.
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1026 March 2026
```

