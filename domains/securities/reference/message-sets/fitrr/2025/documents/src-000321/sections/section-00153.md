---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02", "12.4 Message Building Blocks", "12.4.2 NumberOfRecords <NbOfRcrds>"]
file_pages: [189, 190]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.042.001.02"]
---

# 12.4.2 NumberOfRecords <NbOfRcrds>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 189 to 190.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 189

```text
12.4.2 NumberOfRecords <NbOfRcrds>
Presence: [0..1]
Definition: Number of invalid records in this message.
Datatype: "Number" on page 453
12.4.3 FinancialInstruments <FinInstrms>
Presence: [1..*]
Definition: Provides the details of the financial instruments.
Approved by the Securities SEG on 17 July 2025 auth.042.001.02
FinancialInstrumentReportingInvalidReferenceData
ReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
189 July 2025
```

## File page 190

```text
FinancialInstruments <FinInstrms> contains the following SecuritiesInvalidReferenceDataReport4
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrument <FinInstrm> [1..1]  C16,
C17
191
     TechnicalRecordIdentification <TechRcrdId> [0..1] Text 193
     FinancialInstrumentGeneralAttributes
<FinInstrmGnlAttrbts>
[1..1]  C15,
C18,
C20
194
       Identification <Id> [1..1] IdentifierSet 194
       FullName <FullNm> [1..1] Text 194
       ShortName <ShrtNm> [0..1] Text 194
       ClassificationType <ClssfctnTp> [1..1] IdentifierSet 195
       NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 195
       CommodityDerivativeIndicator <CmmdtyDerivInd> [1..1] Indicator 195
     Issuer <Issr> [1..1] IdentifierSet 195
     TradingVenueRelatedAttributes <TradgVnRltdAttrbts> [1..*] ± C14,
C19,
C21
195
     DebtInstrumentAttributes <DebtInstrmAttrbts> [0..1]  196
       TotalIssuedNominalAmount <TtlIssdNmnlAmt> [1..1] Amount C2, C5 196
       MaturityDate <MtrtyDt> [0..1] Date 197
       NominalValuePerUnit <NmnlValPerUnit> [1..1] Amount C2, C5 197
       InterestRate <IntrstRate> [1..1] ± 197
       DebtSeniority <DebtSnrty> [0..1] CodeSet 198
     DerivativeInstrumentAttributes <DerivInstrmAttrbts> [0..1]  C9 198
       ExpiryDate <XpryDt> [0..1] Date 200
       PriceMultiplier <PricMltplr> [0..1] Quantity C6 200
       UnderlyingInstrument <UndrlygInstrm> [0..1]  200
{Or         Single <Sngl> [1..1] ± 200
Or}         Basket <Bskt> [1..1] ± C3, C10 201
       OptionType <OptnTp> [0..1] CodeSet 201
       StrikePrice <StrkPric> [0..1] ± 201
       OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 202
       DeliveryType <DlvryTp> [0..1] CodeSet 202
Approved by the Securities SEG on 17 July 2025 auth.042.001.02
FinancialInstrumentReportingInvalidReferenceData
ReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
190 July 2025
```

