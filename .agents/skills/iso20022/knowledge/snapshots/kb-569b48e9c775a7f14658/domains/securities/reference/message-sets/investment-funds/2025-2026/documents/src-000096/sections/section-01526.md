---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>"]
file_pages: [2138, 2139, 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2138 to 2147.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2138

```text
BeneficiaryDetails <BnfcryDtls> contains the following elements (see "IndividualPerson32" on
page 5075 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 5076
   BirthDate <BirthDt> [0..1] Date 5076
   CountryAndResidentialStatus <CtryAndResdtlSts> [0..1] ± 5076
   OtherIdentification <OthrId> [0..*]  5076
     Identification <Id> [1..1] Text 5077
     IdentificationType <IdTp> [1..1]  5077
{Or       Code <Cd> [1..1] CodeSet 5077
Or}       Proprietary <Prtry> [1..1] ± 5078
     Issuer <Issr> [0..1] Text 5078
Constraints
• PersonElementRule
One of the elements (Name, BirthDate, CountryAndResidentialStatus, OtherIdentification) must be
present.
44.4.4.9  IndividualOrderDetails <IndvOrdrDtls>
Presence: [1..*]
Definition: Instruction from an investor to sell investment fund units back to the fund.
Impacted by: C29 "PhysicalDeliveryDetails1Rule", C30 "PhysicalDeliveryDetails2Rule", C33
"RequestedSettlementCurrencyRule"
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2138 May 2026
```

## File page 2139

```text
IndividualOrderDetails <IndvOrdrDtls> contains the following RedemptionOrder18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderReference <OrdrRef> [1..1] Text 2149
   ClientReference <ClntRef> [0..1] Text 2149
   NonceIdentification <NonceId> [0..1] Text 2149
   OrderType <OrdrTp> [0..10] ± 2149
   FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C21 2149
     Identification <Id> [1..1]  2151
{Or       ISIN <ISIN> [1..1] IdentifierSet 2151
Or       SEDOL <SEDOL> [1..1] IdentifierSet 2152
Or       CUSIP <CUSIP> [1..1] IdentifierSet 2152
Or       RIC <RIC> [1..1] IdentifierSet 2152
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 2152
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 2152
Or       CTA <CTA> [1..1] IdentifierSet 2152
Or       QUICK <QUICK> [1..1] IdentifierSet 2152
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 2153
Or       Dutch <Dtch> [1..1] IdentifierSet 2153
Or       Valoren <Vlrn> [1..1] IdentifierSet 2153
Or       Sicovam <SCVM> [1..1] IdentifierSet 2153
Or       Belgian <Belgn> [1..1] IdentifierSet 2153
Or       Common <Cmon> [1..1] IdentifierSet 2153
Or       DTI <DTI> [1..1] IdentifierSet 2153
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  2153
         Identification <Id> [1..1] Text 2154
         IdentificationSource <IdSrc> [1..1] ± 2154
     Name <Nm> [0..1] Text 2154
     ShortName <ShrtNm> [0..1] Text 2154
     SupplementaryIdentification <SplmtryId> [0..1] Text 2154
     ClassType <ClssTp> [0..1] Text 2154
     SecuritiesForm <SctiesForm> [0..1] CodeSet 2155
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 2155
     ProductGroup <PdctGrp> [0..1] Text 2155
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2139 May 2026
```

## File page 2140

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     SeriesIdentification <SrsId> [0..1]  C34 2155
       SeriesDate <SrsDt> [0..1] ± 2156
       SeriesName <SrsNm> [0..1] Text 2156
   SubAccountForHolding <SubAcctForHldg> [0..1] ± 2156
   AmountOrUnitsOrPercentage <AmtOrUnitsOrPctg> [1..1]  2156
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 2157
Or     GrossAmount <GrssAmt> [1..1] Amount C4, C9 2157
Or     NetAmount <NetAmt> [1..1] Amount C4, C9 2157
Or     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 2158
Or}     HoldingsRedemptionRate <HldgsRedRate> [1..1] Rate 2158
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
{Or         Code <Cd> [1..1] CodeSet 2166
Or}         Proprietary <Prtry> [1..1] ± 2167
       Basis <Bsis> [0..1]  2167
{Or         Code <Cd> [1..1] CodeSet 2168
Or}         Proprietary <Prtry> [1..1] ± 2168
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2140 May 2026
```

## File page 2141

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       StandardAmount <StdAmt> [0..1] Amount C3, C10 2168
       StandardRate <StdRate> [0..1] Rate 2169
       DiscountDetails <DscntDtls> [0..1]  C16 2169
         Amount <Amt> [0..1] Amount C3, C10 2169
         Rate <Rate> [0..1] Rate 2170
         Basis <Bsis> [0..1]  2170
{Or           Code <Cd> [1..1] CodeSet 2170
Or}           Proprietary <Prtry> [1..1] ± 2171
       RequestedAmount <ReqdAmt> [0..1] Amount C3, C10 2171
       RequestedRate <ReqdRate> [0..1] Rate 2171
       NonStandardSLAReference <NonStdSLARef> [0..1] Text 2172
       RecipientIdentification <RcptId> [0..1] ± 2172
     IndividualTax <IndvTax> [0..*]  2172
       Type <Tp> [1..1]  2173
{Or         Code <Cd> [1..1] CodeSet 2173
Or}         Proprietary <Prtry> [1..1] ± 2175
       Tax <Tax> [0..1]  2175
{Or         Amount <Amt> [1..1] Amount C3, C10 2175
Or}         Rate <Rate> [1..1] Rate 2176
       Country <Ctry> [0..1] CodeSet C8 2176
       ExemptionIndicator <XmptnInd> [1..1] Indicator 2176
       ExemptionReason <XmptnRsn> [0..1]  2176
{Or         Code <Cd> [1..1] CodeSet 2176
Or}         Proprietary <Prtry> [1..1] ± 2179
       RecipientIdentification <RcptId> [0..1] ± 2179
       TaxCalculationDetails <TaxClctnDtls> [0..1]  2180
         Basis <Bsis> [1..1]  2180
{Or           Code <Cd> [1..1] CodeSet 2180
Or}           Proprietary <Prtry> [1..1] ± 2180
     DigitalNetworkFee <DgtlNtwkFee> [0..*]  2181
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
2181
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2141 May 2026
```

