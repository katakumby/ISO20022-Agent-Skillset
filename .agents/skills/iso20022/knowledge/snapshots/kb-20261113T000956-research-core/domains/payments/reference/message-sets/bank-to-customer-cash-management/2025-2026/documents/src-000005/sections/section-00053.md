---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.1 Batch <Btch>", "2.4.2.15.18.1.5 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [108, 109, 110, 111, 112, 113, 114, 115, 116, 117]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.1.5 CreditDebitIndicator <CdtDbtInd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 108 to 117.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 108

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
2.4.2.15.18.1.5  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the batch entry is a credit or a debit entry.
Datatype: "CreditDebitCode" on page 892
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
2.4.2.15.18.2  TransactionDetails <TxDtls>
Presence: [0..*]
Definition: Provides information on the underlying transaction(s).
Impacted by: C25 "PaymentTypeOrLocalInstrumentRule"
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
108 March 2026
```

## File page 109

```text
TransactionDetails <TxDtls> contains the following EntryTransaction16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   References <Refs> [0..1]  120
     MessageIdentification <MsgId> [0..1] Text 121
     AccountServicerReference <AcctSvcrRef> [0..1] Text 121
     PaymentInformationIdentification <PmtInfId> [0..1] Text 121
     InstructionIdentification <InstrId> [0..1] Text 122
     EndToEndIdentification <EndToEndId> [0..1] Text 122
     UETR <UETR> [0..1] IdentifierSet 122
     TransactionIdentification <TxId> [0..1] Text 122
     MandateIdentification <MndtId> [0..1] Text 122
     ChequeNumber <ChqNb> [0..1] Text 123
     ClearingSystemReference <ClrSysRef> [0..1] Text 123
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 123
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 123
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 123
     ProcessingIdentification <PrcgId> [0..1] Text 123
     ReturnIdentification <RtrId> [0..1] Text 123
     Proprietary <Prtry> [0..*]  124
       Type <Tp> [1..1] Text 124
       Reference <Ref> [1..1] Text 124
   Amount <Amt> [0..1] Amount C2, C6 124
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 124
   AmountDetails <AmtDtls> [0..1] ± 125
   Availability <Avlbty> [0..*] ± 125
   BankTransactionCode <BkTxCd> [0..1] ± C11,
C14
125
   Charges <Chrgs> [0..1]  126
     TotalChargesAndTaxAmount <TtlChrgsAndTaxAmt> [0..1] Amount C2, C6 127
     Record <Rcrd> [0..*]  127
       Amount <Amt> [1..1] Amount C2, C6 128
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 128
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
109 March 2026
```

## File page 110

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ChargeIncludedIndicator <ChrgInclInd> [0..1] Indicator 129
       Type <Tp> [0..1]  129
{Or         Code <Cd> [1..1] CodeSet 129
Or}         Proprietary <Prtry> [1..1] ± 129
       Rate <Rate> [0..1] Rate 129
       Bearer <Br> [0..1] CodeSet 130
       Agent <Agt> [0..1] ± 130
       Tax <Tax> [0..1]  131
         Identification <Id> [0..1] Text 131
         Rate <Rate> [0..1] Rate 131
         Amount <Amt> [0..1] Amount C2, C6 131
   Interest <Intrst> [0..1] ± 131
   RelatedParties <RltdPties> [0..1]  132
     InitiatingParty <InitgPty> [0..1]  133
{Or       Party <Pty> [1..1] ± 134
Or}       Agent <Agt> [1..1] ± 135
     Debtor <Dbtr> [0..1]  136
{Or       Party <Pty> [1..1] ± 136
Or}       Agent <Agt> [1..1] ± 137
     DebtorAccount <DbtrAcct> [0..1] ± C20,
C18
138
     UltimateDebtor <UltmtDbtr> [0..1]  139
{Or       Party <Pty> [1..1] ± 139
Or}       Agent <Agt> [1..1] ± 140
     Creditor <Cdtr> [0..1]  141
{Or       Party <Pty> [1..1] ± 141
Or}       Agent <Agt> [1..1] ± 142
     CreditorAccount <CdtrAcct> [0..1] ± C20,
C18
143
     UltimateCreditor <UltmtCdtr> [0..1]  144
{Or       Party <Pty> [1..1] ± 144
Or}       Agent <Agt> [1..1] ± 145
     TradingParty <TradgPty> [0..1]  146
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
110 March 2026
```

