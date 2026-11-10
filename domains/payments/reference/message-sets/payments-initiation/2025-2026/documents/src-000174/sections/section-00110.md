---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.5 StatusReasonInformation <StsRsnInf>", "3.4.3.5.2 Reason <Rsn>", "3.4.3.5.2.1 Code <Cd>"]
file_pages: [164, 165, 166, 167, 168, 169, 170, 171]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.5.2.1 Code <Cd>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 164 to 171.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 164

```text
Reason <Rsn> contains one of the following StatusReason6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 164
Or}   Proprietary <Prtry> [1..1] Text 164
3.4.3.5.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the status, as published in an external reason code list.
Datatype: "ExternalStatusReason1Code" on page 597
3.4.3.5.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the status, in a proprietary form.
Datatype: "Max35Text" on page 609
3.4.3.5.3  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Further details on the status reason.
Usage: Additional information can be used for several purposes such as the reporting of repaired
information.
Datatype: "Max105Text" on page 607
3.4.3.6  NumberOfTransactionsPerStatus <NbOfTxsPerSts>
Presence: [0..*]
Definition: Detailed information on the number of transactions for each identical transaction status.
NumberOfTransactionsPerStatus <NbOfTxsPerSts> contains the following elements (see
"NumberOfTransactionsPerStatus5" on page 552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DetailedNumberOfTransactions <DtldNbOfTxs> [1..1] Text 552
   DetailedStatus <DtldSts> [1..1] CodeSet 552
   DetailedControlSum <DtldCtrlSum> [0..1] Quantity 552
3.4.3.7  TransactionInformationAndStatus <TxInfAndSts>
Presence: [0..*]
Definition: Provides information on the original transactions to which the status report message refers.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 164 March 2026
```

## File page 165

```text
TransactionInformationAndStatus <TxInfAndSts> contains the following PaymentTransaction178
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatusIdentification <StsId> [0..1] Text 172
   OriginalInstructionIdentification <OrgnlInstrId> [0..1] Text 172
   OriginalEndToEndIdentification <OrgnlEndToEndId> [0..1] Text 172
   OriginalUETR <OrgnlUETR> [0..1] IdentifierSet 172
   TransactionStatus <TxSts> [0..1] CodeSet 172
   StatusReasonInformation <StsRsnInf> [0..*]  C30 172
     Originator <Orgtr> [0..1] ± 173
     Reason <Rsn> [0..1]  174
{Or       Code <Cd> [1..1] CodeSet 175
Or}       Proprietary <Prtry> [1..1] Text 175
     AdditionalInformation <AddtlInf> [0..*] Text 175
   ChargesInformation <ChrgsInf> [0..*]  175
     Amount <Amt> [1..1] Amount C2, C8 175
     Agent <Agt> [1..1] ± 176
     Type <Tp> [0..1]  176
{Or       Code <Cd> [1..1] CodeSet 177
Or}       Proprietary <Prtry> [1..1] ± 177
   TrackerData <TrckrData> [0..1]  177
     ConfirmedDate <ConfdDt> [1..1] ± 178
     ConfirmedAmount <ConfdAmt> [1..1] Amount C1, C9 178
     TrackerRecord <TrckrRcrd> [1..*]  178
       Agent <Agt> [1..1] ± 179
       ChargeBearer <ChrgBr> [0..1] CodeSet 179
       ChargesAmount <ChrgsAmt> [0..1] Amount C1, C9 180
       ExchangeRateData <XchgRateData> [0..1]  180
         SourceCurrency <SrcCcy> [1..1] CodeSet C1 181
         TargetCurrency <TrgtCcy> [1..1] CodeSet C1 181
         ExchangeRate <XchgRate> [1..1] Rate 181
         UnitCurrency <UnitCcy> [0..1] CodeSet C1 181
   AcceptanceDateTime <AccptncDtTm> [0..1] DateTime 182
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 165 March 2026
```

## File page 166

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or         Code <Cd> [1..1] CodeSet 195
Or}         Proprietary <Prtry> [1..1] Text 195
       InstructingReimbursementAgent
<InstgRmbrsmntAgt>
[0..1] ± 195
       InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C16,
C15
196
       InstructedReimbursementAgent
<InstdRmbrsmntAgt>
[0..1] ± 196
       InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C16,
C15
197
       ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 198
       ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C16,
