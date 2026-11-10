---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.1.12 InstructedAgent <InstdAgt>"]
file_pages: [729, 730, 731, 732, 733, 734, 735, 736, 737, 738]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.1.12 InstructedAgent <InstdAgt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 729 to 738.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 729

```text
6.4.1.12  InstructedAgent <InstdAgt>
Presence: [0..1]
Definition: Agent that is instructed by the previous party in the chain to carry out the (set of)
instruction(s).
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
6.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>
Presence: [1..*]
Definition: Set of elements providing information specific to the individual credit transfer(s).
Impacted by: C6 "ChargeBearerAndChargesInformationRule", C8
"ChargesInformationAndInstructedAmountRule", C19 "InstructedAmountAndExchangeRate1Rule", C20
"InstructedAmountAndExchangeRate2Rule", C21 "InstructedAmountAndExchangeRate3Rule", C25
"InstructionForCreditorAgentRule", C26 "IntermediaryAgent1AccountRule", C27
"IntermediaryAgent2AccountRule", C28 "IntermediaryAgent2Rule", C29
"IntermediaryAgent3AccountRule", C30 "IntermediaryAgent3Rule", C33
"PreviousInstructingAgent1AccountRule", C35 "PreviousInstructingAgent2AccountRule", C36
"PreviousInstructingAgent2Rule", C37 "PreviousInstructingAgent3AccountRule", C38
"PreviousInstructingAgent3Rule", C7 "ChargesAmountGuideline", C9 "ChargesInformationGuideline",
C34 "PreviousInstructingAgent1Guideline", C54 "UltimateCreditorGuideline", C55
"UltimateDebtorGuideline"
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
729 March 2026
```

## File page 730

```text
CreditTransferTransactionInformation <CdtTrfTxInf> contains the following
CreditTransferTransaction73 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentIdentification <PmtId> [1..1] ± C52 739
   PaymentTypeInformation <PmtTpInf> [0..1] ± 740
   InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount C1, C11 740
   InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 741
   SettlementPriority <SttlmPrty> [0..1] CodeSet 741
   SettlementTimeIndication <SttlmTmIndctn> [0..1]  741
     DebitDateTime <DbtDtTm> [0..1] DateTime 742
     CreditDateTime <CdtDtTm> [0..1] DateTime 742
   SettlementTimeRequest <SttlmTmReq> [0..1] ± 742
   AdditionalDateTime <AddtlDtTm> [0..1]  C3 742
     AcceptanceDateTime <AccptncDtTm> [0..1] DateTime 743
     PoolingAdjustmentDate <PoolgAdjstmntDt> [0..1] Date 743
     ExpiryDateTime <XpryDtTm> [0..1] DateTime 743
   InstructedAmount <InstdAmt> [0..1] Amount C2, C12 743
   ExchangeRate <XchgRate> [0..1] Rate 744
   AgreedRate <AgrdRate> [0..1]  744
     UnitCurrency <UnitCcy> [0..1] CodeSet C2 744
     QuotedCurrency <QtdCcy> [0..1] CodeSet C2 744
     PreAgreedExchangeRate <PreAgrdXchgRate> [1..1] Rate 745
     QuotationDateTime <QtnDtTm> [0..1] DateTime 745
     QuoteIdentification <QtId> [0..1] IdentifierSet 745
     ForeignExchangeAgent <FXAgt> [0..1] ± 745
   ChargeBearer <ChrgBr> [1..1] CodeSet 746
   ChargesInformation <ChrgsInf> [0..*]  746
     Amount <Amt> [1..1] Amount C2, C12 747
     Agent <Agt> [1..1] ± 747
     Type <Tp> [0..1]  748
{Or       Code <Cd> [1..1] CodeSet 748
Or}       Proprietary <Prtry> [1..1] ± 748
   MandateRelatedInformation <MndtRltdInf> [0..1] ± 749
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
730 March 2026
```

## File page 731

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentSignature <PmtSgntr> [0..1]  749
{Or     ILPV4 <ILPV4> [1..1] Text 750
Or}     Signature <Sgntr> [1..1] Text 750
   PreviousInstructingAgent1 <PrvsInstgAgt1> [0..1] ± 750
   PreviousInstructingAgent1Account
<PrvsInstgAgt1Acct>
[0..1] ± C17,
C16
750
   PreviousInstructingAgent2 <PrvsInstgAgt2> [0..1] ± 751
   PreviousInstructingAgent2Account
