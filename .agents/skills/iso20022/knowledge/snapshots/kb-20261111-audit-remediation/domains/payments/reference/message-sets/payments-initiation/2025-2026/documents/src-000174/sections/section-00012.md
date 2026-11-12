---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.1.8 InitiationSource <InitnSrc>", "2.4.1.8.3 Version <Vrsn>"]
file_pages: [22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.1.8.3 Version <Vrsn>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 22 to 31.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 22

```text
2.4.1.8.3  Version <Vrsn>
Presence: [0..1]
Definition: Version of the application or software used to initiate the payment.
Datatype: "Max35Text" on page 609
2.4.2 PaymentInformation <PmtInf>
Presence: [1..*]
Definition: Set of characteristics that applies to the debit side of the payment transactions included in
the credit transfer initiation.
Impacted by: C5 "ChargeBearerRule", C6 "ChargesAccountAgentRule", C7 "ChargesAccountRule", C8
"ChequeAndCreditorAccountRule", C9 "ChequeDeliveryAndCreditorAgentRule", C10
"ChequeDeliveryAndNoCreditorAgentRule", C15 "ChequeInstructionRule", C17
"ChequeNoDeliveryAndNoCreditorAgentRule", C25 "InstructionForDebtorAgentRule", C31
"NonChequePaymentMethodRule", C32 "PaymentTypeInformationRule", C40 "UltimateDebtorRule",
C11 "ChequeFromGuideline", C12 "ChequeInstructionDeliverToCreditorAgentGuideline", C13
"ChequeInstructionDeliverToCreditorGuideline", C14 "ChequeInstructionDeliverToDebtorGuideline",
C38 "UltimateDebtorGuideline"
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 22 March 2026
```

## File page 23

```text
PaymentInformation <PmtInf> contains the following PaymentInstruction51 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentInformationIdentification <PmtInfId> [1..1] Text 33
   PaymentMethod <PmtMtd> [1..1] CodeSet 33
   RequestedAdviceType <ReqdAdvcTp> [0..1]  33
     CreditAdvice <CdtAdvc> [0..1]  34
{Or       Code <Cd> [1..1] CodeSet 34
Or}       Proprietary <Prtry> [1..1] Text 34
     DebitAdvice <DbtAdvc> [0..1]  34
{Or       Code <Cd> [1..1] CodeSet 35
Or}       Proprietary <Prtry> [1..1] Text 35
   BatchBooking <BtchBookg> [0..1] Indicator 35
   NumberOfTransactions <NbOfTxs> [0..1] Text 35
   ControlSum <CtrlSum> [0..1] Quantity 35
   PaymentTypeInformation <PmtTpInf> [0..1] ± 36
   RequestedExecutionDate <ReqdExctnDt> [1..1] ± 36
   PoolingAdjustmentDate <PoolgAdjstmntDt> [0..1] Date 36
   Debtor <Dbtr> [1..1] ± 36
   DebtorAccount <DbtrAcct> [1..1] ± C23,
C22
37
   DebtorAgent <DbtrAgt> [1..1] ± 38
   DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C23,
C22
39
   InstructionForDebtorAgent <InstrForDbtrAgt> [0..1] Text 40
   UltimateDebtor <UltmtDbtr> [0..1] ± 40
   ChargeBearer <ChrgBr> [0..1] CodeSet 41
   ChargesAccount <ChrgsAcct> [0..1] ± C23,
C22
42
   ChargesAccountAgent <ChrgsAcctAgt> [0..1] ± 43
   CreditTransferTransactionInformation <CdtTrfTxInf> [1..*]  C24,
C26,
C27,
C28,
C29,
C30,
C37,
C39
43
     PaymentIdentification <PmtId> [1..1] ± 51
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 23 March 2026
```

## File page 24

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     PaymentTypeInformation <PmtTpInf> [0..1] ± 51
     Amount <Amt> [1..1] ± 52
     ExchangeRateInformation <XchgRateInf> [0..1]  52
       UnitCurrency <UnitCcy> [0..1] CodeSet C2 53
       ExchangeRate <XchgRate> [0..1] Rate 53
       RateType <RateTp> [0..1] CodeSet 53
       ContractIdentification <CtrctId> [0..1] Text 53
     ChargeBearer <ChrgBr> [0..1] CodeSet 54
     MandateRelatedInformation <MndtRltdInf> [0..1] ± 54
     ChequeInstruction <ChqInstr> [0..1]  C16 55
       ChequeType <ChqTp> [0..1] CodeSet 56
       ChequeNumber <ChqNb> [0..1] Text 57
       ChequeFrom <ChqFr> [0..1]  57
         Name <Nm> [1..1] Text 57
         Address <Adr> [1..1] ± 58
       DeliveryMethod <DlvryMtd> [0..1]  58
{Or         Code <Cd> [1..1] CodeSet 59
Or}         Proprietary <Prtry> [1..1] Text 59
       DeliverTo <DlvrTo> [0..1]  59
         Name <Nm> [1..1] Text 60
         Address <Adr> [1..1] ± 60
       InstructionPriority <InstrPrty> [0..1] CodeSet 60
       ChequeMaturityDate <ChqMtrtyDt> [0..1] Date 61
       FormsCode <FrmsCd> [0..1] Text 61
       MemoField <MemoFld> [0..2] Text 61
       RegionalClearingZone <RgnlClrZone> [0..1] Text 61
       PrintLocation <PrtLctn> [0..1] Text 61
       Signature <Sgntr> [0..5] Text 61
     UltimateDebtor <UltmtDbtr> [0..1] ± 61
     IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 62
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C23,
C22
63
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 24 March 2026
```

## File page 25

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 64
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1] ± C23,
C22
64
     IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 65
     IntermediaryAgent3Account <IntrmyAgt3Acct> [0..1] ± C23,
C22
66
     CreditorAgent <CdtrAgt> [0..1] ± 67
     CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C23,
C22
67
     Creditor <Cdtr> [0..1] ± 68
     CreditorAccount <CdtrAcct> [0..1] ± C23,
C22
69
     UltimateCreditor <UltmtCdtr> [0..1] ± 70
     InstructionForCreditorAgent <InstrForCdtrAgt> [0..*] ± 71
     InstructionForDebtorAgent <InstrForDbtrAgt> [0..1]  72
       Code <Cd> [0..1] CodeSet 72
       InstructionInformation <InstrInf> [0..1] Text 72
     Purpose <Purp> [0..1] ± 72
     RegulatoryReporting <RgltryRptg> [0..10] ± 73
     Tax <Tax> [0..1]  73
       Creditor <Cdtr> [0..1] ± 75
       Debtor <Dbtr> [0..1] ± 75
       UltimateDebtor <UltmtDbtr> [0..1] ± 75
       AdministrationZone <AdmstnZone> [0..1] Text 76
       ReferenceNumber <RefNb> [0..1] Text 76
       Method <Mtd> [0..1] Text 76
       TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C19 76
       TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C19 77
       Date <Dt> [0..1] Date 77
       SequenceNumber <SeqNb> [0..1] Quantity 77
       Record <Rcrd> [0..*]  77
         Type <Tp> [0..1] Text 78
         Category <Ctgy> [0..1] Text 78
         CategoryDetails <CtgyDtls> [0..1] Text 78
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 25 March 2026
```

## File page 26

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         DebtorStatus <DbtrSts> [0..1] Text 79
         CertificateIdentification <CertId> [0..1] Text 79
         FormsCode <FrmsCd> [0..1] Text 79
         Period <Prd> [0..1]  79
           Year <Yr> [0..1] Year 79
           Type <Tp> [0..1] CodeSet 79
           FromToDate <FrToDt> [0..1] ± 80
         TaxAmount <TaxAmt> [0..1]  81
           Rate <Rate> [0..1] Rate 81
           TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C19 81
           TotalAmount <TtlAmt> [0..1] Amount C2, C19 81
           Details <Dtls> [0..*]  82
             Period <Prd> [0..1]  82
               Year <Yr> [0..1] Year 82
               Type <Tp> [0..1] CodeSet 83
               FromToDate <FrToDt> [0..1] ± 83
             Amount <Amt> [1..1] Amount C2, C19 84
         AdditionalInformation <AddtlInf> [0..1] Text 84
     RelatedRemittanceInformation <RltdRmtInf> [0..10]  84
       RemittanceIdentification <RmtId> [0..1] Text 85
       RemittanceLocationDetails <RmtLctnDtls> [0..*]  85
         Method <Mtd> [1..1] CodeSet 85
         ElectronicAddress <ElctrncAdr> [0..1] Text 86
         PostalAddress <PstlAdr> [0..1]  86
           Name <Nm> [1..1] Text 86
           Address <Adr> [1..1] ± 86
     RemittanceInformation <RmtInf> [0..1]  87
       Unstructured <Ustrd> [0..*] Text 91
       Structured <Strd> [0..*]  91
         ReferredDocumentInformation <RfrdDocInf> [0..*]  95
           Type <Tp> [0..1]  97
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 26 March 2026
```

## File page 27

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             CodeOrProprietary <CdOrPrtry> [1..1]  97
{Or               Code <Cd> [1..1] CodeSet 97
Or}               Proprietary <Prtry> [1..1] Text 97
             Issuer <Issr> [0..1] Text 97
           Number <Nb> [0..1] Text 98
           RelatedDate <RltdDt> [0..1]  98
             Type <Tp> [1..1]  98
{Or               Code <Cd> [1..1] CodeSet 98
Or}               Proprietary <Prtry> [1..1] Text 98
             Date <Dt> [1..1] Date 98
           LineDetails <LineDtls> [0..*]  99
             Identification <Id> [1..*]  99
               Type <Tp> [0..1]  100
                 CodeOrProprietary <CdOrPrtry> [1..1]  100
{Or                   Code <Cd> [1..1] CodeSet 100
Or}                   Proprietary <Prtry> [1..1] Text 100
                 Issuer <Issr> [0..1] Text 101
               Number <Nb> [0..1] Text 101
               RelatedDate <RltdDt> [0..1] Date 101
             Description <Desc> [0..1] Text 101
             Amount <Amt> [0..1]  C33 101
               RemittanceAmountAndType <RmtAmtAndTp> [0..*]  102
                 Type <Tp> [1..1]  102
{Or                   Code <Cd> [1..1] CodeSet 103
Or}                   Proprietary <Prtry> [1..1] Text 103
                 Amount <Amt> [1..1] Amount C2, C19 103
               AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  103
                 Amount <Amt> [1..1] Amount C2, C19 103
                 CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 104
                 Reason <Rsn> [0..1] Text 104
                 AdditionalInformation <AddtlInf> [0..1] Text 104
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 27 March 2026
```

## File page 28

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         ReferredDocumentAmount <RfrdDocAmt> [0..1]  C33 104
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  105
             Type <Tp> [1..1]  105
{Or               Code <Cd> [1..1] CodeSet 106
Or}               Proprietary <Prtry> [1..1] Text 106
             Amount <Amt> [1..1] Amount C2, C19 106
           AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  106
             Amount <Amt> [1..1] Amount C2, C19 106
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 107
             Reason <Rsn> [0..1] Text 107
             AdditionalInformation <AddtlInf> [0..1] Text 107
         CreditorReferenceInformation <CdtrRefInf> [0..1]  107
           Type <Tp> [0..1]  108
             CodeOrProprietary <CdOrPrtry> [1..1]  108
{Or               Code <Cd> [1..1] CodeSet 108
Or}               Proprietary <Prtry> [1..1] Text 108
             Issuer <Issr> [0..1] Text 109
           Reference <Ref> [0..1] Text 109
         Invoicer <Invcr> [0..1] ± 109
         Invoicee <Invcee> [0..1] ± 110
         TaxRemittance <TaxRmt> [0..1]  111
           Creditor <Cdtr> [0..1] ± 113
           Debtor <Dbtr> [0..1] ± 113
           UltimateDebtor <UltmtDbtr> [0..1] ± 113
           AdministrationZone <AdmstnZone> [0..1] Text 114
           ReferenceNumber <RefNb> [0..1] Text 114
           Method <Mtd> [0..1] Text 114
           TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C19 114
           TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C19 115
           Date <Dt> [0..1] Date 115
           SequenceNumber <SeqNb> [0..1] Quantity 115
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 28 March 2026
```

## File page 29

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Record <Rcrd> [0..*]  115
             Type <Tp> [0..1] Text 116
             Category <Ctgy> [0..1] Text 116
             CategoryDetails <CtgyDtls> [0..1] Text 116
             DebtorStatus <DbtrSts> [0..1] Text 117
             CertificateIdentification <CertId> [0..1] Text 117
             FormsCode <FrmsCd> [0..1] Text 117
             Period <Prd> [0..1]  117
               Year <Yr> [0..1] Year 117
               Type <Tp> [0..1] CodeSet 117
               FromToDate <FrToDt> [0..1] ± 118
             TaxAmount <TaxAmt> [0..1]  119
               Rate <Rate> [0..1] Rate 119
               TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C19 119
               TotalAmount <TtlAmt> [0..1] Amount C2, C19 119
               Details <Dtls> [0..*]  120
                 Period <Prd> [0..1]  120
                   Year <Yr> [0..1] Year 120
                   Type <Tp> [0..1] CodeSet 121
                   FromToDate <FrToDt> [0..1] ± 121
                 Amount <Amt> [1..1] Amount C2, C19 122
             AdditionalInformation <AddtlInf> [0..1] Text 122
         GarnishmentRemittance <GrnshmtRmt> [0..1]  122
           Type <Tp> [1..1]  123
             CodeOrProprietary <CdOrPrtry> [1..1]  123
{Or               Code <Cd> [1..1] CodeSet 124
Or}               Proprietary <Prtry> [1..1] Text 124
             Issuer <Issr> [0..1] Text 124
           Garnishee <Grnshee> [0..1] ± 124
           GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 125
           ReferenceNumber <RefNb> [0..1] Text 126
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 29 March 2026
```

## File page 30

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Date <Dt> [0..1] Date 127
           RemittedAmount <RmtdAmt> [0..1] Amount C2, C19 127
           FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 127
           EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 127
         SecuritiesData <SctiesData> [0..*]  127
           UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 128
           Amount <Amt> [0..1] Amount C1, C20 128
         AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 128
     SupplementaryData <SplmtryData> [0..*] ± C36 128
Constraints
• ChargeBearerRule
If ChargeBearer is present, then CreditTransferTransactionInformation/ChargeBearer is not allowed.
If CreditTransferTransactionInformation/ChargeBearer is present, then ChargeBearer is not allowed.
CreditTransferTransactionInformation/ChargeBearer and ChargeBearer may both be absent.
Following Must be True
    /ChargeBearer Must be absent
 Or    /CreditTransferTransactionInformation[*]/ChargeBearer Must be absent
• ChargesAccountAgentRule
If ChargesAccountAgent is present, then it must contain a branch of the DebtorAgent. It must not
contain a completely different agent.
On Condition
    /ChargesAccountAgent is present
Following Must be True
    /ChargesAccountAgent/FinancialInstitutionIdentification/Name Must be equal to 
value 'Branch of DebtorAgent'
• ChargesAccountRule
If ChargesAccountAgent is present, then ChargesAccount must be present.
On Condition
    /ChargesAccountAgent is present
Following Must be True
    /ChargesAccount Must be present
• ChequeAndCreditorAccountRule
If PaymentMethod is CHK (Cheque), then CreditTransferTransactionInformation/CreditorAccount is
not allowed.
On Condition
    /PaymentMethod is equal to value 'Cheque'
Following Must be True
    /CreditTransferTransactionInformation[*]/CreditorAccount Must be absent
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 30 March 2026
```

## File page 31

```text
• ChequeDeliveryAndCreditorAgentRule
If PaymentMethod is CHK (Cheque) and CreditTransferTransactionInformation/ChequeInstruction/
DeliveryMethod/Code is present and is equal to MLFA (MailToFinalAgent), CRFA
(CourierToFinalAgent), RGFA (RegisteredMailToFinalAgent) or PUFA (PickUpByFinalAgent), then
CreditTransferTransactionInformation/CreditorAgent must be present.
On Condition
    /PaymentMethod is equal to value 'Cheque'
 And    /CreditTransferTransactionInformation[*]/ChequeInstruction is present
 And    /CreditTransferTransactionInformation[*]/ChequeInstruction/DeliveryMethod 
is present
 And    /CreditTransferTransactionInformation[*]/ChequeInstruction/DeliveryMethod/
Code is present
 And    /CreditTransferTransactionInformation[*]/ChequeInstruction/DeliveryMethod/
Code is within DataType <<Code>> ChequeDelivery2Code
Following Must be True
    /CreditTransferTransactionInformation[*]/CreditorAgent Must be present
• ChequeDeliveryAndNoCreditorAgentRule
If PaymentMethod is CHK (Cheque) and CreditTransferTransactionInformation/ChequeInstruction/
DeliveryMethod/Code is present and different from MLFA (MailToFinalAgent), CRFA
(CourierToFinalAgent), RGFA (RegisteredMailToFinalAgent) or PUFA (PickUpByFinalAgent), then
CreditTransferTransactionInformation/CreditorAgent is not allowed.
On Condition
    /PaymentMethod is equal to value 'Cheque'
 And    /CreditTransferTransactionInformation[*]/ChequeInstruction is present
 And    /CreditTransferTransactionInformation[*]/ChequeInstruction/DeliveryMethod 
is present
 And    /CreditTransferTransactionInformation[*]/ChequeInstruction/DeliveryMethod/
Code is present
 And    /CreditTransferTransactionInformation[*]/ChequeInstruction/DeliveryMethod/
Code is not within DataType <<Code>> ChequeDelivery2Code
Following Must be True
    /CreditTransferTransactionInformation[*]/CreditorAgent Must be absent
• ChequeFromGuideline
CreditTransferTransactionInformation/ChequeInstruction/ChequeFrom may only be present if
different from CreditTransferTransactionInformation/UltimateDebtor or Debtor.
• ChequeInstructionDeliverToCreditorAgentGuideline
If CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod is present and is CRFA
(CourierToFinalAgent), MLFA (MailToFinalAgent), PUFA (PickUpByFinalAgent) or RGFA
(RegisteredMailToFinalAgent), then CreditTransferTransactionInformation/ChequeInstruction/
DeliverTo may only be present if different from CreditTransferTransactionInformation/Creditor.
• ChequeInstructionDeliverToCreditorGuideline
If PaymentInformation/CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod is
present and is CRCD (CourierToCreditor), MLCD (MailToCreditor), PUCD (PickUpByCreditor) or
RGCD (RegisteredMailToCreditor), then CreditTransferTransactionInformation/ChequeInstruction/
DeliverTo may only be present if different from CreditTransferTransactionInformation/Creditor.
• ChequeInstructionDeliverToDebtorGuideline
If CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod is present and if
CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod/Code is CRDB
(CourierToDebtor), MLDB (MailToDebtor), PUDB (PickUpByDebtor) or RGDB
(RegisteredMailToDebtor), then CreditTransferTransactionInformation/ChequeInstruction/DeliverTo
may only be present if different from Debtor.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 31 March 2026
```

