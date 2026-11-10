---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.2 Structure"]
file_pages: [133, 134, 135, 136, 137, 138, 139]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.2 Structure

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 133 to 139.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 133

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FIToFICstmrDrctDbt> [1..1]  C12,
C16,
C20,
C26,
C31,
C34,
C35,
C37
   GroupHeader <GrpHdr> [1..1]  C33 0
     MessageIdentification <MsgId> [1..1] Text 144
     CreationDateTime <CreDtTm> [1..1] DateTime 145
     Authorisation <Authstn> [0..2] ± 145
     BatchBooking <BtchBookg> [0..1] Indicator 145
     NumberOfTransactions <NbOfTxs> [1..1] Text 145
     ControlSum <CtrlSum> [0..1] Quantity 146
     TotalInterbankSettlementAmount <TtlIntrBkSttlmAmt> [0..1] Amount C1, C10 146
     InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 146
     SettlementInformation <SttlmInf> [1..1]  C29,
C30
146
       SettlementMethod <SttlmMtd> [1..1] CodeSet 147
       SettlementAccount <SttlmAcct> [0..1] ± C15,
C14
147
       ClearingSystem <ClrSys> [0..1]  148
{Or         Code <Cd> [1..1] CodeSet 148
Or}         Proprietary <Prtry> [1..1] Text 148
     PaymentTypeInformation <PmtTpInf> [0..1] ± 149
     InstructingAgent <InstgAgt> [0..1] ± 149
     InstructedAgent <InstdAgt> [0..1] ± 150
   DirectDebitTransactionInformation <DrctDbtTxInf> [1..*]  C8, C17,
C18,
C19,
C21,
C22,
C23,
C24,
C25, C7,
C38,
C39
151
     PaymentIdentification <PmtId> [1..1] ± C36 159
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
133 March 2026
```

## File page 134

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     PaymentTypeInformation <PmtTpInf> [0..1] ± 160
     InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount C1, C10 161
     InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 161
     SettlementPriority <SttlmPrty> [0..1] CodeSet 161
     SettlementTimeIndication <SttlmTmIndctn> [0..1]  161
       DebitDateTime <DbtDtTm> [0..1] DateTime 162
       CreditDateTime <CdtDtTm> [0..1] DateTime 162
     InstructedAmount <InstdAmt> [0..1] Amount C2, C11 162
     ExchangeRate <XchgRate> [0..1] Rate 162
     ChargeBearer <ChrgBr> [1..1] CodeSet 163
     ChargesInformation <ChrgsInf> [0..*]  163
       Amount <Amt> [1..1] Amount C2, C11 163
       Agent <Agt> [1..1] ± 164
       Type <Tp> [0..1]  164
{Or         Code <Cd> [1..1] CodeSet 165
Or}         Proprietary <Prtry> [1..1] ± 165
     RequestedCollectionDate <ReqdColltnDt> [0..1] Date 165
     DirectDebitTransaction <DrctDbtTx> [0..1]  165
       MandateRelatedInformation <MndtRltdInf> [0..1]  C3, C4 167
         MandateIdentification <MndtId> [0..1] Text 169
         DateOfSignature <DtOfSgntr> [0..1] Date 169
         AmendmentIndicator <AmdmntInd> [0..1] Indicator 169
         AmendmentInformationDetails <AmdmntInfDtls> [0..1]  169
           OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 170
           OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 170
           OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 171
           OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C15,
C14
172
           OriginalDebtor <OrgnlDbtr> [0..1] ± 173
           OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C15,
C14
174
           OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 175
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
134 March 2026
```