<PrvsInstgAgt2Acct>
[0..1] ± C17,
C16
752
   PreviousInstructingAgent3 <PrvsInstgAgt3> [0..1] ± 753
   PreviousInstructingAgent3Account
<PrvsInstgAgt3Acct>
[0..1] ± C17,
C16
753
   InstructingAgent <InstgAgt> [0..1] ± 754
   InstructedAgent <InstdAgt> [0..1] ± 755
   IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 756
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C17,
C16
757
   IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 758
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1] ± C17,
C16
758
   IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 759
   IntermediaryAgent3Account <IntrmyAgt3Acct> [0..1] ± C17,
C16
760
   UltimateDebtor <UltmtDbtr> [0..1] ± 761
   InitiatingParty <InitgPty> [0..1] ± 762
   Debtor <Dbtr> [1..1] ± 763
   DebtorAccount <DbtrAcct> [0..1] ± C17,
C16
764
   DebtorAgent <DbtrAgt> [1..1] ± 765
   DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C17,
C16
766
   CreditorAgent <CdtrAgt> [1..1] ± 767
   CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C17,
C16
767
   Creditor <Cdtr> [1..1] ± 768
   CreditorAccount <CdtrAcct> [0..1] ± C17,
C16
769
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
731 March 2026
```

## File page 732

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UltimateCreditor <UltmtCdtr> [0..1] ± 770
   InstructionForCreditorAgent <InstrForCdtrAgt> [0..*] ± 771
   InstructionForNextAgent <InstrForNxtAgt> [0..*]  772
     Code <Cd> [0..1] CodeSet 772
     InstructionInformation <InstrInf> [0..1] Text 772
   Purpose <Purp> [0..1] ± 772
   RegulatoryReporting <RgltryRptg> [0..10] ± 773
   Tax <Tax> [0..1]  773
     Creditor <Cdtr> [0..1] ± 775
     Debtor <Dbtr> [0..1] ± 775
     UltimateDebtor <UltmtDbtr> [0..1] ± 775
     AdministrationZone <AdmstnZone> [0..1] Text 776
     ReferenceNumber <RefNb> [0..1] Text 776
     Method <Mtd> [0..1] Text 776
     TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C12 776
     TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C12 777
     Date <Dt> [0..1] Date 777
     SequenceNumber <SeqNb> [0..1] Quantity 777
     Record <Rcrd> [0..*]  777
       Type <Tp> [0..1] Text 778
       Category <Ctgy> [0..1] Text 778
       CategoryDetails <CtgyDtls> [0..1] Text 778
       DebtorStatus <DbtrSts> [0..1] Text 779
       CertificateIdentification <CertId> [0..1] Text 779
       FormsCode <FrmsCd> [0..1] Text 779
       Period <Prd> [0..1]  779
         Year <Yr> [0..1] Year 779
         Type <Tp> [0..1] CodeSet 779
         FromToDate <FrToDt> [0..1] ± 780
       TaxAmount <TaxAmt> [0..1]  781
         Rate <Rate> [0..1] Rate 781
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
732 March 2026
```

