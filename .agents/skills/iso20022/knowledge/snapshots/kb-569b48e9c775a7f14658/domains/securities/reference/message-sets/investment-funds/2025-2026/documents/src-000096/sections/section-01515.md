---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.2 Structure"]
file_pages: [2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2102 to 2111.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2102

```text
44.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <RedOrdr> [1..1]  C2
   MessageIdentification <MsgId> [1..1] ± 2118
   PoolReference <PoolRef> [0..1] ± 2119
   PreviousReference <PrvsRef> [0..*] ± 2119
   MultipleOrderDetails <MltplOrdrDtls> [1..1]  C7, C26,
C35,
C38
0
     MasterReference <MstrRef> [0..1] Text 2133
     PlaceOfTrade <PlcOfTrad> [0..1] ± 2133
     OrderDateTime <OrdrDtTm> [0..1] DateTime 2134
     ExpiryDateTime <XpryDtTm> [0..1] ± 2134
     RequestedFutureTradeDate <ReqdFutrTradDt> [0..1] Date 2134
     CancellationRight <CxlRght> [0..1] ± 2134
     InvestmentAccountDetails <InvstmtAcctDtls> [1..1]  C25 2135
       AccountIdentification <AcctId> [1..1] Text 2135
       AccountName <AcctNm> [0..1] Text 2135
       AccountDesignation <AcctDsgnt> [0..1] Text 2136
       OwnerIdentification <OwnrId> [0..*] ± 2136
       AccountServicer <AcctSvcr> [0..1] ± 2136
       OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 2136
       SubAccountDetails <SubAcctDtls> [0..1] ± 2137
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2137
     BeneficiaryDetails <BnfcryDtls> [0..*] ± C28 2137
     IndividualOrderDetails <IndvOrdrDtls> [1..*]  C29,
C30,
C33
2138
       OrderReference <OrdrRef> [1..1] Text 2149
       ClientReference <ClntRef> [0..1] Text 2149
       NonceIdentification <NonceId> [0..1] Text 2149
       OrderType <OrdrTp> [0..10] ± 2149
       FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C21 2149
         Identification <Id> [1..1]  2151
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2102 May 2026
```

## File page 2103

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or           ISIN <ISIN> [1..1] IdentifierSet 2151
Or           SEDOL <SEDOL> [1..1] IdentifierSet 2152
Or           CUSIP <CUSIP> [1..1] IdentifierSet 2152
Or           RIC <RIC> [1..1] IdentifierSet 2152
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 2152
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 2152
Or           CTA <CTA> [1..1] IdentifierSet 2152
Or           QUICK <QUICK> [1..1] IdentifierSet 2152
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 2153
Or           Dutch <Dtch> [1..1] IdentifierSet 2153
Or           Valoren <Vlrn> [1..1] IdentifierSet 2153
Or           Sicovam <SCVM> [1..1] IdentifierSet 2153
Or           Belgian <Belgn> [1..1] IdentifierSet 2153
Or           Common <Cmon> [1..1] IdentifierSet 2153
Or           DTI <DTI> [1..1] IdentifierSet 2153
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  2153
             Identification <Id> [1..1] Text 2154
             IdentificationSource <IdSrc> [1..1] ± 2154
         Name <Nm> [0..1] Text 2154
         ShortName <ShrtNm> [0..1] Text 2154
         SupplementaryIdentification <SplmtryId> [0..1] Text 2154
         ClassType <ClssTp> [0..1] Text 2154
         SecuritiesForm <SctiesForm> [0..1] CodeSet 2155
         DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 2155
         ProductGroup <PdctGrp> [0..1] Text 2155
         SeriesIdentification <SrsId> [0..1]  C34 2155
           SeriesDate <SrsDt> [0..1] ± 2156
           SeriesName <SrsNm> [0..1] Text 2156
       SubAccountForHolding <SubAcctForHldg> [0..1] ± 2156
       AmountOrUnitsOrPercentage <AmtOrUnitsOrPctg> [1..1]  2156
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 2157
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2103 May 2026
```

## File page 2104

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         GrossAmount <GrssAmt> [1..1] Amount C4, C9 2157
Or         NetAmount <NetAmt> [1..1] Amount C4, C9 2157
Or         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 2158
Or}         HoldingsRedemptionRate <HldgsRedRate> [1..1] Rate 2158
       Rounding <Rndg> [0..1] CodeSet 2158
       SettlementAmount <SttlmAmt> [0..1] Amount C3, C10 2158
       CashSettlementDate <CshSttlmDt> [0..1] Date 2159
       SettlementMethod <SttlmMtd> [0..1] CodeSet 2159
       ForeignExchangeDetails <FXDtls> [0..1]  2159
         UnitCurrency <UnitCcy> [1..1] CodeSet C3 2160
         QuotedCurrency <QtdCcy> [1..1] CodeSet C3 2160
         ExchangeRate <XchgRate> [1..1] Rate 2160
         QuotationDate <QtnDt> [0..1] DateTime 2161
         QuotingInstitution <QtgInstn> [0..1] ± 2161
       IncomePreference <IncmPref> [0..1] CodeSet 2161
       Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 2161
       TransactionOverhead <TxOvrhd> [0..1]  C19 2162
         CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 2165
         IndividualFee <IndvFee> [0..*]  C18,
C36,
C37
2165
           Type <Tp> [1..1]  2166
{Or             Code <Cd> [1..1] CodeSet 2166
Or}             Proprietary <Prtry> [1..1] ± 2167
           Basis <Bsis> [0..1]  2167
{Or             Code <Cd> [1..1] CodeSet 2168
Or}             Proprietary <Prtry> [1..1] ± 2168
           StandardAmount <StdAmt> [0..1] Amount C3, C10 2168
           StandardRate <StdRate> [0..1] Rate 2169
           DiscountDetails <DscntDtls> [0..1]  C16 2169
             Amount <Amt> [0..1] Amount C3, C10 2169
             Rate <Rate> [0..1] Rate 2170
             Basis <Bsis> [0..1]  2170
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2104 May 2026
```

## File page 2105

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or               Code <Cd> [1..1] CodeSet 2170
Or}               Proprietary <Prtry> [1..1] ± 2171
           RequestedAmount <ReqdAmt> [0..1] Amount C3, C10 2171
           RequestedRate <ReqdRate> [0..1] Rate 2171
           NonStandardSLAReference <NonStdSLARef> [0..1] Text 2172
           RecipientIdentification <RcptId> [0..1] ± 2172
         IndividualTax <IndvTax> [0..*]  2172
           Type <Tp> [1..1]  2173
{Or             Code <Cd> [1..1] CodeSet 2173
Or}             Proprietary <Prtry> [1..1] ± 2175
           Tax <Tax> [0..1]  2175
{Or             Amount <Amt> [1..1] Amount C3, C10 2175
Or}             Rate <Rate> [1..1] Rate 2176
           Country <Ctry> [0..1] CodeSet C8 2176
           ExemptionIndicator <XmptnInd> [1..1] Indicator 2176
           ExemptionReason <XmptnRsn> [0..1]  2176
{Or             Code <Cd> [1..1] CodeSet 2176
Or}             Proprietary <Prtry> [1..1] ± 2179
           RecipientIdentification <RcptId> [0..1] ± 2179
           TaxCalculationDetails <TaxClctnDtls> [0..1]  2180
             Basis <Bsis> [1..1]  2180
{Or               Code <Cd> [1..1] CodeSet 2180
Or}               Proprietary <Prtry> [1..1] ± 2180
         DigitalNetworkFee <DgtlNtwkFee> [0..*]  2181
           FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
