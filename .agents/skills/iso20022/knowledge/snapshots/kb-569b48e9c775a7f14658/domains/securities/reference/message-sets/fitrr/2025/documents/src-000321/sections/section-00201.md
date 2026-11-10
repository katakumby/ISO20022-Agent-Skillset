---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["16 auth.047.001.01 FinancialInstrumentReportingCountryCodeReportV01", "16.4 Message Building Blocks"]
file_pages: [245]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.047.001.01"]
---

# 16.4 Message Building Blocks

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 245 to 245.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 245

```text
16.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
16.4.1 CountryData <CtryData>
Presence: [1..*]
Definition: Report detailing all countries and their 2 character ISO 3166 code.
CountryData <CtryData> contains the following SecuritiesCountryIdentification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [1..1] ± 245
   EEACountry <EEACtry> [1..1] Indicator 245
   Modification <Mod> [0..1] CodeSet 245
   ValidityPeriod <VldtyPrd> [1..1] ± 246
   LastUpdated <LastUpdtd> [0..1] Date 246
16.4.1.1  Country <Ctry>
Presence: [1..1]
Definition: Two character country code and country name as per ISO 3166.
Country <Ctry> contains the following elements (see "CountryCodeAndName3" on page 339 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] CodeSet C4 339
   Name <Nm> [1..1] Text 340
16.4.1.2  EEACountry <EEACtry>
Presence: [1..1]
Definition: Flag which reflects if the country is a member of the EEA (European Economic Area) or not.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
16.4.1.3  Modification <Mod>
Presence: [0..1]
Definition: Modification status for the record compared to the previous report.
Datatype: "Modification1Code" on page 439
Approved by the Securities SEG on 17 July 2025 auth.047.001.01
FinancialInstrumentReportingCountryCodeReportV0
1
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
245 July 2025
```