## File page 733

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 781
         TotalAmount <TtlAmt> [0..1] Amount C2, C12 781
         Details <Dtls> [0..*]  782
           Period <Prd> [0..1]  782
             Year <Yr> [0..1] Year 782
             Type <Tp> [0..1] CodeSet 783
             FromToDate <FrToDt> [0..1] ± 783
           Amount <Amt> [1..1] Amount C2, C12 784
       AdditionalInformation <AddtlInf> [0..1] Text 784
   RelatedRemittanceInformation <RltdRmtInf> [0..10]  784
     RemittanceIdentification <RmtId> [0..1] Text 785
     RemittanceLocationDetails <RmtLctnDtls> [0..*]  785
       Method <Mtd> [1..1] CodeSet 785
       ElectronicAddress <ElctrncAdr> [0..1] Text 786
       PostalAddress <PstlAdr> [0..1]  786
         Name <Nm> [1..1] Text 786
         Address <Adr> [1..1] ± 786
   RemittanceInformation <RmtInf> [0..1]  787
     Unstructured <Ustrd> [0..*] Text 791
     Structured <Strd> [0..*]  791
       ReferredDocumentInformation <RfrdDocInf> [0..*]  795
         Type <Tp> [0..1]  797
           CodeOrProprietary <CdOrPrtry> [1..1]  797
{Or             Code <Cd> [1..1] CodeSet 797
Or}             Proprietary <Prtry> [1..1] Text 797
           Issuer <Issr> [0..1] Text 797
         Number <Nb> [0..1] Text 798
         RelatedDate <RltdDt> [0..1]  798
           Type <Tp> [1..1]  798
{Or             Code <Cd> [1..1] CodeSet 798
Or}             Proprietary <Prtry> [1..1] Text 798
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
733 March 2026
```

## File page 734

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Date <Dt> [1..1] Date 798
         LineDetails <LineDtls> [0..*]  799
           Identification <Id> [1..*]  799
             Type <Tp> [0..1]  800
               CodeOrProprietary <CdOrPrtry> [1..1]  800
{Or                 Code <Cd> [1..1] CodeSet 800
Or}                 Proprietary <Prtry> [1..1] Text 800
               Issuer <Issr> [0..1] Text 801
             Number <Nb> [0..1] Text 801
             RelatedDate <RltdDt> [0..1] Date 801
           Description <Desc> [0..1] Text 801
           Amount <Amt> [0..1]  C39 801
             RemittanceAmountAndType <RmtAmtAndTp> [0..*]  802
               Type <Tp> [1..1]  802
{Or                 Code <Cd> [1..1] CodeSet 803
Or}                 Proprietary <Prtry> [1..1] Text 803
               Amount <Amt> [1..1] Amount C2, C12 803
             AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  803
               Amount <Amt> [1..1] Amount C2, C12 803
               CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 804
               Reason <Rsn> [0..1] Text 804
               AdditionalInformation <AddtlInf> [0..1] Text 804
       ReferredDocumentAmount <RfrdDocAmt> [0..1]  C39 804
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  805
           Type <Tp> [1..1]  805
{Or             Code <Cd> [1..1] CodeSet 806
Or}             Proprietary <Prtry> [1..1] Text 806
           Amount <Amt> [1..1] Amount C2, C12 806
         AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  806
           Amount <Amt> [1..1] Amount C2, C12 806
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 807
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
734 March 2026
```

## File page 735

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Reason <Rsn> [0..1] Text 807
           AdditionalInformation <AddtlInf> [0..1] Text 807
       CreditorReferenceInformation <CdtrRefInf> [0..1]  807
         Type <Tp> [0..1]  808
           CodeOrProprietary <CdOrPrtry> [1..1]  808
{Or             Code <Cd> [1..1] CodeSet 808
Or}             Proprietary <Prtry> [1..1] Text 808
           Issuer <Issr> [0..1] Text 809
         Reference <Ref> [0..1] Text 809
       Invoicer <Invcr> [0..1] ± 809
       Invoicee <Invcee> [0..1] ± 810
       TaxRemittance <TaxRmt> [0..1]  811
         Creditor <Cdtr> [0..1] ± 813
         Debtor <Dbtr> [0..1] ± 813
         UltimateDebtor <UltmtDbtr> [0..1] ± 813
         AdministrationZone <AdmstnZone> [0..1] Text 814
         ReferenceNumber <RefNb> [0..1] Text 814
         Method <Mtd> [0..1] Text 814
         TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C12 814
         TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C12 815
         Date <Dt> [0..1] Date 815
         SequenceNumber <SeqNb> [0..1] Quantity 815
         Record <Rcrd> [0..*]  815
           Type <Tp> [0..1] Text 816
           Category <Ctgy> [0..1] Text 816
           CategoryDetails <CtgyDtls> [0..1] Text 816
           DebtorStatus <DbtrSts> [0..1] Text 817
           CertificateIdentification <CertId> [0..1] Text 817
           FormsCode <FrmsCd> [0..1] Text 817
           Period <Prd> [0..1]  817
             Year <Yr> [0..1] Year 817
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
735 March 2026
```

## File page 736

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Type <Tp> [0..1] CodeSet 817
             FromToDate <FrToDt> [0..1] ± 818
           TaxAmount <TaxAmt> [0..1]  819
             Rate <Rate> [0..1] Rate 819
             TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 819
             TotalAmount <TtlAmt> [0..1] Amount C2, C12 819
             Details <Dtls> [0..*]  820
               Period <Prd> [0..1]  820
                 Year <Yr> [0..1] Year 820
                 Type <Tp> [0..1] CodeSet 821
                 FromToDate <FrToDt> [0..1] ± 821
               Amount <Amt> [1..1] Amount C2, C12 822
           AdditionalInformation <AddtlInf> [0..1] Text 822
       GarnishmentRemittance <GrnshmtRmt> [0..1]  822
         Type <Tp> [1..1]  823
           CodeOrProprietary <CdOrPrtry> [1..1]  823
{Or             Code <Cd> [1..1] CodeSet 824
Or}             Proprietary <Prtry> [1..1] Text 824
           Issuer <Issr> [0..1] Text 824
         Garnishee <Grnshee> [0..1] ± 824
         GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 825
         ReferenceNumber <RefNb> [0..1] Text 826
         Date <Dt> [0..1] Date 827
         RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 827
         FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 827
         EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 827
       SecuritiesData <SctiesData> [0..*]  827
         UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 828
         Amount <Amt> [0..1] Amount C1, C11 828
       AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 828
   SupplementaryData <SplmtryData> [0..*] ± C46 828
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
736 March 2026
```

