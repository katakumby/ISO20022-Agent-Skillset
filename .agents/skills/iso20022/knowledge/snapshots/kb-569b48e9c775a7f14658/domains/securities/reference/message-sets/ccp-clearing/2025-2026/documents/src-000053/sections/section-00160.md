---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.15 SettlementDate <SttlmDt>", "5.4.5.15.2 DateCode <DtCd>", "5.4.5.15.2.1 Code <Cd>"]
file_pages: [211, 212, 213]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.15.2.1 Code <Cd>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 211 to 213.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 211

```text
DateCode <DtCd> contains one of the following DateCode20Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 211
Or}   Proprietary <Prtry> [1..1] ± 211
5.4.5.15.2.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to indicate the date is unknown.
Datatype: DateType1Code on page 476
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
5.4.5.15.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of date.
Proprietary <Prtry> contains the following elements (see GenericIdentification30 on page 400 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 400
   Issuer <Issr> [1..1] Text 401
   SchemeName <SchmeNm> [0..1] Text 401
5.4.5.16  TradeLegDetails <TradLegDtls>
Presence: [0..*]
Definition: Provides the trade leg details such as trade leg identification and trade type.
Impacted by:   'C17 TradeIdentificationPresenceRule  '
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 211
```

## File page 212

```text
TradeLegDetails <TradLegDtls> contains the following TradeLeg13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeLegIdentification <TradLegId> [1..1] Text 214
   TradeIdentification <TradId> [0..1] Text 214
   TradeExecutionIdentification <TradExctnId> [0..1] Text 214
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 214
   OrderIdentification <OrdrId> [0..1] Text 214
   AllocationIdentification <AllcnId> [0..1] Text 215
   TradeDate <TradDt> [1..1] Date 215
   TransactionDateAndTime <TxDtAndTm> [0..1] DateTime 215
   SettlementDate <SttlmDt> [1..1]  215
{Or     Date <Dt> [1..1] Date 215
Or}     DateCode <DtCd> [1..1]  215
{Or       Code <Cd> [1..1] CodeSet 216
Or}       Proprietary <Prtry> [1..1] ± 216
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
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet   'C3 222
Or       ProprietaryIdentification <PrtryId> [1..1] ± 222
Or}       NameAndAddress <NmAndAdr> [1..1]  223
         Name <Nm> [1..1] Text 223
         Address <Adr> [0..1]  223
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 212
```

## File page 213

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           AddressType <AdrTp> [0..1] CodeSet 224
           AddressLine <AdrLine> [0..5] Text 224
           StreetName <StrtNm> [0..1] Text 224
           BuildingNumber <BldgNb> [0..1] Text 224
           PostCode <PstCd> [0..1] Text 225
           TownName <TwnNm> [0..1] Text 225
           CountrySubDivision <CtrySubDvsn> [0..1] Text 225
           Country <Ctry> [1..1] CodeSet   'C4 225
     AlternateIdentification <AltrnId> [0..1] ± 225
     SafekeepingAccount <SfkpgAcct> [0..1] Text 226
     ProcessingIdentification <PrcgId> [0..1] Text 226
     AdditionalInformation <AddtlInf> [0..1] ± C2 226
   TradingParty <TradgPty> [1..1] ± 226
   TradeRegistrationOrigin <TradRegnOrgn> [0..1] Text 227
   TradingPartyAccount <TradgPtyAcct> [0..1] ± 227
   TradingCapacity <TradgCpcty> [1..1] CodeSet 227
   TradePostingCode <TradPstngCd> [0..1] CodeSet 227
   SafekeepingPlace <SfkpgPlc> [0..1]  228
{Or     Identification <Id> [1..1]  228
       SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 228
       Identification <Id> [0..1] Text 229
Or     Country <Ctry> [1..1] CodeSet   'C4 229
Or     TypeAndIdentification <TpAndId> [1..1]  229
       SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 229
       Identification <Id> [1..1] IdentifierSet   'C3 230
Or}     Proprietary <Prtry> [1..1]  230
       Identification <Id> [0..1] Text 230
       Type <Tp> [1..1] ± 231
   SafekeepingAccount <SfkpgAcct> [0..1] ± 231
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 213
```

