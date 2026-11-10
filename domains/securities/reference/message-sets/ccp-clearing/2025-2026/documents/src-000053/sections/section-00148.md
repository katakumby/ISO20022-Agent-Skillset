---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.2 Structure"]
file_pages: [192, 193, 194]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.2 Structure

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 192 to 194.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 192

```text
5.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <NetPos> [1..1]  
   ReportParameters <RptParams> [1..1]  C15 198
     NetPositionIdentification <NetPosId> [1..1] Text 199
     ReportDateAndTime <RptDtAndTm> [1..1] ± 199
     UpdateType <UpdTp> [1..1] CodeSet 199
     Frequency <Frqcy> [1..1] CodeSet 199
     ReportNumber <RptNb> [0..1] Text 200
     ActivityIndicator <ActvtyInd> [1..1] Indicator 200
   Pagination <Pgntn> [1..1] ± 200
   ClearingMember <ClrMmb> [1..1] ± 200
   ClearingSegment <ClrSgmt> [0..1] ± 200
   NetPositionReport <NetPosRpt> [1..*]    'C6 201
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
{Or       Date <Dt> [1..1] Date 210
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 192
```

## File page 193

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}       DateCode <DtCd> [1..1]  210
{Or         Code <Cd> [1..1] CodeSet 211
Or}         Proprietary <Prtry> [1..1] ± 211
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
{Or         Date <Dt> [1..1] Date 215
Or}         DateCode <DtCd> [1..1]  215
{Or           Code <Cd> [1..1] CodeSet 216
Or}           Proprietary <Prtry> [1..1] ± 216
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
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet   'C3 222
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 193
```

## File page 194

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or           ProprietaryIdentification <PrtryId> [1..1] ± 222
Or}           NameAndAddress <NmAndAdr> [1..1]  223
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
         SafekeepingAccount <SfkpgAcct> [0..1] Text 226
         ProcessingIdentification <PrcgId> [0..1] Text 226
         AdditionalInformation <AddtlInf> [0..1] ± C2 226
       TradingParty <TradgPty> [1..1] ± 226
       TradeRegistrationOrigin <TradRegnOrgn> [0..1] Text 227
       TradingPartyAccount <TradgPtyAcct> [0..1] ± 227
       TradingCapacity <TradgCpcty> [1..1] CodeSet 227
       TradePostingCode <TradPstngCd> [0..1] CodeSet 227
       SafekeepingPlace <SfkpgPlc> [0..1]  228
{Or         Identification <Id> [1..1]  228
           SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 228
           Identification <Id> [0..1] Text 229
Or         Country <Ctry> [1..1] CodeSet   'C4 229
Or         TypeAndIdentification <TpAndId> [1..1]  229
           SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 229
           Identification <Id> [1..1] IdentifierSet   'C3 230
Or}         Proprietary <Prtry> [1..1]  230
           Identification <Id> [0..1] Text 230
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 194
```

