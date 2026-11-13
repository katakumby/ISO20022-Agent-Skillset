---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>"]
file_pages: [141, 142, 143, 144, 145]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4 TradeLegsDetails <TradLegsDtls>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 141 to 145.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 141

```text
NonClearingMember <NonClrMmb> contains the following elements (see
PartyIdentificationAndAccount227 on page 457 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 457
   AlternateIdentification <AltrnId> [0..1] ± 457
   AdditionalInformation <AddtlInf> [0..1] ± C3 457
   ClearingAccount <ClrAcct> [0..1] ± 458
4.4.5.4  TradeLegsDetails <TradLegsDtls>
Presence: [1..*]
Definition: Provides the lists of all trades during the period in consideration for the statement.
Impacted by:   'C10 DepositoryOrPlaceOfListingPresenceRule  ',   'C20
TradeIdentificationPresenceRule  '
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 141
```

## File page 142

```text
TradeLegsDetails <TradLegsDtls> contains the following TradeLeg15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarginAccount <MrgnAcct> [0..1] ± 146
   DeliveryAccount <DlvryAcct> [0..1] ± 146
   TradeLegIdentification <TradLegId> [1..1] Text 147
   TradeIdentification <TradId> [0..1] Text 147
   TradeExecutionIdentification <TradExctnId> [0..1] Text 147
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 147
   OrderIdentification <OrdrId> [0..1] Text 147
   AllocationIdentification <AllcnId> [0..1] Text 147
   NonClearingMember <NonClrMmb> [0..1] ± 148
   TradeDate <TradDt> [1..1] ± 148
   TransactionDateAndTime <TxDtAndTm> [0..1] DateTime 148
   SettlementDate <SttlmDt> [0..1]  148
{Or     Date <Dt> [1..1] Date 149
Or}     DateCode <DtCd> [1..1]  149
{Or       Code <Cd> [1..1] CodeSet 149
Or}       Proprietary <Prtry> [1..1] ± 149
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ±   'C11,
C12,
C13,
  'C14,
  'C17
149
   TradingCurrency <TradgCcy> [0..1] CodeSet C21 151
   BuySellIndicator <BuySellInd> [1..1] CodeSet 151
   TradeQuantity <TradQty> [1..1] ± 153
   DealPrice <DealPric> [1..1] ± 153
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 153
   PlaceOfTrade <PlcOfTrad> [1..1] ± C15 153
   PlaceOfListing <PlcOfListg> [0..1]  C16 154
     Identification <Id> [0..1] ± 154
     Type <Tp> [1..1] ± 155
   TradeType <TradTp> [1..1] CodeSet 155
   TradeTransactionCondition <TradTxCond> [0..*] ± 155
   DerivativeRelatedTrade <DerivRltdTrad> [0..1] Indicator 156
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 142
```

