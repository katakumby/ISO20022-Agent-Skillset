---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["9 auth.039.001.01 FinancialInstrumentReportingNonWorkingDayReportV01", "9.4 Message Building Blocks", "9.4.2 NonWorkingDay <NonWorkgDay>", "9.4.2.1 Identification <Id>"]
file_pages: [168]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.039.001.01"]
---

# 9.4.2.1 Identification <Id>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 168 to 168.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 168

```text
9.4.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the specific venue this relates to - operating MIC, segment MIC, NCA
Impacted by: C3 "ValidMICRule"
Identification <Id> contains one of the following elements (see "TradingVenueIdentification1Choice"
on page 337 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentificationCode <MktIdCd> [1..1] IdentifierSet 337
Or   NationalCompetentAuthority <NtlCmptntAuthrty> [1..1] CodeSet C4 337
Or}   Other <Othr> [1..1] ± 338
Constraints
• ValidMICRule
Market Identification code must be an active market at the time of reporting.
9.4.2.2  NonWorkingDay <NonWorkgDay>
Presence: [1..*]
Definition: Provides the non working days of the identified venue. Details on why it is a non working day
are also captured.
NonWorkingDay <NonWorkgDay> contains the following SecuritiesNonTradingDay1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TechnicalRecordIdentification <TechRcrdId> [0..1] Text 168
   Date <Dt> [1..1] Date 168
   Reason <Rsn> [0..1] CodeSet 169
9.4.2.2.1  TechnicalRecordIdentification <TechRcrdId>
Presence: [0..1]
Definition: Unique identifier of a record in a message used as part of error management and status
advice messages.
Usage:
This identification will be used in the status advice report sent back.
Datatype: "Max35Text" on page 456
9.4.2.2.2  Date <Dt>
Presence: [1..1]
Definition: Non-working date.
Approved by the Securities SEG on 17 July 2025 auth.039.001.01
FinancialInstrumentReportingNonWorkingDayRepor
tV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
168 July 2025
```

