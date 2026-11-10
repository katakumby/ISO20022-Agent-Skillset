---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks", "8.4.2 FinancialInstrument <FinInstrm>", "8.4.2.2 NewRecord <NewRcrd>", "8.4.2.2.1 TechnicalRecordIdentification <TechRcrdId>"]
file_pages: [126]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4.2.2.1 TechnicalRecordIdentification <TechRcrdId>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 126 to 126.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 126

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         TransactionType <TxTp> [0..1] CodeSet 137
         FinalPriceType <FnlPricTp> [0..1] CodeSet 138
       Interest <Intrst> [0..1]  138
         InterestRate <IntrstRate> [1..1] ± 138
         FirstLegInterestRate <FrstLegIntrstRate> [0..1] ± 139
         OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 139
         OtherLegInterestRate <OthrLegIntrstRate> [0..1] ± 139
       ForeignExchange <FX> [0..1]  140
         FXType <FxTp> [0..1] CodeSet 140
         OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 140
   TechnicalAttributes <TechAttrbts> [0..1]  C12 141
     InconsistencyIndicator <IncnsstncyInd> [0..1] Indicator 141
     LastUpdate <LastUpd> [0..1] DateTime 141
     SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 141
     RelevantCompetentAuthority <RlvntCmptntAuthrty> [0..1] CodeSet C4 142
     PublicationPeriod <PblctnPrd> [0..1] ± 142
     NeverPublished <NvrPblshd> [0..1] Indicator 142
     RelevantTradingVenue <RlvntTradgVn> [0..1] IdentifierSet 142
Constraints
• ValidDebtMaturityDateRule
DebtInstrumentAttributes/MaturityDate cannot be a date earlier than TradingVenueRelatedAttributes/
FirstTradeDate, TradingVenueRelatedAttributes/RequestForAdmissionDate or
TradingVenueRelatedAttributes/AdmissionApprovalDate.
• ValidDerivativeExpiryDateRule
DerivativesInstrumentAttributes/ExpiryDate cannot be a date earlier than
TradingVenueRelatedAttributes/FirstTradeDate, TradingVenueRelatedAttributes/
RequestForAdmissionDate or TradingVenueRelatedAttributes/AdmissionApprovalDate.
8.4.2.2.1  TechnicalRecordIdentification <TechRcrdId>
Presence: [0..1]
Definition: Unique identifier of a record in a message used as part of error management and status
advice message.
Usage:
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
126 July 2025
```