## File page 2142

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
C23,
C27
         ISIN <ISIN> [0..1] IdentifierSet 2183
         OtherIdentification <OthrId> [0..*]  2183
           Identification <Id> [1..1] Text 2183
           Suffix <Sfx> [0..1] Text 2183
           Type <Tp> [1..1]  2183
{Or             Code <Cd> [1..1] CodeSet 2184
Or}             Proprietary <Prtry> [1..1] Text 2185
         Description <Desc> [0..1] Text 2185
       Quantity <Qty> [1..1]  2186
{Or         Quantity <Qty> [1..1] ± C15 2186
Or}         ProprietaryQuantity <PrtryQty> [1..1]  2186
           Quantity <Qty> [1..1] Quantity 2187
           QuantityType <QtyTp> [1..1] Text 2187
           Issuer <Issr> [1..1] Text 2187
           SchemeName <SchmeNm> [0..1] Text 2187
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2187
   SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  2187
     SettlementDate <SttlmDt> [0..1] Date 2189
     SettlementPlace <SttlmPlc> [1..1]  2189
       Party <Pty> [1..1]  2190
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C5 2190
Or         ProprietaryIdentification <PrtryId> [1..1] ± 2190
Or         NameAndAddress <NmAndAdr> [1..1] ± 2191
Or}         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2191
       LEI <LEI> [0..1] IdentifierSet 2191
     SafekeepingPlace <SfkpgPlc> [0..1] ± 2191
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 2192
     TradeTransactionCondition <TradTxCond> [0..*] ± 2192
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 2192
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2142 May 2026
```

## File page 2143

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     ReceivingSideDetails <RcvgSdDtls> [0..1]  C31,
C32
2193
       ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  2194
         PartyIdentification <PtyId> [1..1] ± 2194
         AccountIdentification <AcctId> [0..1] Text 2194
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2194
       ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  2195
         PartyIdentification <PtyId> [1..1] ± 2195
         AccountIdentification <AcctId> [0..1] Text 2195
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2195
       ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  2196
         PartyIdentification <PtyId> [1..1] ± 2196
         AccountIdentification <AcctId> [0..1] Text 2196
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2196
       ReceivingAgentDetails <RcvgAgtDtls> [1..1]  2197
         PartyIdentification <PtyId> [1..1] ± 2197
         AccountIdentification <AcctId> [0..1] Text 2197
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2197
     DeliveringSideDetails <DlvrgSdDtls> [1..1]  C11,
C12
2198
       DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  2199
         PartyIdentification <PtyId> [1..1] ± 2199
         AccountIdentification <AcctId> [0..1] Text 2199
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2200
       DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  2200
         PartyIdentification <PtyId> [1..1] ± 2200
         AccountIdentification <AcctId> [0..1] Text 2200
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2200
       DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  2201
         PartyIdentification <PtyId> [1..1] ± 2201
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2143 May 2026
```

