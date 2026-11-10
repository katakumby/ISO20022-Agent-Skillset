---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks", "8.4.3 SupplementaryData <SplmtryData>"]
file_pages: [164, 165]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4.3 SupplementaryData <SplmtryData>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 164 to 165.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 164

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 407
         OtherLegInterestRate <OthrLegIntrstRate> [0..1] ± 407
       ForeignExchange <FX> [0..1]  408
         FXType <FxTp> [0..1] CodeSet 408
         OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 408
   TechnicalAttributes <TechAttrbts> [0..1]  C12 409
     InconsistencyIndicator <IncnsstncyInd> [0..1] Indicator 409
     LastUpdate <LastUpd> [0..1] DateTime 409
     SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 409
     RelevantCompetentAuthority <RlvntCmptntAuthrty> [0..1] CodeSet C4 410
     PublicationPeriod <PblctnPrd> [0..1] ± 410
     NeverPublished <NvrPblshd> [0..1] Indicator 410
     RelevantTradingVenue <RlvntTradgVn> [0..1] IdentifierSet 410
Constraints
• ValidDebtMaturityDateRule
DebtInstrumentAttributes/MaturityDate cannot be a date earlier than TradingVenueRelatedAttributes/
FirstTradeDate, TradingVenueRelatedAttributes/RequestForAdmissionDate or
TradingVenueRelatedAttributes/AdmissionApprovalDate.
• ValidDerivativeExpiryDateRule
DerivativesInstrumentAttributes/ExpiryDate cannot be a date earlier than
TradingVenueRelatedAttributes/FirstTradeDate, TradingVenueRelatedAttributes/
RequestForAdmissionDate or TradingVenueRelatedAttributes/AdmissionApprovalDate.
8.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C13 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 341 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 341
   Envelope <Envlp> [1..1] (External Schema) 341
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
164 July 2025
```

## File page 165

```text
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
165 July 2025
```