## File page 111

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       Party <Pty> [1..1] ± 146
Or}       Agent <Agt> [1..1] ± 147
     Proprietary <Prtry> [0..*]  148
       Type <Tp> [1..1] Text 148
       Party <Pty> [1..1]  148
{Or         Party <Pty> [1..1] ± 149
Or}         Agent <Agt> [1..1] ± 150
   RelatedAgents <RltdAgts> [0..1]  151
     InstructingAgent <InstgAgt> [0..1] ± 152
     InstructedAgent <InstdAgt> [0..1] ± 153
     DebtorAgent <DbtrAgt> [0..1] ± 154
     CreditorAgent <CdtrAgt> [0..1] ± 155
     IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 155
     IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 156
     IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 157
     ReceivingAgent <RcvgAgt> [0..1] ± 158
     DeliveringAgent <DlvrgAgt> [0..1] ± 159
     IssuingAgent <IssgAgt> [0..1] ± 160
     SettlementPlace <SttlmPlc> [0..1] ± 161
     Proprietary <Prtry> [0..*]  161
       Type <Tp> [1..1] Text 161
       Agent <Agt> [1..1] ± 161
   LocalInstrument <LclInstrm> [0..1]  162
{Or     Code <Cd> [1..1] CodeSet 162
Or}     Proprietary <Prtry> [1..1] Text 162
   PaymentTypeInformation <PmtTpInf> [0..1] ± 163
   Purpose <Purp> [0..1] ± 163
   RelatedRemittanceInformation <RltdRmtInf> [0..10]  163
     RemittanceIdentification <RmtId> [0..1] Text 164
     RemittanceLocationDetails <RmtLctnDtls> [0..*]  164
       Method <Mtd> [1..1] CodeSet 164
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
111 March 2026
```

## File page 112

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ElectronicAddress <ElctrncAdr> [0..1] Text 165
       PostalAddress <PstlAdr> [0..1]  165
         Name <Nm> [1..1] Text 165
         Address <Adr> [1..1] ± 165
   RemittanceInformation <RmtInf> [0..1]  166
     Unstructured <Ustrd> [0..*] Text 170
     Structured <Strd> [0..*]  170
       ReferredDocumentInformation <RfrdDocInf> [0..*]  174
         Type <Tp> [0..1]  176
           CodeOrProprietary <CdOrPrtry> [1..1]  176
{Or             Code <Cd> [1..1] CodeSet 176
Or}             Proprietary <Prtry> [1..1] Text 176
           Issuer <Issr> [0..1] Text 176
         Number <Nb> [0..1] Text 177
         RelatedDate <RltdDt> [0..1]  177
           Type <Tp> [1..1]  177
{Or             Code <Cd> [1..1] CodeSet 177
Or}             Proprietary <Prtry> [1..1] Text 177
           Date <Dt> [1..1] Date 177
         LineDetails <LineDtls> [0..*]  178
           Identification <Id> [1..*]  178
             Type <Tp> [0..1]  179
               CodeOrProprietary <CdOrPrtry> [1..1]  179
{Or                 Code <Cd> [1..1] CodeSet 179
Or}                 Proprietary <Prtry> [1..1] Text 179
               Issuer <Issr> [0..1] Text 180
             Number <Nb> [0..1] Text 180
             RelatedDate <RltdDt> [0..1] Date 180
           Description <Desc> [0..1] Text 180
           Amount <Amt> [0..1]  C27 180
             RemittanceAmountAndType <RmtAmtAndTp> [0..*]  181
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
112 March 2026
```

