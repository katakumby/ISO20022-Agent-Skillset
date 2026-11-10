---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02", "3.4 Message Building Blocks", "3.4.2 ReferenceData <RefData>", "3.4.2.1 TechnicalRecordIdentification <TechRcrdId>"]
file_pages: [21]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.017.001.02"]
---

# 3.4.2.1 TechnicalRecordIdentification <TechRcrdId>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 21 to 21.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 21

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         TransactionType <TxTp> [0..1] CodeSet 32
         FinalPriceType <FnlPricTp> [0..1] CodeSet 33
       Interest <Intrst> [0..1]  33
         InterestRate <IntrstRate> [1..1] ± 33
         FirstLegInterestRate <FrstLegIntrstRate> [0..1] ± 34
         OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 34
         OtherLegInterestRate <OthrLegIntrstRate> [0..1] ± 34
       ForeignExchange <FX> [0..1]  35
         FXType <FxTp> [0..1] CodeSet 35
         OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 35
   TechnicalAttributes <TechAttrbts> [0..1]  C12 36
     InconsistencyIndicator <IncnsstncyInd> [0..1] Indicator 36
     LastUpdate <LastUpd> [0..1] DateTime 36
     SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 37
     RelevantCompetentAuthority <RlvntCmptntAuthrty> [0..1] CodeSet C4 37
     PublicationPeriod <PblctnPrd> [0..1] ± 37
     NeverPublished <NvrPblshd> [0..1] Indicator 37
     RelevantTradingVenue <RlvntTradgVn> [0..1] IdentifierSet 37
Constraints
• ValidDebtMaturityDateRule
DebtInstrumentAttributes/MaturityDate cannot be a date earlier than TradingVenueRelatedAttributes/
FirstTradeDate, TradingVenueRelatedAttributes/RequestForAdmissionDate or
TradingVenueRelatedAttributes/AdmissionApprovalDate.
• ValidDerivativeExpiryDateRule
DerivativesInstrumentAttributes/ExpiryDate cannot be a date earlier than
TradingVenueRelatedAttributes/FirstTradeDate, TradingVenueRelatedAttributes/
RequestForAdmissionDate or TradingVenueRelatedAttributes/AdmissionApprovalDate.
3.4.2.1  TechnicalRecordIdentification <TechRcrdId>
Presence: [0..1]
Definition: Unique identifier of a record in a message used as part of error management and status
advice message.
Usage:
Approved by the Securities SEG on 17 July 2025 auth.017.001.02
FinancialInstrumentReportingReferenceDataReport
V02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
21 July 2025
```

