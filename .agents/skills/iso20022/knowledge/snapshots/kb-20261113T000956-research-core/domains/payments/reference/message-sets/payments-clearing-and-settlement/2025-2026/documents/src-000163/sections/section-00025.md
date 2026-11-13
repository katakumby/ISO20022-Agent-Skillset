---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.18 OriginalTransactionReference <OrgnlTxRef>"]
file_pages: [42, 43, 44, 45, 46, 47]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.18 OriginalTransactionReference <OrgnlTxRef>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 42 to 47.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 42

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
2.4.3.18  OriginalTransactionReference <OrgnlTxRef>
Presence: [0..1]
Definition: Key elements used to identify the original transaction that is being referred to.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
42 March 2026
```

## File page 43

```text
OriginalTransactionReference <OrgnlTxRef> contains the following
OriginalTransactionReference47 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or       Code <Cd> [1..1] CodeSet 55
Or}       Proprietary <Prtry> [1..1] Text 55
     InstructingReimbursementAgent
<InstgRmbrsmntAgt>
[0..1] ± 55
     InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C16,
C15
56
     InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 56
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
{Or     DirectDebitMandate <DrctDbtMndt> [1..1]  C3, C4 62
       MandateIdentification <MndtId> [0..1] Text 64
       DateOfSignature <DtOfSgntr> [0..1] Date 64
       AmendmentIndicator <AmdmntInd> [0..1] Indicator 64
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
43 March 2026
```

## File page 44

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
         OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C16,
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
{Or           Code <Cd> [1..1] CodeSet 72
Or}           Proprietary <Prtry> [1..1] Text 72
         OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 73
       ElectronicSignature <ElctrncSgntr> [0..1] Text 73
       FirstCollectionDate <FrstColltnDt> [0..1] Date 73
       FinalCollectionDate <FnlColltnDt> [0..1] Date 73
       Frequency <Frqcy> [0..1] ± 73
       Reason <Rsn> [0..1]  73
{Or         Code <Cd> [1..1] CodeSet 74
Or}         Proprietary <Prtry> [1..1] Text 74
       TrackingDays <TrckgDays> [0..1] Text 74
Or}     CreditTransferMandate <CdtTrfMndt> [1..1] ± 74
   RemittanceInformation <RmtInf> [0..1]  75
     Unstructured <Ustrd> [0..*] Text 79
     Structured <Strd> [0..*]  79
       ReferredDocumentInformation <RfrdDocInf> [0..*]  83
         Type <Tp> [0..1]  85
           CodeOrProprietary <CdOrPrtry> [1..1]  85
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
44 March 2026
```

## File page 45

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or             Code <Cd> [1..1] CodeSet 85
Or}             Proprietary <Prtry> [1..1] Text 85
           Issuer <Issr> [0..1] Text 85
         Number <Nb> [0..1] Text 86
         RelatedDate <RltdDt> [0..1]  86
           Type <Tp> [1..1]  86
{Or             Code <Cd> [1..1] CodeSet 86
Or}             Proprietary <Prtry> [1..1] Text 86
           Date <Dt> [1..1] Date 86
         LineDetails <LineDtls> [0..*]  87
           Identification <Id> [1..*]  87
             Type <Tp> [0..1]  88
               CodeOrProprietary <CdOrPrtry> [1..1]  88
{Or                 Code <Cd> [1..1] CodeSet 88
Or}                 Proprietary <Prtry> [1..1] Text 88
               Issuer <Issr> [0..1] Text 89
             Number <Nb> [0..1] Text 89
             RelatedDate <RltdDt> [0..1] Date 89
           Description <Desc> [0..1] Text 89
           Amount <Amt> [0..1]  C23 89
             RemittanceAmountAndType <RmtAmtAndTp> [0..*]  90
               Type <Tp> [1..1]  90
{Or                 Code <Cd> [1..1] CodeSet 91
Or}                 Proprietary <Prtry> [1..1] Text 91
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
45 March 2026
```

## File page 46

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  93
           Type <Tp> [1..1]  93
{Or             Code <Cd> [1..1] CodeSet 94
Or}             Proprietary <Prtry> [1..1] Text 94
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
{Or             Code <Cd> [1..1] CodeSet 96
Or}             Proprietary <Prtry> [1..1] Text 96
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
46 March 2026
```

## File page 47

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
{Or             Code <Cd> [1..1] CodeSet 112
Or}             Proprietary <Prtry> [1..1] Text 112
           Issuer <Issr> [0..1] Text 112
         Garnishee <Grnshee> [0..1] ± 112
         GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 113
         ReferenceNumber <RefNb> [0..1] Text 114
         Date <Dt> [0..1] Date 115
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
47 March 2026
```

