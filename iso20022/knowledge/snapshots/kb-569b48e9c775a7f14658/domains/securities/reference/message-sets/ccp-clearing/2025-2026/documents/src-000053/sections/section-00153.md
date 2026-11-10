---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>"]
file_pages: [201, 202, 203, 204]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5 NetPositionReport <NetPosRpt>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 201 to 204.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 201

```text
Definition: Clearing organisation that will clear the trade.
Note: This field allows Clearing Member Firm to segregate flows coming from clearing counterparty's
clearing system. Indeed, Clearing Member Firms receive messages from the same system (same
sender) and this field allows them to know if the message is related to equities or derivatives.
ClearingSegment <ClrSgmt> contains one of the following elements (see
PartyIdentification253Choice on page 453 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C3 453
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 453
5.4.5 NetPositionReport <NetPosRpt>
Presence: [1..*]
Definition: Provides the net position details such as the average deal price and net quantity.
Impacted by:   'C6 DepositoryOrPlaceOfListingPresenceRule  '
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 201
```

## File page 202

```text
NetPositionReport <NetPosRpt> contains the following NetPosition4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingAccount <ClrAcct> [1..1] ± 205
   NonClearingMember <NonClrMmb> [0..1] ± 205
   DeliveryAccount <DlvryAcct> [0..1] ± 205
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ±   'C7,
C8, C9,
  'C10,
  'C14
206
   InitialPositionAmount <InitlPosAmt> [0..1] ± 207
   NetPositionAmount <NetPosAmt> [1..1] ± 207
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 208
   AverageDealPrice <AvrgDealPric> [0..1] ± 208
   NetQuantity <NetQty> [1..1] ± 208
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 209
   Depository <Dpstry> [1..1] ± 209
   TradingCapacity <TradgCpcty> [0..1] CodeSet 209
   PlaceOfTrade <PlcOfTrad> [0..1] ± C11 209
   TradeDate <TradDt> [0..1] Date 210
   SettlementDate <SttlmDt> [0..1]  210
{Or     Date <Dt> [1..1] Date 210
Or}     DateCode <DtCd> [1..1]  210
{Or       Code <Cd> [1..1] CodeSet 211
Or}       Proprietary <Prtry> [1..1] ± 211
   TradeLegDetails <TradLegDtls> [0..*]    'C17 211
     TradeLegIdentification <TradLegId> [1..1] Text 214
     TradeIdentification <TradId> [0..1] Text 214
     TradeExecutionIdentification <TradExctnId> [0..1] Text 214
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 214
     OrderIdentification <OrdrId> [0..1] Text 214
     AllocationIdentification <AllcnId> [0..1] Text 215
     TradeDate <TradDt> [1..1] Date 215
     TransactionDateAndTime <TxDtAndTm> [0..1] DateTime 215
     SettlementDate <SttlmDt> [1..1]  215
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 202
```

## File page 203

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       Date <Dt> [1..1] Date 215
Or}       DateCode <DtCd> [1..1]  215
{Or         Code <Cd> [1..1] CodeSet 216
Or}         Proprietary <Prtry> [1..1] ± 216
     TradingCurrency <TradgCcy> [0..1] CodeSet C18 216
     BuySellIndicator <BuySellInd> [1..1] CodeSet 216
     TradeQuantity <TradQty> [1..1] ± 218
     DealPrice <DealPric> [1..1] ± 218
     GrossAmount <GrssAmt> [0..1] ± 218
     PlaceOfTrade <PlcOfTrad> [1..1] ± C12 219
     PlaceOfListing <PlcOfListg> [0..1]  C13 219
       Identification <Id> [0..1] ± 220
       Type <Tp> [1..1] ± 220
     TradeType <TradTp> [1..1] CodeSet 220
     DerivativeRelatedTrade <DerivRltdTrad> [0..1] Indicator 221
     Broker <Brkr> [0..1]  221
       Identification <Id> [1..1]  221
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet   'C3 222
Or         ProprietaryIdentification <PrtryId> [1..1] ± 222
Or}         NameAndAddress <NmAndAdr> [1..1]  223
           Name <Nm> [1..1] Text 223
           Address <Adr> [0..1]  223
             AddressType <AdrTp> [0..1] CodeSet 224
             AddressLine <AdrLine> [0..5] Text 224
             StreetName <StrtNm> [0..1] Text 224
             BuildingNumber <BldgNb> [0..1] Text 224
             PostCode <PstCd> [0..1] Text 225
             TownName <TwnNm> [0..1] Text 225
             CountrySubDivision <CtrySubDvsn> [0..1] Text 225
             Country <Ctry> [1..1] CodeSet   'C4 225
       AlternateIdentification <AltrnId> [0..1] ± 225
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 203
```

## File page 204

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       SafekeepingAccount <SfkpgAcct> [0..1] Text 226
       ProcessingIdentification <PrcgId> [0..1] Text 226
       AdditionalInformation <AddtlInf> [0..1] ± C2 226
     TradingParty <TradgPty> [1..1] ± 226
     TradeRegistrationOrigin <TradRegnOrgn> [0..1] Text 227
     TradingPartyAccount <TradgPtyAcct> [0..1] ± 227
     TradingCapacity <TradgCpcty> [1..1] CodeSet 227
     TradePostingCode <TradPstngCd> [0..1] CodeSet 227
     SafekeepingPlace <SfkpgPlc> [0..1]  228
{Or       Identification <Id> [1..1]  228
         SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 228
         Identification <Id> [0..1] Text 229
Or       Country <Ctry> [1..1] CodeSet   'C4 229
Or       TypeAndIdentification <TpAndId> [1..1]  229
         SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 229
         Identification <Id> [1..1] IdentifierSet   'C3 230
Or}       Proprietary <Prtry> [1..1]  230
         Identification <Id> [0..1] Text 230
         Type <Tp> [1..1] ± 231
     SafekeepingAccount <SfkpgAcct> [0..1] ± 231
Constraints
• DepositoryOrPlaceOfListingPresenceRule
(Rule)
At least Depository or PlaceOfListing must be present.
Following Must be True
    /Depository Must be present
 Or    /TradeLegDetails[*]/PlaceOfListing Must be present
Error handling:
– Error severity: Fatal
– Error Code: X00200
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 204
```

