---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.39 UnderlyingAllocation <UndrlygAllcn>", "7.4.2.39.6 RelatedReferences <RltdRefs>"]
file_pages: [900, 901, 902, 903, 904, 905, 906, 907]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.39.6 RelatedReferences <RltdRefs>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 900 to 907.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 900

```text
7.4.2.39.6  RelatedReferences <RltdRefs>
Presence: [0..*]
Definition: Reference relating to the allocation which is meaningful to both parties (for example the
original Securities Settlement Transaction Identification).
RelatedReferences <RltdRefs> contains one of the following elements (see "References80Choice" on
page 1181 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 1182
Or   IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 1182
Or   IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 1182
Or   AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 1182
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 1182
Or   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[1..1] Text 1182
Or   PoolIdentification <PoolId> [1..1] Text 1182
Or   CommonIdentification <CmonId> [1..1] Text 1182
Or   TradeIdentification <TradId> [1..1] Text 1183
Or   UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 1183
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 1183
7.4.2.40  UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>
Presence: [0..1]
Definition: Provides information on the underlying customer credit transfer for which cover is provided.
Impacted by: C22 "IntermediaryAgent1AccountRule", C27 "IntermediaryAgent2AccountRule", C30
"IntermediaryAgent2Rule", C33 "IntermediaryAgent3AccountRule", C36 "IntermediaryAgent3Rule", C40
"PreviousInstructingAgent1AccountRule", C46 "PreviousInstructingAgent2AccountRule", C49
"PreviousInstructingAgent2Rule", C52 "PreviousInstructingAgent3AccountRule", C55
"PreviousInstructingAgent3Rule", C43 "PreviousInstructingAgent1Guideline", C73
"UltimateCreditorGuideline", C76 "UltimateDebtorGuideline"
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
900 March 2026
```

## File page 901

```text
UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf> contains the following
CreditTransferTransaction72 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentIdentification <PmtId> [0..1] ± C70 908
   PaymentTypeInformation <PmtTpInf> [0..1] ± 908
   UltimateDebtor <UltmtDbtr> [0..1] ± 909
   InitiatingParty <InitgPty> [0..1] ± 910
   Debtor <Dbtr> [1..1] ± 911
   DebtorAccount <DbtrAcct> [0..1] ± C16,
C15
912
   DebtorAgent <DbtrAgt> [1..1] ± 913
   DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C16,
C15
914
   PreviousInstructingAgent1 <PrvsInstgAgt1> [0..1] ± 915
   PreviousInstructingAgent1Account
<PrvsInstgAgt1Acct>
[0..1] ± C16,
C15
915
   PreviousInstructingAgent2 <PrvsInstgAgt2> [0..1] ± 916
   PreviousInstructingAgent2Account
<PrvsInstgAgt2Acct>
[0..1] ± C16,
C15
917
   PreviousInstructingAgent3 <PrvsInstgAgt3> [0..1] ± 918
   PreviousInstructingAgent3Account
<PrvsInstgAgt3Acct>
[0..1] ± C16,
C15
918
   IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 919
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C16,
C15
920
   IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 921
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1] ± C16,
C15
921
   IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 922
   IntermediaryAgent3Account <IntrmyAgt3Acct> [0..1] ± C16,
C15
923
   CreditorAgent <CdtrAgt> [1..1] ± 924
   CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C16,
C15
924
   Creditor <Cdtr> [1..1] ± 925
   CreditorAccount <CdtrAcct> [0..1] ± C16,
C15
926
   UltimateCreditor <UltmtCdtr> [0..1] ± 927
   InstructionForCreditorAgent <InstrForCdtrAgt> [0..*] ± 928
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
901 March 2026
```

