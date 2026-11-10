---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.2 Structure"]
file_pages: [66, 67, 68, 69]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.2 Structure

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 66 to 69.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 66

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <TradLegNtfctnCxl> [1..1]    'C10
   ClearingMember <ClrMmb> [1..1] ± 74
   ClearingAccount <ClrAcct> [1..1] ± 74
   DeliveryAccount <DlvryAcct> [0..1] ± 74
   NonClearingMember <NonClrMmb> [0..1] ± 75
   ClearingDetails <ClrDtls> [0..1]  75
     SettlementNettingEligibleCode <SttlmNetgElgblCd> [1..1] CodeSet 77
     ClearingSegment <ClrSgmt> [0..1] ± 78
     GuaranteedTrade <GrntedTrad> [0..1] Indicator 78
     TradeCounterpartyIdentification <TradCtrPtyId> [0..1]  78
       TradeCounterpartyMemberIdentification
<TradCtrPtyMmbId>
[1..1] ± 80
       TradeCounterpartyClearingMemberIdentification
<TradCtrPtyClrMmbId>
[1..1] ± 80
       DeliveringParties <DlvrgPties> [0..1]  C8 81
         Depository <Dpstry> [1..1] ± 82
         Party1 <Pty1> [1..1]  83
           PartyIdentification <PtyId> [1..1] ± 83
           AccountIdentification <AcctId> [0..1] Text 84
           ProcessingIdentification <PrcgId> [0..1] Text 84
           ProcessingDate <PrcgDt> [0..1] ± 84
           SubAccount <SubAcct> [0..1]  84
             Identification <Id> [1..1] ± 85
             Name <Nm> [0..1] Text 85
             Characteristic <Chrtc> [0..1] Text 85
           ContactPerson <CtctPrsn> [0..1] ± 85
         Party2 <Pty2> [0..1]  86
           PartyIdentification <PtyId> [1..1] ± 86
           AccountIdentification <AcctId> [0..1] Text 87
           ProcessingIdentification <PrcgId> [0..1] Text 87
           ProcessingDate <PrcgDt> [0..1] ± 87
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 66
```

## File page 67

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           SubAccount <SubAcct> [0..1]  87
             Identification <Id> [1..1] ± 88
             Name <Nm> [0..1] Text 88
             Characteristic <Chrtc> [0..1] Text 88
           ContactPerson <CtctPrsn> [0..1] ± 88
         SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 89
       ReceivingParties <RcvgPties> [0..1]  C9 89
         Depository <Dpstry> [1..1] ± 90
         Party1 <Pty1> [1..1]  91
           PartyIdentification <PtyId> [1..1] ± 91
           AccountIdentification <AcctId> [0..1] Text 92
           ProcessingIdentification <PrcgId> [0..1] Text 92
           ProcessingDate <PrcgDt> [0..1] ± 92
           SubAccount <SubAcct> [0..1]  92
             Identification <Id> [1..1] ± 93
             Name <Nm> [0..1] Text 93
             Characteristic <Chrtc> [0..1] Text 93
           ContactPerson <CtctPrsn> [0..1] ± 93
         Party2 <Pty2> [0..1]  94
           PartyIdentification <PtyId> [1..1] ± 94
           AccountIdentification <AcctId> [0..1] Text 95
           ProcessingIdentification <PrcgId> [0..1] Text 95
           ProcessingDate <PrcgDt> [0..1] ± 95
           SubAccount <SubAcct> [0..1]  95
             Identification <Id> [1..1] ± 96
             Name <Nm> [0..1] Text 96
             Characteristic <Chrtc> [0..1] Text 96
           ContactPerson <CtctPrsn> [0..1] ± 96
         SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 97
   TradeLegDetails <TradLegDtls> [1..1]    'C19 97
     TradeLegIdentification <TradLegId> [1..1] Text 100
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 67
```

## File page 68

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     TradeIdentification <TradId> [0..1] Text 100
     TradeExecutionIdentification <TradExctnId> [0..1] Text 100
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 100
     OrderIdentification <OrdrId> [0..1] Text 101
     AllocationIdentification <AllcnId> [0..1] Text 101
     Status <Sts> [0..1] CodeSet 101
     TradeDate <TradDt> [1..1] ± 101
     TransactionDateTime <TxDtTm> [0..1] DateTime 101
     SettlementDate <SttlmDt> [0..1]  102
{Or       Date <Dt> [1..1] Date 102
Or}       DateCode <DtCd> [1..1]  102
{Or         Code <Cd> [1..1] CodeSet 102
Or}         Proprietary <Prtry> [1..1] ± 102
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
       Identification <Id> [1..1]  110
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet   'C4 111
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 68
```

## File page 69

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         ProprietaryIdentification <PrtryId> [1..1] ± 111
Or}         NameAndAddress <NmAndAdr> [1..1]  112
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
{Or       Identification <Id> [1..1]  117
         SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 117
         Identification <Id> [0..1] Text 118
Or       Country <Ctry> [1..1] CodeSet   'C5 118
Or       TypeAndIdentification <TpAndId> [1..1]  118
         SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 118
         Identification <Id> [1..1] IdentifierSet   'C4 119
Or}       Proprietary <Prtry> [1..1]  119
         Identification <Id> [0..1] Text 120
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 69
```

