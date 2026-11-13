---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.14 TransactionsSummary <TxsSummry>"]
file_pages: [53, 54, 55, 56, 57, 58, 59, 60, 61, 62]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.14 TransactionsSummary <TxsSummry>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 53 to 62.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 53

```text
Constraints
• ForwardBalanceAndAvailabilityRule
If Type is equal to ForwardAvailable, Availability is not allowed.
2.4.2.14  TransactionsSummary <TxsSummry>
Presence: [0..1]
Definition: Provides summary information on entries.
TransactionsSummary <TxsSummry> contains the following elements (see "TotalTransactions6" on
page 845 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalEntries <TtlNtries> [0..1]  846
     NumberOfEntries <NbOfNtries> [0..1] Text 846
     Sum <Sum> [0..1] Quantity 846
     TotalNetEntry <TtlNetNtry> [0..1] ± 847
   TotalCreditEntries <TtlCdtNtries> [0..1] ± 847
   TotalDebitEntries <TtlDbtNtries> [0..1] ± 847
   TotalEntriesPerBankTransactionCode
<TtlNtriesPerBkTxCd>
[0..*]  847
     NumberOfEntries <NbOfNtries> [0..1] Text 848
     Sum <Sum> [0..1] Quantity 848
     TotalNetEntry <TtlNetNtry> [0..1] ± 848
     CreditEntries <CdtNtries> [0..1] ± 848
     DebitEntries <DbtNtries> [0..1] ± 849
     ForecastIndicator <FcstInd> [0..1] Indicator 849
     BankTransactionCode <BkTxCd> [1..1] ± C11,
C14
849
     Availability <Avlbty> [0..*] ± 850
     Date <Dt> [0..1] ± 850
2.4.2.15  Entry <Ntry>
Presence: [0..*]
Definition: Specifies an entry in the report.
Usage: At least one reference must be provided to identify the entry and its underlying transaction(s).
Usage Rule: In case of a Payments R-transaction the creditor / debtor referenced of the original
payment initiation messages is also used for reporting of the R-transaction. The original debtor/creditor
in the reporting of R-Transactions is not inverted.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
53 March 2026
```

## File page 54

```text
Following elements all defined in the TransactionDetails in RelatedParties or RelatedAgents are
impacted by this usage rule:
Creditor, UltimateCreditor, CreditorAccount, CreditorAgent, Debtor, UltimateDebtor, DebtorAccount and
DebtorAgent.
Impacted by: C26 "ReferenceGuideline"
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
54 March 2026
```

## File page 55

```text
Entry <Ntry> contains the following ReportEntry16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EntryReference <NtryRef> [0..1] Text 69
   Amount <Amt> [1..1] Amount C2, C6 69
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 70
   ReversalIndicator <RvslInd> [0..1] Indicator 70
   Status <Sts> [1..1] ± 70
   BookingDate <BookgDt> [0..1] ± 71
   ValueDate <ValDt> [0..1] ± 71
   AccountServicerReference <AcctSvcrRef> [0..1] Text 71
   Availability <Avlbty> [0..*] ± 72
   BankTransactionCode <BkTxCd> [1..1] ± C11,
C14
72
   CommissionWaiverIndicator <ComssnWvrInd> [0..1] Indicator 73
   AdditionalInformationIndicator <AddtlInfInd> [0..1]  73
     MessageNameIdentification <MsgNmId> [0..1] Text 73
     MessageIdentification <MsgId> [0..1] Text 73
   AmountDetails <AmtDtls> [0..1] ± 73
   Charges <Chrgs> [0..1]  74
     TotalChargesAndTaxAmount <TtlChrgsAndTaxAmt> [0..1] Amount C2, C6 74
     Record <Rcrd> [0..*]  75
       Amount <Amt> [1..1] Amount C2, C6 75
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 76
       ChargeIncludedIndicator <ChrgInclInd> [0..1] Indicator 76
       Type <Tp> [0..1]  76
{Or         Code <Cd> [1..1] CodeSet 76
Or}         Proprietary <Prtry> [1..1] ± 77
       Rate <Rate> [0..1] Rate 77
       Bearer <Br> [0..1] CodeSet 77
       Agent <Agt> [0..1] ± 77
       Tax <Tax> [0..1]  78
         Identification <Id> [0..1] Text 78
         Rate <Rate> [0..1] Rate 78
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
55 March 2026
```

