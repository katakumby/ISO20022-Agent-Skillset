---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2.7 StatusReasonInformation <StsRsnInf>", "2.4.2.7.2 Reason <Rsn>", "2.4.2.7.2.1 Code <Cd>"]
file_pages: [25, 26, 27, 28, 29, 30, 31]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.2.7.2.1 Code <Cd>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 25 to 31.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 25

```text
Reason <Rsn> contains one of the following StatusReason6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 25
Or}   Proprietary <Prtry> [1..1] Text 25
2.4.2.7.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the status, as published in an external reason code list.
Datatype: "ExternalStatusReason1Code" on page 1233
2.4.2.7.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the status, in a proprietary form.
Datatype: "Max35Text" on page 1246
2.4.2.7.3  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Further details on the status reason.
Usage: Additional information can be used for several purposes such as the reporting of repaired
information.
Datatype: "Max105Text" on page 1244
2.4.2.8  NumberOfTransactionsPerStatus <NbOfTxsPerSts>
Presence: [0..*]
Definition: Detailed information on the number of transactions for each identical transaction status.
NumberOfTransactionsPerStatus <NbOfTxsPerSts> contains the following elements (see
"NumberOfTransactionsPerStatus5" on page 1192 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DetailedNumberOfTransactions <DtldNbOfTxs> [1..1] Text 1192
   DetailedStatus <DtldSts> [1..1] CodeSet 1192
   DetailedControlSum <DtldCtrlSum> [0..1] Quantity 1192
2.4.3 TransactionInformationAndStatus <TxInfAndSts>
Presence: [0..*]
Definition: Information concerning the original transactions, to which the status report message refers.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
25 March 2026
```

## File page 26

```text
TransactionInformationAndStatus <TxInfAndSts> contains the following PaymentTransaction177
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatusIdentification <StsId> [0..1] Text 32
   OriginalGroupInformation <OrgnlGrpInf> [0..1]  33
     OriginalMessageIdentification <OrgnlMsgId> [1..1] Text 33
     OriginalMessageNameIdentification
<OrgnlMsgNmId>
[1..1] Text 33
     OriginalCreationDateTime <OrgnlCreDtTm> [0..1] DateTime 33
   OriginalInstructionIdentification <OrgnlInstrId> [0..1] Text 33
   OriginalEndToEndIdentification <OrgnlEndToEndId> [0..1] Text 33
   OriginalTransactionIdentification <OrgnlTxId> [0..1] Text 34
   OriginalUETR <OrgnlUETR> [0..1] IdentifierSet 34
   TransactionStatus <TxSts> [0..1] CodeSet 34
   StatusReasonInformation <StsRsnInf> [0..*]  C29 34
     Originator <Orgtr> [0..1] ± 35
     Reason <Rsn> [0..1]  36
{Or       Code <Cd> [1..1] CodeSet 37
Or}       Proprietary <Prtry> [1..1] Text 37
     AdditionalInformation <AddtlInf> [0..*] Text 37
   ChargesInformation <ChrgsInf> [0..*]  37
     Amount <Amt> [1..1] Amount C2, C8 37
     Agent <Agt> [1..1] ± 38
     Type <Tp> [0..1]  38
{Or       Code <Cd> [1..1] CodeSet 39
Or}       Proprietary <Prtry> [1..1] ± 39
   AcceptanceDateTime <AccptncDtTm> [0..1] DateTime 39
   ProcessingDate <PrcgDt> [0..1] ± 39
   EffectiveInterbankSettlementDate <FctvIntrBkSttlmDt> [0..1] ± 39
   AccountServicerReference <AcctSvcrRef> [0..1] Text 40
   ClearingSystemReference <ClrSysRef> [0..1] Text 40
   CreditSettlementKey <CdtSttlmKey> [0..1] Text 40
   InstructingAgent <InstgAgt> [0..1] ± 40
   InstructedAgent <InstdAgt> [0..1] ± 41
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
26 March 2026
```