C15
198
     PaymentTypeInformation <PmtTpInf> [0..1] ± 199
     PaymentMethod <PmtMtd> [0..1] CodeSet 200
     MandateRelatedInformation <MndtRltdInf> [0..1]  200
{Or       DirectDebitMandate <DrctDbtMndt> [1..1]  C3, C4 202
         MandateIdentification <MndtId> [0..1] Text 204
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 166 March 2026
```

## File page 167

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         DateOfSignature <DtOfSgntr> [0..1] Date 204
         AmendmentIndicator <AmdmntInd> [0..1] Indicator 204
         AmendmentInformationDetails <AmdmntInfDtls> [0..1]  204
           OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 205
           OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 205
           OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 206
           OriginalCreditorAgentAccount
<OrgnlCdtrAgtAcct>
[0..1] ± C16,
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
{Or             Code <Cd> [1..1] CodeSet 212
Or}             Proprietary <Prtry> [1..1] Text 212
           OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 213
         ElectronicSignature <ElctrncSgntr> [0..1] Text 213
         FirstCollectionDate <FrstColltnDt> [0..1] Date 213
         FinalCollectionDate <FnlColltnDt> [0..1] Date 213
         Frequency <Frqcy> [0..1] ± 213
         Reason <Rsn> [0..1]  213
{Or           Code <Cd> [1..1] CodeSet 214
Or}           Proprietary <Prtry> [1..1] Text 214
         TrackingDays <TrckgDays> [0..1] Text 214
Or}       CreditTransferMandate <CdtTrfMndt> [1..1] ± 214
     RemittanceInformation <RmtInf> [0..1]  215
       Unstructured <Ustrd> [0..*] Text 219
       Structured <Strd> [0..*]  219
         ReferredDocumentInformation <RfrdDocInf> [0..*]  223
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 167 March 2026
```

## File page 168

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Type <Tp> [0..1]  225
             CodeOrProprietary <CdOrPrtry> [1..1]  225
{Or               Code <Cd> [1..1] CodeSet 225
Or}               Proprietary <Prtry> [1..1] Text 225
             Issuer <Issr> [0..1] Text 225
           Number <Nb> [0..1] Text 226
           RelatedDate <RltdDt> [0..1]  226
             Type <Tp> [1..1]  226
{Or               Code <Cd> [1..1] CodeSet 226
Or}               Proprietary <Prtry> [1..1] Text 226
             Date <Dt> [1..1] Date 226
           LineDetails <LineDtls> [0..*]  227
             Identification <Id> [1..*]  227
               Type <Tp> [0..1]  228
                 CodeOrProprietary <CdOrPrtry> [1..1]  228
{Or                   Code <Cd> [1..1] CodeSet 228
Or}                   Proprietary <Prtry> [1..1] Text 228
                 Issuer <Issr> [0..1] Text 229
               Number <Nb> [0..1] Text 229
               RelatedDate <RltdDt> [0..1] Date 229
             Description <Desc> [0..1] Text 229
             Amount <Amt> [0..1]  C24 229
               RemittanceAmountAndType <RmtAmtAndTp> [0..*]  230
                 Type <Tp> [1..1]  230
{Or                   Code <Cd> [1..1] CodeSet 231
Or}                   Proprietary <Prtry> [1..1] Text 231
                 Amount <Amt> [1..1] Amount C2, C8 231
               AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  231
                 Amount <Amt> [1..1] Amount C2, C8 231
                 CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 232
                 Reason <Rsn> [0..1] Text 232
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 168 March 2026
```

## File page 169

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
                 AdditionalInformation <AddtlInf> [0..1] Text 232
         ReferredDocumentAmount <RfrdDocAmt> [0..1]  C24 232
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  233
             Type <Tp> [1..1]  233
{Or               Code <Cd> [1..1] CodeSet 234
Or}               Proprietary <Prtry> [1..1] Text 234
             Amount <Amt> [1..1] Amount C2, C8 234
           AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  234
             Amount <Amt> [1..1] Amount C2, C8 234
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 235
             Reason <Rsn> [0..1] Text 235
             AdditionalInformation <AddtlInf> [0..1] Text 235
         CreditorReferenceInformation <CdtrRefInf> [0..1]  235
           Type <Tp> [0..1]  236
             CodeOrProprietary <CdOrPrtry> [1..1]  236
{Or               Code <Cd> [1..1] CodeSet 236
Or}               Proprietary <Prtry> [1..1] Text 236
             Issuer <Issr> [0..1] Text 237
           Reference <Ref> [0..1] Text 237
         Invoicer <Invcr> [0..1] ± 237
         Invoicee <Invcee> [0..1] ± 238
         TaxRemittance <TaxRmt> [0..1]  239
           Creditor <Cdtr> [0..1] ± 241
           Debtor <Dbtr> [0..1] ± 241
           UltimateDebtor <UltmtDbtr> [0..1] ± 241
           AdministrationZone <AdmstnZone> [0..1] Text 242
           ReferenceNumber <RefNb> [0..1] Text 242
           Method <Mtd> [0..1] Text 242
           TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C8 242
           TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C8 243
           Date <Dt> [0..1] Date 243
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 169 March 2026
```

## File page 170

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
         GarnishmentRemittance <GrnshmtRmt> [0..1]  250
           Type <Tp> [1..1]  251
             CodeOrProprietary <CdOrPrtry> [1..1]  251
{Or               Code <Cd> [1..1] CodeSet 252
Or}               Proprietary <Prtry> [1..1] Text 252
             Issuer <Issr> [0..1] Text 252
           Garnishee <Grnshee> [0..1] ± 252
           GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 253
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 170 March 2026
```

## File page 171

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           ReferenceNumber <RefNb> [0..1] Text 254
           Date <Dt> [0..1] Date 255
           RemittedAmount <RmtdAmt> [0..1] Amount C2, C8 255
           FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 255
           EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 255
         SecuritiesData <SctiesData> [0..*]  255
           UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 256
           Amount <Amt> [0..1] Amount C1, C9 256
         AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 256
     UltimateDebtor <UltmtDbtr> [0..1]  256
{Or       Party <Pty> [1..1] ± 257
Or}       Agent <Agt> [1..1] ± 258
     Debtor <Dbtr> [0..1]  259
{Or       Party <Pty> [1..1] ± 259
Or}       Agent <Agt> [1..1] ± 260
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
{Or       Party <Pty> [1..1] ± 265
Or}       Agent <Agt> [1..1] ± 266
     CreditorAccount <CdtrAcct> [0..1] ± C16,
C15
267
     UltimateCreditor <UltmtCdtr> [0..1]  268
{Or       Party <Pty> [1..1] ± 268
Or}       Agent <Agt> [1..1] ± 269
     Purpose <Purp> [0..1] ± 270
   SupplementaryData <SplmtryData> [0..*] ± C32 270
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 171 March 2026
```