## File page 56

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Amount <Amt> [0..1] Amount C2, C6 79
   TechnicalInputChannel <TechInptChanl> [0..1]  79
{Or     Code <Cd> [1..1] CodeSet 79
Or}     Proprietary <Prtry> [1..1] Text 79
   Interest <Intrst> [0..1] ± 79
   CardTransaction <CardTx> [0..1]  80
     Card <Card> [0..1]  82
       PlainCardData <PlainCardData> [0..1]  83
         PAN <PAN> [1..1] Text 84
         CardSequenceNumber <CardSeqNb> [0..1] Text 84
         EffectiveDate <FctvDt> [0..1] YearMonth 84
         ExpiryDate <XpryDt> [1..1] YearMonth 84
         ServiceCode <SvcCd> [0..1] Text 84
         TrackData <TrckData> [0..*]  85
           TrackNumber <TrckNb> [0..1] Text 85
           TrackValue <TrckVal> [1..1] Text 85
         CardSecurityCode <CardSctyCd> [0..1]  85
           CSCManagement <CSCMgmt> [1..1] CodeSet 85
           CSCValue <CSCVal> [0..1] Text 86
       CardCountryCode <CardCtryCd> [0..1] Text 86
       CardBrand <CardBrnd> [0..1] ± 86
       AdditionalCardData <AddtlCardData> [0..1] Text 86
     POI <POI> [0..1]  86
       Identification <Id> [1..1] ± 87
       SystemName <SysNm> [0..1] Text 88
       GroupIdentification <GrpId> [0..1] Text 88
       Capabilities <Cpblties> [0..1]  88
         CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 88
         CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 89
         OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 89
         DisplayCapabilities <DispCpblties> [0..*]  90
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
56 March 2026
```

## File page 57

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           DisplayType <DispTp> [1..1] CodeSet 90
           NumberOfLines <NbOfLines> [1..1] Text 90
           LineWidth <LineWidth> [1..1] Text 90
         PrintLineWidth <PrtLineWidth> [0..1] Text 90
       Component <Cmpnt> [0..*]  90
         POIComponentType <POICmpntTp> [1..1] CodeSet 91
         ManufacturerIdentification <ManfctrId> [0..1] Text 91
         Model <Mdl> [0..1] Text 91
         VersionNumber <VrsnNb> [0..1] Text 91
         SerialNumber <SrlNb> [0..1] Text 92
         ApprovalNumber <ApprvlNb> [0..*] Text 92
     AggregatedEntry <AggtdNtry> [0..1]  92
       AdditionalService <AddtlSvc> [0..1] CodeSet 92
       TransactionCategory <TxCtgy> [0..1] CodeSet 93
       SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 93
       SequenceNumberRange <SeqNbRg> [0..1]  93
         FirstTransaction <FrstTx> [0..1] Text 93
         LastTransaction <LastTx> [0..1] Text 93
       TransactionDateRange <TxDtRg> [0..1] ± 94
     PrePaidAccount <PrePdAcct> [0..1] ± C20,
C18
94
   EntryDetails <NtryDtls> [0..*]  94
     Batch <Btch> [0..1]  107
       MessageIdentification <MsgId> [0..1] Text 107
       PaymentInformationIdentification <PmtInfId> [0..1] Text 107
       NumberOfTransactions <NbOfTxs> [0..1] Text 107
       TotalAmount <TtlAmt> [0..1] Amount C2, C6 107
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 108
     TransactionDetails <TxDtls> [0..*]  C25 108
       References <Refs> [0..1]  120
         MessageIdentification <MsgId> [0..1] Text 121
         AccountServicerReference <AcctSvcrRef> [0..1] Text 121
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
57 March 2026
```

## File page 58

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
         TotalChargesAndTaxAmount
