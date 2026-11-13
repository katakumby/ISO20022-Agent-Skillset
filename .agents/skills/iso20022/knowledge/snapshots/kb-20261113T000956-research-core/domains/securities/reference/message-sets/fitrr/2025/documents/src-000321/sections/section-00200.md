---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["16 auth.047.001.01 FinancialInstrumentReportingCountryCodeReportV01"]
file_pages: [244]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.047.001.01"]
---

# 16 auth.047.001.01 FinancialInstrumentReportingCountryCodeReportV01

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 244 to 244.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 244

```text
16 auth.047.001.01
FinancialInstrumentReportingCountryCodeR
eportV01
16.1 MessageDefinition Functionality
The FinancialInstrumentReportingCountryCodeReport message provides the details of the two
character country codes and is created by ESMA for distribution to national competent authorities.
Outline
The FinancialInstrumentReportingCountryCodeReportV01 MessageDefinition is composed of 2
MessageBuildingBlocks:
A. CountryData
Report detailing all countries and their 2 character ISO 3166 code.
B. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
16.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FinInstrmRptgCtryCdRpt> [1..1]  
   CountryData <CtryData> [1..*]  245
     Country <Ctry> [1..1] ± 245
     EEACountry <EEACtry> [1..1] Indicator 245
     Modification <Mod> [0..1] CodeSet 245
     ValidityPeriod <VldtyPrd> [1..1] ± 246
     LastUpdated <LastUpdtd> [0..1] Date 246
   SupplementaryData <SplmtryData> [0..*] ± C2 246
16.3 Constraints
C1 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C2 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 17 July 2025 auth.047.001.01
FinancialInstrumentReportingCountryCodeReportV0
1
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
244 July 2025
```

