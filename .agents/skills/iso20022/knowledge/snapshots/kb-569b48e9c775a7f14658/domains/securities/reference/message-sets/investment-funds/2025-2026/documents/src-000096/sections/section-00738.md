---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.9 PaymentDetails <PmtDtls>", "35.4.14.9.2 CreditTransferDetails <CdtTrfDtls>", "35.4.14.9.2.12 CreditorAccount <CdtrAcct>", "35.4.14.9.2.12.3 BlockChainCashWallet <BlckChainCshWllt>"]
file_pages: [1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.9.2.12.3 BlockChainCashWallet <BlckChainCshWllt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1010 to 1018.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1010

```text
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
35.4.14.9.2.12.3  BlockChainCashWallet <BlckChainCshWllt>
Presence: [0..1]
Definition: Block Chain Wallet where digital currencies are maintained. This is the equivalent of cash
account for digital currencies.
BlockChainCashWallet <BlckChainCshWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
35.4.14.9.2.12.4  Other <Othr>
Presence: [0..1]
Definition: Unique identification of the account, as assigned by the account servicer, using an
identification scheme.
Other <Othr> contains the following elements (see "GenericAccountIdentification1" on page 4326 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4326
   SchemeName <SchmeNm> [0..1]  4326
{Or     Code <Cd> [1..1] CodeSet 4326
Or}     Proprietary <Prtry> [1..1] Text 4326
   Issuer <Issr> [0..1] Text 4326
35.4.14.10  FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>
Presence: [0..*]
Definition: Asset to be transferred.
Impacted by: C7 "AssetLiquidatedCurrencyGuideline", C8 "AssetQuantity1Guideline", C9
"AssetQuantity2Guideline", C12 "Conversion1Rule", C13 "Conversion2Rule", C36
"PartialInstructedQuantityRule"
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1010 May 2026
```

## File page 1011

```text
FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf> contains the following
FinancialInstrument108 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LineIdentification <LineId> [0..1] Text 1019
   Instrument <Instrm> [1..1]  1019
{Or     Security <Scty> [1..1]  C27 1020
       Identification <Id> [1..1]  1021
{Or         ISIN <ISIN> [1..1] IdentifierSet 1022
Or         SEDOL <SEDOL> [1..1] IdentifierSet 1022
Or         CUSIP <CUSIP> [1..1] IdentifierSet 1023
Or         RIC <RIC> [1..1] IdentifierSet 1023
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 1023
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 1023
Or         CTA <CTA> [1..1] IdentifierSet 1023
Or         QUICK <QUICK> [1..1] IdentifierSet 1023
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 1023
Or         Dutch <Dtch> [1..1] IdentifierSet 1024
Or         Valoren <Vlrn> [1..1] IdentifierSet 1024
Or         Sicovam <SCVM> [1..1] IdentifierSet 1024
Or         Belgian <Belgn> [1..1] IdentifierSet 1024
Or         Common <Cmon> [1..1] IdentifierSet 1024
Or         DTI <DTI> [1..1] IdentifierSet 1024
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  1024
           Identification <Id> [1..1] Text 1025
           IdentificationSource <IdSrc> [1..1] ± 1025
       Name <Nm> [0..1] Text 1025
       ShortName <ShrtNm> [0..1] Text 1025
       ClassificationType <ClssfctnTp> [0..1] ± 1025
Or     CashAsset <CshAsst> [1..1] ± C25 1025
Or}     OtherAsset <OthrAsst> [1..1] ± 1026
   Quantity <Qty> [0..1]  1026
     Unit <Unit> [0..1]  1027
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 1027
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1011 May 2026
```

## File page 1012

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1027
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
{Or         ISIN <ISIN> [1..1] IdentifierSet 1032
Or         SEDOL <SEDOL> [1..1] IdentifierSet 1032
Or         CUSIP <CUSIP> [1..1] IdentifierSet 1033
Or         RIC <RIC> [1..1] IdentifierSet 1033
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 1033
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 1033
Or         CTA <CTA> [1..1] IdentifierSet 1033
Or         QUICK <QUICK> [1..1] IdentifierSet 1033
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 1033
Or         Dutch <Dtch> [1..1] IdentifierSet 1034
Or         Valoren <Vlrn> [1..1] IdentifierSet 1034
Or         Sicovam <SCVM> [1..1] IdentifierSet 1034
Or         Belgian <Belgn> [1..1] IdentifierSet 1034
Or         Common <Cmon> [1..1] IdentifierSet 1034
Or         DTI <DTI> [1..1] IdentifierSet 1034
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  1034
           Identification <Id> [1..1] Text 1035
           IdentificationSource <IdSrc> [1..1] ± 1035
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1012 May 2026
```

## File page 1013

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Name <Nm> [0..1] Text 1035
       ShortName <ShrtNm> [0..1] Text 1035
     AdditionalInformation <AddtlInf> [0..*] ± 1035
   UnitsDetails <UnitsDtls> [0..*]  1035
     Units <Units> [1..1]  1038
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 1038
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1038
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
{Or           Code <Cd> [1..1] CodeSet 1044
Or}           Proprietary <Prtry> [1..1] ± 1045
         Basis <Bsis> [0..1]  1045
{Or           Code <Cd> [1..1] CodeSet 1045
Or}           Proprietary <Prtry> [1..1] ± 1046
         StandardAmount <StdAmt> [0..1] Amount C1, C18 1046
         StandardRate <StdRate> [0..1] Rate 1046
         DiscountDetails <DscntDtls> [0..1]  C23 1047
           Amount <Amt> [0..1] Amount C1, C18 1047
           Rate <Rate> [0..1] Rate 1048
           Basis <Bsis> [0..1]  1048
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1013 May 2026
```

## File page 1014

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or             Code <Cd> [1..1] CodeSet 1048
Or}             Proprietary <Prtry> [1..1] ± 1048
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
{Or               Code <Cd> [1..1] CodeSet 1054
Or}               Proprietary <Prtry> [1..1] Text 1055
           Description <Desc> [0..1] Text 1055
         Quantity <Qty> [1..1]  1056
{Or           Quantity <Qty> [1..1] ± C22 1056
Or}           ProprietaryQuantity <PrtryQty> [1..1]  1056
             Quantity <Qty> [1..1] Quantity 1057
             QuantityType <QtyTp> [1..1] Text 1057
             Issuer <Issr> [1..1] Text 1057
             SchemeName <SchmeNm> [0..1] Text 1057
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1057
     OtherAmount <OthrAmt> [0..*]  1057
       Type <Tp> [1..1]  1058
{Or         Code <Cd> [1..1] CodeSet 1058
Or}         ProprietaryCode <PrtryCd> [1..1] ± 1058
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1014 May 2026
```

## File page 1015

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1015 May 2026
```

## File page 1016

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       DebtorAccount <DbtrAcct> [0..1]  1072
         Name <Nm> [0..1] Text 1072
         IBAN <IBAN> [0..1] IdentifierSet C26 1072
         BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1073
         Other <Othr> [0..1] ± 1073
       DebtorAgent <DbtrAgt> [0..1]  1073
         BICFI <BICFI> [0..1] IdentifierSet C10 1074
         ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1074
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
         ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1078
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
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1016 May 2026
```

## File page 1017

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1082
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
         ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1086
         NameAndAddress <NmAndAdr> [0..1] ± 1087
         LEI <LEI> [0..1] IdentifierSet 1087
         ProprietaryIdentification <PrtryId> [0..1] Text 1088
         BranchIdentification <BrnchId> [0..1] ± 1088
       CreditorAgentAccount <CdtrAgtAcct> [0..1]  1088
         Name <Nm> [0..1] Text 1088
         IBAN <IBAN> [0..1] IdentifierSet C26 1088
         BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1089
         Other <Othr> [0..1] ± 1089
       Creditor <Cdtr> [0..1] ± 1089
       CreditorAccount <CdtrAcct> [1..1]  1090
         Name <Nm> [0..1] Text 1090
         IBAN <IBAN> [0..1] IdentifierSet C26 1090
         BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1091
         Other <Othr> [0..1] ± 1091
   CrystallisationDetails <CrstllstnDtls> [0..*] ± 1091
   TaxValuationPoint <TaxValtnPt> [0..1] ± 1092
   SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  1092
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1017 May 2026
```

## File page 1018

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     SafekeepingPlace <SfkpgPlc> [0..1] ± 1093
     TradeTransactionCondition <TradTxCond> [0..*] ± 1094
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1094
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 1094
     ReceivingSideDetails <RcvgSdDtls> [0..1]  C11,
C19,
C37,
C38,
C39,
C40,
C42
1095
       Depository <Dpstry> [0..1] ± 1096
       Party1 <Pty1> [0..1] ± 1097
       Party2 <Pty2> [0..1] ± 1097
       Party3 <Pty3> [0..1] ± 1098
       Party4 <Pty4> [0..1] ± 1098
       Party5 <Pty5> [0..1] ± 1099
     DeliveringSideDetails <DlvrgSdDtls> [0..1]  C11,
C19,
C37,
C38,
C39,
C40,
C42
1099
       Depository <Dpstry> [0..1] ± 1101
       Party1 <Pty1> [0..1] ± 1102
       Party2 <Pty2> [0..1] ± 1102
       Party3 <Pty3> [0..1] ± 1102
       Party4 <Pty4> [0..1] ± 1103
       Party5 <Pty5> [0..1] ± 1103
   AssetsHeldInOwnName <AsstsHeldInOwnNm> [0..1] Indicator 1104
   TransferResultsInChangeOfBeneficialOwner
<TrfRsltsInChngOfBnfclOwnr>
[0..1] Indicator 1104
   AdditionalInformation <AddtlInf> [0..*] ± 1104
Constraints
• AssetLiquidatedCurrencyGuideline
When a security is to be liquidated and transferred as cash (TransferType is CASH), then the
currency of the resulting cash is specified in TransferCurrency.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1018 May 2026
```

