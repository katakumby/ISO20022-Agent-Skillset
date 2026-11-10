---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks", "8.4.2 FinancialInstrument <FinInstrm>", "8.4.2.4 CancelledRecord <CancRcrd>"]
file_pages: [162, 163]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4.2.4 CancelledRecord <CancRcrd>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 162 to 163.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 162

```text
8.4.2.4  CancelledRecord <CancRcrd>
Presence: [1..1]
Definition: Specifies data that has been cancelled since the previous report.
Impacted by: C19 "ValidDebtMaturityDateRule", C21 "ValidDerivativeExpiryDateRule"
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
162 July 2025
```

## File page 163

```text
CancelledRecord <CancRcrd> contains the following elements (see
"SecuritiesReferenceDataReport7" on page 393 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TechnicalRecordIdentification <TechRcrdId> [0..1] Text 395
   FinancialInstrumentGeneralAttributes
<FinInstrmGnlAttrbts>
[1..1] ± C15,
C18,
C21
395
   Issuer <Issr> [0..1] IdentifierSet 396
   TradingVenueRelatedAttributes <TradgVnRltdAttrbts> [1..*] ± C14,
C20,
C22
396
   DebtInstrumentAttributes <DebtInstrmAttrbts> [0..1]  397
     TotalIssuedNominalAmount <TtlIssdNmnlAmt> [1..1] Amount C2, C5 397
     MaturityDate <MtrtyDt> [0..1] Date 398
     NominalValuePerUnit <NmnlValPerUnit> [1..1] Amount C2, C5 398
     InterestRate <IntrstRate> [1..1] ± 398
     DebtSeniority <DebtSnrty> [0..1] CodeSet 399
   DerivativeInstrumentAttributes <DerivInstrmAttrbts> [0..1]  C9 399
     ExpiryDate <XpryDt> [0..1] Date 401
     PriceMultiplier <PricMltplr> [0..1] Quantity C6 401
     UnderlyingInstrument <UndrlygInstrm> [0..1]  401
{Or       Single <Sngl> [1..1] ± 401
Or}       Basket <Bskt> [1..1] ± C3, C10 402
     OptionType <OptnTp> [0..1] CodeSet 402
     StrikePrice <StrkPric> [0..1] ± 402
     OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 403
     DeliveryType <DlvryTp> [0..1] CodeSet 403
     AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> [0..1]  C11 404
       Commodity <Cmmdty> [0..1]  404
         Product <Pdct> [1..1] ± 405
         TransactionType <TxTp> [0..1] CodeSet 405
         FinalPriceType <FnlPricTp> [0..1] CodeSet 406
       Interest <Intrst> [0..1]  406
         InterestRate <IntrstRate> [1..1] ± 406
         FirstLegInterestRate <FrstLegIntrstRate> [0..1] ± 407
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
163 July 2025
```

