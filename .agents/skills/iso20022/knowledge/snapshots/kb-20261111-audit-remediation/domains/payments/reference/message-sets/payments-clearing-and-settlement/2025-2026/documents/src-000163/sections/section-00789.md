---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.1.2 CreationDateTime <CreDtTm>"]
file_pages: [1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.1.2 CreationDateTime <CreDtTm>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1060 to 1067.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1060

```text
9.4.1.2  CreationDateTime <CreDtTm>
Presence: [1..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 1239
9.4.1.3  InstructingAgent <InstgAgt>
Presence: [0..1]
Definition: Agent that instructs the next party in the chain to carry out the (set of) instruction(s).
Usage: The instructing agent is the party sending the status message and not the party that sent the
original instruction that is being reported on.
InstructingAgent <InstgAgt> contains the following elements (see
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
9.4.1.4  InstructedAgent <InstdAgt>
Presence: [0..1]
Definition: Agent that is instructed by the previous party in the chain to carry out the (set of)
instruction(s).
Usage: The instructed agent is the party receiving the status message and not the party that received
the original instruction that is being reported on.
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1060 March 2026
```

## File page 1061

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
9.4.2 OriginalGroupInformation <OrgnlGrpInf>
Presence: [0..*]
Definition: Original group information concerning the group of transactions, to which the status request
message refers to.
OriginalGroupInformation <OrgnlGrpInf> contains the following elements (see
"OriginalGroupInformation27" on page 1189 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMessageIdentification <OrgnlMsgId> [1..1] Text 1189
   OriginalMessageNameIdentification <OrgnlMsgNmId> [1..1] Text 1189
   OriginalCreationDateTime <OrgnlCreDtTm> [0..1] DateTime 1189
   OriginalNumberOfTransactions <OrgnlNbOfTxs> [0..1] Text 1189
   OriginalControlSum <OrgnlCtrlSum> [0..1] Quantity 1190
9.4.3 TransactionInformation <TxInf>
Presence: [0..*]
Definition: Information concerning the original transaction, to which the status request message refers.
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1061 March 2026
```

## File page 1062

```text
TransactionInformation <TxInf> contains the following PaymentTransaction171 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatusRequestIdentification <StsReqId> [0..1] Text 1068
   OriginalGroupInformation <OrgnlGrpInf> [0..1]  1068
     OriginalMessageIdentification <OrgnlMsgId> [1..1] Text 1068
     OriginalMessageNameIdentification
<OrgnlMsgNmId>
[1..1] Text 1069
     OriginalCreationDateTime <OrgnlCreDtTm> [0..1] DateTime 1069
   OriginalInstructionIdentification <OrgnlInstrId> [0..1] Text 1069
   OriginalEndToEndIdentification <OrgnlEndToEndId> [0..1] Text 1069
   OriginalTransactionIdentification <OrgnlTxId> [0..1] Text 1069
   OriginalUETR <OrgnlUETR> [0..1] IdentifierSet 1069
   AcceptanceDateTime <AccptncDtTm> [0..1] DateTime 1069
   ClearingSystemReference <ClrSysRef> [0..1] Text 1070
   InstructingAgent <InstgAgt> [0..1] ± 1070
   InstructedAgent <InstdAgt> [0..1] ± 1070
   OriginalTransactionReference <OrgnlTxRef> [0..1]  1071
     InterbankSettlementAmount <IntrBkSttlmAmt> [0..1] Amount C2, C8 1077
     Amount <Amt> [0..1] ± 1078
     InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 1078
     RequestedCollectionDate <ReqdColltnDt> [0..1] Date 1078
     RequestedExecutionDate <ReqdExctnDt> [0..1] ± 1078
     CreditorSchemeIdentification <CdtrSchmeId> [0..1] ± 1079
     SettlementInformation <SttlmInf> [0..1]  C13,
C14,
C19,
C20,
C21,
C22,
C25,
C26
1080
       SettlementMethod <SttlmMtd> [1..1] CodeSet 1082
       SettlementAccount <SttlmAcct> [0..1] ± C12,
C11
1083
       ClearingSystem <ClrSys> [0..1]  1083
{Or         Code <Cd> [1..1] CodeSet 1084
Or}         Proprietary <Prtry> [1..1] Text 1084
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1062 March 2026
```

## File page 1063

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       InstructingReimbursementAgent
<InstgRmbrsmntAgt>
[0..1] ± 1084
       InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C12,
C11
1085
       InstructedReimbursementAgent
<InstdRmbrsmntAgt>
[0..1] ± 1085
       InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C12,
C11
1086
       ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 1087
       ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C12,
C11
1087
     PaymentTypeInformation <PmtTpInf> [0..1] ± 1088
     PaymentMethod <PmtMtd> [0..1] CodeSet 1089
     MandateRelatedInformation <MndtRltdInf> [0..1]  1089
{Or       DirectDebitMandate <DrctDbtMndt> [1..1]  C3, C4 1091
         MandateIdentification <MndtId> [0..1] Text 1093
         DateOfSignature <DtOfSgntr> [0..1] Date 1093
         AmendmentIndicator <AmdmntInd> [0..1] Indicator 1093
         AmendmentInformationDetails <AmdmntInfDtls> [0..1]  1093
           OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 1094
           OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 1094
           OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 1095
           OriginalCreditorAgentAccount
<OrgnlCdtrAgtAcct>
[0..1] ± C12,
C11
1096
           OriginalDebtor <OrgnlDbtr> [0..1] ± 1097
           OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C12,
C11
1098
           OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 1099
           OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C12,
C11
1100
           OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 1101
           OriginalFrequency <OrgnlFrqcy> [0..1] ± 1101
           OriginalReason <OrgnlRsn> [0..1]  1101
{Or             Code <Cd> [1..1] CodeSet 1101
Or}             Proprietary <Prtry> [1..1] Text 1101
           OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 1102
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1063 March 2026
```

## File page 1064

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         ElectronicSignature <ElctrncSgntr> [0..1] Text 1102
         FirstCollectionDate <FrstColltnDt> [0..1] Date 1102
         FinalCollectionDate <FnlColltnDt> [0..1] Date 1102
         Frequency <Frqcy> [0..1] ± 1102
         Reason <Rsn> [0..1]  1102
{Or           Code <Cd> [1..1] CodeSet 1103
Or}           Proprietary <Prtry> [1..1] Text 1103
         TrackingDays <TrckgDays> [0..1] Text 1103
Or}       CreditTransferMandate <CdtTrfMndt> [1..1] ± 1103
     RemittanceInformation <RmtInf> [0..1]  1104
       Unstructured <Ustrd> [0..*] Text 1108
       Structured <Strd> [0..*]  1108
         ReferredDocumentInformation <RfrdDocInf> [0..*]  1112
           Type <Tp> [0..1]  1114
             CodeOrProprietary <CdOrPrtry> [1..1]  1114
{Or               Code <Cd> [1..1] CodeSet 1114
Or}               Proprietary <Prtry> [1..1] Text 1114
             Issuer <Issr> [0..1] Text 1114
           Number <Nb> [0..1] Text 1115
           RelatedDate <RltdDt> [0..1]  1115
             Type <Tp> [1..1]  1115
{Or               Code <Cd> [1..1] CodeSet 1115
Or}               Proprietary <Prtry> [1..1] Text 1115
             Date <Dt> [1..1] Date 1115
           LineDetails <LineDtls> [0..*]  1116
             Identification <Id> [1..*]  1116
               Type <Tp> [0..1]  1117
                 CodeOrProprietary <CdOrPrtry> [1..1]  1117
{Or                   Code <Cd> [1..1] CodeSet 1117
Or}                   Proprietary <Prtry> [1..1] Text 1117
                 Issuer <Issr> [0..1] Text 1118
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1064 March 2026
```

## File page 1065

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
               Number <Nb> [0..1] Text 1118
               RelatedDate <RltdDt> [0..1] Date 1118
             Description <Desc> [0..1] Text 1118
             Amount <Amt> [0..1]  C18 1118
               RemittanceAmountAndType <RmtAmtAndTp> [0..*]  1119
                 Type <Tp> [1..1]  1119
{Or                   Code <Cd> [1..1] CodeSet 1120
Or}                   Proprietary <Prtry> [1..1] Text 1120
                 Amount <Amt> [1..1] Amount C2, C8 1120
               AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  1120
                 Amount <Amt> [1..1] Amount C2, C8 1120
                 CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1121
                 Reason <Rsn> [0..1] Text 1121
                 AdditionalInformation <AddtlInf> [0..1] Text 1121
         ReferredDocumentAmount <RfrdDocAmt> [0..1]  C18 1121
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  1122
             Type <Tp> [1..1]  1122
{Or               Code <Cd> [1..1] CodeSet 1123
Or}               Proprietary <Prtry> [1..1] Text 1123
             Amount <Amt> [1..1] Amount C2, C8 1123
           AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  1123
             Amount <Amt> [1..1] Amount C2, C8 1123
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1124
             Reason <Rsn> [0..1] Text 1124
             AdditionalInformation <AddtlInf> [0..1] Text 1124
         CreditorReferenceInformation <CdtrRefInf> [0..1]  1124
           Type <Tp> [0..1]  1125
             CodeOrProprietary <CdOrPrtry> [1..1]  1125
{Or               Code <Cd> [1..1] CodeSet 1125
Or}               Proprietary <Prtry> [1..1] Text 1125
             Issuer <Issr> [0..1] Text 1126
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1065 March 2026
```

## File page 1066

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Reference <Ref> [0..1] Text 1126
         Invoicer <Invcr> [0..1] ± 1126
         Invoicee <Invcee> [0..1] ± 1127
         TaxRemittance <TaxRmt> [0..1]  1128
           Creditor <Cdtr> [0..1] ± 1130
           Debtor <Dbtr> [0..1] ± 1130
           UltimateDebtor <UltmtDbtr> [0..1] ± 1130
           AdministrationZone <AdmstnZone> [0..1] Text 1131
           ReferenceNumber <RefNb> [0..1] Text 1131
           Method <Mtd> [0..1] Text 1131
           TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C8 1131
           TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C8 1132
           Date <Dt> [0..1] Date 1132
           SequenceNumber <SeqNb> [0..1] Quantity 1132
           Record <Rcrd> [0..*]  1132
             Type <Tp> [0..1] Text 1133
             Category <Ctgy> [0..1] Text 1133
             CategoryDetails <CtgyDtls> [0..1] Text 1133
             DebtorStatus <DbtrSts> [0..1] Text 1134
             CertificateIdentification <CertId> [0..1] Text 1134
             FormsCode <FrmsCd> [0..1] Text 1134
             Period <Prd> [0..1]  1134
               Year <Yr> [0..1] Year 1134
               Type <Tp> [0..1] CodeSet 1134
               FromToDate <FrToDt> [0..1] ± 1135
             TaxAmount <TaxAmt> [0..1]  1136
               Rate <Rate> [0..1] Rate 1136
               TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C8 1136
               TotalAmount <TtlAmt> [0..1] Amount C2, C8 1136
               Details <Dtls> [0..*]  1137
                 Period <Prd> [0..1]  1137
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1066 March 2026
```

## File page 1067

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
                   Year <Yr> [0..1] Year 1137
                   Type <Tp> [0..1] CodeSet 1138
                   FromToDate <FrToDt> [0..1] ± 1138
                 Amount <Amt> [1..1] Amount C2, C8 1139
             AdditionalInformation <AddtlInf> [0..1] Text 1139
         GarnishmentRemittance <GrnshmtRmt> [0..1]  1139
           Type <Tp> [1..1]  1140
             CodeOrProprietary <CdOrPrtry> [1..1]  1140
{Or               Code <Cd> [1..1] CodeSet 1141
Or}               Proprietary <Prtry> [1..1] Text 1141
             Issuer <Issr> [0..1] Text 1141
           Garnishee <Grnshee> [0..1] ± 1141
           GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 1142
           ReferenceNumber <RefNb> [0..1] Text 1143
           Date <Dt> [0..1] Date 1144
           RemittedAmount <RmtdAmt> [0..1] Amount C2, C8 1144
           FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 1144
           EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 1144
         SecuritiesData <SctiesData> [0..*]  1144
           UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 1145
           Amount <Amt> [0..1] Amount C1, C9 1145
         AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 1145
     UltimateDebtor <UltmtDbtr> [0..1]  1145
{Or       Party <Pty> [1..1] ± 1146
Or}       Agent <Agt> [1..1] ± 1147
     Debtor <Dbtr> [0..1]  1148
{Or       Party <Pty> [1..1] ± 1148
Or}       Agent <Agt> [1..1] ± 1149
     DebtorAccount <DbtrAcct> [0..1] ± C12,
C11
1150
     DebtorAgent <DbtrAgt> [0..1] ± 1151
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1067 March 2026
```

