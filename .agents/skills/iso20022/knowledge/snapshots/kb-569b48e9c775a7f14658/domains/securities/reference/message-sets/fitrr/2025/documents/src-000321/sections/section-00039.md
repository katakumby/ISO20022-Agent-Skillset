---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["5 auth.032.001.01 FinancialInstrumentReportingEquityTransparencyDataReportV01", "5.2 Structure"]
file_pages: [49]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.032.001.01"]
---

# 5.2 Structure

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 49 to 49.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 49

```text
5.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document>
<FinInstrmRptgEqtyTrnsprncyDataRpt>
[1..1]  
   ReportHeader <RptHdr> [1..1] ± 50
   EquityTransparencyData <EqtyTrnsprncyData> [1..*]  C5, C7 50
     TechnicalRecordIdentification <TechRcrdId> [0..1] Text 51
     Identification <Id> [1..1] IdentifierSet 51
     FullName <FullNm> [0..1] Text 51
     TradingVenue <TradgVn> [0..1] IdentifierSet 52
     ReportingDate <RptgDt> [0..1] Date 52
     FinancialInstrumentClassification <FinInstrmClssfctn> [1..1] CodeSet 52
     NumberOutstandingInstruments <NbOutsdngInstrms> [0..1] Quantity 52
     HoldingsExceedingTotalVotingRightThreshold
<HldgsExcdgTtlVtngRghtThrshld>
[0..1] Quantity 52
     IssuanceSize <IssncSz> [0..1] Amount C1, C3 53
     InstrumentPrice <InstrmPric> [0..1] Amount C1 53
   SupplementaryData <SplmtryData> [0..*] ± C4 53
5.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C4 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 17 July 2025 auth.032.001.01
FinancialInstrumentReportingEquityTransparencyD
ataReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
49 July 2025
```

