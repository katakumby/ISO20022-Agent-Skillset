---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks", "3.4.5 ClearingDetails <ClrDtls>", "3.4.5.4 TradeCounterpartyIdentification <TradCtrPtyId>", "3.4.5.4.4 ReceivingParties <RcvgPties>", "3.4.5.4.4.4 SecuritiesSettlementSystem <SctiesSttlmSys>"]
file_pages: [97, 98, 99]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.4.5.4.4.4 SecuritiesSettlementSystem <SctiesSttlmSys>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 97 to 99.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 97

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
3.4.5.4.4.4  SecuritiesSettlementSystem <SctiesSttlmSys>
Presence: [0..1]
Definition: Identifies the securities settlement system to be used.
Datatype: Max35Text on page 493
3.4.6 TradeLegDetails <TradLegDtls>
Presence: [1..1]
Definition: Provides details about the trade leg such as the trade date, the settlement date or the trading
currency.
Impacted by:   'C19 TradeIdentificationPresenceRule  '
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 97
```

## File page 98

```text
TradeLegDetails <TradLegDtls> contains the following TradeLeg14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeLegIdentification <TradLegId> [1..1] Text 100
   TradeIdentification <TradId> [0..1] Text 100
   TradeExecutionIdentification <TradExctnId> [0..1] Text 100
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 100
   OrderIdentification <OrdrId> [0..1] Text 101
   AllocationIdentification <AllcnId> [0..1] Text 101
   Status <Sts> [0..1] CodeSet 101
   TradeDate <TradDt> [1..1] ± 101
   TransactionDateTime <TxDtTm> [0..1] DateTime 101
   SettlementDate <SttlmDt> [0..1]  102
{Or     Date <Dt> [1..1] Date 102
Or}     DateCode <DtCd> [1..1]  102
{Or       Code <Cd> [1..1] CodeSet 102
Or}       Proprietary <Prtry> [1..1] ± 102
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ±   'C11,
C12,
C13,
  'C14,
  'C17
103
   TradingCurrency <TradgCcy> [0..1] CodeSet C20 104
   BuySellIndicator <BuySellInd> [1..1] CodeSet 105
   TradeQuantity <TradQty> [1..1] ± 106
   DealPrice <DealPric> [1..1] ± 106
   GrossAmount <GrssAmt> [0..1] ± 106
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 107
   PlaceOfTrade <PlcOfTrad> [1..1] ± C15 107
   PlaceOfListing <PlcOfListg> [0..1]  C16 107
     Identification <Id> [0..1] ± 108
     Type <Tp> [1..1] ± 108
   TradeType <TradTp> [1..1] CodeSet 108
   TradeTransactionCondition <TradTxCond> [0..*] ± 109
   DerivativeRelatedTrade <DerivRltdTrad> [0..1] Indicator 109
   Broker <Brkr> [0..1]  109
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 98
```

## File page 99

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Identification <Id> [1..1]  110
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet   'C4 111
Or       ProprietaryIdentification <PrtryId> [1..1] ± 111
Or}       NameAndAddress <NmAndAdr> [1..1]  112
         Name <Nm> [1..1] Text 112
         Address <Adr> [0..1]  112
           AddressType <AdrTp> [0..1] CodeSet 113
           AddressLine <AdrLine> [0..5] Text 113
           StreetName <StrtNm> [0..1] Text 113
           BuildingNumber <BldgNb> [0..1] Text 113
           PostCode <PstCd> [0..1] Text 114
           TownName <TwnNm> [0..1] Text 114
           CountrySubDivision <CtrySubDvsn> [0..1] Text 114
           Country <Ctry> [1..1] CodeSet   'C5 114
     AlternateIdentification <AltrnId> [0..1] ± 114
     SafekeepingAccount <SfkpgAcct> [0..1] Text 115
     ProcessingIdentification <PrcgId> [0..1] Text 115
     AdditionalInformation <AddtlInf> [0..1] ± C3 115
   TradingParty <TradgPty> [1..1] ± 115
   TradeRegistrationOrigin <TradRegnOrgn> [0..1] Text 116
   TradingPartyAccount <TradgPtyAcct> [0..1] ± 116
   TradingCapacity <TradgCpcty> [1..1] CodeSet 116
   TradePostingCode <TradPstngCd> [0..1] CodeSet 116
   SafekeepingPlace <SfkpgPlc> [0..1]  117
{Or     Identification <Id> [1..1]  117
       SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 117
       Identification <Id> [0..1] Text 118
Or     Country <Ctry> [1..1] CodeSet   'C5 118
Or     TypeAndIdentification <TpAndId> [1..1]  118
       SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 118
       Identification <Id> [1..1] IdentifierSet   'C4 119
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 99
```