## File page 143

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Broker <Brkr> [0..1]  156
     Identification <Id> [1..1]  156
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet   'C4 157
Or       ProprietaryIdentification <PrtryId> [1..1] ± 157
Or}       NameAndAddress <NmAndAdr> [1..1]  158
         Name <Nm> [1..1] Text 158
         Address <Adr> [0..1]  158
           AddressType <AdrTp> [0..1] CodeSet 159
           AddressLine <AdrLine> [0..5] Text 159
           StreetName <StrtNm> [0..1] Text 159
           BuildingNumber <BldgNb> [0..1] Text 159
           PostCode <PstCd> [0..1] Text 160
           TownName <TwnNm> [0..1] Text 160
           CountrySubDivision <CtrySubDvsn> [0..1] Text 160
           Country <Ctry> [1..1] CodeSet   'C5 160
     AlternateIdentification <AltrnId> [0..1] ± 160
     SafekeepingAccount <SfkpgAcct> [0..1] Text 161
     ProcessingIdentification <PrcgId> [0..1] Text 161
     AdditionalInformation <AddtlInf> [0..1] ± C3 161
   TradingParty <TradgPty> [1..1] ± 161
   TradeRegistrationOrigin <TradRegnOrgn> [0..1] Text 162
   TradingPartyAccount <TradgPtyAcct> [0..1] ± 162
   TradingCapacity <TradgCpcty> [1..1] CodeSet 162
   TradePostingCode <TradPstngCd> [0..1] CodeSet 162
   SafekeepingPlace <SfkpgPlc> [0..1]  163
{Or     Identification <Id> [1..1]  163
       SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 163
       Identification <Id> [0..1] Text 164
Or     Country <Ctry> [1..1] CodeSet   'C5 164
Or     TypeAndIdentification <TpAndId> [1..1]  164
       SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 164
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 143
```

## File page 144

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Identification <Id> [1..1] IdentifierSet   'C4 165
Or}     Proprietary <Prtry> [1..1]  165
       Identification <Id> [0..1] Text 166
       Type <Tp> [1..1] ± 166
   SafekeepingAccount <SfkpgAcct> [0..1] ± 166
   SettlementDetails <SttlmDtls> [0..1]  166
     SettlementAmount <SttlmAmt> [1..1] ± 166
     Depository <Dpstry> [0..1] ± 167
   ClearingDetails <ClrDtls> [0..1]  167
     SettlementNettingEligibleCode <SttlmNetgElgblCd> [1..1] CodeSet 169
     ClearingSegment <ClrSgmt> [0..1] ± 170
     GuaranteedTrade <GrntedTrad> [0..1] Indicator 170
     TradeCounterpartyIdentification <TradCtrPtyId> [0..1]  170
       TradeCounterpartyMemberIdentification
<TradCtrPtyMmbId>
[1..1] ± 172
       TradeCounterpartyClearingMemberIdentification
<TradCtrPtyClrMmbId>
[1..1] ± 172
       DeliveringParties <DlvrgPties> [0..1]  C8 173
         Depository <Dpstry> [1..1] ± 174
         Party1 <Pty1> [1..1]  175
           PartyIdentification <PtyId> [1..1] ± 175
           AccountIdentification <AcctId> [0..1] Text 176
           ProcessingIdentification <PrcgId> [0..1] Text 176
           ProcessingDate <PrcgDt> [0..1] ± 176
           SubAccount <SubAcct> [0..1]  176
             Identification <Id> [1..1] ± 177
             Name <Nm> [0..1] Text 177
             Characteristic <Chrtc> [0..1] Text 177
           ContactPerson <CtctPrsn> [0..1] ± 177
         Party2 <Pty2> [0..1]  178
           PartyIdentification <PtyId> [1..1] ± 178
           AccountIdentification <AcctId> [0..1] Text 179
           ProcessingIdentification <PrcgId> [0..1] Text 179
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 144
```

## File page 145

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           ProcessingDate <PrcgDt> [0..1] ± 179
           SubAccount <SubAcct> [0..1]  179
             Identification <Id> [1..1] ± 180
             Name <Nm> [0..1] Text 180
             Characteristic <Chrtc> [0..1] Text 180
           ContactPerson <CtctPrsn> [0..1] ± 180
         SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 181
       ReceivingParties <RcvgPties> [0..1]  C9 181
         Depository <Dpstry> [1..1] ± 182
         Party1 <Pty1> [1..1]  183
           PartyIdentification <PtyId> [1..1] ± 183
           AccountIdentification <AcctId> [0..1] Text 184
           ProcessingIdentification <PrcgId> [0..1] Text 184
           ProcessingDate <PrcgDt> [0..1] ± 184
           SubAccount <SubAcct> [0..1]  184
             Identification <Id> [1..1] ± 185
             Name <Nm> [0..1] Text 185
             Characteristic <Chrtc> [0..1] Text 185
           ContactPerson <CtctPrsn> [0..1] ± 185
         Party2 <Pty2> [0..1]  186
           PartyIdentification <PtyId> [1..1] ± 186
           AccountIdentification <AcctId> [0..1] Text 187
           ProcessingIdentification <PrcgId> [0..1] Text 187
           ProcessingDate <PrcgDt> [0..1] ± 187
           SubAccount <SubAcct> [0..1]  187
             Identification <Id> [1..1] ± 188
             Name <Nm> [0..1] Text 188
             Characteristic <Chrtc> [0..1] Text 188
           ContactPerson <CtctPrsn> [0..1] ± 188
         SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 189
   GrossAmount <GrssAmt> [0..1] ± 189
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 145
```

