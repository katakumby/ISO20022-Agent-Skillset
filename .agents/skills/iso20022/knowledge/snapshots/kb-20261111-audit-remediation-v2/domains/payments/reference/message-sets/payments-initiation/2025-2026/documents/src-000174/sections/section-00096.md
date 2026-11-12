---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.2 Structure"]
file_pages: [131, 132, 133, 134, 135, 136, 137, 138]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.2 Structure

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 131 to 138.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 131

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CstmrPmtStsRpt> [1..1]  C10,
C11,
C12,
C13,
C31
   GroupHeader <GrpHdr> [1..1]  0
     MessageIdentification <MsgId> [1..1] Text 143
     CreationDateTime <CreDtTm> [1..1] DateTime 143
     InitiatingParty <InitgPty> [0..1] ± 143
     ForwardingAgent <FwdgAgt> [0..1] ± 144
     DebtorAgent <DbtrAgt> [0..1] ± 145
     CreditorAgent <CdtrAgt> [0..1] ± 146
   OriginalGroupInformationAndStatus <OrgnlGrpInfAndSts> [1..1]  C29,
C19
146
     OriginalMessageIdentification <OrgnlMsgId> [1..1] Text 147
     OriginalMessageNameIdentification <OrgnlMsgNmId> [1..1] Text 147
     OriginalCreationDateTime <OrgnlCreDtTm> [0..1] DateTime 148
     OriginalNumberOfTransactions <OrgnlNbOfTxs> [0..1] Text 148
     OriginalControlSum <OrgnlCtrlSum> [0..1] Quantity 148
     GroupStatus <GrpSts> [0..1] CodeSet 148
     StatusReasonInformation <StsRsnInf> [0..*]  C30 148
       Originator <Orgtr> [0..1] ± 149
       Reason <Rsn> [0..1]  150
{Or         Code <Cd> [1..1] CodeSet 151
Or}         Proprietary <Prtry> [1..1] Text 151
       AdditionalInformation <AddtlInf> [0..*] Text 151
     NumberOfTransactionsPerStatus <NbOfTxsPerSts> [0..*] ± 151
   OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts> [0..*]  C20,
C21,
C22,
C23
151
     OriginalPaymentInformationIdentification <OrgnlPmtInfId> [1..1] Text 161
     OriginalNumberOfTransactions <OrgnlNbOfTxs> [0..1] Text 161
     OriginalControlSum <OrgnlCtrlSum> [0..1] Quantity 161
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 131 March 2026
```

## File page 132

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     PaymentInformationStatus <PmtInfSts> [0..1] CodeSet 161
     StatusReasonInformation <StsRsnInf> [0..*]  C30 161
       Originator <Orgtr> [0..1] ± 162
       Reason <Rsn> [0..1]  163
{Or         Code <Cd> [1..1] CodeSet 164
Or}         Proprietary <Prtry> [1..1] Text 164
       AdditionalInformation <AddtlInf> [0..*] Text 164
     NumberOfTransactionsPerStatus <NbOfTxsPerSts> [0..*] ± 164
     TransactionInformationAndStatus <TxInfAndSts> [0..*]  164
       StatusIdentification <StsId> [0..1] Text 172
       OriginalInstructionIdentification <OrgnlInstrId> [0..1] Text 172
       OriginalEndToEndIdentification <OrgnlEndToEndId> [0..1] Text 172
       OriginalUETR <OrgnlUETR> [0..1] IdentifierSet 172
       TransactionStatus <TxSts> [0..1] CodeSet 172
       StatusReasonInformation <StsRsnInf> [0..*]  C30 172
         Originator <Orgtr> [0..1] ± 173
         Reason <Rsn> [0..1]  174
{Or           Code <Cd> [1..1] CodeSet 175
Or}           Proprietary <Prtry> [1..1] Text 175
         AdditionalInformation <AddtlInf> [0..*] Text 175
       ChargesInformation <ChrgsInf> [0..*]  175
         Amount <Amt> [1..1] Amount C2, C8 175
         Agent <Agt> [1..1] ± 176
         Type <Tp> [0..1]  176
{Or           Code <Cd> [1..1] CodeSet 177
Or}           Proprietary <Prtry> [1..1] ± 177
       TrackerData <TrckrData> [0..1]  177
         ConfirmedDate <ConfdDt> [1..1] ± 178
         ConfirmedAmount <ConfdAmt> [1..1] Amount C1, C9 178
         TrackerRecord <TrckrRcrd> [1..*]  178
           Agent <Agt> [1..1] ± 179
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 132 March 2026
```

