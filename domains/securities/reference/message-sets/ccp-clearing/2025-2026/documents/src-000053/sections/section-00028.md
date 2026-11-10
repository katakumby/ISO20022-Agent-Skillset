---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.5 ClearingDetails <ClrDtls>", "2.4.5.4 TradeCounterpartyIdentification <TradCtrPtyId>", "2.4.5.4.4 ReceivingParties <RcvgPties>", "2.4.5.4.4.4 SecuritiesSettlementSystem <SctiesSttlmSys>"]
file_pages: [39, 40, 41]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.5.4.4.4 SecuritiesSettlementSystem <SctiesSttlmSys>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 39 to 41.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 39

```text
ContactPerson <CtctPrsn> contains the following elements (see ContactIdentification2 on page 458
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 459
   GivenName <GvnNm> [0..1] Text 459
   Name <Nm> [1..1] Text 459
   PhoneNumber <PhneNb> [0..1] Text 459
   MobileNumber <MobNb> [0..1] Text 459
   FaxNumber <FaxNb> [0..1] Text 459
   EmailAddress <EmailAdr> [0..1] Text 459
2.4.5.4.4.4  SecuritiesSettlementSystem <SctiesSttlmSys>
Presence: [0..1]
Definition: Identifies the securities settlement system to be used.
Datatype: Max35Text on page 493
2.4.6 TradeLegDetails <TradLegDtls>
Presence: [1..1]
Definition: Provides details about the trade leg such as the trade date, the settlement date or the trading
currency.
Impacted by:   'C19 TradeIdentificationPresenceRule  '
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 39
```

## File page 40

```text
TradeLegDetails <TradLegDtls> contains the following TradeLeg14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeLegIdentification <TradLegId> [1..1] Text 42
   TradeIdentification <TradId> [0..1] Text 42
   TradeExecutionIdentification <TradExctnId> [0..1] Text 42
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 42
   OrderIdentification <OrdrId> [0..1] Text 43
   AllocationIdentification <AllcnId> [0..1] Text 43
   Status <Sts> [0..1] CodeSet 43
   TradeDate <TradDt> [1..1] ± 43
   TransactionDateTime <TxDtTm> [0..1] DateTime 43
   SettlementDate <SttlmDt> [0..1]  44
{Or     Date <Dt> [1..1] Date 44
Or}     DateCode <DtCd> [1..1]  44
{Or       Code <Cd> [1..1] CodeSet 44
Or}       Proprietary <Prtry> [1..1] ± 44
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ±   'C11,
C12,
C13,
  'C14,
  'C17
45
   TradingCurrency <TradgCcy> [0..1] CodeSet C20 46
   BuySellIndicator <BuySellInd> [1..1] CodeSet 47
   TradeQuantity <TradQty> [1..1] ± 48
   DealPrice <DealPric> [1..1] ± 48
   GrossAmount <GrssAmt> [0..1] ± 48
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 49
   PlaceOfTrade <PlcOfTrad> [1..1] ± C15 49
   PlaceOfListing <PlcOfListg> [0..1]  C16 49
     Identification <Id> [0..1] ± 50
     Type <Tp> [1..1] ± 50
   TradeType <TradTp> [1..1] CodeSet 50
   TradeTransactionCondition <TradTxCond> [0..*] ± 51
   DerivativeRelatedTrade <DerivRltdTrad> [0..1] Indicator 51
   Broker <Brkr> [0..1]  51
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 40
```

## File page 41

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Identification <Id> [1..1]  52
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet   'C4 53
Or       ProprietaryIdentification <PrtryId> [1..1] ± 53
Or}       NameAndAddress <NmAndAdr> [1..1]  54
         Name <Nm> [1..1] Text 54
         Address <Adr> [0..1]  54
           AddressType <AdrTp> [0..1] CodeSet 55
           AddressLine <AdrLine> [0..5] Text 55
           StreetName <StrtNm> [0..1] Text 55
           BuildingNumber <BldgNb> [0..1] Text 55
           PostCode <PstCd> [0..1] Text 56
           TownName <TwnNm> [0..1] Text 56
           CountrySubDivision <CtrySubDvsn> [0..1] Text 56
           Country <Ctry> [1..1] CodeSet   'C5 56
     AlternateIdentification <AltrnId> [0..1] ± 56
     SafekeepingAccount <SfkpgAcct> [0..1] Text 57
     ProcessingIdentification <PrcgId> [0..1] Text 57
     AdditionalInformation <AddtlInf> [0..1] ± C3 57
   TradingParty <TradgPty> [1..1] ± 57
   TradeRegistrationOrigin <TradRegnOrgn> [0..1] Text 58
   TradingPartyAccount <TradgPtyAcct> [0..1] ± 58
   TradingCapacity <TradgCpcty> [1..1] CodeSet 58
   TradePostingCode <TradPstngCd> [0..1] CodeSet 58
   SafekeepingPlace <SfkpgPlc> [0..1]  59
{Or     Identification <Id> [1..1]  59
       SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 59
       Identification <Id> [0..1] Text 60
Or     Country <Ctry> [1..1] CodeSet   'C5 60
Or     TypeAndIdentification <TpAndId> [1..1]  60
       SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 60
       Identification <Id> [1..1] IdentifierSet   'C4 61
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 41
```

