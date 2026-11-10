---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.8 Transaction <Tx>", "22.1.13.2.8.11 TradePlaceMatchingIdentification <TradPlcMtchgId>"]
file_pages: [376, 377]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.8.11 TradePlaceMatchingIdentification <TradPlcMtchgId>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 376 to 377.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 376

```text
22.1.13.2.8.11  TradePlaceMatchingIdentification <TradPlcMtchgId>
Presence: [0..1]
Definition: Common matching identification when executed on a trade place.
Usage: Must be present when a trade venue has been provided.
Datatype: "Max52Text" on page 456
22.1.13.2.8.12  ComplexTradeComponentIdentification <CmplxTradCmpntId>
Presence: [0..1]
Definition: Identification, internal to the reporting party to identify all the reports related to the same
execution of a combination of financial instruments. The code must be unique for the reporting party for
the group of reports for the execution.
Usage:
Field only applies when the instrument is complex.
Datatype: "Max35Text" on page 456
22.1.13.2.9  FinancialInstrument <FinInstrm>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
376 July 2025
```

## File page 377

```text
FinancialInstrument <FinInstrm> contains one of the following
FinancialInstrumentAttributes5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1] IdentifierSet 378
Or   AlternateIdentification <AltrnId> [1..1] ± C5, C6,
C7, C8,
C11
378
Or}   Other <Othr> [1..1]  379
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
{Or         Swap <Swp> [1..1]  C13 384
           SwapIn <SwpIn> [0..1] ± 384
           SwapOut <SwpOut> [0..1] ± 385
Or}         Other <Othr> [1..1] ± 385
       OptionType <OptnTp> [0..1] CodeSet 385
       StrikePrice <StrkPric> [0..1] ± 386
       OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 386
       DeliveryType <DlvryTp> [1..1] CodeSet 386
       AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> [0..1]  387
{Or         Interest <Intrst> [1..1] ± 387
Or         ForeignExchange <FX> [1..1] ± 387
Or}         Both <Both> [1..1]  387
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
377 July 2025
```

