---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.6 ReportDetails <RptDtls>", "11.4.6.1 NonClearingMember <NonClrMmb>"]
file_pages: [331, 332, 333, 334]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.6.1 NonClearingMember <NonClrMmb>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 331 to 334.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 331

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or           TradeLegNotificationIdentification
<TradLegNtfctnId>
[1..1] Text 367
Or}           UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 367
         NetPositionIdentification <NetPosId> [0..1] Text 367
11.4.6.1  NonClearingMember <NonClrMmb>
Presence: [0..*]
Definition: Provides the identification for the non-clearing member. This is mandatory if the clearing
member identification equals a general clearing member.
NonClearingMember <NonClrMmb> contains the following elements (see
PartyIdentificationAndAccount227 on page 457 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 457
   AlternateIdentification <AltrnId> [0..1] ± 457
   AdditionalInformation <AddtlInf> [0..1] ± C3 457
   ClearingAccount <ClrAcct> [0..1] ± 458
11.4.6.2  SettlementObligationDetails <SttlmOblgtnDtls>
Presence: [1..*]
Definition: Provides information about the settlement obligation details.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 331
```

## File page 332

```text
SettlementObligationDetails <SttlmOblgtnDtls> contains the following SettlementObligation9
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementObligationIdentification <SttlmOblgtnId> [1..1] Text 335
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ±   'C12,
C13,
C14,
  'C15,
  'C17
335
   IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 336
   Quantity <Qty> [1..1] ± 337
   SettlementAmount <SttlmAmt> [1..1] ± 337
   PlaceOfTrade <PlcOfTrad> [1..1] ± C16 337
   TradeDate <TradDt> [0..1]  338
{Or     Date <Dt> [1..1] Date 338
Or}     DateCode <DtCd> [1..1] CodeSet 338
   TradingCapacity <TradgCpcty> [0..1] CodeSet 338
   ClearingAccountType <ClrAcctTp> [0..1] CodeSet 339
   SafekeepingPlace <SfkpgPlc> [0..1]  339
{Or     Identification <Id> [1..1]  340
       SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 340
       Identification <Id> [0..1] Text 340
Or     Country <Ctry> [1..1] CodeSet   'C5 341
Or     TypeAndIdentification <TpAndId> [1..1]  341
       SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 341
       Identification <Id> [1..1] IdentifierSet   'C4 342
Or}     Proprietary <Prtry> [1..1]  342
       Identification <Id> [0..1] Text 342
       Type <Tp> [1..1] ± 342
   SafekeepingAccount <SfkpgAcct> [0..1] ± 343
   SecuritiesMovementType <SctiesMvmntTp> [0..1] CodeSet 343
   Payment <Pmt> [1..1] CodeSet 343
   SettlementParties <SttlmPties> [0..1]  344
{Or     DeliveringSettlementParties <DlvrgSttlmPties> [0..1]  C8 346
       Depository <Dpstry> [1..1] ± 348
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 332
```

## File page 333

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Party1 <Pty1> [1..1]  348
         PartyIdentification <PtyId> [1..1] ± 348
         AccountIdentification <AcctId> [0..1] Text 349
         ProcessingIdentification <PrcgId> [0..1] Text 349
         ProcessingDate <PrcgDt> [0..1] ± 349
         SubAccount <SubAcct> [0..1]  349
           Identification <Id> [1..1] ± 350
           Name <Nm> [0..1] Text 350
           Characteristic <Chrtc> [0..1] Text 350
         ContactPerson <CtctPrsn> [0..1] ± 350
       Party2 <Pty2> [0..1]  351
         PartyIdentification <PtyId> [1..1] ± 351
         AccountIdentification <AcctId> [0..1] Text 352
         ProcessingIdentification <PrcgId> [0..1] Text 352
         ProcessingDate <PrcgDt> [0..1] ± 352
         SubAccount <SubAcct> [0..1]  352
           Identification <Id> [1..1] ± 353
           Name <Nm> [0..1] Text 353
           Characteristic <Chrtc> [0..1] Text 353
         ContactPerson <CtctPrsn> [0..1] ± 353
       SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 354
Or}     ReceivingSettlementParties <RcvgSttlmPties> [0..1]  C9 354
       Depository <Dpstry> [1..1] ± 356
       Party1 <Pty1> [1..1]  356
         PartyIdentification <PtyId> [1..1] ± 356
         AccountIdentification <AcctId> [0..1] Text 357
         ProcessingIdentification <PrcgId> [0..1] Text 357
         ProcessingDate <PrcgDt> [0..1] ± 357
         SubAccount <SubAcct> [0..1]  357
           Identification <Id> [1..1] ± 358
           Name <Nm> [0..1] Text 358
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 333
```

## File page 334

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Characteristic <Chrtc> [0..1] Text 358
         ContactPerson <CtctPrsn> [0..1] ± 358
       Party2 <Pty2> [0..1]  359
         PartyIdentification <PtyId> [1..1] ± 359
         AccountIdentification <AcctId> [0..1] Text 360
         ProcessingIdentification <PrcgId> [0..1] Text 360
         ProcessingDate <PrcgDt> [0..1] ± 360
         SubAccount <SubAcct> [0..1]  360
           Identification <Id> [1..1] ± 361
           Name <Nm> [0..1] Text 361
           Characteristic <Chrtc> [0..1] Text 361
         ContactPerson <CtctPrsn> [0..1] ± 361
       SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 362
   AdditionalSettlementObligationDetails
<AddtlSttlmOblgtnDtls>
[0..*]  362
     RelatedSettlementObligationIdentification
<RltdSttlmOblgtnId>
[0..1] Text 363
     ObligationType <OblgtnTp> [0..1]  363
{Or       Code <Cd> [1..1] CodeSet 364
Or}       Proprietary <Prtry> [1..1] ± 364
     Description <Desc> [0..1] Text 364
     TradeDate <TradDt> [0..1] Date 364
     Quantity <Qty> [1..1] ± 364
     NetPositionPrice <NetPosPric> [0..1] ± 365
     TradingCurrency <TradgCcy> [0..1] CodeSet C19 365
     SettlementAmount <SttlmAmt> [1..1] ± 365
     SettlementDate <SttlmDt> [1..1] Date 366
     SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 366
     Payment <Pmt> [1..1] CodeSet 366
     References <Refs> [0..1]  366
       TradeLegNotificationIdentification
<TradLegNtfctnId>
[0..*]  367
{Or         TradeLegNotificationIdentification
<TradLegNtfctnId>
[1..1] Text 367
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 334
```