## File page 902

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionForNextAgent <InstrForNxtAgt> [0..*]  929
     Code <Cd> [0..1] CodeSet 929
     InstructionInformation <InstrInf> [0..1] Text 929
   Purpose <Purp> [0..1] ± 929
   Tax <Tax> [0..1]  930
     Creditor <Cdtr> [0..1] ± 932
     Debtor <Dbtr> [0..1] ± 932
     UltimateDebtor <UltmtDbtr> [0..1] ± 932
     AdministrationZone <AdmstnZone> [0..1] Text 933
     ReferenceNumber <RefNb> [0..1] Text 933
     Method <Mtd> [0..1] Text 933
     TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C9 933
     TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C9 934
     Date <Dt> [0..1] Date 934
     SequenceNumber <SeqNb> [0..1] Quantity 934
     Record <Rcrd> [0..*]  934
       Type <Tp> [0..1] Text 935
       Category <Ctgy> [0..1] Text 935
       CategoryDetails <CtgyDtls> [0..1] Text 935
       DebtorStatus <DbtrSts> [0..1] Text 936
       CertificateIdentification <CertId> [0..1] Text 936
       FormsCode <FrmsCd> [0..1] Text 936
       Period <Prd> [0..1]  936
         Year <Yr> [0..1] Year 936
         Type <Tp> [0..1] CodeSet 936
         FromToDate <FrToDt> [0..1] ± 937
       TaxAmount <TaxAmt> [0..1]  938
         Rate <Rate> [0..1] Rate 938
         TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C9 938
         TotalAmount <TtlAmt> [0..1] Amount C2, C9 938
         Details <Dtls> [0..*]  939
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
902 March 2026
```

## File page 903

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Period <Prd> [0..1]  939
             Year <Yr> [0..1] Year 939
             Type <Tp> [0..1] CodeSet 940
             FromToDate <FrToDt> [0..1] ± 940
           Amount <Amt> [1..1] Amount C2, C9 941
       AdditionalInformation <AddtlInf> [0..1] Text 941
   RemittanceInformation <RmtInf> [0..1]  941
     Unstructured <Ustrd> [0..*] Text 945
     Structured <Strd> [0..*]  945
       ReferredDocumentInformation <RfrdDocInf> [0..*]  949
         Type <Tp> [0..1]  951
           CodeOrProprietary <CdOrPrtry> [1..1]  951
{Or             Code <Cd> [1..1] CodeSet 951
Or}             Proprietary <Prtry> [1..1] Text 951
           Issuer <Issr> [0..1] Text 951
         Number <Nb> [0..1] Text 952
         RelatedDate <RltdDt> [0..1]  952
           Type <Tp> [1..1]  952
{Or             Code <Cd> [1..1] CodeSet 952
Or}             Proprietary <Prtry> [1..1] Text 952
           Date <Dt> [1..1] Date 952
         LineDetails <LineDtls> [0..*]  953
           Identification <Id> [1..*]  953
             Type <Tp> [0..1]  954
               CodeOrProprietary <CdOrPrtry> [1..1]  954
{Or                 Code <Cd> [1..1] CodeSet 954
Or}                 Proprietary <Prtry> [1..1] Text 954
               Issuer <Issr> [0..1] Text 955
             Number <Nb> [0..1] Text 955
             RelatedDate <RltdDt> [0..1] Date 955
           Description <Desc> [0..1] Text 955
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
903 March 2026
```

