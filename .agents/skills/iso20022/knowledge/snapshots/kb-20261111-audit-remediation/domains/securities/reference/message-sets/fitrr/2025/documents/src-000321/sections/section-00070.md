---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["7 auth.035.001.01 FinancialInstrumentReportingTradingVolumeCapDataReportV01", "7.2 Structure"]
file_pages: [86]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.035.001.01"]
---

# 7.2 Structure

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 86 to 86.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 86

```text
7.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FinInstrmRptgTradgVolCapDataRpt> [1..1]  
   ReportHeader <RptHdr> [1..1] ± 87
   VolumeCapData <VolCapData> [1..*]  C6 87
     ReportingPeriod <RptgPrd> [0..1] ± 88
     TradingVenue <TradgVn> [0..1] IdentifierSet 88
     InstrumentReport <InstrmRpt> [1..*]  C4 88
       TechnicalRecordIdentification <TechRcrdId> [0..1] Text 89
       Identification <Id> [1..1] IdentifierSet 89
       Currency <Ccy> [1..1] CodeSet C1 89
       TotalTradingVolume <TtlTradgVol> [1..1] Amount 89
       TotalReferencePriceTradingVolume <TtlRefPricTradgVol> [1..1] Amount 89
       TotalNegotiatedTransactionsTradingVolume
<TtlNgtdTxsTradgVol>
[1..1] Amount 90
   SupplementaryData <SplmtryData> [0..*] ± C3 90
7.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C4 ValidISINRule
ISIN code must pass checksum validation.
C5 ValidMICRule
Market Identification code must be an active market at the time of reporting.
Approved by the Securities SEG on 17 July 2025 auth.035.001.01
FinancialInstrumentReportingTradingVolumeCapDa
taReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
86 July 2025
```

