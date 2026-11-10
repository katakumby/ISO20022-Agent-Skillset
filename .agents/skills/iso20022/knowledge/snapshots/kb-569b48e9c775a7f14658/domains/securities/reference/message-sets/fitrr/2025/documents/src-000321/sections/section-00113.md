---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks", "8.4.2 FinancialInstrument <FinInstrm>", "8.4.2.3 TerminatedRecord <TermntdRcrd>"]
file_pages: [143, 144]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4.2.3 TerminatedRecord <TermntdRcrd>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 143 to 144.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 143

```text
8.4.2.3  TerminatedRecord <TermntdRcrd>
Presence: [1..1]
Definition: Specifies instruments which have been terminated / have reached there pre-set termination
data and are no longer valid instruments.
Impacted by: C18 "ValidDebtMaturityDateRule", C20 "ValidDerivativeExpiryDateRule"
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
143 July 2025
```

## File page 144

```text
TerminatedRecord <TermntdRcrd> contains the following SecuritiesReferenceDataReport6
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TechnicalRecordIdentification <TechRcrdId> [0..1] Text 145
   FinancialInstrumentGeneralAttributes
<FinInstrmGnlAttrbts>
[1..1]  C16,
C22,
C27
146
     Identification <Id> [1..1] IdentifierSet 146
     FullName <FullNm> [1..1] Text 146
     ShortName <ShrtNm> [0..1] Text 146
     ClassificationType <ClssfctnTp> [1..1] IdentifierSet 147
     NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 147
     CommodityDerivativeIndicator <CmmdtyDerivInd> [1..1] Indicator 147
   Issuer <Issr> [1..1] IdentifierSet 147
   TradingVenueRelatedAttributes <TradgVnRltdAttrbts> [1..*] ± C14,
C25,
C29
147
   DebtInstrumentAttributes <DebtInstrmAttrbts> [0..1]  148
     TotalIssuedNominalAmount <TtlIssdNmnlAmt> [1..1] Amount C2, C5 148
     MaturityDate <MtrtyDt> [0..1] Date 149
     NominalValuePerUnit <NmnlValPerUnit> [1..1] Amount C2, C5 149
     InterestRate <IntrstRate> [1..1] ± 149
     DebtSeniority <DebtSnrty> [0..1] CodeSet 150
   DerivativeInstrumentAttributes <DerivInstrmAttrbts> [0..1]  C9 150
     ExpiryDate <XpryDt> [0..1] Date 152
     PriceMultiplier <PricMltplr> [0..1] Quantity C6 152
     UnderlyingInstrument <UndrlygInstrm> [0..1]  152
{Or       Single <Sngl> [1..1] ± 152
Or}       Basket <Bskt> [1..1] ± C3, C10 153
     OptionType <OptnTp> [0..1] CodeSet 153
     StrikePrice <StrkPric> [0..1] ± 153
     OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 154
     DeliveryType <DlvryTp> [0..1] CodeSet 154
     AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> [0..1]  C11 155
       Commodity <Cmmdty> [0..1]  155
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
144 July 2025
```

