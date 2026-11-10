---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.2 Structure"]
file_pages: [945, 946, 947, 948, 949, 950, 951, 952, 953, 954]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 945 to 954.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 945

```text
35.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PrtflTrfInstr> [1..1]  C14,
C15,
C29,
C30,
C33
   MessageReference <MsgRef> [1..1] ± 961
   PoolReference <PoolRef> [0..1] ± 961
   PreviousReference <PrvsRef> [0..1] ± 961
   RelatedReference <RltdRef> [0..1] ± 961
   PrimaryIndividualInvestor <PmryIndvInvstr> [0..1] ± C43 962
   SecondaryIndividualInvestor <ScndryIndvInvstr> [0..1] ± C43 0
   OtherIndividualInvestor <OthrIndvInvstr> [0..*] ± C43 0
   PrimaryCorporateInvestor <PmryCorpInvstr> [0..1] ± 964
   SecondaryCorporateInvestor <ScndryCorpInvstr> [0..1] ± 964
   OtherCorporateInvestor <OthrCorpInvstr> [0..*] ± 965
   TransferorAccount <TrfrAcct> [1..1] ± 0
   NomineeAccount <NmneeAcct> [0..1] ± 966
   Transferee <Trfee> [1..1] ± 0
   ProductTransfer <PdctTrf> [1..*]  0
     MasterReference <MstrRef> [0..1] Text 978
     TransferIdentification <TrfId> [1..1] Text 978
     TransferConfirmationIdentification <TrfConfId> [0..1] Text 979
     RequestedTransferDate <ReqdTrfDt> [0..1] Date 979
     Portfolio <Prtfl> [0..1]  979
{Or       TaxEfficientProduct <TaxEffcntPdct> [1..1] ± 979
Or       GeneralInvestment <GnlInvstmt> [1..1] ± 980
Or}       Pension <Pnsn> [1..1]  981
         Identification <Id> [0..1]  981
           Identifier <Idr> [1..1] Text 981
           SubIdentifier <SubIdr> [0..1] Text 981
           AdditionalInformation <AddtlInf> [0..1] ± 982
         Type <Tp> [0..1]  982
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 945 May 2026
```

## File page 946

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or           Code <Cd> [1..1] CodeSet 982
Or}           Proprietary <Prtry> [1..1] ± 983
         TransferScope <TrfScp> [0..1] ± 983
         TaxReference <TaxRef> [0..*] ± 984
         DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 984
         NonWrapperTransfer <NonWrpprTrf> [0..1] Indicator 984
         AdditionalInformation <AddtlInf> [0..*] ± 984
     AllOtherCash <AllOthrCsh> [0..*] ± 985
     CashAll <CshAll> [0..*] ± 985
     ResidualCash <RsdlCsh> [0..*] ± 985
     PaymentDetails <PmtDtls> [0..1]  985
       Reference <Ref> [0..1] Text 988
       CreditTransferDetails <CdtTrfDtls> [0..1]  988
         Debtor <Dbtr> [0..1] ± 991
         DebtorAccount <DbtrAcct> [0..1]  991
           Name <Nm> [0..1] Text 991
           IBAN <IBAN> [0..1] IdentifierSet C26 991
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 992
           Other <Othr> [0..1] ± 992
         DebtorAgent <DbtrAgt> [0..1]  992
           BICFI <BICFI> [0..1] IdentifierSet C10 993
           ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 993
           NameAndAddress <NmAndAdr> [0..1] ± 994
           LEI <LEI> [0..1] IdentifierSet 994
           ProprietaryIdentification <PrtryId> [0..1] Text 995
           BranchIdentification <BrnchId> [0..1] ± 995
         DebtorAgentAccount <DbtrAgtAcct> [0..1]  995
           Name <Nm> [0..1] Text 995
           IBAN <IBAN> [0..1] IdentifierSet C26 995
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 996
           Other <Othr> [0..1] ± 996
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 946 May 2026
```

## File page 947

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         IntermediaryAgent1 <IntrmyAgt1> [0..1]  996
           BICFI <BICFI> [0..1] IdentifierSet C10 997
           ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 997
           NameAndAddress <NmAndAdr> [0..1] ± 998
           LEI <LEI> [0..1] IdentifierSet 998
           ProprietaryIdentification <PrtryId> [0..1] Text 999
           BranchIdentification <BrnchId> [0..1] ± 999
         IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  999
           Name <Nm> [0..1] Text 999
           IBAN <IBAN> [0..1] IdentifierSet C26 999
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1000
           Other <Othr> [0..1] ± 1000
         IntermediaryAgent2 <IntrmyAgt2> [0..1]  1000
           BICFI <BICFI> [0..1] IdentifierSet C10 1001
           ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1001
           NameAndAddress <NmAndAdr> [0..1] ± 1002
           LEI <LEI> [0..1] IdentifierSet 1002
           ProprietaryIdentification <PrtryId> [0..1] Text 1003
           BranchIdentification <BrnchId> [0..1] ± 1003
         IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1003
           Name <Nm> [0..1] Text 1003
           IBAN <IBAN> [0..1] IdentifierSet C26 1003
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1004
           Other <Othr> [0..1] ± 1004
         CreditorAgent <CdtrAgt> [1..1]  1004
           BICFI <BICFI> [0..1] IdentifierSet C10 1005
           ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1005
           NameAndAddress <NmAndAdr> [0..1] ± 1006
           LEI <LEI> [0..1] IdentifierSet 1006
           ProprietaryIdentification <PrtryId> [0..1] Text 1007
           BranchIdentification <BrnchId> [0..1] ± 1007
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 947 May 2026
```