C23,
C27
2181
             ISIN <ISIN> [0..1] IdentifierSet 2183
             OtherIdentification <OthrId> [0..*]  2183
               Identification <Id> [1..1] Text 2183
               Suffix <Sfx> [0..1] Text 2183
               Type <Tp> [1..1]  2183
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2105 May 2026
```

## File page 2106

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or                 Code <Cd> [1..1] CodeSet 2184
Or}                 Proprietary <Prtry> [1..1] Text 2185
             Description <Desc> [0..1] Text 2185
           Quantity <Qty> [1..1]  2186
{Or             Quantity <Qty> [1..1] ± C15 2186
Or}             ProprietaryQuantity <PrtryQty> [1..1]  2186
               Quantity <Qty> [1..1] Quantity 2187
               QuantityType <QtyTp> [1..1] Text 2187
               Issuer <Issr> [1..1] Text 2187
               SchemeName <SchmeNm> [0..1] Text 2187
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2187
       SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  2187
         SettlementDate <SttlmDt> [0..1] Date 2189
         SettlementPlace <SttlmPlc> [1..1]  2189
           Party <Pty> [1..1]  2190
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C5 2190
Or             ProprietaryIdentification <PrtryId> [1..1] ± 2190
Or             NameAndAddress <NmAndAdr> [1..1] ± 2191
Or}             DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2191
           LEI <LEI> [0..1] IdentifierSet 2191
         SafekeepingPlace <SfkpgPlc> [0..1] ± 2191
         SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 2192
         TradeTransactionCondition <TradTxCond> [0..*] ± 2192
         SettlementTransactionCondition <SttlmTxCond> [0..*] ± 2192
         ReceivingSideDetails <RcvgSdDtls> [0..1]  C31,
C32
2193
           ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  2194
             PartyIdentification <PtyId> [1..1] ± 2194
             AccountIdentification <AcctId> [0..1] Text 2194
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2194
           ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  2195
             PartyIdentification <PtyId> [1..1] ± 2195
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2106 May 2026
```

