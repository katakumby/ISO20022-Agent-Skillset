---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.3 SecuritiesReferenceDataReport7", "22.1.13.3.1 TechnicalRecordIdentification <TechRcrdId>"]
file_pages: [395]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.3.1 TechnicalRecordIdentification <TechRcrdId>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 395 to 395.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 395

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
22.1.13.3.1  TechnicalRecordIdentification <TechRcrdId>
Presence: [0..1]
Definition: Unique identifier of a record in a message used as part of error management and status
advice message.
Usage:
This identification will be used in the status advice report sent back.
Datatype: "Max35Text" on page 456
22.1.13.3.2  FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts>
Presence: [1..1]
Definition: Attributes and characteristics of the financial instrument.
Impacted by: C15 "ValidCFIRule", C18 "ValidISINRule", C21 "ValidShortNameRule"
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
395 July 2025
```

