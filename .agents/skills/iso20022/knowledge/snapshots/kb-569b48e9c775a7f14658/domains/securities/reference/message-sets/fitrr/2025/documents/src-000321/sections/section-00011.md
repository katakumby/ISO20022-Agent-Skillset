---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02", "3.3 Constraints"]
file_pages: [17, 18]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.017.001.02"]
---

# 3.3 Constraints

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 17 to 18.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 17

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       DeliveryType <DlvryTp> [0..1] CodeSet 30
       AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> [0..1]  C11 31
         Commodity <Cmmdty> [0..1]  31
           Product <Pdct> [1..1] ± 32
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
   SupplementaryData <SplmtryData> [0..*] ± C13 38
3.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 17 July 2025 auth.017.001.02
FinancialInstrumentReportingReferenceDataReport
V02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
17 July 2025
```

## File page 18

```text
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
C16 ValidDebtMaturityDateRule
DebtInstrumentAttributes/MaturityDate cannot be a date earlier than
TradingVenueRelatedAttributes/FirstTradeDate, TradingVenueRelatedAttributes/
RequestForAdmissionDate or TradingVenueRelatedAttributes/AdmissionApprovalDate.
Approved by the Securities SEG on 17 July 2025 auth.017.001.02
FinancialInstrumentReportingReferenceDataReport
V02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
18 July 2025
```

