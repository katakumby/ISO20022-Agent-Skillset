---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.2 Structure"]
file_pages: [1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1894 to 1903.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1894

```text
43.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <RedBlkOrdrConf> [1..1]  C2, C27
   MessageIdentification <MsgId> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 0
   PreviousReference <PrvsRef> [0..*] ± 1912
   RelatedReference <RltdRef> [0..1] ± 1912
   BulkExecutionDetails <BlkExctnDtls> [1..1]  C8, C35,
C37
0
     AmendmentIndicator <AmdmntInd> [0..1] Indicator 1927
     MasterReference <MstrRef> [0..1] Text 1927
     PlaceOfTrade <PlcOfTrad> [0..1] ± 1927
     OrderDateTime <OrdrDtTm> [0..1] DateTime 1928
     ReceivedDateTime <RcvdDtTm> [0..1] DateTime 1928
     RequestedFutureTradeDate <ReqdFutrTradDt> [0..1] Date 1928
     CancellationRight <CxlRght> [0..1] ± 1928
     FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C20 1928
       Identification <Id> [1..1]  1930
{Or         ISIN <ISIN> [1..1] IdentifierSet 1930
Or         SEDOL <SEDOL> [1..1] IdentifierSet 1931
Or         CUSIP <CUSIP> [1..1] IdentifierSet 1931
Or         RIC <RIC> [1..1] IdentifierSet 1931
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 1931
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 1931
Or         CTA <CTA> [1..1] IdentifierSet 1931
Or         QUICK <QUICK> [1..1] IdentifierSet 1931
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 1932
Or         Dutch <Dtch> [1..1] IdentifierSet 1932
Or         Valoren <Vlrn> [1..1] IdentifierSet 1932
Or         Sicovam <SCVM> [1..1] IdentifierSet 1932
Or         Belgian <Belgn> [1..1] IdentifierSet 1932
Or         Common <Cmon> [1..1] IdentifierSet 1932
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1894 May 2026
```

## File page 1895

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         DTI <DTI> [1..1] IdentifierSet 1932
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  1932
           Identification <Id> [1..1] Text 1933
           IdentificationSource <IdSrc> [1..1] ± 1933
       Name <Nm> [0..1] Text 1933
       ShortName <ShrtNm> [0..1] Text 1933
       SupplementaryIdentification <SplmtryId> [0..1] Text 1933
       ClassType <ClssTp> [0..1] Text 1933
       SecuritiesForm <SctiesForm> [0..1] CodeSet 1934
       DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 1934
       ProductGroup <PdctGrp> [0..1] Text 1934
       SeriesIdentification <SrsId> [0..1]  C36 1934
         SeriesDate <SrsDt> [0..1] ± 1935
         SeriesName <SrsNm> [0..1] Text 1935
     IndividualExecutionDetails <IndvExctnDtls> [1..*]  C26,
C30,
C31,
C32
1935
       OrderReference <OrdrRef> [1..1] Text 1946
       ClientReference <ClntRef> [0..1] Text 1946
       DealReference <DealRef> [1..1] Text 1946
       NonceIdentification <NonceId> [0..1] Text 1946
       OrderType <OrdrTp> [0..10] ± 1946
       BeneficiaryDetails <BnfcryDtls> [0..*] ± C29 1946
       Units <Units> [1..1]  1947
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 1947
Or}         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1947
       Rounding <Rndg> [0..1] CodeSet 1948
       NetAmount <NetAmt> [0..1] Amount C3, C10 1948
       InvestmentAccountDetails <InvstmtAcctDtls> [1..1]  C25 1948
         AccountIdentification <AcctId> [1..1] Text 1949
         AccountName <AcctNm> [0..1] Text 1949
         AccountDesignation <AcctDsgnt> [0..1] Text 1949
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1895 May 2026
```

## File page 1896

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         OwnerIdentification <OwnrId> [0..*] ± 1949
         AccountServicer <AcctSvcr> [0..1] ± 1950
         OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 1950
         SubAccountDetails <SubAcctDtls> [0..1] ± 1950
         BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1951
       HoldingsRedemptionRate <HldgsRedRate> [0..1] Rate 1951
       GrossAmount <GrssAmt> [0..1] Amount C3, C10 1951
       TradeDateTime <TradDtTm> [1..1] ± 1952
       SettlementAmount <SttlmAmt> [1..1] Amount C3, C10 1952
       CashSettlementDate <CshSttlmDt> [0..1] Date 1952
       SettlementMethod <SttlmMtd> [0..1] CodeSet 1952
       DealingPriceDetails <DealgPricDtls> [1..1] ± 1953
       InformativePriceDetails <InftvPricDtls> [0..2] ± 1953
       PartiallyExecutedIndicator <PrtlyExctdInd> [1..1] Indicator 1954
       BestExecution <BestExctn> [0..1] CodeSet 1954
       CumDividendIndicator <CumDvddInd> [1..1] Indicator 1954
       InterimProfitAmount <IntrmPrftAmt> [0..1] ± 1955
       ForeignExchangeDetails <FXDtls> [0..*] ± 1955
       IncomePreference <IncmPref> [0..1] CodeSet 1956
       Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 1956
       TransactionOverhead <TxOvrhd> [0..1]  C23,
C39
1956
         TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C3, C10 1958
         TotalFees <TtlFees> [0..1] Amount C3, C10 1959
         TotalTaxes <TtlTaxs> [0..1] Amount C3, C10 1959
         CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 1959
         IndividualFee <IndvFee> [0..*]  C6 1960
           Type <Tp> [1..1]  1960
{Or             Code <Cd> [1..1] CodeSet 1961
Or}             Proprietary <Prtry> [1..1] ± 1962
           Basis <Bsis> [0..1]  1962
{Or             Code <Cd> [1..1] CodeSet 1962
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1896 May 2026
```

