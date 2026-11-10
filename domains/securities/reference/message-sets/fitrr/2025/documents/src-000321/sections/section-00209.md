---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["18 auth.049.001.02 FinancialInstrumentReportingMarketIdentificationCodeReportV02", "18.4 Message Building Blocks", "18.4.1 MarketIdentification <MktId>"]
file_pages: [254]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.049.001.02"]
---

# 18.4.1 MarketIdentification <MktId>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 254 to 254.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 254

```text
18.4.1 MarketIdentification <MktId>
Presence: [1..*]
Definition: Report of the market and associate descriptive details.
MarketIdentification <MktId> contains the following MarketIdentification95 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Operating <Oprg> [1..1] IdentifierSet 254
   Segment <Sgmt> [1..1] IdentifierSet 254
   Type <Tp> [1..1] CodeSet 254
   Category <Ctgy> [0..1] CodeSet 255
   InstitutionName <InstnNm> [1..1] Text 255
   Acronym <Acrnm> [0..1] Text 256
   City <City> [0..1] Text 256
   Country <Ctry> [1..1] ± 256
   AuthorityName <AuthrtyNm> [0..1] Text 256
   WebSite <WebSite> [0..1] Text 256
   Note <Note> [0..1] Text 256
   Modification <Mod> [0..1] CodeSet 256
   CreationDate <CreDt> [0..1] Date 257
   ValidityPeriod <VldtyPrd> [1..1] ± 257
   StatusDate <StsDt> [0..1] Date 257
   LastUpdatedDate <LastUpdtdDt> [0..1] DateTime 257
18.4.1.1  Operating <Oprg>
Presence: [1..1]
Definition: Operating MIC of the venue.
Datatype: "MICIdentifier" on page 451
18.4.1.2  Segment <Sgmt>
Presence: [1..1]
Definition: Segment MIC of the venue where it exists, otherwise the Operating MIC.
Datatype: "MICIdentifier" on page 451
18.4.1.3  Type <Tp>
Presence: [1..1]
Definition: Define the type of Market Identification Code that is being supplied.
Approved by the Securities SEG on 17 July 2025 auth.049.001.02
FinancialInstrumentReportingMarketIdentificationCo
deReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
254 July 2025
```