## File page 2144

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         AccountIdentification <AcctId> [0..1] Text 2201
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2201
       DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  2202
         PartyIdentification <PtyId> [1..1] ± 2202
         AccountIdentification <AcctId> [0..1] Text 2202
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2202
   PhysicalDeliveryIndicator <PhysDlvryInd> [1..1] Indicator 2203
   PhysicalDeliveryDetails <PhysDlvryDtls> [0..1] ± 2203
   RequestedSettlementCurrency <ReqdSttlmCcy> [0..1] CodeSet C3 2203
   RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C4 2203
   CashSettlementDetails <CshSttlmDtls> [0..1]  2204
     PaymentInstrument <PmtInstrm> [1..1]  2208
{Or       CreditTransferDetails <CdtTrfDtls> [1..1]  2212
         Reference <Ref> [0..1] Text 2215
         Debtor <Dbtr> [0..1] ± 2215
         DebtorAccount <DbtrAcct> [0..1]  2215
           Identification <Id> [1..1]  2215
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 2216
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2216
Or}             Other <Othr> [1..1] ± 2216
           Name <Nm> [0..1] Text 2217
         DebtorAgent <DbtrAgt> [0..1]  2217
           Party <Pty> [1..1]  2217
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2218
Or             BICFI <BICFI> [1..1] IdentifierSet C6 2218
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2218
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2219
           LEI <LEI> [0..1] IdentifierSet 2219
         DebtorAgentAccount <DbtrAgtAcct> [0..1]  2220
           Identification <Id> [1..1]  2220
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2144 May 2026
```

## File page 2145

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 2220
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2221
Or}             Other <Othr> [1..1] ± 2221
           Name <Nm> [0..1] Text 2221
         IntermediaryAgent1 <IntrmyAgt1> [0..1]  2221
           Party <Pty> [1..1]  2222
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2222
Or             BICFI <BICFI> [1..1] IdentifierSet C6 2222
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2223
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2224
           LEI <LEI> [0..1] IdentifierSet 2224
         IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2225
           Identification <Id> [1..1]  2225
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 2225
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2226
Or}             Other <Othr> [1..1] ± 2226
           Name <Nm> [0..1] Text 2226
         IntermediaryAgent2 <IntrmyAgt2> [0..1]  2226
           Party <Pty> [1..1]  2227
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2227
Or             BICFI <BICFI> [1..1] IdentifierSet C6 2227
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2228
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2229
           LEI <LEI> [0..1] IdentifierSet 2229
         IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2230
           Identification <Id> [1..1]  2230
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 2230
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2231
Or}             Other <Othr> [1..1] ± 2231
           Name <Nm> [0..1] Text 2231
         CreditorAgent <CdtrAgt> [1..1]  2231
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2145 May 2026
```

## File page 2146

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Party <Pty> [1..1]  2232
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2232
Or             BICFI <BICFI> [1..1] IdentifierSet C6 2232
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2233
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2234
           LEI <LEI> [0..1] IdentifierSet 2234
         CreditorAgentAccount <CdtrAgtAcct> [0..1]  2235
           Identification <Id> [1..1]  2235
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 2235
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2236
Or}             Other <Othr> [1..1] ± 2236
           Name <Nm> [0..1] Text 2236
         Creditor <Cdtr> [0..1] ± 2236
         CreditorAccount <CdtrAcct> [1..1]  2237
           Identification <Id> [1..1]  2237
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 2237
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2238
Or}             Other <Othr> [1..1] ± 2238
           Name <Nm> [0..1] Text 2238
Or       ChequeDetails <ChqDtls> [1..1]  2238
         Number <Nb> [0..1] Text 2239
         PayeeIdentification <PyeeId> [1..1] ± 2239
         DraweeIdentification <DrweeId> [0..1]  2239
           Party <Pty> [1..1]  2240
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2240
Or             BICFI <BICFI> [1..1] IdentifierSet C6 2240
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2241
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2242
           LEI <LEI> [0..1] IdentifierSet 2242
         DrawerIdentification <DrwrId> [0..1] ± 2243
Or       BankersDraftDetails <BkrsDrftDtls> [1..1]  2243
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2146 May 2026
```

## File page 2147

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Number <Nb> [0..1] Text 2243
         PayeeIdentification <PyeeId> [1..1] ± 2243
         DraweeIdentification <DrweeId> [0..1]  2244
           Party <Pty> [1..1]  2244
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2244
Or             BICFI <BICFI> [1..1] IdentifierSet C6 2245
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2245
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2246
           LEI <LEI> [0..1] IdentifierSet 2246
         DrawerIdentification <DrwrId> [0..1] ± 2247
Or       CashAccountDetails <CshAcctDtls> [1..1]  C1 2247
         AccountIdentification <AcctId> [0..1] Text 2247
         Type <Tp> [0..1] ± 2247
Or}       BlockChainCashWallet <BlckChainCshWllt> [1..1]  2248
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
{Or           Code <Cd> [1..1] CodeSet 2252
Or}           Proprietary <Prtry> [1..1] Text 2253
       Description <Desc> [0..1] Text 2253
     Quantity <Qty> [1..1]  2254
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2147 May 2026
```