## File page 1897

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}             Proprietary <Prtry> [1..1] ± 1963
           StandardAmount <StdAmt> [0..1] Amount C3, C10 1963
           StandardRate <StdRate> [0..1] Rate 1963
           DiscountDetails <DscntDtls> [0..1]  C17 1964
             Amount <Amt> [0..1] Amount C3, C10 1964
             Rate <Rate> [0..1] Rate 1965
             Basis <Bsis> [0..1]  1965
{Or               Code <Cd> [1..1] CodeSet 1965
Or}               Proprietary <Prtry> [1..1] ± 1965
           AppliedAmount <ApldAmt> [0..1] Amount C3, C10 1966
           AppliedRate <ApldRate> [0..1] Rate 1966
           NonStandardSLAReference <NonStdSLARef> [0..1] Text 1966
           RecipientIdentification <RcptId> [0..1] ± 1966
           InformativeIndicator <InftvInd> [1..1] Indicator 1967
         IndividualTax <IndvTax> [0..*] ± 1967
         DigitalNetworkFee <DgtlNtwkFee> [0..*]  1967
           FinancialInstrumentIdentification <FinInstrmId> [1..1]  C14,
C15,
C21,
C22,
C28
1968
             ISIN <ISIN> [0..1] IdentifierSet 1970
             OtherIdentification <OthrId> [0..*]  1970
               Identification <Id> [1..1] Text 1970
               Suffix <Sfx> [0..1] Text 1970
               Type <Tp> [1..1]  1970
{Or                 Code <Cd> [1..1] CodeSet 1971
Or}                 Proprietary <Prtry> [1..1] Text 1972
             Description <Desc> [0..1] Text 1972
           Quantity <Qty> [1..1]  1973
{Or             Quantity <Qty> [1..1] ± C16 1973
Or}             ProprietaryQuantity <PrtryQty> [1..1]  1973
               Quantity <Qty> [1..1] Quantity 1974
               QuantityType <QtyTp> [1..1] Text 1974
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1897 May 2026
```

## File page 1898

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               Issuer <Issr> [1..1] Text 1974
               SchemeName <SchmeNm> [0..1] Text 1974
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1974
       InformativeTaxDetails <InftvTaxDtls> [0..1] ± C38 1974
       StaffClientBreakdown <StffClntBrkdwn> [0..4] ± 1976
       SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  1976
         SettlementDate <SttlmDt> [0..1] Date 1978
         SettlementPlace <SttlmPlc> [1..1]  1978
           Party <Pty> [1..1]  1979
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1979
Or             ProprietaryIdentification <PrtryId> [1..1] ± 1979
Or             NameAndAddress <NmAndAdr> [1..1] ± 1980
Or}             DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1980
           LEI <LEI> [0..1] IdentifierSet 1980
         SafekeepingPlace <SfkpgPlc> [0..1] ± 1980
         SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 1981
         TradeTransactionCondition <TradTxCond> [0..*] ± 1981
         SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1981
         ReceivingSideDetails <RcvgSdDtls> [1..1]  C33,
C34
1982
           ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  1983
             PartyIdentification <PtyId> [1..1] ± 1983
             AccountIdentification <AcctId> [0..1] Text 1983
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1983
           ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  1984
             PartyIdentification <PtyId> [1..1] ± 1984
             AccountIdentification <AcctId> [0..1] Text 1984
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1984
           ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  1985
             PartyIdentification <PtyId> [1..1] ± 1985
             AccountIdentification <AcctId> [0..1] Text 1985
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1985
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1898 May 2026
```