## File page 904

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Amount <Amt> [0..1]  C57 955
             RemittanceAmountAndType <RmtAmtAndTp> [0..*]  956
               Type <Tp> [1..1]  956
{Or                 Code <Cd> [1..1] CodeSet 957
Or}                 Proprietary <Prtry> [1..1] Text 957
               Amount <Amt> [1..1] Amount C2, C9 957
             AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  957
               Amount <Amt> [1..1] Amount C2, C9 957
               CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 958
               Reason <Rsn> [0..1] Text 958
               AdditionalInformation <AddtlInf> [0..1] Text 958
       ReferredDocumentAmount <RfrdDocAmt> [0..1]  C57 958
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  959
           Type <Tp> [1..1]  959
{Or             Code <Cd> [1..1] CodeSet 960
Or}             Proprietary <Prtry> [1..1] Text 960
           Amount <Amt> [1..1] Amount C2, C9 960
         AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  960
           Amount <Amt> [1..1] Amount C2, C9 960
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 961
           Reason <Rsn> [0..1] Text 961
           AdditionalInformation <AddtlInf> [0..1] Text 961
       CreditorReferenceInformation <CdtrRefInf> [0..1]  961
         Type <Tp> [0..1]  962
           CodeOrProprietary <CdOrPrtry> [1..1]  962
{Or             Code <Cd> [1..1] CodeSet 962
Or}             Proprietary <Prtry> [1..1] Text 962
           Issuer <Issr> [0..1] Text 963
         Reference <Ref> [0..1] Text 963
       Invoicer <Invcr> [0..1] ± 963
       Invoicee <Invcee> [0..1] ± 964
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
904 March 2026
```

## File page 905

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       TaxRemittance <TaxRmt> [0..1]  965
         Creditor <Cdtr> [0..1] ± 967
         Debtor <Dbtr> [0..1] ± 967
         UltimateDebtor <UltmtDbtr> [0..1] ± 967
         AdministrationZone <AdmstnZone> [0..1] Text 968
         ReferenceNumber <RefNb> [0..1] Text 968
         Method <Mtd> [0..1] Text 968
         TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C9 968
         TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C9 969
         Date <Dt> [0..1] Date 969
         SequenceNumber <SeqNb> [0..1] Quantity 969
         Record <Rcrd> [0..*]  969
           Type <Tp> [0..1] Text 970
           Category <Ctgy> [0..1] Text 970
           CategoryDetails <CtgyDtls> [0..1] Text 970
           DebtorStatus <DbtrSts> [0..1] Text 971
           CertificateIdentification <CertId> [0..1] Text 971
           FormsCode <FrmsCd> [0..1] Text 971
           Period <Prd> [0..1]  971
             Year <Yr> [0..1] Year 971
             Type <Tp> [0..1] CodeSet 971
             FromToDate <FrToDt> [0..1] ± 972
           TaxAmount <TaxAmt> [0..1]  973
             Rate <Rate> [0..1] Rate 973
             TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C9 973
             TotalAmount <TtlAmt> [0..1] Amount C2, C9 973
             Details <Dtls> [0..*]  974
               Period <Prd> [0..1]  974
                 Year <Yr> [0..1] Year 974
                 Type <Tp> [0..1] CodeSet 975
                 FromToDate <FrToDt> [0..1] ± 975
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
905 March 2026
```

## File page 906

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
               Amount <Amt> [1..1] Amount C2, C9 976
           AdditionalInformation <AddtlInf> [0..1] Text 976
       GarnishmentRemittance <GrnshmtRmt> [0..1]  976
         Type <Tp> [1..1]  977
           CodeOrProprietary <CdOrPrtry> [1..1]  977
{Or             Code <Cd> [1..1] CodeSet 978
Or}             Proprietary <Prtry> [1..1] Text 978
           Issuer <Issr> [0..1] Text 978
         Garnishee <Grnshee> [0..1] ± 978
         GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 979
         ReferenceNumber <RefNb> [0..1] Text 980
         Date <Dt> [0..1] Date 981
         RemittedAmount <RmtdAmt> [0..1] Amount C2, C9 981
         FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 981
         EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 981
       SecuritiesData <SctiesData> [0..*]  981
         UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 982
         Amount <Amt> [0..1] Amount C1, C8 982
       AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 982
   InstructedAmount <InstdAmt> [0..1] Amount C2, C9 982
Constraints
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
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
906 March 2026
```

## File page 907

```text
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
• PreviousInstructingAgent1Guideline
It is recommended that, when present, PreviousInstructingAgent1 is the closest to the DebtorAgent
in the payment chain.
• PreviousInstructingAgent2AccountRule
If PreviousInstructingAgent2Account is present, then PreviousInstructingAgent2 must be present.
On Condition
    /PreviousInstructingAgent2 is absent
Following Must be True
    /PreviousInstructingAgent2Account Must be absent
• PreviousInstructingAgent2Rule
If PreviousInstructingAgent2 is present, then PreviousInstructingAgent1 must be present.
On Condition
    /PreviousInstructingAgent2 is present
Following Must be True
    /PreviousInstructingAgent1 Must be present
• PreviousInstructingAgent3AccountRule
If PreviousInstructingAgent3Account is present, then PreviousInstructingAgent3 must be present.
On Condition
    /PreviousInstructingAgent3 is absent
Following Must be True
    /PreviousInstructingAgent3Account Must be absent
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
907 March 2026
```