<TtlChrgsAndTaxAmt>
[0..1] Amount C2, C6 127
         Record <Rcrd> [0..*]  127
           Amount <Amt> [1..1] Amount C2, C6 128
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 128
           ChargeIncludedIndicator <ChrgInclInd> [0..1] Indicator 129
           Type <Tp> [0..1]  129
{Or             Code <Cd> [1..1] CodeSet 129
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
58 March 2026
```

## File page 59

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}             Proprietary <Prtry> [1..1] ± 129
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
{Or           Party <Pty> [1..1] ± 134
Or}           Agent <Agt> [1..1] ± 135
         Debtor <Dbtr> [0..1]  136
{Or           Party <Pty> [1..1] ± 136
Or}           Agent <Agt> [1..1] ± 137
         DebtorAccount <DbtrAcct> [0..1] ± C20,
C18
138
         UltimateDebtor <UltmtDbtr> [0..1]  139
{Or           Party <Pty> [1..1] ± 139
Or}           Agent <Agt> [1..1] ± 140
         Creditor <Cdtr> [0..1]  141
{Or           Party <Pty> [1..1] ± 141
Or}           Agent <Agt> [1..1] ± 142
         CreditorAccount <CdtrAcct> [0..1] ± C20,
C18
143
         UltimateCreditor <UltmtCdtr> [0..1]  144
{Or           Party <Pty> [1..1] ± 144
Or}           Agent <Agt> [1..1] ± 145
         TradingParty <TradgPty> [0..1]  146
{Or           Party <Pty> [1..1] ± 146
Or}           Agent <Agt> [1..1] ± 147
         Proprietary <Prtry> [0..*]  148
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
59 March 2026
```

## File page 60

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Type <Tp> [1..1] Text 148
           Party <Pty> [1..1]  148
{Or             Party <Pty> [1..1] ± 149
Or}             Agent <Agt> [1..1] ± 150
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
{Or         Code <Cd> [1..1] CodeSet 162
Or}         Proprietary <Prtry> [1..1] Text 162
       PaymentTypeInformation <PmtTpInf> [0..1] ± 163
       Purpose <Purp> [0..1] ± 163
       RelatedRemittanceInformation <RltdRmtInf> [0..10]  163
         RemittanceIdentification <RmtId> [0..1] Text 164
         RemittanceLocationDetails <RmtLctnDtls> [0..*]  164
           Method <Mtd> [1..1] CodeSet 164
           ElectronicAddress <ElctrncAdr> [0..1] Text 165
           PostalAddress <PstlAdr> [0..1]  165
             Name <Nm> [1..1] Text 165
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
60 March 2026
```

## File page 61

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Address <Adr> [1..1] ± 165
       RemittanceInformation <RmtInf> [0..1]  166
         Unstructured <Ustrd> [0..*] Text 170
         Structured <Strd> [0..*]  170
           ReferredDocumentInformation <RfrdDocInf> [0..*]  174
             Type <Tp> [0..1]  176
               CodeOrProprietary <CdOrPrtry> [1..1]  176
{Or                 Code <Cd> [1..1] CodeSet 176
Or}                 Proprietary <Prtry> [1..1] Text 176
               Issuer <Issr> [0..1] Text 176
             Number <Nb> [0..1] Text 177
             RelatedDate <RltdDt> [0..1]  177
               Type <Tp> [1..1]  177
{Or                 Code <Cd> [1..1] CodeSet 177
Or}                 Proprietary <Prtry> [1..1] Text 177
               Date <Dt> [1..1] Date 177
             LineDetails <LineDtls> [0..*]  178
               Identification <Id> [1..*]  178
                 Type <Tp> [0..1]  179
                   CodeOrProprietary <CdOrPrtry> [1..1]  179
{Or                     Code <Cd> [1..1] CodeSet 179
Or}                     Proprietary <Prtry> [1..1] Text 179
                   Issuer <Issr> [0..1] Text 180
                 Number <Nb> [0..1] Text 180
                 RelatedDate <RltdDt> [0..1] Date 180
               Description <Desc> [0..1] Text 180
               Amount <Amt> [0..1]  C27 180
                 RemittanceAmountAndType <RmtAmtAndTp> [0..*]  181
                   Type <Tp> [1..1]  181
{Or                     Code <Cd> [1..1] CodeSet 182
Or}                     Proprietary <Prtry> [1..1] Text 182
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
61 March 2026
```

## File page 62

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or                 Code <Cd> [1..1] CodeSet 185
Or}                 Proprietary <Prtry> [1..1] Text 185
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
{Or                 Code <Cd> [1..1] CodeSet 187
Or}                 Proprietary <Prtry> [1..1] Text 187
               Issuer <Issr> [0..1] Text 188
             Reference <Ref> [0..1] Text 188
           Invoicer <Invcr> [0..1] ± 188
           Invoicee <Invcee> [0..1] ± 189
           TaxRemittance <TaxRmt> [0..1]  190
             Creditor <Cdtr> [0..1] ± 192
             Debtor <Dbtr> [0..1] ± 192
             UltimateDebtor <UltmtDbtr> [0..1] ± 192
             AdministrationZone <AdmstnZone> [0..1] Text 193
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
62 March 2026
```