## File page 27

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalTransactionReference <OrgnlTxRef> [0..1]  42
     InterbankSettlementAmount <IntrBkSttlmAmt> [0..1] Amount C2, C8 48
     Amount <Amt> [0..1] ± 49
     InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 49
     RequestedCollectionDate <ReqdColltnDt> [0..1] Date 49
     RequestedExecutionDate <ReqdExctnDt> [0..1] ± 49
     CreditorSchemeIdentification <CdtrSchmeId> [0..1] ± 50
     SettlementInformation <SttlmInf> [0..1]  C17,
C18,
C24,
C25,
C26,
C27,
C32,
C33
51
       SettlementMethod <SttlmMtd> [1..1] CodeSet 53
       SettlementAccount <SttlmAcct> [0..1] ± C16,
C15
54
       ClearingSystem <ClrSys> [0..1]  54
{Or         Code <Cd> [1..1] CodeSet 55
Or}         Proprietary <Prtry> [1..1] Text 55
       InstructingReimbursementAgent
<InstgRmbrsmntAgt>
[0..1] ± 55
       InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C16,
C15
56
       InstructedReimbursementAgent
<InstdRmbrsmntAgt>
[0..1] ± 56
       InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C16,
C15
57
       ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 58
       ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C16,
C15
58
     PaymentTypeInformation <PmtTpInf> [0..1] ± 59
     PaymentMethod <PmtMtd> [0..1] CodeSet 60
     MandateRelatedInformation <MndtRltdInf> [0..1]  60
{Or       DirectDebitMandate <DrctDbtMndt> [1..1]  C3, C4 62
         MandateIdentification <MndtId> [0..1] Text 64
         DateOfSignature <DtOfSgntr> [0..1] Date 64
         AmendmentIndicator <AmdmntInd> [0..1] Indicator 64
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
27 March 2026
```

## File page 28

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         AmendmentInformationDetails <AmdmntInfDtls> [0..1]  64
           OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 65
           OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 65
           OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 66
           OriginalCreditorAgentAccount
<OrgnlCdtrAgtAcct>
[0..1] ± C16,
C15
67
           OriginalDebtor <OrgnlDbtr> [0..1] ± 68
           OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C16,
C15
69
           OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 70
           OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C16,
C15
71
           OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 72
           OriginalFrequency <OrgnlFrqcy> [0..1] ± 72
           OriginalReason <OrgnlRsn> [0..1]  72
{Or             Code <Cd> [1..1] CodeSet 72
Or}             Proprietary <Prtry> [1..1] Text 72
           OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 73
         ElectronicSignature <ElctrncSgntr> [0..1] Text 73
         FirstCollectionDate <FrstColltnDt> [0..1] Date 73
         FinalCollectionDate <FnlColltnDt> [0..1] Date 73
         Frequency <Frqcy> [0..1] ± 73
         Reason <Rsn> [0..1]  73
{Or           Code <Cd> [1..1] CodeSet 74
Or}           Proprietary <Prtry> [1..1] Text 74
         TrackingDays <TrckgDays> [0..1] Text 74
Or}       CreditTransferMandate <CdtTrfMndt> [1..1] ± 74
     RemittanceInformation <RmtInf> [0..1]  75
       Unstructured <Ustrd> [0..*] Text 79
       Structured <Strd> [0..*]  79
         ReferredDocumentInformation <RfrdDocInf> [0..*]  83
           Type <Tp> [0..1]  85
             CodeOrProprietary <CdOrPrtry> [1..1]  85
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
28 March 2026
```

## File page 29

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or               Code <Cd> [1..1] CodeSet 85
Or}               Proprietary <Prtry> [1..1] Text 85
             Issuer <Issr> [0..1] Text 85
           Number <Nb> [0..1] Text 86
           RelatedDate <RltdDt> [0..1]  86
             Type <Tp> [1..1]  86
{Or               Code <Cd> [1..1] CodeSet 86
Or}               Proprietary <Prtry> [1..1] Text 86
             Date <Dt> [1..1] Date 86
           LineDetails <LineDtls> [0..*]  87
             Identification <Id> [1..*]  87
               Type <Tp> [0..1]  88
                 CodeOrProprietary <CdOrPrtry> [1..1]  88
{Or                   Code <Cd> [1..1] CodeSet 88
Or}                   Proprietary <Prtry> [1..1] Text 88
                 Issuer <Issr> [0..1] Text 89
               Number <Nb> [0..1] Text 89
               RelatedDate <RltdDt> [0..1] Date 89
             Description <Desc> [0..1] Text 89
             Amount <Amt> [0..1]  C23 89
               RemittanceAmountAndType <RmtAmtAndTp> [0..*]  90
                 Type <Tp> [1..1]  90
{Or                   Code <Cd> [1..1] CodeSet 91
Or}                   Proprietary <Prtry> [1..1] Text 91
                 Amount <Amt> [1..1] Amount C2, C8 91
               AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  91
                 Amount <Amt> [1..1] Amount C2, C8 91
                 CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 92
                 Reason <Rsn> [0..1] Text 92
                 AdditionalInformation <AddtlInf> [0..1] Text 92
         ReferredDocumentAmount <RfrdDocAmt> [0..1]  C23 92
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
29 March 2026
```

## File page 30

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  93
             Type <Tp> [1..1]  93
{Or               Code <Cd> [1..1] CodeSet 94
Or}               Proprietary <Prtry> [1..1] Text 94
             Amount <Amt> [1..1] Amount C2, C8 94
           AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  94
             Amount <Amt> [1..1] Amount C2, C8 94
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 95
             Reason <Rsn> [0..1] Text 95
             AdditionalInformation <AddtlInf> [0..1] Text 95
         CreditorReferenceInformation <CdtrRefInf> [0..1]  95
           Type <Tp> [0..1]  96
             CodeOrProprietary <CdOrPrtry> [1..1]  96
{Or               Code <Cd> [1..1] CodeSet 96
Or}               Proprietary <Prtry> [1..1] Text 96
             Issuer <Issr> [0..1] Text 97
           Reference <Ref> [0..1] Text 97
         Invoicer <Invcr> [0..1] ± 97
         Invoicee <Invcee> [0..1] ± 98
         TaxRemittance <TaxRmt> [0..1]  99
           Creditor <Cdtr> [0..1] ± 101
           Debtor <Dbtr> [0..1] ± 101
           UltimateDebtor <UltmtDbtr> [0..1] ± 101
           AdministrationZone <AdmstnZone> [0..1] Text 102
           ReferenceNumber <RefNb> [0..1] Text 102
           Method <Mtd> [0..1] Text 102
           TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C8 102
           TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C8 103
           Date <Dt> [0..1] Date 103
           SequenceNumber <SeqNb> [0..1] Quantity 103
           Record <Rcrd> [0..*]  103
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
30 March 2026
```

