---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02", "3.4 Message Building Blocks"]
file_pages: [19, 20]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.017.001.02"]
---

# 3.4 Message Building Blocks

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 19 to 20.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 19

```text
C17 ValidDerivativeExpiryDateRule
DerivativesInstrumentAttributes/ExpiryDate cannot be a date earlier than
TradingVenueRelatedAttributes/FirstTradeDate, TradingVenueRelatedAttributes/
RequestForAdmissionDate or TradingVenueRelatedAttributes/AdmissionApprovalDate.
C18 ValidISINRule
ISIN code must pass checksum validation.
C19 ValidMICRule
Market Identification code must be an active market at the time of reporting.
C20 ValidMICRule
Market Identification code must be an active market at the time of reporting.
C21 ValidShortNameRule
ShortName must conform with ISO 18774.
C22 ValidTerminationDateRule
TerminationDate cannot be a date earlier than FirstTradeDate, RequestForAdmissionDate or
AdmissionApprovalDate.
3.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
3.4.1 ReportHeader <RptHdr>
Presence: [1..1]
Definition: Header information related to the global report.
ReportHeader <RptHdr> contains the following elements (see "SecuritiesMarketReportHeader1" on
page 411 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportingEntity <RptgNtty> [1..1] ± C19 411
   ReportingPeriod <RptgPrd> [1..1] ± 411
   SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 411
3.4.2 ReferenceData <RefData>
Presence: [1..*]
Definition: Details of the reference data reported by the trading venue.
Impacted by: C16 "ValidDebtMaturityDateRule", C17 "ValidDerivativeExpiryDateRule"
Approved by the Securities SEG on 17 July 2025 auth.017.001.02
FinancialInstrumentReportingReferenceDataReport
V02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
19 July 2025
```

## File page 20

```text
ReferenceData <RefData> contains the following SecuritiesReferenceDataReport6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TechnicalRecordIdentification <TechRcrdId> [0..1] Text 21
   FinancialInstrumentGeneralAttributes
<FinInstrmGnlAttrbts>
[1..1]  C15,
C18,
C21
22
     Identification <Id> [1..1] IdentifierSet 22
     FullName <FullNm> [1..1] Text 22
     ShortName <ShrtNm> [0..1] Text 22
     ClassificationType <ClssfctnTp> [1..1] IdentifierSet 23
     NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 23
     CommodityDerivativeIndicator <CmmdtyDerivInd> [1..1] Indicator 23
   Issuer <Issr> [1..1] IdentifierSet 23
   TradingVenueRelatedAttributes <TradgVnRltdAttrbts> [1..*] ± C14,
C20,
C22
23
   DebtInstrumentAttributes <DebtInstrmAttrbts> [0..1]  24
     TotalIssuedNominalAmount <TtlIssdNmnlAmt> [1..1] Amount C2, C5 24
     MaturityDate <MtrtyDt> [0..1] Date 25
     NominalValuePerUnit <NmnlValPerUnit> [1..1] Amount C2, C5 25
     InterestRate <IntrstRate> [1..1] ± 25
     DebtSeniority <DebtSnrty> [0..1] CodeSet 26
   DerivativeInstrumentAttributes <DerivInstrmAttrbts> [0..1]  C9 26
     ExpiryDate <XpryDt> [0..1] Date 28
     PriceMultiplier <PricMltplr> [0..1] Quantity C6 28
     UnderlyingInstrument <UndrlygInstrm> [0..1]  28
{Or       Single <Sngl> [1..1] ± 28
Or}       Basket <Bskt> [1..1] ± C3, C10 29
     OptionType <OptnTp> [0..1] CodeSet 29
     StrikePrice <StrkPric> [0..1] ± 29
     OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 30
     DeliveryType <DlvryTp> [0..1] CodeSet 30
     AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> [0..1]  C11 31
       Commodity <Cmmdty> [0..1]  31
         Product <Pdct> [1..1] ± 32
Approved by the Securities SEG on 17 July 2025 auth.017.001.02
FinancialInstrumentReportingReferenceDataReport
V02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
20 July 2025
```

