---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["11 auth.041.001.01 FinancialInstrumentReportingNonEquityTradingActivityReportV01", "11.2 Structure"]
file_pages: [179]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.041.001.01"]
---

# 11.2 Structure

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 179 to 179.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 179

```text
11.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document>
<FinInstrmRptgNonEqtyTradgActvtyRpt>
[1..1]  
   ReportHeader <RptHdr> [1..1] ± 180
   NonEquityTransparencyData <NonEqtyTrnsprncyData> [1..*]  C3, C5 180
     TechnicalRecordIdentification <TechRcrdId> [0..1] Text 181
     Identification <Id> [1..1] IdentifierSet 181
     ReportingDate <RptgDt> [0..1] Date 181
     TradingVenue <TradgVn> [0..1] IdentifierSet 181
     Suspension <Sspnsn> [1..1] Indicator 181
     NumberTransactions <NbTxs> [0..1] Quantity 182
     AggregatedQuantitativeData <AggtdQttvData> [0..*]  182
       NumberOfTransactions <NbOfTxs> [1..1] Quantity 182
       TotalNotionalAmount <TtlNtnlAmt> [1..1] Quantity 182
       Range <Rg> [1..1]  182
         FromQuantity <FrQty> [1..1] Quantity 183
         ToQuantity <ToQty> [1..1] Quantity 183
   SupplementaryData <SplmtryData> [0..*] ± C2 183
11.3 Constraints
C1 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C2 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C3 ValidISINRule
ISIN code must pass checksum validation.
C4 ValidMICRule
Market Identification code must be an active market at the time of reporting.
C5 ValidMICRule
Market Identification code must be an active market at the time of reporting.
Approved by the Securities SEG on 17 July 2025 auth.041.001.01
FinancialInstrumentReportingNonEquityTradingActi
vityReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
179 July 2025
```

