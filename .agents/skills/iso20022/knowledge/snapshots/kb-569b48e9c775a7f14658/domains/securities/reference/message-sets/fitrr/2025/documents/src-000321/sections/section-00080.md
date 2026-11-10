---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks", "8.4.2 FinancialInstrument <FinInstrm>", "8.4.2.1 ModifiedRecord <ModfdRcrd>", "8.4.2.1.1 TechnicalRecordIdentification <TechRcrdId>"]
file_pages: [107]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4.2.1.1 TechnicalRecordIdentification <TechRcrdId>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 107 to 107.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 107

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         TransactionType <TxTp> [0..1] CodeSet 118
         FinalPriceType <FnlPricTp> [0..1] CodeSet 119
       Interest <Intrst> [0..1]  119
         InterestRate <IntrstRate> [1..1] ± 119
         FirstLegInterestRate <FrstLegIntrstRate> [0..1] ± 120
         OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 120
         OtherLegInterestRate <OthrLegIntrstRate> [0..1] ± 120
       ForeignExchange <FX> [0..1]  121
         FXType <FxTp> [0..1] CodeSet 121
         OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 121
   TechnicalAttributes <TechAttrbts> [0..1]  C12 122
     InconsistencyIndicator <IncnsstncyInd> [0..1] Indicator 122
     LastUpdate <LastUpd> [0..1] DateTime 122
     SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 122
     RelevantCompetentAuthority <RlvntCmptntAuthrty> [0..1] CodeSet C4 123
     PublicationPeriod <PblctnPrd> [0..1] ± 123
     NeverPublished <NvrPblshd> [0..1] Indicator 123
     RelevantTradingVenue <RlvntTradgVn> [0..1] IdentifierSet 123
Constraints
• ValidDebtMaturityDateRule
DebtInstrumentAttributes/MaturityDate cannot be a date earlier than TradingVenueRelatedAttributes/
FirstTradeDate, TradingVenueRelatedAttributes/RequestForAdmissionDate or
TradingVenueRelatedAttributes/AdmissionApprovalDate.
• ValidDerivativeExpiryDateRule
DerivativesInstrumentAttributes/ExpiryDate cannot be a date earlier than
TradingVenueRelatedAttributes/FirstTradeDate, TradingVenueRelatedAttributes/
RequestForAdmissionDate or TradingVenueRelatedAttributes/AdmissionApprovalDate.
8.4.2.1.1  TechnicalRecordIdentification <TechRcrdId>
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
107 July 2025
```

