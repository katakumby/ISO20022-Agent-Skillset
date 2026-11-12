---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["18 auth.049.001.02 FinancialInstrumentReportingMarketIdentificationCodeReportV02", "18.4 Message Building Blocks", "18.4.1 MarketIdentification <MktId>", "18.4.1.6 Acronym <Acrnm>"]
file_pages: [256]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.049.001.02"]
---

# 18.4.1.6 Acronym <Acrnm>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 256 to 256.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 256

```text
18.4.1.6  Acronym <Acrnm>
Presence: [0..1]
Definition: Known acronym of the institution, market, or infrastructure.
Datatype: "Max35Text" on page 456
18.4.1.7  City <City>
Presence: [0..1]
Definition: City where the institution, market, or infrastructure operates.
Datatype: "Max35Text" on page 456
18.4.1.8  Country <Ctry>
Presence: [1..1]
Definition: Two character country code and country name as per ISO 3166.
Country <Ctry> contains the following elements (see "CountryCodeAndName3" on page 339 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] CodeSet C4 339
   Name <Nm> [1..1] Text 340
18.4.1.9  AuthorityName <AuthrtyNm>
Presence: [0..1]
Definition: The name of the national competent authority associated with the MIC.
Datatype: "Max450Text" on page 456
18.4.1.10  WebSite <WebSite>
Presence: [0..1]
Definition: Website URI of the institution, market, or infrastructure.
Datatype: "Max210Text" on page 455
18.4.1.11  Note <Note>
Presence: [0..1]
Definition: Details additional information about the market operator.
Datatype: "Max450Text" on page 456
18.4.1.12  Modification <Mod>
Presence: [0..1]
Definition: Additional information to help users identify the exchange or understand a modification.
Datatype: "Modification1Code" on page 439
Approved by the Securities SEG on 17 July 2025 auth.049.001.02
FinancialInstrumentReportingMarketIdentificationCo
deReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
256 July 2025
```