## File page 113

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
               Type <Tp> [1..1]  181
{Or                 Code <Cd> [1..1] CodeSet 182
Or}                 Proprietary <Prtry> [1..1] Text 182
               Amount <Amt> [1..1] Amount C2, C6 182
             AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  182
               Amount <Amt> [1..1] Amount C2, C6 182
               CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 183
               Reason <Rsn> [0..1] Text 183
               AdditionalInformation <AddtlInf> [0..1] Text 183
       ReferredDocumentAmount <RfrdDocAmt> [0..1]  C27 183
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  184
           Type <Tp> [1..1]  184
{Or             Code <Cd> [1..1] CodeSet 185
Or}             Proprietary <Prtry> [1..1] Text 185
           Amount <Amt> [1..1] Amount C2, C6 185
         AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  185
           Amount <Amt> [1..1] Amount C2, C6 185
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 186
           Reason <Rsn> [0..1] Text 186
           AdditionalInformation <AddtlInf> [0..1] Text 186
       CreditorReferenceInformation <CdtrRefInf> [0..1]  186
         Type <Tp> [0..1]  187
           CodeOrProprietary <CdOrPrtry> [1..1]  187
{Or             Code <Cd> [1..1] CodeSet 187
Or}             Proprietary <Prtry> [1..1] Text 187
           Issuer <Issr> [0..1] Text 188
         Reference <Ref> [0..1] Text 188
       Invoicer <Invcr> [0..1] ± 188
       Invoicee <Invcee> [0..1] ± 189
       TaxRemittance <TaxRmt> [0..1]  190
         Creditor <Cdtr> [0..1] ± 192
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
113 March 2026
```

## File page 114

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Debtor <Dbtr> [0..1] ± 192
         UltimateDebtor <UltmtDbtr> [0..1] ± 192
         AdministrationZone <AdmstnZone> [0..1] Text 193
         ReferenceNumber <RefNb> [0..1] Text 193
         Method <Mtd> [0..1] Text 193
         TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C6 193
         TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C6 194
         Date <Dt> [0..1] Date 194
         SequenceNumber <SeqNb> [0..1] Quantity 194
         Record <Rcrd> [0..*]  194
           Type <Tp> [0..1] Text 195
           Category <Ctgy> [0..1] Text 195
           CategoryDetails <CtgyDtls> [0..1] Text 195
           DebtorStatus <DbtrSts> [0..1] Text 196
           CertificateIdentification <CertId> [0..1] Text 196
           FormsCode <FrmsCd> [0..1] Text 196
           Period <Prd> [0..1]  196
             Year <Yr> [0..1] Year 196
             Type <Tp> [0..1] CodeSet 196
             FromToDate <FrToDt> [0..1] ± 197
           TaxAmount <TaxAmt> [0..1]  198
             Rate <Rate> [0..1] Rate 198
             TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 198
             TotalAmount <TtlAmt> [0..1] Amount C2, C6 198
             Details <Dtls> [0..*]  199
               Period <Prd> [0..1]  199
                 Year <Yr> [0..1] Year 199
                 Type <Tp> [0..1] CodeSet 200
                 FromToDate <FrToDt> [0..1] ± 200
               Amount <Amt> [1..1] Amount C2, C6 201
           AdditionalInformation <AddtlInf> [0..1] Text 201
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
114 March 2026
```

## File page 115

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       GarnishmentRemittance <GrnshmtRmt> [0..1]  201
         Type <Tp> [1..1]  202
           CodeOrProprietary <CdOrPrtry> [1..1]  202
{Or             Code <Cd> [1..1] CodeSet 203
Or}             Proprietary <Prtry> [1..1] Text 203
           Issuer <Issr> [0..1] Text 203
         Garnishee <Grnshee> [0..1] ± 203
         GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 204
         ReferenceNumber <RefNb> [0..1] Text 205
         Date <Dt> [0..1] Date 206
         RemittedAmount <RmtdAmt> [0..1] Amount C2, C6 206
         FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 206
         EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 206
       SecuritiesData <SctiesData> [0..*]  206
         UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 207
         Amount <Amt> [0..1] Amount C1, C7 207
       AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 207
   RelatedDates <RltdDts> [0..1]  207
     AcceptanceDateTime <AccptncDtTm> [0..1] DateTime 208
     TradeActivityContractualSettlementDate