## File page 133

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           ChargeBearer <ChrgBr> [0..1] CodeSet 179
           ChargesAmount <ChrgsAmt> [0..1] Amount C1, C9 180
           ExchangeRateData <XchgRateData> [0..1]  180
             SourceCurrency <SrcCcy> [1..1] CodeSet C1 181
             TargetCurrency <TrgtCcy> [1..1] CodeSet C1 181
             ExchangeRate <XchgRate> [1..1] Rate 181
             UnitCurrency <UnitCcy> [0..1] CodeSet C1 181
       AcceptanceDateTime <AccptncDtTm> [0..1] DateTime 182
       AccountServicerReference <AcctSvcrRef> [0..1] Text 182
       ClearingSystemReference <ClrSysRef> [0..1] Text 182
       OriginalTransactionReference <OrgnlTxRef> [0..1]  182
         InterbankSettlementAmount <IntrBkSttlmAmt> [0..1] Amount C2, C8 188
         Amount <Amt> [0..1] ± 189
         InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 189
         RequestedCollectionDate <ReqdColltnDt> [0..1] Date 189
         RequestedExecutionDate <ReqdExctnDt> [0..1] ± 189
         CreditorSchemeIdentification <CdtrSchmeId> [0..1] ± 190
         SettlementInformation <SttlmInf> [0..1]  C17,
C18,
C25,
C26,
C27,
C28,
C33,
C34
191
           SettlementMethod <SttlmMtd> [1..1] CodeSet 193
           SettlementAccount <SttlmAcct> [0..1] ± C16,
C15
194
           ClearingSystem <ClrSys> [0..1]  194
{Or             Code <Cd> [1..1] CodeSet 195
Or}             Proprietary <Prtry> [1..1] Text 195
           InstructingReimbursementAgent <InstgRmbrsmntAgt> [0..1] ± 195
           InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C16,
C15
196
           InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 196
           InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C16,
C15
197
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 133 March 2026
```

## File page 134

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 198
           ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C16,
C15
198
         PaymentTypeInformation <PmtTpInf> [0..1] ± 199
         PaymentMethod <PmtMtd> [0..1] CodeSet 200
         MandateRelatedInformation <MndtRltdInf> [0..1]  200
{Or           DirectDebitMandate <DrctDbtMndt> [1..1]  C3, C4 202
             MandateIdentification <MndtId> [0..1] Text 204
             DateOfSignature <DtOfSgntr> [0..1] Date 204
             AmendmentIndicator <AmdmntInd> [0..1] Indicator 204
             AmendmentInformationDetails <AmdmntInfDtls> [0..1]  204
               OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 205
               OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 205
               OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 206
               OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C16,
C15
207
               OriginalDebtor <OrgnlDbtr> [0..1] ± 208
               OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C16,
C15
209
               OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 210
               OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C16,
C15
211
               OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 212
               OriginalFrequency <OrgnlFrqcy> [0..1] ± 212
               OriginalReason <OrgnlRsn> [0..1]  212
{Or                 Code <Cd> [1..1] CodeSet 212
Or}                 Proprietary <Prtry> [1..1] Text 212
               OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 213
             ElectronicSignature <ElctrncSgntr> [0..1] Text 213
             FirstCollectionDate <FrstColltnDt> [0..1] Date 213
             FinalCollectionDate <FnlColltnDt> [0..1] Date 213
             Frequency <Frqcy> [0..1] ± 213
             Reason <Rsn> [0..1]  213
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 134 March 2026
```

## File page 135

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or               Code <Cd> [1..1] CodeSet 214
Or}               Proprietary <Prtry> [1..1] Text 214
             TrackingDays <TrckgDays> [0..1] Text 214
Or}           CreditTransferMandate <CdtTrfMndt> [1..1] ± 214
         RemittanceInformation <RmtInf> [0..1]  215
           Unstructured <Ustrd> [0..*] Text 219
           Structured <Strd> [0..*]  219
             ReferredDocumentInformation <RfrdDocInf> [0..*]  223
               Type <Tp> [0..1]  225
                 CodeOrProprietary <CdOrPrtry> [1..1]  225
{Or                   Code <Cd> [1..1] CodeSet 225
Or}                   Proprietary <Prtry> [1..1] Text 225
                 Issuer <Issr> [0..1] Text 225
               Number <Nb> [0..1] Text 226
               RelatedDate <RltdDt> [0..1]  226
                 Type <Tp> [1..1]  226
{Or                   Code <Cd> [1..1] CodeSet 226
Or}                   Proprietary <Prtry> [1..1] Text 226
                 Date <Dt> [1..1] Date 226
               LineDetails <LineDtls> [0..*]  227
                 Identification <Id> [1..*]  227
                   Type <Tp> [0..1]  228
                     CodeOrProprietary <CdOrPrtry> [1..1]  228
{Or                       Code <Cd> [1..1] CodeSet 228
Or}                       Proprietary <Prtry> [1..1] Text 228
                     Issuer <Issr> [0..1] Text 229
                   Number <Nb> [0..1] Text 229
                   RelatedDate <RltdDt> [0..1] Date 229
                 Description <Desc> [0..1] Text 229
                 Amount <Amt> [0..1]  C24 229
                   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  230
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 135 March 2026
```

## File page 136

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
                     Type <Tp> [1..1]  230
{Or                       Code <Cd> [1..1] CodeSet 231
Or}                       Proprietary <Prtry> [1..1] Text 231
                     Amount <Amt> [1..1] Amount C2, C8 231
                   AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  231
                     Amount <Amt> [1..1] Amount C2, C8 231
                     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 232
                     Reason <Rsn> [0..1] Text 232
                     AdditionalInformation <AddtlInf> [0..1] Text 232
             ReferredDocumentAmount <RfrdDocAmt> [0..1]  C24 232
               RemittanceAmountAndType <RmtAmtAndTp> [0..*]  233
                 Type <Tp> [1..1]  233
{Or                   Code <Cd> [1..1] CodeSet 234
Or}                   Proprietary <Prtry> [1..1] Text 234
                 Amount <Amt> [1..1] Amount C2, C8 234
               AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  234
                 Amount <Amt> [1..1] Amount C2, C8 234
                 CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 235
                 Reason <Rsn> [0..1] Text 235
                 AdditionalInformation <AddtlInf> [0..1] Text 235
             CreditorReferenceInformation <CdtrRefInf> [0..1]  235
               Type <Tp> [0..1]  236
                 CodeOrProprietary <CdOrPrtry> [1..1]  236
{Or                   Code <Cd> [1..1] CodeSet 236
Or}                   Proprietary <Prtry> [1..1] Text 236
                 Issuer <Issr> [0..1] Text 237
               Reference <Ref> [0..1] Text 237
             Invoicer <Invcr> [0..1] ± 237
             Invoicee <Invcee> [0..1] ± 238
             TaxRemittance <TaxRmt> [0..1]  239
               Creditor <Cdtr> [0..1] ± 241
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 136 March 2026
```

