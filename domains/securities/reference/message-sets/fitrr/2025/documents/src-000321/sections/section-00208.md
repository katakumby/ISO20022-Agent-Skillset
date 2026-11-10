---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["18 auth.049.001.02 FinancialInstrumentReportingMarketIdentificationCodeReportV02", "18.2 Structure"]
file_pages: [253]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.049.001.02"]
---

# 18.2 Structure

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 253 to 253.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 253

```text
18.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FinInstrmRptgMktIdCdRpt> [1..1]  
   MarketIdentification <MktId> [1..*]  254
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
   SupplementaryData <SplmtryData> [0..*] ± C2 257
18.3 Constraints
C1 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C2 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
18.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Securities SEG on 17 July 2025 auth.049.001.02
FinancialInstrumentReportingMarketIdentificationCo
deReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
253 July 2025
```

