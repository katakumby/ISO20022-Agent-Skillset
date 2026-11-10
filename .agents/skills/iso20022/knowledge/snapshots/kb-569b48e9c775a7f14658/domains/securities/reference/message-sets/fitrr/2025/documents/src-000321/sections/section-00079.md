---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks", "8.4.2 FinancialInstrument <FinInstrm>", "8.4.2.1 ModifiedRecord <ModfdRcrd>"]
file_pages: [105, 106]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4.2.1 ModifiedRecord <ModfdRcrd>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 105 to 106.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 105

```text
8.4.2.1  ModifiedRecord <ModfdRcrd>
Presence: [1..1]
Definition: Specifies data that has been modified since the previous report.
Impacted by: C18 "ValidDebtMaturityDateRule", C20 "ValidDerivativeExpiryDateRule"
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
105 July 2025
```

## File page 106

```text
ModifiedRecord <ModfdRcrd> contains the following SecuritiesReferenceDataReport6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TechnicalRecordIdentification <TechRcrdId> [0..1] Text 107
   FinancialInstrumentGeneralAttributes
<FinInstrmGnlAttrbts>
[1..1]  C16,
C22,
C27
108
     Identification <Id> [1..1] IdentifierSet 108
     FullName <FullNm> [1..1] Text 108
     ShortName <ShrtNm> [0..1] Text 108
     ClassificationType <ClssfctnTp> [1..1] IdentifierSet 109
     NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 109
     CommodityDerivativeIndicator <CmmdtyDerivInd> [1..1] Indicator 109
   Issuer <Issr> [1..1] IdentifierSet 109
   TradingVenueRelatedAttributes <TradgVnRltdAttrbts> [1..*] ± C14,
C25,
C29
109
   DebtInstrumentAttributes <DebtInstrmAttrbts> [0..1]  110
     TotalIssuedNominalAmount <TtlIssdNmnlAmt> [1..1] Amount C2, C5 110
     MaturityDate <MtrtyDt> [0..1] Date 111
     NominalValuePerUnit <NmnlValPerUnit> [1..1] Amount C2, C5 111
     InterestRate <IntrstRate> [1..1] ± 111
     DebtSeniority <DebtSnrty> [0..1] CodeSet 112
   DerivativeInstrumentAttributes <DerivInstrmAttrbts> [0..1]  C9 112
     ExpiryDate <XpryDt> [0..1] Date 114
     PriceMultiplier <PricMltplr> [0..1] Quantity C6 114
     UnderlyingInstrument <UndrlygInstrm> [0..1]  114
{Or       Single <Sngl> [1..1] ± 114
Or}       Basket <Bskt> [1..1] ± C3, C10 115
     OptionType <OptnTp> [0..1] CodeSet 115
     StrikePrice <StrkPric> [0..1] ± 115
     OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 116
     DeliveryType <DlvryTp> [0..1] CodeSet 116
     AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> [0..1]  C11 117
       Commodity <Cmmdty> [0..1]  117
         Product <Pdct> [1..1] ± 118
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
106 July 2025
```

