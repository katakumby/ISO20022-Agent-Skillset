---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02", "3.2 Structure"]
file_pages: [16]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.017.001.02"]
---

# 3.2 Structure

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 16 to 16.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 16

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FinInstrmRptgRefDataRpt> [1..1]  
   ReportHeader <RptHdr> [1..1] ± 19
   ReferenceData <RefData> [1..*]  C16,
C17
19
     TechnicalRecordIdentification <TechRcrdId> [0..1] Text 21
     FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts> [1..1]  C15,
C18,
C21
22
       Identification <Id> [1..1] IdentifierSet 22
       FullName <FullNm> [1..1] Text 22
       ShortName <ShrtNm> [0..1] Text 22
       ClassificationType <ClssfctnTp> [1..1] IdentifierSet 23
       NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 23
       CommodityDerivativeIndicator <CmmdtyDerivInd> [1..1] Indicator 23
     Issuer <Issr> [1..1] IdentifierSet 23
     TradingVenueRelatedAttributes <TradgVnRltdAttrbts> [1..*] ± C14,
C20,
C22
23
     DebtInstrumentAttributes <DebtInstrmAttrbts> [0..1]  24
       TotalIssuedNominalAmount <TtlIssdNmnlAmt> [1..1] Amount C2, C5 24
       MaturityDate <MtrtyDt> [0..1] Date 25
       NominalValuePerUnit <NmnlValPerUnit> [1..1] Amount C2, C5 25
       InterestRate <IntrstRate> [1..1] ± 25
       DebtSeniority <DebtSnrty> [0..1] CodeSet 26
     DerivativeInstrumentAttributes <DerivInstrmAttrbts> [0..1]  C9 26
       ExpiryDate <XpryDt> [0..1] Date 28
       PriceMultiplier <PricMltplr> [0..1] Quantity C6 28
       UnderlyingInstrument <UndrlygInstrm> [0..1]  28
{Or         Single <Sngl> [1..1] ± 28
Or}         Basket <Bskt> [1..1] ± C3, C10 29
       OptionType <OptnTp> [0..1] CodeSet 29
       StrikePrice <StrkPric> [0..1] ± 29
       OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 30
Approved by the Securities SEG on 17 July 2025 auth.017.001.02
FinancialInstrumentReportingReferenceDataReport
V02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
16 July 2025
```

