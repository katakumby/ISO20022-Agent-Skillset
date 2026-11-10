---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02", "12.4 Message Building Blocks", "12.4.3 FinancialInstruments <FinInstrms>", "12.4.3.1 FinancialInstrument <FinInstrm>"]
file_pages: [191, 192]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.042.001.02"]
---

# 12.4.3.1 FinancialInstrument <FinInstrm>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 191 to 192.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 191

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AssetClassSpecificAttributes
<AsstClssSpcfcAttrbts>
[0..1]  C11 203
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
12.4.3.1  FinancialInstrument <FinInstrm>
Presence: [1..1]
Definition: Instrument details at the time this specific details on the financial instrument was invalidated.
Impacted by: C16 "ValidDebtMaturityDateRule", C17 "ValidDerivativeExpiryDateRule"
Approved by the Securities SEG on 17 July 2025 auth.042.001.02
FinancialInstrumentReportingInvalidReferenceData
ReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
191 July 2025
```

## File page 192

```text
FinancialInstrument <FinInstrm> contains the following SecuritiesReferenceDataReport6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or       Single <Sngl> [1..1] ± 200
Or}       Basket <Bskt> [1..1] ± C3, C10 201
     OptionType <OptnTp> [0..1] CodeSet 201
     StrikePrice <StrkPric> [0..1] ± 201
     OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 202
     DeliveryType <DlvryTp> [0..1] CodeSet 202
     AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> [0..1]  C11 203
       Commodity <Cmmdty> [0..1]  203
         Product <Pdct> [1..1] ± 204
Approved by the Securities SEG on 17 July 2025 auth.042.001.02
FinancialInstrumentReportingInvalidReferenceData
ReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
192 July 2025
```