## File page 1899

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           ReceivingAgentDetails <RcvgAgtDtls> [1..1]  1986
             PartyIdentification <PtyId> [1..1] ± 1986
             AccountIdentification <AcctId> [0..1] Text 1986
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1986
         DeliveringSideDetails <DlvrgSdDtls> [0..1]  C12,
C13
1987
           DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  1988
             PartyIdentification <PtyId> [1..1] ± 1988
             AccountIdentification <AcctId> [0..1] Text 1988
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1989
           DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  1989
             PartyIdentification <PtyId> [1..1] ± 1989
             AccountIdentification <AcctId> [0..1] Text 1989
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1989
           DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  1990
             PartyIdentification <PtyId> [1..1] ± 1990
             AccountIdentification <AcctId> [0..1] Text 1990
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1990
           DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  1991
             PartyIdentification <PtyId> [1..1] ± 1991
             AccountIdentification <AcctId> [0..1] Text 1991
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1991
       PhysicalDeliveryIndicator <PhysDlvryInd> [1..1] Indicator 1992
       PhysicalDeliveryDetails <PhysDlvryDtls> [0..1] ± 1992
       CashSettlementDetails <CshSttlmDtls> [0..1]  1992
         PaymentInstrument <PmtInstrm> [1..1]  1996
{Or           CreditTransferDetails <CdtTrfDtls> [1..1]  2000
             Reference <Ref> [0..1] Text 2003
             Debtor <Dbtr> [0..1] ± 2003
             DebtorAccount <DbtrAcct> [0..1]  2003
               Identification <Id> [1..1]  2003
{Or                 IBAN <IBAN> [1..1] IdentifierSet C19 2004
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1899 May 2026
```

## File page 1900

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2004
Or}                 Other <Othr> [1..1] ± 2004
               Name <Nm> [0..1] Text 2005
             DebtorAgent <DbtrAgt> [0..1]  2005
               Party <Pty> [1..1]  2005
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2006
Or                 BICFI <BICFI> [1..1] IdentifierSet C7 2006
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2006
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2007
               LEI <LEI> [0..1] IdentifierSet 2007
             DebtorAgentAccount <DbtrAgtAcct> [0..1]  2008
               Identification <Id> [1..1]  2008
{Or                 IBAN <IBAN> [1..1] IdentifierSet C19 2008
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2009
Or}                 Other <Othr> [1..1] ± 2009
               Name <Nm> [0..1] Text 2009
             IntermediaryAgent1 <IntrmyAgt1> [0..1]  2009
               Party <Pty> [1..1]  2010
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2010
Or                 BICFI <BICFI> [1..1] IdentifierSet C7 2010
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2011
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2012
               LEI <LEI> [0..1] IdentifierSet 2012
             IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2013
               Identification <Id> [1..1]  2013
{Or                 IBAN <IBAN> [1..1] IdentifierSet C19 2013
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2014
Or}                 Other <Othr> [1..1] ± 2014
               Name <Nm> [0..1] Text 2014
             IntermediaryAgent2 <IntrmyAgt2> [0..1]  2014
               Party <Pty> [1..1]  2015
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1900 May 2026
```

## File page 1901

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2015
Or                 BICFI <BICFI> [1..1] IdentifierSet C7 2015
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2016
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2017
               LEI <LEI> [0..1] IdentifierSet 2017
             IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2018
               Identification <Id> [1..1]  2018
{Or                 IBAN <IBAN> [1..1] IdentifierSet C19 2018
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2019
Or}                 Other <Othr> [1..1] ± 2019
               Name <Nm> [0..1] Text 2019
             CreditorAgent <CdtrAgt> [1..1]  2019
               Party <Pty> [1..1]  2020
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2020
Or                 BICFI <BICFI> [1..1] IdentifierSet C7 2020
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2021
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2022
               LEI <LEI> [0..1] IdentifierSet 2022
             CreditorAgentAccount <CdtrAgtAcct> [0..1]  2023
               Identification <Id> [1..1]  2023
{Or                 IBAN <IBAN> [1..1] IdentifierSet C19 2023
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2024
Or}                 Other <Othr> [1..1] ± 2024
               Name <Nm> [0..1] Text 2024
             Creditor <Cdtr> [0..1] ± 2024
             CreditorAccount <CdtrAcct> [1..1]  2025
               Identification <Id> [1..1]  2025
{Or                 IBAN <IBAN> [1..1] IdentifierSet C19 2025
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2026
Or}                 Other <Othr> [1..1] ± 2026
               Name <Nm> [0..1] Text 2026
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1901 May 2026
```

## File page 1902

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or           ChequeDetails <ChqDtls> [1..1]  2026
             Number <Nb> [0..1] Text 2027
             PayeeIdentification <PyeeId> [1..1] ± 2027
             DraweeIdentification <DrweeId> [0..1]  2027
               Party <Pty> [1..1]  2028
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2028
Or                 BICFI <BICFI> [1..1] IdentifierSet C7 2028
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2029
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2030
               LEI <LEI> [0..1] IdentifierSet 2030
             DrawerIdentification <DrwrId> [0..1] ± 2031
Or           BankersDraftDetails <BkrsDrftDtls> [1..1]  2031
             Number <Nb> [0..1] Text 2031
             PayeeIdentification <PyeeId> [1..1] ± 2031
             DraweeIdentification <DrweeId> [0..1]  2032
               Party <Pty> [1..1]  2032
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2032
Or                 BICFI <BICFI> [1..1] IdentifierSet C7 2033
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2033
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2034
               LEI <LEI> [0..1] IdentifierSet 2034
             DrawerIdentification <DrwrId> [0..1] ± 2035
Or           CashAccountDetails <CshAcctDtls> [1..1]  C1 2035
             AccountIdentification <AcctId> [0..1] Text 2035
             Type <Tp> [0..1] ± 2035
Or}           BlockChainCashWallet <BlckChainCshWllt> [1..1]  2036
             Identification <Id> [1..1] Text 2036
             Type <Tp> [0..1] ± 2036
             Name <Nm> [0..1] Text 2036
             DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2037
       DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  2037
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1902 May 2026
```

## File page 1903

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         FinancialInstrumentIdentification <FinInstrmId> [1..1]  C14,
C15,
C21,
C22,
C28
2037
           ISIN <ISIN> [0..1] IdentifierSet 2039
           OtherIdentification <OthrId> [0..*]  2039
             Identification <Id> [1..1] Text 2039
             Suffix <Sfx> [0..1] Text 2039
             Type <Tp> [1..1]  2039
{Or               Code <Cd> [1..1] CodeSet 2040
Or}               Proprietary <Prtry> [1..1] Text 2041
           Description <Desc> [0..1] Text 2041
         Quantity <Qty> [1..1]  2042
{Or           Quantity <Qty> [1..1] ± C16 2042
Or}           ProprietaryQuantity <PrtryQty> [1..1]  2042
             Quantity <Qty> [1..1] Quantity 2043
             QuantityType <QtyTp> [1..1] Text 2043
             Issuer <Issr> [1..1] Text 2043
             SchemeName <SchmeNm> [0..1] Text 2043
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2043
       NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 2043
       PartialSettlementOfUnits <PrtlSttlmOfUnits> [0..1] Rate 2043
       PartialSettlementOfCash <PrtlSttlmOfCsh> [0..1] Rate 2044
       PartialRedemptionWithholdingAmount <PrtlRedWhldgAmt> [0..1] Amount C3, C10 2044
       FinancialAdvice <FinAdvc> [0..1] CodeSet 2044
       NegotiatedTrade <NgtdTrad> [0..1] CodeSet 2044
       LateReport <LateRpt> [0..1] CodeSet 2045
       RelatedPartyDetails <RltdPtyDtls> [0..10] ± C24 2045
       Equalisation <Equlstn> [0..1] ± 2045
       CustomerConductClassification <CstmrCndctClssfctn> [0..1] ± 2046
       TransactionChannelType <TxChanlTp> [0..1] ± 2046
       SignatureType <SgntrTp> [0..1] ± 2046
       OrderWaiverDetails <OrdrWvrDtls> [0..1] ± C40 2046
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1903 May 2026
```

