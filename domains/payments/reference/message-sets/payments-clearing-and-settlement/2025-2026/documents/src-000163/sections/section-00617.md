---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.2 Structure"]
file_pages: [831, 832, 833, 834, 835, 836, 837, 838, 839, 840]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.2 Structure

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 831 to 840.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 831

```text
7.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FICdtTrf> [1..1]  C12,
C13,
C17,
C19,
C38,
C63,
C68,
C69,
C71
   GroupHeader <GrpHdr> [1..1]  C67 848
     MessageIdentification <MsgId> [1..1] Text 850
     CreationDateTime <CreDtTm> [1..1] DateTime 850
     ExpiryDateTime <XpryDtTm> [0..1] DateTime 850
     BatchBooking <BtchBookg> [0..1] Indicator 850
     NumberOfTransactions <NbOfTxs> [1..1] Text 850
     ControlSum <CtrlSum> [0..1] Quantity 851
     TotalInterbankSettlementAmount <TtlIntrBkSttlmAmt> [0..1] Amount C1, C8 851
     InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 851
     SettlementInformation <SttlmInf> [1..1]  C18,
C20,
C59,
C60,
C61,
C62,
C65,
C66
851
       SettlementMethod <SttlmMtd> [1..1] CodeSet 853
       SettlementAccount <SttlmAcct> [0..1] ± C16,
C15
854
       ClearingSystem <ClrSys> [0..1]  854
{Or         Code <Cd> [1..1] CodeSet 855
Or}         Proprietary <Prtry> [1..1] Text 855
       InstructingReimbursementAgent <InstgRmbrsmntAgt> [0..1] ± 855
       InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C16,
C15
856
       InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 856
       InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C16,
C15
857
       ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 858
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
831 March 2026
```

## File page 832

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C16,
C15
858
     PaymentTypeInformation <PmtTpInf> [0..1] ± 859
     InstructingAgent <InstgAgt> [0..1] ± 860
     InstructedAgent <InstdAgt> [0..1] ± 861
   CreditTransferTransactionInformation <CdtTrfTxInf> [1..*]  C6, C10,
C21,
C24,
C26,
C29,
C32,
C35,
C39,
C45,
C48,
C51,
C54,
C79,
C42,
C72,
C75
861
     PaymentIdentification <PmtId> [1..1] ± C70 873
     PaymentTypeInformation <PmtTpInf> [0..1] ± 874
     InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount C1, C8 874
     InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 875
     SettlementPriority <SttlmPrty> [0..1] CodeSet 875
     SettlementTimeIndication <SttlmTmIndctn> [0..1]  875
       DebitDateTime <DbtDtTm> [0..1] DateTime 876
       CreditDateTime <CdtDtTm> [0..1] DateTime 876
     SettlementTimeRequest <SttlmTmReq> [0..1] ± 876
     ExpiryDateTime <XpryDtTm> [0..1] DateTime 876
     PaymentSignature <PmtSgntr> [0..1]  876
{Or       ILPV4 <ILPV4> [1..1] Text 877
Or}       Signature <Sgntr> [1..1] Text 877
     PreviousInstructingAgent1 <PrvsInstgAgt1> [0..1] ± 877
     PreviousInstructingAgent1Account <PrvsInstgAgt1Acct> [0..1] ± C16,
C15
877
     PreviousInstructingAgent2 <PrvsInstgAgt2> [0..1] ± 878
     PreviousInstructingAgent2Account <PrvsInstgAgt2Acct> [0..1] ± C16,
