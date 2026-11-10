---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.9 FinancialInstrument <FinInstrm>", "22.1.13.2.9.3 Other <Othr>", "22.1.13.2.9.3.3 DerivativeInstrumentAttributes <DerivInstrmAttrbts>"]
file_pages: [383]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.9.3.3 DerivativeInstrumentAttributes <DerivInstrmAttrbts>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 383 to 383.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 383

```text
22.1.13.2.9.3.3  DerivativeInstrumentAttributes <DerivInstrmAttrbts>
Presence: [1..1]
Definition: Attributes specific to derivative instruments.
DerivativeInstrumentAttributes <DerivInstrmAttrbts> contains the following DerivativeInstrument6
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExpiryDate <XpryDt> [0..1] Date 383
   PriceMultiplier <PricMltplr> [1..1] Quantity C9 383
   UnderlyingInstrument <UndrlygInstrm> [1..1]  384
{Or     Swap <Swp> [1..1]  C13 384
       SwapIn <SwpIn> [0..1] ± 384
       SwapOut <SwpOut> [0..1] ± 385
Or}     Other <Othr> [1..1] ± 385
   OptionType <OptnTp> [0..1] CodeSet 385
   StrikePrice <StrkPric> [0..1] ± 386
   OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 386
   DeliveryType <DlvryTp> [1..1] CodeSet 386
   AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> [0..1]  387
{Or     Interest <Intrst> [1..1] ± 387
Or     ForeignExchange <FX> [1..1] ± 387
Or}     Both <Both> [1..1]  387
       Interest <Intrst> [1..1] ± 388
       ForeignExchange <FX> [1..1] ± 388
22.1.13.2.9.3.3.1  ExpiryDate <XpryDt>
Presence: [0..1]
Definition: Original expiry date of the reported financial instrument.
Usage:
Field applies to derivatives with defined expiry date.
Datatype: "ISODate" on page 449
22.1.13.2.9.3.3.2  PriceMultiplier <PricMltplr>
Presence: [1..1]
Definition: Number of units of the underlying instrument represented by a single derivative contract.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
383 July 2025
```