## File page 737

```text
Constraints
• ChargeBearerAndChargesInformationRule
If ChargeBearer contains DEBT, then ChargesInformation may be present to communicate charges
that have been added for (the) InstructedAgent(s).
If ChargeBearer contains CRED, then at least one occurrence of ChargesInformation must be
present to communicate charges that have been deducted from the InstructedAmount by (the)
InstructingAgent(s).
If ChargeBearer contains SHAR or SLEV, then ChargesInformation is optional.
On Condition
    /ChargeBearer is equal to value 'BorneByCreditor'
Following Must be True
    /ChargesInformation[1] Must be present
• ChargesAmountGuideline
If ChargesInformation is present, then the currency of ChargesInformation/ChargesAmount is
recommended to be the same as the currency of InterbankSettlementAmount.
• ChargesInformationAndInstructedAmountRule
If ChargesInformation is present, then InstructedAmount must be present.
On Condition
    /ChargesInformation[1] is present
 And    /ChargesInformation[*]/Amount is present
Following Must be True
    /InstructedAmount Must be present
• ChargesInformationGuideline
The repetitive ChargesInformation should contain all information on charges amount and which party
has taken the charges, separately for each agent along the payment chain.
• InstructedAmountAndExchangeRate1Rule
If InstructedAmount is present and the currency is different from the currency in
InterbankSettlementAmount, then ExchangeRate must be present.
On Condition
    /InstructedAmount is present
 And    /InstructedAmount/attribute::Currency is different from /
InterbankSettlementAmount/attribute::Currency
Following Must be True
    /ExchangeRate Must be present
• InstructedAmountAndExchangeRate2Rule
If InstructedAmount is present and the currency is the same as the currency in
InterbankSettlementAmount, then ExchangeRate is not allowed.
On Condition
    /InstructedAmount is present
 And    /InstructedAmount/attribute::Currency is equal to /
InterbankSettlementAmount/attribute::Currency
Following Must be True
    /ExchangeRate Must be absent
• InstructedAmountAndExchangeRate3Rule
If InstructedAmount is not present, then ExchangeRate is not allowed.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
737 March 2026
```

## File page 738

```text
On Condition
    /InstructedAmount is absent
Following Must be True
    /ExchangeRate Must be absent
• InstructionForCreditorAgentRule
If InstructionForCreditorAgent/Code contains CHQB (PayCreditorByCheque), then CreditorAccount
is not allowed.
if 
    at least one occurrence of [InstructionForCreditorAgent/Code] has value 
included in the following list 'CHQB' 
, then 
    the following element(s) [CreditorAccount] must be absent 
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
• IntermediaryAgent3AccountRule
If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present.
On Condition
    /IntermediaryAgent3 is absent
Following Must be True
    /IntermediaryAgent3Account Must be absent
• IntermediaryAgent3Rule
If IntermediaryAgent3 is present, then IntermediaryAgent2 must be present.
On Condition
    /IntermediaryAgent3 is present
Following Must be True
    /IntermediaryAgent2 Must be present
• PreviousInstructingAgent1AccountRule
If PreviousInstructingAgent1Account is present, then PreviousInstructingAgent1 must be present.
On Condition
    /PreviousInstructingAgent1 is absent
Following Must be True
    /PreviousInstructingAgent1Account Must be absent
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
738 March 2026
```