C15
879
     PreviousInstructingAgent3 <PrvsInstgAgt3> [0..1] ± 880
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
832 March 2026
```

## File page 833

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     PreviousInstructingAgent3Account <PrvsInstgAgt3Acct> [0..1] ± C16,
C15
880
     InstructingAgent <InstgAgt> [0..1] ± 881
     InstructedAgent <InstdAgt> [0..1] ± 882
     IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 883
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C16,
C15
884
     IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 885
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1] ± C16,
C15
885
     IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 886
     IntermediaryAgent3Account <IntrmyAgt3Acct> [0..1] ± C16,
C15
887
     UltimateDebtor <UltmtDbtr> [0..1] ± 888
     Debtor <Dbtr> [1..1] ± 888
     DebtorAccount <DbtrAcct> [0..1] ± C16,
C15
889
     DebtorAgent <DbtrAgt> [0..1] ± 890
     DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C16,
C15
890
     CreditorAgent <CdtrAgt> [0..1] ± 891
     CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C16,
C15
892
     Creditor <Cdtr> [1..1] ± 893
     CreditorAccount <CdtrAcct> [0..1] ± C16,
C15
893
     UltimateCreditor <UltmtCdtr> [0..1] ± 894
     InstructionForCreditorAgent <InstrForCdtrAgt> [0..*] ± 895
     InstructionForNextAgent <InstrForNxtAgt> [0..*]  895
       Code <Cd> [0..1] CodeSet 896
       InstructionInformation <InstrInf> [0..1] Text 896
     Purpose <Purp> [0..1] ± 896
     RegulatoryReporting <RgltryRptg> [0..10] ± 896
     RemittanceInformation <RmtInf> [0..1] ± 897
     UnderlyingAllocation <UndrlygAllcn> [0..*]  C78 897
       Amount <Amt> [1..1] Amount C2, C9 898
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
833 March 2026
```

## File page 834

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 898
       Account <Acct> [1..1] ± C16,
C15
899
       Purpose <Purp> [1..1] ± 899
       Reference <Ref> [1..1] Text 899
       RelatedReferences <RltdRefs> [0..*] ± 900
     UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf> [0..1]  C22,
C27,
C30,
C33,
C36,
C40,
C46,
C49,
C52,
C55,
C43,
C73,
C76
900
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
       PreviousInstructingAgent1Account <PrvsInstgAgt1Acct> [0..1] ± C16,
C15
915
       PreviousInstructingAgent2 <PrvsInstgAgt2> [0..1] ± 916
       PreviousInstructingAgent2Account <PrvsInstgAgt2Acct> [0..1] ± C16,
C15
917
       PreviousInstructingAgent3 <PrvsInstgAgt3> [0..1] ± 918
       PreviousInstructingAgent3Account <PrvsInstgAgt3Acct> [0..1] ± C16,
C15
918
       IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 919
       IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C16,
C15
920
       IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 921
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
834 March 2026
```

## File page 835

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
835 March 2026
```

## File page 836

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
{Or                 Code <Cd> [1..1] CodeSet 951
Or}                 Proprietary <Prtry> [1..1] Text 951
               Issuer <Issr> [0..1] Text 951
             Number <Nb> [0..1] Text 952
             RelatedDate <RltdDt> [0..1]  952
               Type <Tp> [1..1]  952
{Or                 Code <Cd> [1..1] CodeSet 952
Or}                 Proprietary <Prtry> [1..1] Text 952
               Date <Dt> [1..1] Date 952
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
836 March 2026
```

## File page 837

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             LineDetails <LineDtls> [0..*]  953
               Identification <Id> [1..*]  953
                 Type <Tp> [0..1]  954
                   CodeOrProprietary <CdOrPrtry> [1..1]  954
{Or                     Code <Cd> [1..1] CodeSet 954
Or}                     Proprietary <Prtry> [1..1] Text 954
                   Issuer <Issr> [0..1] Text 955
                 Number <Nb> [0..1] Text 955
                 RelatedDate <RltdDt> [0..1] Date 955
               Description <Desc> [0..1] Text 955
               Amount <Amt> [0..1]  C57 955
                 RemittanceAmountAndType <RmtAmtAndTp> [0..*]  956
                   Type <Tp> [1..1]  956
{Or                     Code <Cd> [1..1] CodeSet 957
Or}                     Proprietary <Prtry> [1..1] Text 957
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
{Or                 Code <Cd> [1..1] CodeSet 960
Or}                 Proprietary <Prtry> [1..1] Text 960
               Amount <Amt> [1..1] Amount C2, C9 960
             AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  960
               Amount <Amt> [1..1] Amount C2, C9 960
               CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 961
               Reason <Rsn> [0..1] Text 961
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
837 March 2026
```