## File page 2107

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             AccountIdentification <AcctId> [0..1] Text 2195
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2195
           ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  2196
             PartyIdentification <PtyId> [1..1] ± 2196
             AccountIdentification <AcctId> [0..1] Text 2196
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2196
           ReceivingAgentDetails <RcvgAgtDtls> [1..1]  2197
             PartyIdentification <PtyId> [1..1] ± 2197
             AccountIdentification <AcctId> [0..1] Text 2197
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2197
         DeliveringSideDetails <DlvrgSdDtls> [1..1]  C11,
C12
2198
           DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  2199
             PartyIdentification <PtyId> [1..1] ± 2199
             AccountIdentification <AcctId> [0..1] Text 2199
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2200
           DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  2200
             PartyIdentification <PtyId> [1..1] ± 2200
             AccountIdentification <AcctId> [0..1] Text 2200
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2200
           DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  2201
             PartyIdentification <PtyId> [1..1] ± 2201
             AccountIdentification <AcctId> [0..1] Text 2201
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2201
           DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  2202
             PartyIdentification <PtyId> [1..1] ± 2202
             AccountIdentification <AcctId> [0..1] Text 2202
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2202
       PhysicalDeliveryIndicator <PhysDlvryInd> [1..1] Indicator 2203
       PhysicalDeliveryDetails <PhysDlvryDtls> [0..1] ± 2203
       RequestedSettlementCurrency <ReqdSttlmCcy> [0..1] CodeSet C3 2203
       RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C4 2203
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2107 May 2026
```

## File page 2108

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       CashSettlementDetails <CshSttlmDtls> [0..1]  2204
         PaymentInstrument <PmtInstrm> [1..1]  2208
{Or           CreditTransferDetails <CdtTrfDtls> [1..1]  2212
             Reference <Ref> [0..1] Text 2215
             Debtor <Dbtr> [0..1] ± 2215
             DebtorAccount <DbtrAcct> [0..1]  2215
               Identification <Id> [1..1]  2215
{Or                 IBAN <IBAN> [1..1] IdentifierSet C20 2216
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2216
Or}                 Other <Othr> [1..1] ± 2216
               Name <Nm> [0..1] Text 2217
             DebtorAgent <DbtrAgt> [0..1]  2217
               Party <Pty> [1..1]  2217
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2218
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 2218
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2218
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2219
               LEI <LEI> [0..1] IdentifierSet 2219
             DebtorAgentAccount <DbtrAgtAcct> [0..1]  2220
               Identification <Id> [1..1]  2220
{Or                 IBAN <IBAN> [1..1] IdentifierSet C20 2220
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2221
Or}                 Other <Othr> [1..1] ± 2221
               Name <Nm> [0..1] Text 2221
             IntermediaryAgent1 <IntrmyAgt1> [0..1]  2221
               Party <Pty> [1..1]  2222
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2222
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 2222
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2223
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2224
               LEI <LEI> [0..1] IdentifierSet 2224
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2108 May 2026
```