## File page 135

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C15,
C14
176
           OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 177
           OriginalFrequency <OrgnlFrqcy> [0..1] ± 177
           OriginalReason <OrgnlRsn> [0..1]  177
{Or             Code <Cd> [1..1] CodeSet 177
Or}             Proprietary <Prtry> [1..1] Text 177
           OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 178
         ElectronicSignature <ElctrncSgntr> [0..1] Text 178
         FirstCollectionDate <FrstColltnDt> [0..1] Date 178
         FinalCollectionDate <FnlColltnDt> [0..1] Date 178
         Frequency <Frqcy> [0..1] ± 178
         Reason <Rsn> [0..1]  178
{Or           Code <Cd> [1..1] CodeSet 179
Or}           Proprietary <Prtry> [1..1] Text 179
         TrackingDays <TrckgDays> [0..1] Text 179
       CreditorSchemeIdentification <CdtrSchmeId> [0..1] ± 179
       PreNotificationIdentification <PreNtfctnId> [0..1] Text 180
       PreNotificationDate <PreNtfctnDt> [0..1] Date 181
     Creditor <Cdtr> [1..1] ± 181
     CreditorAccount <CdtrAcct> [0..1] ± C15,
C14
182
     CreditorAgent <CdtrAgt> [1..1] ± 183
     CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C15,
C14
184
     UltimateCreditor <UltmtCdtr> [0..1] ± 185
     InitiatingParty <InitgPty> [0..1] ± 186
     InstructingAgent <InstgAgt> [0..1] ± 187
     InstructedAgent <InstdAgt> [0..1] ± 188
     IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 189
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C15,
C14
190
     IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 191
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
135 March 2026
```

## File page 136

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1] ± C15,
C14
191
     IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 192
     IntermediaryAgent3Account <IntrmyAgt3Acct> [0..1] ± C15,
C14
193
     Debtor <Dbtr> [1..1] ± 194
     DebtorAccount <DbtrAcct> [1..1] ± C15,
C14
195
     DebtorAgent <DbtrAgt> [1..1] ± 196
     DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C15,
C14
197
     UltimateDebtor <UltmtDbtr> [0..1] ± 198
     Purpose <Purp> [0..1] ± 199
     RegulatoryReporting <RgltryRptg> [0..10] ± 200
     RelatedRemittanceInformation <RltdRmtInf> [0..10]  200
       RemittanceIdentification <RmtId> [0..1] Text 201
       RemittanceLocationDetails <RmtLctnDtls> [0..*]  201
         Method <Mtd> [1..1] CodeSet 201
         ElectronicAddress <ElctrncAdr> [0..1] Text 202
         PostalAddress <PstlAdr> [0..1]  202
           Name <Nm> [1..1] Text 202
           Address <Adr> [1..1] ± 202
     RemittanceInformation <RmtInf> [0..1]  203
       Unstructured <Ustrd> [0..*] Text 207
       Structured <Strd> [0..*]  207
         ReferredDocumentInformation <RfrdDocInf> [0..*]  211
           Type <Tp> [0..1]  213
             CodeOrProprietary <CdOrPrtry> [1..1]  213
{Or               Code <Cd> [1..1] CodeSet 213
Or}               Proprietary <Prtry> [1..1] Text 213
             Issuer <Issr> [0..1] Text 213
           Number <Nb> [0..1] Text 214
           RelatedDate <RltdDt> [0..1]  214
             Type <Tp> [1..1]  214
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
136 March 2026
```