## File page 838

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               AdditionalInformation <AddtlInf> [0..1] Text 961
           CreditorReferenceInformation <CdtrRefInf> [0..1]  961
             Type <Tp> [0..1]  962
               CodeOrProprietary <CdOrPrtry> [1..1]  962
{Or                 Code <Cd> [1..1] CodeSet 962
Or}                 Proprietary <Prtry> [1..1] Text 962
               Issuer <Issr> [0..1] Text 963
             Reference <Ref> [0..1] Text 963
           Invoicer <Invcr> [0..1] ± 963
           Invoicee <Invcee> [0..1] ± 964
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
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
838 March 2026
```

## File page 839

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
                   Amount <Amt> [1..1] Amount C2, C9 976
               AdditionalInformation <AddtlInf> [0..1] Text 976
           GarnishmentRemittance <GrnshmtRmt> [0..1]  976
             Type <Tp> [1..1]  977
               CodeOrProprietary <CdOrPrtry> [1..1]  977
{Or                 Code <Cd> [1..1] CodeSet 978
Or}                 Proprietary <Prtry> [1..1] Text 978
               Issuer <Issr> [0..1] Text 978
             Garnishee <Grnshee> [0..1] ± 978
             GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 979
             ReferenceNumber <RefNb> [0..1] Text 980
             Date <Dt> [0..1] Date 981
             RemittedAmount <RmtdAmt> [0..1] Amount C2, C9 981
             FamilyMedicalInsuranceIndicator <FmlyMdclInsrncInd> [0..1] Indicator 981
             EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 981
           SecuritiesData <SctiesData> [0..*]  981
             UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 982
             Amount <Amt> [0..1] Amount C1, C8 982
           AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 982
       InstructedAmount <InstdAmt> [0..1] Amount C2, C9 982
     UnderlyingFinancialInstitutionCreditTransfer
<UndrlygFICdtTrf>
[0..1]  C7, C11,
C23,
C25,
983
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
839 March 2026
```

## File page 840

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
C28,
C31,
C34,
C37,
C41,
C47,
C50,
C53,
C56,
C44,
C74,
C77
       PaymentIdentification <PmtId> [1..1] ± C70 987
       PaymentTypeInformation <PmtTpInf> [0..1] ± 988
       InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount C1, C8 988
       InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 989
       SettlementPriority <SttlmPrty> [0..1] CodeSet 989
       SettlementTimeIndication <SttlmTmIndctn> [0..1]  989
         DebitDateTime <DbtDtTm> [0..1] DateTime 990
         CreditDateTime <CdtDtTm> [0..1] DateTime 990
       SettlementTimeRequest <SttlmTmReq> [0..1] ± 990
       ExpiryDateTime <XpryDtTm> [0..1] DateTime 990
       PaymentSignature <PmtSgntr> [0..1]  990
{Or         ILPV4 <ILPV4> [1..1] Text 991
Or}         Signature <Sgntr> [1..1] Text 991
       PreviousInstructingAgent1 <PrvsInstgAgt1> [0..1] ± 991
       PreviousInstructingAgent1Account <PrvsInstgAgt1Acct> [0..1] ± C16,
C15
991
       PreviousInstructingAgent2 <PrvsInstgAgt2> [0..1] ± 992
       PreviousInstructingAgent2Account <PrvsInstgAgt2Acct> [0..1] ± C16,
C15
993
       PreviousInstructingAgent3 <PrvsInstgAgt3> [0..1] ± 994
       PreviousInstructingAgent3Account <PrvsInstgAgt3Acct> [0..1] ± C16,
C15
994
       InstructingAgent <InstgAgt> [0..1] ± 995
       InstructedAgent <InstdAgt> [0..1] ± 996
       IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 997
       IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C16,
C15
998
       IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 999
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
840 March 2026
```

