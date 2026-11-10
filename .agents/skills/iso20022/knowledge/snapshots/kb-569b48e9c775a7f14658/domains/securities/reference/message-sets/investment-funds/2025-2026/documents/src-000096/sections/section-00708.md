---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>"]
file_pages: [966, 967, 968, 969, 970, 971, 972, 973, 974, 975]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.12 NomineeAccount <NmneeAcct>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 966 to 975.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 966

```text
TransferorAccount <TrfrAcct> contains the following elements (see "InvestmentAccount69" on
page 4331 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4331
   Designation <Dsgnt> [0..1] Text 4331
   AccountName <AcctNm> [0..1] Text 4332
   Servicer <Svcr> [0..1] ± 4332
35.4.12 NomineeAccount <NmneeAcct>
Presence: [0..1]
Definition: Account held in the name of a party that is not the name of the beneficial owner of the
shares.
NomineeAccount <NmneeAcct> contains the following elements (see "InvestmentAccount69" on
page 4331 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4331
   Designation <Dsgnt> [0..1] Text 4331
   AccountName <AcctNm> [0..1] Text 4332
   Servicer <Svcr> [0..1] ± 4332
35.4.13 Transferee <Trfee>
Presence: [1..1]
Definition: Identification of the institution to which the financial instrument is to be transferred. This may
also be known as the new plan manager.
Transferee <Trfee> contains the following elements (see "PartyIdentification132" on page 5029 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 5029
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 5029
   NameAndAddress <NmAndAdr> [0..1] ± 5030
   ProprietaryIdentification <PrtryId> [0..1] ± 5031
   LEI <LEI> [0..1] IdentifierSet 5031
35.4.14 ProductTransfer <PdctTrf>
Presence: [1..*]
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 966 May 2026
```

## File page 967

```text
Definition: Information about the portfolio and assets.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 967 May 2026
```

## File page 968

```text
ProductTransfer <PdctTrf> contains the following PortfolioTransfer14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MasterReference <MstrRef> [0..1] Text 978
   TransferIdentification <TrfId> [1..1] Text 978
   TransferConfirmationIdentification <TrfConfId> [0..1] Text 979
   RequestedTransferDate <ReqdTrfDt> [0..1] Date 979
   Portfolio <Prtfl> [0..1]  979
{Or     TaxEfficientProduct <TaxEffcntPdct> [1..1] ± 979
Or     GeneralInvestment <GnlInvstmt> [1..1] ± 980
Or}     Pension <Pnsn> [1..1]  981
       Identification <Id> [0..1]  981
         Identifier <Idr> [1..1] Text 981
         SubIdentifier <SubIdr> [0..1] Text 981
         AdditionalInformation <AddtlInf> [0..1] ± 982
       Type <Tp> [0..1]  982
{Or         Code <Cd> [1..1] CodeSet 982
Or}         Proprietary <Prtry> [1..1] ± 983
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
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 968 May 2026
```

## File page 969

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Other <Othr> [0..1] ± 992
       DebtorAgent <DbtrAgt> [0..1]  992
         BICFI <BICFI> [0..1] IdentifierSet C10 993
         ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 993
         NameAndAddress <NmAndAdr> [0..1] ± 994
         LEI <LEI> [0..1] IdentifierSet 994
         ProprietaryIdentification <PrtryId> [0..1] Text 995
         BranchIdentification <BrnchId> [0..1] ± 995
       DebtorAgentAccount <DbtrAgtAcct> [0..1]  995
         Name <Nm> [0..1] Text 995
         IBAN <IBAN> [0..1] IdentifierSet C26 995
         BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 996
         Other <Othr> [0..1] ± 996
       IntermediaryAgent1 <IntrmyAgt1> [0..1]  996
         BICFI <BICFI> [0..1] IdentifierSet C10 997
         ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 997
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
         ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1001
         NameAndAddress <NmAndAdr> [0..1] ± 1002
         LEI <LEI> [0..1] IdentifierSet 1002
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 969 May 2026
```

## File page 970

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         ProprietaryIdentification <PrtryId> [0..1] Text 1003
         BranchIdentification <BrnchId> [0..1] ± 1003
       IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1003
         Name <Nm> [0..1] Text 1003
         IBAN <IBAN> [0..1] IdentifierSet C26 1003
         BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1004
         Other <Othr> [0..1] ± 1004
       CreditorAgent <CdtrAgt> [1..1]  1004
         BICFI <BICFI> [0..1] IdentifierSet C10 1005
         ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1005
         NameAndAddress <NmAndAdr> [0..1] ± 1006
         LEI <LEI> [0..1] IdentifierSet 1006
         ProprietaryIdentification <PrtryId> [0..1] Text 1007
         BranchIdentification <BrnchId> [0..1] ± 1007
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
   FinancialInstrumentAssetForTransfer
<FinInstrmAsstForTrf>
[0..*]  C7, C8,
C9, C12,
C13,
C36
1010
     LineIdentification <LineId> [0..1] Text 1019
     Instrument <Instrm> [1..1]  1019
{Or       Security <Scty> [1..1]  C27 1020
         Identification <Id> [1..1]  1021
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 970 May 2026
```