## File page 137

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or               Code <Cd> [1..1] CodeSet 214
Or}               Proprietary <Prtry> [1..1] Text 214
             Date <Dt> [1..1] Date 214
           LineDetails <LineDtls> [0..*]  215
             Identification <Id> [1..*]  215
               Type <Tp> [0..1]  216
                 CodeOrProprietary <CdOrPrtry> [1..1]  216
{Or                   Code <Cd> [1..1] CodeSet 216
Or}                   Proprietary <Prtry> [1..1] Text 216
                 Issuer <Issr> [0..1] Text 217
               Number <Nb> [0..1] Text 217
               RelatedDate <RltdDt> [0..1] Date 217
             Description <Desc> [0..1] Text 217
             Amount <Amt> [0..1]  C27 217
               RemittanceAmountAndType <RmtAmtAndTp> [0..*]  218
                 Type <Tp> [1..1]  218
{Or                   Code <Cd> [1..1] CodeSet 219
Or}                   Proprietary <Prtry> [1..1] Text 219
                 Amount <Amt> [1..1] Amount C2, C11 219
               AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  219
                 Amount <Amt> [1..1] Amount C2, C11 219
                 CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 220
                 Reason <Rsn> [0..1] Text 220
                 AdditionalInformation <AddtlInf> [0..1] Text 220
         ReferredDocumentAmount <RfrdDocAmt> [0..1]  C27 220
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  221
             Type <Tp> [1..1]  221
{Or               Code <Cd> [1..1] CodeSet 222
Or}               Proprietary <Prtry> [1..1] Text 222
             Amount <Amt> [1..1] Amount C2, C11 222
           AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  222
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
137 March 2026
```

## File page 138

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Amount <Amt> [1..1] Amount C2, C11 222
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 223
             Reason <Rsn> [0..1] Text 223
             AdditionalInformation <AddtlInf> [0..1] Text 223
         CreditorReferenceInformation <CdtrRefInf> [0..1]  223
           Type <Tp> [0..1]  224
             CodeOrProprietary <CdOrPrtry> [1..1]  224
{Or               Code <Cd> [1..1] CodeSet 224
Or}               Proprietary <Prtry> [1..1] Text 224
             Issuer <Issr> [0..1] Text 225
           Reference <Ref> [0..1] Text 225
         Invoicer <Invcr> [0..1] ± 225
         Invoicee <Invcee> [0..1] ± 226
         TaxRemittance <TaxRmt> [0..1]  227
           Creditor <Cdtr> [0..1] ± 229
           Debtor <Dbtr> [0..1] ± 229
           UltimateDebtor <UltmtDbtr> [0..1] ± 229
           AdministrationZone <AdmstnZone> [0..1] Text 230
           ReferenceNumber <RefNb> [0..1] Text 230
           Method <Mtd> [0..1] Text 230
           TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C11 230
           TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C11 231
           Date <Dt> [0..1] Date 231
           SequenceNumber <SeqNb> [0..1] Quantity 231
           Record <Rcrd> [0..*]  231
             Type <Tp> [0..1] Text 232
             Category <Ctgy> [0..1] Text 232
             CategoryDetails <CtgyDtls> [0..1] Text 232
             DebtorStatus <DbtrSts> [0..1] Text 233
             CertificateIdentification <CertId> [0..1] Text 233
             FormsCode <FrmsCd> [0..1] Text 233
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
138 March 2026
```

## File page 139

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Period <Prd> [0..1]  233
               Year <Yr> [0..1] Year 233
               Type <Tp> [0..1] CodeSet 233
               FromToDate <FrToDt> [0..1] ± 234
             TaxAmount <TaxAmt> [0..1]  235
               Rate <Rate> [0..1] Rate 235
               TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C11 235
               TotalAmount <TtlAmt> [0..1] Amount C2, C11 235
               Details <Dtls> [0..*]  236
                 Period <Prd> [0..1]  236
                   Year <Yr> [0..1] Year 236
                   Type <Tp> [0..1] CodeSet 237
                   FromToDate <FrToDt> [0..1] ± 237
                 Amount <Amt> [1..1] Amount C2, C11 238
             AdditionalInformation <AddtlInf> [0..1] Text 238
         GarnishmentRemittance <GrnshmtRmt> [0..1]  238
           Type <Tp> [1..1]  239
             CodeOrProprietary <CdOrPrtry> [1..1]  239
{Or               Code <Cd> [1..1] CodeSet 240
Or}               Proprietary <Prtry> [1..1] Text 240
             Issuer <Issr> [0..1] Text 240
           Garnishee <Grnshee> [0..1] ± 240
           GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 241
           ReferenceNumber <RefNb> [0..1] Text 242
           Date <Dt> [0..1] Date 243
           RemittedAmount <RmtdAmt> [0..1] Amount C2, C11 243
           FamilyMedicalInsuranceIndicator <FmlyMdclInsrncInd> [0..1] Indicator 243
           EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 243
         SecuritiesData <SctiesData> [0..*]  243
           UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 244
           Amount <Amt> [0..1] Amount C1, C10 244
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
139 March 2026
```

