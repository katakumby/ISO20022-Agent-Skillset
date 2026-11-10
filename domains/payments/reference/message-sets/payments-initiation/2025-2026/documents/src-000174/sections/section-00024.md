---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.18 ChargesAccountAgent <ChrgsAcctAgt>"]
file_pages: [43, 44, 45, 46, 47, 48, 49, 50]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.18 ChargesAccountAgent <ChrgsAcctAgt>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 43 to 50.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 43

```text
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
2.4.2.18  ChargesAccountAgent <ChrgsAcctAgt>
Presence: [0..1]
Definition: Agent that services a charges account.
Usage: Charges account agent should only be used when the charges account agent is different from
the debtor agent.
ChargesAccountAgent <ChrgsAcctAgt> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 539 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  540
     BICFI <BICFI> [0..1] IdentifierSet C4 540
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 541
     LEI <LEI> [0..1] IdentifierSet 541
     Name <Nm> [0..1] Text 541
     PostalAddress <PstlAdr> [0..1] ± 541
     Other <Othr> [0..1] ± 542
   BranchIdentification <BrnchId> [0..1]  543
     Identification <Id> [0..1] Text 543
     LEI <LEI> [0..1] IdentifierSet 543
     Name <Nm> [0..1] Text 543
     PostalAddress <PstlAdr> [0..1] ± 543
2.4.2.19  CreditTransferTransactionInformation <CdtTrfTxInf>
Presence: [1..*]
Definition: Provides information on the individual transaction(s) included in the message.
Impacted by: C24 "InstructionForCreditorAgentRule", C26 "IntermediaryAgent1AccountRule", C27
"IntermediaryAgent2AccountRule", C28 "IntermediaryAgent2Rule", C29
"IntermediaryAgent3AccountRule", C30 "IntermediaryAgent3Rule", C37 "UltimateCreditorGuideline",
C39 "UltimateDebtorGuideline"
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 43 March 2026
```

## File page 44

```text
CreditTransferTransactionInformation <CdtTrfTxInf> contains the following
CreditTransferTransaction76 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentIdentification <PmtId> [1..1] ± 51
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
{Or       Code <Cd> [1..1] CodeSet 59
Or}       Proprietary <Prtry> [1..1] Text 59
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
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 44 March 2026
```

## File page 45

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 62
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C23,
C22
63
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
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 45 March 2026
```

## File page 46

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Type <Tp> [0..1] Text 78
       Category <Ctgy> [0..1] Text 78
       CategoryDetails <CtgyDtls> [0..1] Text 78
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
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 46 March 2026
```

## File page 47

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Structured <Strd> [0..*]  91
       ReferredDocumentInformation <RfrdDocInf> [0..*]  95
         Type <Tp> [0..1]  97
           CodeOrProprietary <CdOrPrtry> [1..1]  97
{Or             Code <Cd> [1..1] CodeSet 97
Or}             Proprietary <Prtry> [1..1] Text 97
           Issuer <Issr> [0..1] Text 97
         Number <Nb> [0..1] Text 98
         RelatedDate <RltdDt> [0..1]  98
           Type <Tp> [1..1]  98
{Or             Code <Cd> [1..1] CodeSet 98
Or}             Proprietary <Prtry> [1..1] Text 98
           Date <Dt> [1..1] Date 98
         LineDetails <LineDtls> [0..*]  99
           Identification <Id> [1..*]  99
             Type <Tp> [0..1]  100
               CodeOrProprietary <CdOrPrtry> [1..1]  100
{Or                 Code <Cd> [1..1] CodeSet 100
Or}                 Proprietary <Prtry> [1..1] Text 100
               Issuer <Issr> [0..1] Text 101
             Number <Nb> [0..1] Text 101
             RelatedDate <RltdDt> [0..1] Date 101
           Description <Desc> [0..1] Text 101
           Amount <Amt> [0..1]  C33 101
             RemittanceAmountAndType <RmtAmtAndTp> [0..*]  102
               Type <Tp> [1..1]  102
{Or                 Code <Cd> [1..1] CodeSet 103
Or}                 Proprietary <Prtry> [1..1] Text 103
               Amount <Amt> [1..1] Amount C2, C19 103
             AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  103
               Amount <Amt> [1..1] Amount C2, C19 103
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 47 March 2026
```

## File page 48

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
               CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 104
               Reason <Rsn> [0..1] Text 104
               AdditionalInformation <AddtlInf> [0..1] Text 104
       ReferredDocumentAmount <RfrdDocAmt> [0..1]  C33 104
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  105
           Type <Tp> [1..1]  105
{Or             Code <Cd> [1..1] CodeSet 106
Or}             Proprietary <Prtry> [1..1] Text 106
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
{Or             Code <Cd> [1..1] CodeSet 108
Or}             Proprietary <Prtry> [1..1] Text 108
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
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 48 March 2026
```

## File page 49

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C19 115
         Date <Dt> [0..1] Date 115
         SequenceNumber <SeqNb> [0..1] Quantity 115
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
{Or             Code <Cd> [1..1] CodeSet 124
Or}             Proprietary <Prtry> [1..1] Text 124
           Issuer <Issr> [0..1] Text 124
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 49 March 2026
```

## File page 50

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Garnishee <Grnshee> [0..1] ± 124
         GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 125
         ReferenceNumber <RefNb> [0..1] Text 126
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
• InstructionForCreditorAgentRule
If InstructionForCreditorAgent/Code contains CHQB, then CreditorAccount is not allowed.
On Condition
    /InstructionForCreditorAgent[*]/Code is within DataType <<Code>> 
ValidationRulePayCreditorByCheque1Code
Following Must be True
    /CreditorAccount Must be absent
• IntermediaryAgent1AccountRule
If IntermediaryAgent1Account is present, then IntermediaryAgent1 must be present.
On Condition
    /IntermediaryAgent1 is absent
Following Must be True
    /IntermediaryAgent1Account Must be absent
• IntermediaryAgent2AccountRule
If IntermediaryAgent2Account is present, then IntermediaryAgent2 must be present.
On Condition
    /IntermediaryAgent2 is absent
Following Must be True
    /IntermediaryAgent2Account Must be absent
• IntermediaryAgent2Rule
If IntermediaryAgent2 is present, then IntermediaryAgent1 must be present.
On Condition
    /IntermediaryAgent2 is present
Following Must be True
    /IntermediaryAgent1 Must be present
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 50 March 2026
```