## File page 971

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or           ISIN <ISIN> [1..1] IdentifierSet 1022
Or           SEDOL <SEDOL> [1..1] IdentifierSet 1022
Or           CUSIP <CUSIP> [1..1] IdentifierSet 1023
Or           RIC <RIC> [1..1] IdentifierSet 1023
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 1023
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 1023
Or           CTA <CTA> [1..1] IdentifierSet 1023
Or           QUICK <QUICK> [1..1] IdentifierSet 1023
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 1023
Or           Dutch <Dtch> [1..1] IdentifierSet 1024
Or           Valoren <Vlrn> [1..1] IdentifierSet 1024
Or           Sicovam <SCVM> [1..1] IdentifierSet 1024
Or           Belgian <Belgn> [1..1] IdentifierSet 1024
Or           Common <Cmon> [1..1] IdentifierSet 1024
Or           DTI <DTI> [1..1] IdentifierSet 1024
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  1024
             Identification <Id> [1..1] Text 1025
             IdentificationSource <IdSrc> [1..1] ± 1025
         Name <Nm> [0..1] Text 1025
         ShortName <ShrtNm> [0..1] Text 1025
         ClassificationType <ClssfctnTp> [0..1] ± 1025
Or       CashAsset <CshAsst> [1..1] ± C25 1025
Or}       OtherAsset <OthrAsst> [1..1] ± 1026
     Quantity <Qty> [0..1]  1026
       Unit <Unit> [0..1]  1027
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 1027
Or}         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1027
       PercentageRate <PctgRate> [0..1] Rate 1027
       FaceAmount <FaceAmt> [0..1] Amount 1027
       AmortisedValue <AmtsdVal> [0..1] Amount 1028
       CashAmount <CshAmt> [0..1] Amount C1 1028
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 971 May 2026
```

## File page 972

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       OtherAsset <OthrAsst> [0..1] Text 1028
     PartialInstructedQuantity <PrtlInstdQty> [0..1] Indicator 1028
     TransferType <TrfTp> [1..1] ± C41 1028
     AdditionalAsset <AddtlAsst> [0..1] Indicator 1029
     NotAvailable <NotAvlbl> [0..1] Indicator 1029
     Conversion <Convs> [0..1]  1029
       TargetSecurity <TrgtScty> [1..1]  C28 1030
         Identification <Id> [1..1]  1031
{Or           ISIN <ISIN> [1..1] IdentifierSet 1032
Or           SEDOL <SEDOL> [1..1] IdentifierSet 1032
Or           CUSIP <CUSIP> [1..1] IdentifierSet 1033
Or           RIC <RIC> [1..1] IdentifierSet 1033
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 1033
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 1033
Or           CTA <CTA> [1..1] IdentifierSet 1033
Or           QUICK <QUICK> [1..1] IdentifierSet 1033
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 1033
Or           Dutch <Dtch> [1..1] IdentifierSet 1034
Or           Valoren <Vlrn> [1..1] IdentifierSet 1034
Or           Sicovam <SCVM> [1..1] IdentifierSet 1034
Or           Belgian <Belgn> [1..1] IdentifierSet 1034
Or           Common <Cmon> [1..1] IdentifierSet 1034
Or           DTI <DTI> [1..1] IdentifierSet 1034
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  1034
             Identification <Id> [1..1] Text 1035
             IdentificationSource <IdSrc> [1..1] ± 1035
         Name <Nm> [0..1] Text 1035
         ShortName <ShrtNm> [0..1] Text 1035
       AdditionalInformation <AddtlInf> [0..*] ± 1035
     UnitsDetails <UnitsDtls> [0..*]  1035
       Units <Units> [1..1]  1038
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 972 May 2026
```

## File page 973

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 1038
Or}         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1038
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
         CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 1042
         IndividualFee <IndvFee> [0..*]  C6 1043
           Type <Tp> [1..1]  1043
{Or             Code <Cd> [1..1] CodeSet 1044
Or}             Proprietary <Prtry> [1..1] ± 1045
           Basis <Bsis> [0..1]  1045
{Or             Code <Cd> [1..1] CodeSet 1045
Or}             Proprietary <Prtry> [1..1] ± 1046
           StandardAmount <StdAmt> [0..1] Amount C1, C18 1046
           StandardRate <StdRate> [0..1] Rate 1046
           DiscountDetails <DscntDtls> [0..1]  C23 1047
             Amount <Amt> [0..1] Amount C1, C18 1047
             Rate <Rate> [0..1] Rate 1048
             Basis <Bsis> [0..1]  1048
{Or               Code <Cd> [1..1] CodeSet 1048
Or}               Proprietary <Prtry> [1..1] ± 1048
           AppliedAmount <ApldAmt> [0..1] Amount C1, C18 1049
           AppliedRate <ApldRate> [0..1] Rate 1049
           NonStandardSLAReference <NonStdSLARef> [0..1] Text 1049
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 973 May 2026
```

## File page 974

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or                 Code <Cd> [1..1] CodeSet 1054
Or}                 Proprietary <Prtry> [1..1] Text 1055
             Description <Desc> [0..1] Text 1055
           Quantity <Qty> [1..1]  1056
{Or             Quantity <Qty> [1..1] ± C22 1056
Or}             ProprietaryQuantity <PrtryQty> [1..1]  1056
               Quantity <Qty> [1..1] Quantity 1057
               QuantityType <QtyTp> [1..1] Text 1057
               Issuer <Issr> [1..1] Text 1057
               SchemeName <SchmeNm> [0..1] Text 1057
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1057
       OtherAmount <OthrAmt> [0..*]  1057
         Type <Tp> [1..1]  1058
{Or           Code <Cd> [1..1] CodeSet 1058
Or}           ProprietaryCode <PrtryCd> [1..1] ± 1058
         Amount <Amt> [1..1] Amount C1, C18 1058
     ClientReference <ClntRef> [0..1] ± 1059
     CounterpartyReference <CtrPtyRef> [0..1] ± 1059
     BusinessFlowType <BizFlowTp> [0..1] CodeSet 1059
     AverageAcquisitionPrice <AvrgAcqstnPric> [0..1] Amount C2, C17 1060
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 974 May 2026
```

## File page 975

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 975 May 2026
```

