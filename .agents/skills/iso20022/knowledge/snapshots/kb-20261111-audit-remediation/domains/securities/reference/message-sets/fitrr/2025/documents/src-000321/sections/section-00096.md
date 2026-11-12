---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks", "8.4.2 FinancialInstrument <FinInstrm>", "8.4.2.2 NewRecord <NewRcrd>"]
file_pages: [124, 125]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4.2.2 NewRecord <NewRcrd>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 124 to 125.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 124

```text
8.4.2.2  NewRecord <NewRcrd>
Presence: [1..1]
Definition: Specifies new instruments that have been added since the previous report.
Impacted by: C18 "ValidDebtMaturityDateRule", C20 "ValidDerivativeExpiryDateRule"
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
124 July 2025
```

## File page 125

```text
NewRecord <NewRcrd> contains the following SecuritiesReferenceDataReport6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TechnicalRecordIdentification <TechRcrdId> [0..1] Text 126
   FinancialInstrumentGeneralAttributes
<FinInstrmGnlAttrbts>
[1..1]  C16,
C22,
C27
127
     Identification <Id> [1..1] IdentifierSet 127
     FullName <FullNm> [1..1] Text 127
     ShortName <ShrtNm> [0..1] Text 127
     ClassificationType <ClssfctnTp> [1..1] IdentifierSet 128
     NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 128
     CommodityDerivativeIndicator <CmmdtyDerivInd> [1..1] Indicator 128
   Issuer <Issr> [1..1] IdentifierSet 128
   TradingVenueRelatedAttributes <TradgVnRltdAttrbts> [1..*] ± C14,
C25,
C29
128
   DebtInstrumentAttributes <DebtInstrmAttrbts> [0..1]  129
     TotalIssuedNominalAmount <TtlIssdNmnlAmt> [1..1] Amount C2, C5 129
     MaturityDate <MtrtyDt> [0..1] Date 130
     NominalValuePerUnit <NmnlValPerUnit> [1..1] Amount C2, C5 130
     InterestRate <IntrstRate> [1..1] ± 130
     DebtSeniority <DebtSnrty> [0..1] CodeSet 131
   DerivativeInstrumentAttributes <DerivInstrmAttrbts> [0..1]  C9 131
     ExpiryDate <XpryDt> [0..1] Date 133
     PriceMultiplier <PricMltplr> [0..1] Quantity C6 133
     UnderlyingInstrument <UndrlygInstrm> [0..1]  133
{Or       Single <Sngl> [1..1] ± 133
Or}       Basket <Bskt> [1..1] ± C3, C10 134
     OptionType <OptnTp> [0..1] CodeSet 134
     StrikePrice <StrkPric> [0..1] ± 134
     OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 135
     DeliveryType <DlvryTp> [0..1] CodeSet 135
     AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> [0..1]  C11 136
       Commodity <Cmmdty> [0..1]  136
         Product <Pdct> [1..1] ± 137
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
125 July 2025
```