## File page 2109

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2225
               Identification <Id> [1..1]  2225
{Or                 IBAN <IBAN> [1..1] IdentifierSet C20 2225
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2226
Or}                 Other <Othr> [1..1] ± 2226
               Name <Nm> [0..1] Text 2226
             IntermediaryAgent2 <IntrmyAgt2> [0..1]  2226
               Party <Pty> [1..1]  2227
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2227
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 2227
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2228
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2229
               LEI <LEI> [0..1] IdentifierSet 2229
             IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2230
               Identification <Id> [1..1]  2230
{Or                 IBAN <IBAN> [1..1] IdentifierSet C20 2230
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2231
Or}                 Other <Othr> [1..1] ± 2231
               Name <Nm> [0..1] Text 2231
             CreditorAgent <CdtrAgt> [1..1]  2231
               Party <Pty> [1..1]  2232
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2232
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 2232
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2233
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2234
               LEI <LEI> [0..1] IdentifierSet 2234
             CreditorAgentAccount <CdtrAgtAcct> [0..1]  2235
               Identification <Id> [1..1]  2235
{Or                 IBAN <IBAN> [1..1] IdentifierSet C20 2235
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2236
Or}                 Other <Othr> [1..1] ± 2236
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2109 May 2026
```

## File page 2110

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               Name <Nm> [0..1] Text 2236
             Creditor <Cdtr> [0..1] ± 2236
             CreditorAccount <CdtrAcct> [1..1]  2237
               Identification <Id> [1..1]  2237
{Or                 IBAN <IBAN> [1..1] IdentifierSet C20 2237
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2238
Or}                 Other <Othr> [1..1] ± 2238
               Name <Nm> [0..1] Text 2238
Or           ChequeDetails <ChqDtls> [1..1]  2238
             Number <Nb> [0..1] Text 2239
             PayeeIdentification <PyeeId> [1..1] ± 2239
             DraweeIdentification <DrweeId> [0..1]  2239
               Party <Pty> [1..1]  2240
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2240
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 2240
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2241
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2242
               LEI <LEI> [0..1] IdentifierSet 2242
             DrawerIdentification <DrwrId> [0..1] ± 2243
Or           BankersDraftDetails <BkrsDrftDtls> [1..1]  2243
             Number <Nb> [0..1] Text 2243
             PayeeIdentification <PyeeId> [1..1] ± 2243
             DraweeIdentification <DrweeId> [0..1]  2244
               Party <Pty> [1..1]  2244
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2244
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 2245
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2245
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2246
               LEI <LEI> [0..1] IdentifierSet 2246
             DrawerIdentification <DrwrId> [0..1] ± 2247
Or           CashAccountDetails <CshAcctDtls> [1..1]  C1 2247
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2110 May 2026
```

## File page 2111

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             AccountIdentification <AcctId> [0..1] Text 2247
             Type <Tp> [0..1] ± 2247
Or}           BlockChainCashWallet <BlckChainCshWllt> [1..1]  2248
             Identification <Id> [1..1] Text 2248
             Type <Tp> [0..1] ± 2248
             Name <Nm> [0..1] Text 2248
             DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2249
       DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  2249
         FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
C23,
C27
2249
           ISIN <ISIN> [0..1] IdentifierSet 2251
           OtherIdentification <OthrId> [0..*]  2251
             Identification <Id> [1..1] Text 2251
             Suffix <Sfx> [0..1] Text 2251
             Type <Tp> [1..1]  2251
{Or               Code <Cd> [1..1] CodeSet 2252
Or}               Proprietary <Prtry> [1..1] Text 2253
           Description <Desc> [0..1] Text 2253
         Quantity <Qty> [1..1]  2254
{Or           Quantity <Qty> [1..1] ± C15 2254
Or}           ProprietaryQuantity <PrtryQty> [1..1]  2254
             Quantity <Qty> [1..1] Quantity 2255
             QuantityType <QtyTp> [1..1] Text 2255
             Issuer <Issr> [1..1] Text 2255
             SchemeName <SchmeNm> [0..1] Text 2255
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2255
       NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 2255
       StaffClientBreakdown <StffClntBrkdwn> [0..4] ± 2255
       FinancialAdvice <FinAdvc> [0..1] CodeSet 2256
       NegotiatedTrade <NgtdTrad> [0..1] CodeSet 2256
       RelatedPartyDetails <RltdPtyDtls> [0..10] ± C24 2256
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2111 May 2026
```