## File page 137

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               Debtor <Dbtr> [0..1] ± 241
               UltimateDebtor <UltmtDbtr> [0..1] ± 241
               AdministrationZone <AdmstnZone> [0..1] Text 242
               ReferenceNumber <RefNb> [0..1] Text 242
               Method <Mtd> [0..1] Text 242
               TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C8 242
               TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C8 243
               Date <Dt> [0..1] Date 243
               SequenceNumber <SeqNb> [0..1] Quantity 243
               Record <Rcrd> [0..*]  243
                 Type <Tp> [0..1] Text 244
                 Category <Ctgy> [0..1] Text 244
                 CategoryDetails <CtgyDtls> [0..1] Text 244
                 DebtorStatus <DbtrSts> [0..1] Text 245
                 CertificateIdentification <CertId> [0..1] Text 245
                 FormsCode <FrmsCd> [0..1] Text 245
                 Period <Prd> [0..1]  245
                   Year <Yr> [0..1] Year 245
                   Type <Tp> [0..1] CodeSet 245
                   FromToDate <FrToDt> [0..1] ± 246
                 TaxAmount <TaxAmt> [0..1]  247
                   Rate <Rate> [0..1] Rate 247
                   TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C8 247
                   TotalAmount <TtlAmt> [0..1] Amount C2, C8 247
                   Details <Dtls> [0..*]  248
                     Period <Prd> [0..1]  248
                       Year <Yr> [0..1] Year 248
                       Type <Tp> [0..1] CodeSet 249
                       FromToDate <FrToDt> [0..1] ± 249
                     Amount <Amt> [1..1] Amount C2, C8 250
                 AdditionalInformation <AddtlInf> [0..1] Text 250
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 137 March 2026
```

## File page 138

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             GarnishmentRemittance <GrnshmtRmt> [0..1]  250
               Type <Tp> [1..1]  251
                 CodeOrProprietary <CdOrPrtry> [1..1]  251
{Or                   Code <Cd> [1..1] CodeSet 252
Or}                   Proprietary <Prtry> [1..1] Text 252
                 Issuer <Issr> [0..1] Text 252
               Garnishee <Grnshee> [0..1] ± 252
               GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 253
               ReferenceNumber <RefNb> [0..1] Text 254
               Date <Dt> [0..1] Date 255
               RemittedAmount <RmtdAmt> [0..1] Amount C2, C8 255
               FamilyMedicalInsuranceIndicator <FmlyMdclInsrncInd> [0..1] Indicator 255
               EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 255
             SecuritiesData <SctiesData> [0..*]  255
               UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 256
               Amount <Amt> [0..1] Amount C1, C9 256
             AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 256
         UltimateDebtor <UltmtDbtr> [0..1]  256
{Or           Party <Pty> [1..1] ± 257
Or}           Agent <Agt> [1..1] ± 258
         Debtor <Dbtr> [0..1]  259
{Or           Party <Pty> [1..1] ± 259
Or}           Agent <Agt> [1..1] ± 260
         DebtorAccount <DbtrAcct> [0..1] ± C16,
C15
261
         DebtorAgent <DbtrAgt> [0..1] ± 262
         DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C16,
C15
262
         CreditorAgent <CdtrAgt> [0..1] ± 263
         CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C16,
C15
264
         Creditor <Cdtr> [0..1]  265
{Or           Party <Pty> [1..1] ± 265
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 138 March 2026
```

