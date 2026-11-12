---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02", "12.3 Constraints"]
file_pages: [186, 187]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.042.001.02"]
topic_continuations: [{"constraint_ids": ["C16", "C17", "C18", "C19", "C20", "C21"], "until_heading": "12.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 188, "topic": "12.3 Constraints", "reference_path": "domains/securities/reference/message-sets/fitrr/2025/documents/src-000321/sections/section-00152.md"}]
---

# 12.3 Constraints

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 186 to 187.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 12.3 Constraints topic continues in [Constraints continuation C16–C21 (file p188)](section-00152.md#file-page-188). Read the text before **12.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 186

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         StrikePrice <StrkPric> [0..1] ± 201
         OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 202
         DeliveryType <DlvryTp> [0..1] CodeSet 202
         AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> [0..1]  C11 203
           Commodity <Cmmdty> [0..1]  203
             Product <Pdct> [1..1] ± 204
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
     SupplementaryData <SplmtryData> [0..*] ± C13 210
   SupplementaryData <SplmtryData> [0..*] ± C13 210
12.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
Approved by the Securities SEG on 17 July 2025 auth.042.001.02
FinancialInstrumentReportingInvalidReferenceData
ReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
186 July 2025
```

## File page 187

```text
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 BasketInstrumentUniquenessRule
Where an underlying instrument basket is populated, all ISINs or LEIs must be unique.
C4 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C5 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C6 MultiplierRule
Price Multiplier must not be zero.
C7 NumberRule
If Number is negative, then Sign must be present.
C8 NumberRule
If Number is negative, then Sign must be present.
C9 OneElementPresentRule
At least one of 5 elements must be present.
C10 OneElementPresentRule
At least one of 5 elements must be present.
C11 OneElementPresentRule
At least one of the 3 elements must be present.
C12 OneElementPresentRule
At least one of the 5 elements must be present.
C13 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C14 ValidateAdmissionIssuerRule
When IssuerRequest is equal to true, then AdmissionApprovalDateByIssuer must be present.
C15 ValidCFIRule
The CFI code must be a valid CFI code as defined by 10962.
Approved by the Securities SEG on 17 July 2025 auth.042.001.02
FinancialInstrumentReportingInvalidReferenceData
ReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
187 July 2025
```