<TradActvtyCtrctlSttlmDt>
[0..1] Date 208
     TradeDate <TradDt> [0..1] Date 208
     InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 208
     StartDate <StartDt> [0..1] Date 208
     EndDate <EndDt> [0..1] Date 209
     TransactionDateTime <TxDtTm> [0..1] DateTime 209
     Proprietary <Prtry> [0..*]  209
       Type <Tp> [1..1] Text 209
       Date <Dt> [1..1] ± 209
   RelatedPrice <RltdPric> [0..1]  209
{Or     DealPrice <DealPric> [1..1] ± 210
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
115 March 2026
```

## File page 116

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}     Proprietary <Prtry> [1..*]  210
       Type <Tp> [1..1] Text 210
       Price <Pric> [1..1] Amount C2, C6 210
   RelatedQuantities <RltdQties> [0..*]  211
{Or     Quantity <Qty> [1..1] ± C10 211
Or     OriginalAndCurrentFaceAmount
<OrgnlAndCurFaceAmt>
[1..1] ± 212
Or}     Proprietary <Prtry> [1..1]  212
       Type <Tp> [1..1] Text 212
       Quantity <Qty> [1..1] Text 212
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C8, C9,
C21,
C22,
C24
212
   Tax <Tax> [0..1]  213
     Creditor <Cdtr> [0..1] ± 215
     Debtor <Dbtr> [0..1] ± 215
     UltimateDebtor <UltmtDbtr> [0..1] ± 215
     AdministrationZone <AdmstnZone> [0..1] Text 216
     ReferenceNumber <RefNb> [0..1] Text 216
     Method <Mtd> [0..1] Text 216
     TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C6 216
     TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C6 217
     Date <Dt> [0..1] Date 217
     SequenceNumber <SeqNb> [0..1] Quantity 217
     Record <Rcrd> [0..*]  217
       Type <Tp> [0..1] Text 218
       Category <Ctgy> [0..1] Text 218
       CategoryDetails <CtgyDtls> [0..1] Text 218
       DebtorStatus <DbtrSts> [0..1] Text 219
       CertificateIdentification <CertId> [0..1] Text 219
       FormsCode <FrmsCd> [0..1] Text 219
       Period <Prd> [0..1]  219
         Year <Yr> [0..1] Year 219
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
116 March 2026
```

## File page 117

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Type <Tp> [0..1] CodeSet 219
         FromToDate <FrToDt> [0..1] ± 220
       TaxAmount <TaxAmt> [0..1]  221
         Rate <Rate> [0..1] Rate 221
         TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 221
         TotalAmount <TtlAmt> [0..1] Amount C2, C6 221
         Details <Dtls> [0..*]  222
           Period <Prd> [0..1]  222
             Year <Yr> [0..1] Year 222
             Type <Tp> [0..1] CodeSet 223
             FromToDate <FrToDt> [0..1] ± 223
           Amount <Amt> [1..1] Amount C2, C6 224
       AdditionalInformation <AddtlInf> [0..1] Text 224
   ReturnInformation <RtrInf> [0..1]  C28 224
     OriginalBankTransactionCode <OrgnlBkTxCd> [0..1] ± C11,
C14
225
     Originator <Orgtr> [0..1] ± 226
     Reason <Rsn> [0..1]  227
{Or       Code <Cd> [1..1] CodeSet 228
Or}       Proprietary <Prtry> [1..1] Text 228
     AdditionalInformation <AddtlInf> [0..*] Text 228
   RelatedCorporateAction <RltdCorpActn> [0..1]  228
     EventType <EvtTp> [1..1] ± C12 228
     CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 229
     OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 229
   SafekeepingAccount <SfkpgAcct> [0..1] ± 229
   UnderlyingAllocation <UndrlygAllcn> [0..*]  C31 230
     Amount <Amt> [1..1] Amount C2, C6 230
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 230
     Account <Acct> [1..1] ± C20,
C18
231
     Purpose <Purp> [1..1] ± 231
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
117 March 2026
```

