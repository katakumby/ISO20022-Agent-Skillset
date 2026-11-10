---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.1 SecurityInstrumentDescription17", "22.1.13.1.6 CommodityDerivativeIndicator <CmmdtyDerivInd>"]
file_pages: [366, 367, 368]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.1.6 CommodityDerivativeIndicator <CmmdtyDerivInd>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 366 to 368.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 366

```text
Definition: Currency in which the notional is denominated.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 417
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
22.1.13.1.6  CommodityDerivativeIndicator <CmmdtyDerivInd>
Presence: [0..1]
Definition: Indicates whether the financial instrument falls within the definition of commodities derivative
under the local regulation.
Usage: when not present, the indicator in not applicable.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
22.1.13.2  SecuritiesTransactionReport7
Definition: Details of the securities transaction report.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
366 July 2025
```

## File page 367

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 369
   ExecutingParty <ExctgPty> [1..1] IdentifierSet 369
   InvestmentPartyIndicator <InvstmtPtyInd> [1..1] Indicator 369
   SubmittingParty <SubmitgPty> [1..1] IdentifierSet 369
   Buyer <Buyr> [1..1] ± 370
   Seller <Sellr> [1..1] ± 370
   OrderTransmission <OrdrTrnsmssn> [1..1]  370
     TransmissionIndicator <TrnsmssnInd> [1..1] Indicator 371
     TransmittingBuyer <TrnsmttgBuyr> [0..1] IdentifierSet 371
     TransmittingSeller <TrnsmttgSellr> [0..1] IdentifierSet 371
   Transaction <Tx> [1..1]  371
     TradeDate <TradDt> [1..1] DateTime 372
     TradingCapacity <TradgCpcty> [1..1] CodeSet 372
     Quantity <Qty> [1..1] ± 373
     DigitalTokenQuantity <DgtlTknQty> [0..*]  373
       Identifier <Idr> [1..1] IdentifierSet 373
       Unit <Unit> [0..1] Quantity 373
       Description <Desc> [0..1] Text 373
     DerivativeNotionalChange <DerivNtnlChng> [0..1] CodeSet 373
     Price <Pric> [1..1] ± 374
     NetAmount <NetAmt> [0..1] Amount 374
     TradeVenue <TradVn> [1..1] IdentifierSet 374
     CountryOfBranch <CtryOfBrnch> [0..1] CodeSet C4 375
     UpFrontPayment <UpFrntPmt> [0..1] ± 375
     TradePlaceMatchingIdentification <TradPlcMtchgId> [0..1] Text 376
     ComplexTradeComponentIdentification
<CmplxTradCmpntId>
[0..1] Text 376
   FinancialInstrument <FinInstrm> [1..1]  376
{Or     Identification <Id> [1..1] IdentifierSet 378
Or     AlternateIdentification <AltrnId> [1..1] ± C5, C6,
C7, C8,
C11
378
Or}     Other <Othr> [1..1]  379
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
367 July 2025
```

## File page 368

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       FinancialInstrumentGeneralAttributes
<FinInstrmGnlAttrbts>
[1..1]  380
         Identification <Id> [0..1] IdentifierSet 381
         OtherIdentification <OthrId> [0..*]  381
           Identification <Id> [1..1] Text 381
           Suffix <Sfx> [0..1] Text 381
           Type <Tp> [1..1] ± 382
         FullName <FullNm> [1..1] Text 382
         ClassificationType <ClssfctnTp> [1..1] IdentifierSet 382
         NotionalCurrency <NtnlCcy> [0..1] CodeSet C2 382
       DebtInstrumentAttributes <DebtInstrmAttrbts> [0..1] ± 382
       DerivativeInstrumentAttributes <DerivInstrmAttrbts> [1..1]  383
         ExpiryDate <XpryDt> [0..1] Date 383
         PriceMultiplier <PricMltplr> [1..1] Quantity C9 383
         UnderlyingInstrument <UndrlygInstrm> [1..1]  384
{Or           Swap <Swp> [1..1]  C13 384
             SwapIn <SwpIn> [0..1] ± 384
             SwapOut <SwpOut> [0..1] ± 385
Or}           Other <Othr> [1..1] ± 385
         OptionType <OptnTp> [0..1] CodeSet 385
         StrikePrice <StrkPric> [0..1] ± 386
         OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 386
         DeliveryType <DlvryTp> [1..1] CodeSet 386
         AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> [0..1]  387
{Or           Interest <Intrst> [1..1] ± 387
Or           ForeignExchange <FX> [1..1] ± 387
Or}           Both <Both> [1..1]  387
             Interest <Intrst> [1..1] ± 388
             ForeignExchange <FX> [1..1] ± 388
   InvestmentDecisionPerson <InvstmtDcsnPrsn> [0..1]  388
{Or     Person <Prsn> [1..1] ± 388
Or}     Algorithm <Algo> [1..1] Text 389
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
368 July 2025
```

