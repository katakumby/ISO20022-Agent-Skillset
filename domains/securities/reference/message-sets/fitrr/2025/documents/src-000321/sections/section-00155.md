---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02", "12.4 Message Building Blocks", "12.4.3 FinancialInstruments <FinInstrms>", "12.4.3.1 FinancialInstrument <FinInstrm>", "12.4.3.1.1 TechnicalRecordIdentification <TechRcrdId>"]
file_pages: [193]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.042.001.02"]
---

# 12.4.3.1.1 TechnicalRecordIdentification <TechRcrdId>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 193 to 193.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 193

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         TransactionType <TxTp> [0..1] CodeSet 204
         FinalPriceType <FnlPricTp> [0..1] CodeSet 205
       Interest <Intrst> [0..1]  205
         InterestRate <IntrstRate> [1..1] ± 205
         FirstLegInterestRate <FrstLegIntrstRate> [0..1] ± 206
         OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 206
         OtherLegInterestRate <OthrLegIntrstRate> [0..1] ± 206
       ForeignExchange <FX> [0..1]  207
         FXType <FxTp> [0..1] CodeSet 207
         OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 207
   TechnicalAttributes <TechAttrbts> [0..1]  C12 208
     InconsistencyIndicator <IncnsstncyInd> [0..1] Indicator 208
     LastUpdate <LastUpd> [0..1] DateTime 208
     SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 208
     RelevantCompetentAuthority <RlvntCmptntAuthrty> [0..1] CodeSet C4 209
     PublicationPeriod <PblctnPrd> [0..1] ± 209
     NeverPublished <NvrPblshd> [0..1] Indicator 209
     RelevantTradingVenue <RlvntTradgVn> [0..1] IdentifierSet 209
Constraints
• ValidDebtMaturityDateRule
DebtInstrumentAttributes/MaturityDate cannot be a date earlier than TradingVenueRelatedAttributes/
FirstTradeDate, TradingVenueRelatedAttributes/RequestForAdmissionDate or
TradingVenueRelatedAttributes/AdmissionApprovalDate.
• ValidDerivativeExpiryDateRule
DerivativesInstrumentAttributes/ExpiryDate cannot be a date earlier than
TradingVenueRelatedAttributes/FirstTradeDate, TradingVenueRelatedAttributes/
RequestForAdmissionDate or TradingVenueRelatedAttributes/AdmissionApprovalDate.
12.4.3.1.1  TechnicalRecordIdentification <TechRcrdId>
Presence: [0..1]
Definition: Unique identifier of a record in a message used as part of error management and status
advice message.
Usage:
Approved by the Securities SEG on 17 July 2025 auth.042.001.02
FinancialInstrumentReportingInvalidReferenceData
ReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
193 July 2025
```