## File page 31

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Type <Tp> [0..1] Text 104
             Category <Ctgy> [0..1] Text 104
             CategoryDetails <CtgyDtls> [0..1] Text 104
             DebtorStatus <DbtrSts> [0..1] Text 105
             CertificateIdentification <CertId> [0..1] Text 105
             FormsCode <FrmsCd> [0..1] Text 105
             Period <Prd> [0..1]  105
               Year <Yr> [0..1] Year 105
               Type <Tp> [0..1] CodeSet 105
               FromToDate <FrToDt> [0..1] ± 106
             TaxAmount <TaxAmt> [0..1]  107
               Rate <Rate> [0..1] Rate 107
               TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C8 107
               TotalAmount <TtlAmt> [0..1] Amount C2, C8 107
               Details <Dtls> [0..*]  108
                 Period <Prd> [0..1]  108
                   Year <Yr> [0..1] Year 108
                   Type <Tp> [0..1] CodeSet 109
                   FromToDate <FrToDt> [0..1] ± 109
                 Amount <Amt> [1..1] Amount C2, C8 110
             AdditionalInformation <AddtlInf> [0..1] Text 110
         GarnishmentRemittance <GrnshmtRmt> [0..1]  110
           Type <Tp> [1..1]  111
             CodeOrProprietary <CdOrPrtry> [1..1]  111
{Or               Code <Cd> [1..1] CodeSet 112
Or}               Proprietary <Prtry> [1..1] Text 112
             Issuer <Issr> [0..1] Text 112
           Garnishee <Grnshee> [0..1] ± 112
           GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 113
           ReferenceNumber <RefNb> [0..1] Text 114
           Date <Dt> [0..1] Date 115
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
31 March 2026
```

