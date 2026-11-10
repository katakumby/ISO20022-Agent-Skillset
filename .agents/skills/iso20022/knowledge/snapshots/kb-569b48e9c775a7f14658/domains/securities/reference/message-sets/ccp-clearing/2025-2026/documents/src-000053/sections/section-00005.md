---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.2 Structure"]
file_pages: [8, 9, 10, 11]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.2 Structure

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 8 to 11.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 8

```text
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <TradLegNtfctn> [1..1]    'C10
   ClearingMember <ClrMmb> [1..1] ± 16
   ClearingAccount <ClrAcct> [1..1] ± 16
   DeliveryAccount <DlvryAcct> [0..1] ± 16
   NonClearingMember <NonClrMmb> [0..1] ± 17
   ClearingDetails <ClrDtls> [0..1]  17
     SettlementNettingEligibleCode <SttlmNetgElgblCd> [1..1] CodeSet 19
     ClearingSegment <ClrSgmt> [0..1] ± 20
     GuaranteedTrade <GrntedTrad> [0..1] Indicator 20
     TradeCounterpartyIdentification <TradCtrPtyId> [0..1]  20
       TradeCounterpartyMemberIdentification
<TradCtrPtyMmbId>
[1..1] ± 22
       TradeCounterpartyClearingMemberIdentification
<TradCtrPtyClrMmbId>
[1..1] ± 22
       DeliveringParties <DlvrgPties> [0..1]  C8 23
         Depository <Dpstry> [1..1] ± 24
         Party1 <Pty1> [1..1]  25
           PartyIdentification <PtyId> [1..1] ± 25
           AccountIdentification <AcctId> [0..1] Text 26
           ProcessingIdentification <PrcgId> [0..1] Text 26
           ProcessingDate <PrcgDt> [0..1] ± 26
           SubAccount <SubAcct> [0..1]  26
             Identification <Id> [1..1] ± 27
             Name <Nm> [0..1] Text 27
             Characteristic <Chrtc> [0..1] Text 27
           ContactPerson <CtctPrsn> [0..1] ± 27
         Party2 <Pty2> [0..1]  28
           PartyIdentification <PtyId> [1..1] ± 28
           AccountIdentification <AcctId> [0..1] Text 29
           ProcessingIdentification <PrcgId> [0..1] Text 29
           ProcessingDate <PrcgDt> [0..1] ± 29
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 8
```

## File page 9

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           SubAccount <SubAcct> [0..1]  29
             Identification <Id> [1..1] ± 30
             Name <Nm> [0..1] Text 30
             Characteristic <Chrtc> [0..1] Text 30
           ContactPerson <CtctPrsn> [0..1] ± 30
         SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 31
       ReceivingParties <RcvgPties> [0..1]  C9 31
         Depository <Dpstry> [1..1] ± 32
         Party1 <Pty1> [1..1]  33
           PartyIdentification <PtyId> [1..1] ± 33
           AccountIdentification <AcctId> [0..1] Text 34
           ProcessingIdentification <PrcgId> [0..1] Text 34
           ProcessingDate <PrcgDt> [0..1] ± 34
           SubAccount <SubAcct> [0..1]  34
             Identification <Id> [1..1] ± 35
             Name <Nm> [0..1] Text 35
             Characteristic <Chrtc> [0..1] Text 35
           ContactPerson <CtctPrsn> [0..1] ± 35
         Party2 <Pty2> [0..1]  36
           PartyIdentification <PtyId> [1..1] ± 36
           AccountIdentification <AcctId> [0..1] Text 37
           ProcessingIdentification <PrcgId> [0..1] Text 37
           ProcessingDate <PrcgDt> [0..1] ± 37
           SubAccount <SubAcct> [0..1]  37
             Identification <Id> [1..1] ± 38
             Name <Nm> [0..1] Text 38
             Characteristic <Chrtc> [0..1] Text 38
           ContactPerson <CtctPrsn> [0..1] ± 38
         SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 39
   TradeLegDetails <TradLegDtls> [1..1]    'C19 39
     TradeLegIdentification <TradLegId> [1..1] Text 42
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 9
```

## File page 10

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     TradeIdentification <TradId> [0..1] Text 42
     TradeExecutionIdentification <TradExctnId> [0..1] Text 42
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 42
     OrderIdentification <OrdrId> [0..1] Text 43
     AllocationIdentification <AllcnId> [0..1] Text 43
     Status <Sts> [0..1] CodeSet 43
     TradeDate <TradDt> [1..1] ± 43
     TransactionDateTime <TxDtTm> [0..1] DateTime 43
     SettlementDate <SttlmDt> [0..1]  44
{Or       Date <Dt> [1..1] Date 44
Or}       DateCode <DtCd> [1..1]  44
{Or         Code <Cd> [1..1] CodeSet 44
Or}         Proprietary <Prtry> [1..1] ± 44
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
       Identification <Id> [1..1]  52
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet   'C4 53
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 10
```

## File page 11

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         ProprietaryIdentification <PrtryId> [1..1] ± 53
Or}         NameAndAddress <NmAndAdr> [1..1]  54
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
{Or       Identification <Id> [1..1]  59
         SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 59
         Identification <Id> [0..1] Text 60
Or       Country <Ctry> [1..1] CodeSet   'C5 60
Or       TypeAndIdentification <TpAndId> [1..1]  60
         SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 60
         Identification <Id> [1..1] IdentifierSet   'C4 61
Or}       Proprietary <Prtry> [1..1]  61
         Identification <Id> [0..1] Text 62
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 11
```