## File page 948

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         CreditorAgentAccount <CdtrAgtAcct> [0..1]  1007
           Name <Nm> [0..1] Text 1007
           IBAN <IBAN> [0..1] IdentifierSet C26 1007
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1008
           Other <Othr> [0..1] ± 1008
         Creditor <Cdtr> [0..1] ± 1008
         CreditorAccount <CdtrAcct> [1..1]  1009
           Name <Nm> [0..1] Text 1009
           IBAN <IBAN> [0..1] IdentifierSet C26 1009
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1010
           Other <Othr> [0..1] ± 1010
     FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf> [0..*]  C7, C8,
C9, C12,
C13,
C36
1010
       LineIdentification <LineId> [0..1] Text 1019
       Instrument <Instrm> [1..1]  1019
{Or         Security <Scty> [1..1]  C27 1020
           Identification <Id> [1..1]  1021
{Or             ISIN <ISIN> [1..1] IdentifierSet 1022
Or             SEDOL <SEDOL> [1..1] IdentifierSet 1022
Or             CUSIP <CUSIP> [1..1] IdentifierSet 1023
Or             RIC <RIC> [1..1] IdentifierSet 1023
Or             TickerSymbol <TckrSymb> [1..1] IdentifierSet 1023
Or             Bloomberg <Blmbrg> [1..1] IdentifierSet 1023
Or             CTA <CTA> [1..1] IdentifierSet 1023
Or             QUICK <QUICK> [1..1] IdentifierSet 1023
Or             Wertpapier <Wrtppr> [1..1] IdentifierSet 1023
Or             Dutch <Dtch> [1..1] IdentifierSet 1024
Or             Valoren <Vlrn> [1..1] IdentifierSet 1024
Or             Sicovam <SCVM> [1..1] IdentifierSet 1024
Or             Belgian <Belgn> [1..1] IdentifierSet 1024
Or             Common <Cmon> [1..1] IdentifierSet 1024
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 948 May 2026
```

## File page 949

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or             DTI <DTI> [1..1] IdentifierSet 1024
Or}             OtherProprietaryIdentification <OthrPrtryId> [1..1]  1024
               Identification <Id> [1..1] Text 1025
               IdentificationSource <IdSrc> [1..1] ± 1025
           Name <Nm> [0..1] Text 1025
           ShortName <ShrtNm> [0..1] Text 1025
           ClassificationType <ClssfctnTp> [0..1] ± 1025
Or         CashAsset <CshAsst> [1..1] ± C25 1025
Or}         OtherAsset <OthrAsst> [1..1] ± 1026
       Quantity <Qty> [0..1]  1026
         Unit <Unit> [0..1]  1027
{Or           UnitsNumber <UnitsNb> [1..1] Quantity 1027
Or}           DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1027
         PercentageRate <PctgRate> [0..1] Rate 1027
         FaceAmount <FaceAmt> [0..1] Amount 1027
         AmortisedValue <AmtsdVal> [0..1] Amount 1028
         CashAmount <CshAmt> [0..1] Amount C1 1028
         OtherAsset <OthrAsst> [0..1] Text 1028
       PartialInstructedQuantity <PrtlInstdQty> [0..1] Indicator 1028
       TransferType <TrfTp> [1..1] ± C41 1028
       AdditionalAsset <AddtlAsst> [0..1] Indicator 1029
       NotAvailable <NotAvlbl> [0..1] Indicator 1029
       Conversion <Convs> [0..1]  1029
         TargetSecurity <TrgtScty> [1..1]  C28 1030
           Identification <Id> [1..1]  1031
{Or             ISIN <ISIN> [1..1] IdentifierSet 1032
Or             SEDOL <SEDOL> [1..1] IdentifierSet 1032
Or             CUSIP <CUSIP> [1..1] IdentifierSet 1033
Or             RIC <RIC> [1..1] IdentifierSet 1033
Or             TickerSymbol <TckrSymb> [1..1] IdentifierSet 1033
Or             Bloomberg <Blmbrg> [1..1] IdentifierSet 1033
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 949 May 2026
```

## File page 950

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or             CTA <CTA> [1..1] IdentifierSet 1033
Or             QUICK <QUICK> [1..1] IdentifierSet 1033
Or             Wertpapier <Wrtppr> [1..1] IdentifierSet 1033
Or             Dutch <Dtch> [1..1] IdentifierSet 1034
Or             Valoren <Vlrn> [1..1] IdentifierSet 1034
Or             Sicovam <SCVM> [1..1] IdentifierSet 1034
Or             Belgian <Belgn> [1..1] IdentifierSet 1034
Or             Common <Cmon> [1..1] IdentifierSet 1034
Or             DTI <DTI> [1..1] IdentifierSet 1034
Or}             OtherProprietaryIdentification <OthrPrtryId> [1..1]  1034
               Identification <Id> [1..1] Text 1035
               IdentificationSource <IdSrc> [1..1] ± 1035
           Name <Nm> [0..1] Text 1035
           ShortName <ShrtNm> [0..1] Text 1035
         AdditionalInformation <AddtlInf> [0..*] ± 1035
       UnitsDetails <UnitsDtls> [0..*]  1035
         Units <Units> [1..1]  1038
{Or           UnitsNumber <UnitsNb> [1..1] Quantity 1038
Or}           DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1038
         OrderDate <OrdrDt> [0..1] Date 1038
         AcquisitionDate <AcqstnDt> [0..1] Date 1038
         CertificateNumber <CertNb> [0..*] Text 1038
         Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 1038
         Reference <Ref> [0..1] Text 1039
         PriceDetails <PricDtls> [0..1] ± 1039
         TransactionOverhead <TxOvrhd> [0..1]  C34,
C46
1039
           TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C18 1041
           TotalFees <TtlFees> [0..1] Amount C1, C18 1042
           TotalTaxes <TtlTaxs> [0..1] Amount C1, C18 1042
           CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 1042
           IndividualFee <IndvFee> [0..*]  C6 1043
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 950 May 2026
```

## File page 951

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Type <Tp> [1..1]  1043
{Or               Code <Cd> [1..1] CodeSet 1044
Or}               Proprietary <Prtry> [1..1] ± 1045
             Basis <Bsis> [0..1]  1045
{Or               Code <Cd> [1..1] CodeSet 1045
Or}               Proprietary <Prtry> [1..1] ± 1046
             StandardAmount <StdAmt> [0..1] Amount C1, C18 1046
             StandardRate <StdRate> [0..1] Rate 1046
             DiscountDetails <DscntDtls> [0..1]  C23 1047
               Amount <Amt> [0..1] Amount C1, C18 1047
               Rate <Rate> [0..1] Rate 1048
               Basis <Bsis> [0..1]  1048
{Or                 Code <Cd> [1..1] CodeSet 1048
Or}                 Proprietary <Prtry> [1..1] ± 1048
             AppliedAmount <ApldAmt> [0..1] Amount C1, C18 1049
             AppliedRate <ApldRate> [0..1] Rate 1049
             NonStandardSLAReference <NonStdSLARef> [0..1] Text 1049
             RecipientIdentification <RcptId> [0..1] ± 1049
             InformativeIndicator <InftvInd> [1..1] Indicator 1050
           IndividualTax <IndvTax> [0..*] ± 1050
           DigitalNetworkFee <DgtlNtwkFee> [0..2]  1050
             FinancialInstrumentIdentification <FinInstrmId> [1..1]  C20,
C21,
C31,
C32,
C35
1051
               ISIN <ISIN> [0..1] IdentifierSet 1053
               OtherIdentification <OthrId> [0..*]  1053
                 Identification <Id> [1..1] Text 1053
                 Suffix <Sfx> [0..1] Text 1053
                 Type <Tp> [1..1]  1053
{Or                   Code <Cd> [1..1] CodeSet 1054
Or}                   Proprietary <Prtry> [1..1] Text 1055
               Description <Desc> [0..1] Text 1055
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 951 May 2026
```

## File page 952

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Quantity <Qty> [1..1]  1056
{Or               Quantity <Qty> [1..1] ± C22 1056
Or}               ProprietaryQuantity <PrtryQty> [1..1]  1056
                 Quantity <Qty> [1..1] Quantity 1057
                 QuantityType <QtyTp> [1..1] Text 1057
                 Issuer <Issr> [1..1] Text 1057
                 SchemeName <SchmeNm> [0..1] Text 1057
             DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1057
         OtherAmount <OthrAmt> [0..*]  1057
           Type <Tp> [1..1]  1058
{Or             Code <Cd> [1..1] CodeSet 1058
Or}             ProprietaryCode <PrtryCd> [1..1] ± 1058
           Amount <Amt> [1..1] Amount C1, C18 1058
       ClientReference <ClntRef> [0..1] ± 1059
       CounterpartyReference <CtrPtyRef> [0..1] ± 1059
       BusinessFlowType <BizFlowTp> [0..1] CodeSet 1059
       AverageAcquisitionPrice <AvrgAcqstnPric> [0..1] Amount C2, C17 1060
       TransferCurrency <TrfCcy> [0..1] CodeSet C2 1060
       TotalBookValue <TtlBookVal> [0..1] ± 1060
       TransfereeAccount <TrfeeAcct> [0..1]  1061
         OwnerIdentification <OwnrId> [0..1] ± 1061
         AccountIdentification <AcctId> [0..1] Text 1061
         Designation <Dsgnt> [0..1] Text 1062
         AccountName <AcctNm> [0..1] Text 1062
         Servicer <Svcr> [0..1] ± 1062
         SubAccountDetails <SubAcctDtls> [0..1] ± 1062
         BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1063
       Transferor <Trfr> [0..1]  1063
         OwnerIdentification <OwnrId> [0..1] ± 1063
         AccountIdentification <AcctId> [0..1] Text 1064
         Designation <Dsgnt> [0..1] Text 1064
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 952 May 2026
```

## File page 953

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         AccountName <AcctNm> [0..1] Text 1064
         Servicer <Svcr> [0..1] ± 1064
         SubAccountDetails <SubAcctDtls> [0..1] ± 1065
         BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1065
       IntermediaryInformation <IntrmyInf> [0..*] ± 1065
       RequestedTransferDate <ReqdTrfDt> [0..1] Date 1065
       RequestedTradeDate <ReqdTradDt> [0..1] Date 1066
       RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 1066
       PaymentDetails <PmtDtls> [0..1]  1066
         Reference <Ref> [0..1] Text 1069
         CreditTransferDetails <CdtTrfDtls> [0..1]  1069
           Debtor <Dbtr> [0..1] ± 1072
           DebtorAccount <DbtrAcct> [0..1]  1072
             Name <Nm> [0..1] Text 1072
             IBAN <IBAN> [0..1] IdentifierSet C26 1072
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1073
             Other <Othr> [0..1] ± 1073
           DebtorAgent <DbtrAgt> [0..1]  1073
             BICFI <BICFI> [0..1] IdentifierSet C10 1074
             ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1074
             NameAndAddress <NmAndAdr> [0..1] ± 1075
             LEI <LEI> [0..1] IdentifierSet 1075
             ProprietaryIdentification <PrtryId> [0..1] Text 1076
             BranchIdentification <BrnchId> [0..1] ± 1076
           DebtorAgentAccount <DbtrAgtAcct> [0..1]  1076
             Name <Nm> [0..1] Text 1076
             IBAN <IBAN> [0..1] IdentifierSet C26 1076
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1077
             Other <Othr> [0..1] ± 1077
           IntermediaryAgent1 <IntrmyAgt1> [0..1]  1077
             BICFI <BICFI> [0..1] IdentifierSet C10 1078
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 953 May 2026
```

## File page 954

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1078
             NameAndAddress <NmAndAdr> [0..1] ± 1079
             LEI <LEI> [0..1] IdentifierSet 1079
             ProprietaryIdentification <PrtryId> [0..1] Text 1080
             BranchIdentification <BrnchId> [0..1] ± 1080
           IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1080
             Name <Nm> [0..1] Text 1080
             IBAN <IBAN> [0..1] IdentifierSet C26 1080
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1081
             Other <Othr> [0..1] ± 1081
           IntermediaryAgent2 <IntrmyAgt2> [0..1]  1081
             BICFI <BICFI> [0..1] IdentifierSet C10 1082
             ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1082
             NameAndAddress <NmAndAdr> [0..1] ± 1083
             LEI <LEI> [0..1] IdentifierSet 1083
             ProprietaryIdentification <PrtryId> [0..1] Text 1084
             BranchIdentification <BrnchId> [0..1] ± 1084
           IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1084
             Name <Nm> [0..1] Text 1084
             IBAN <IBAN> [0..1] IdentifierSet C26 1084
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1085
             Other <Othr> [0..1] ± 1085
           CreditorAgent <CdtrAgt> [1..1]  1085
             BICFI <BICFI> [0..1] IdentifierSet C10 1086
             ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1086
             NameAndAddress <NmAndAdr> [0..1] ± 1087
             LEI <LEI> [0..1] IdentifierSet 1087
             ProprietaryIdentification <PrtryId> [0..1] Text 1088
             BranchIdentification <BrnchId> [0..1] ± 1088
           CreditorAgentAccount <CdtrAgtAcct> [0..1]  1088
             Name <Nm> [0..1] Text 1088
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 954 May 2026
```

