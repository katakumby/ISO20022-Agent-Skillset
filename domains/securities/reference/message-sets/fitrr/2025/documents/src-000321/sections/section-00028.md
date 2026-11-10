---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02", "3.4 Message Building Blocks", "3.4.2 ReferenceData <RefData>", "3.4.2.7 TechnicalAttributes <TechAttrbts>", "3.4.2.7.3 SubmissionDateTime <SubmissnDtTm>"]
file_pages: [37]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.017.001.02"]
---

# 3.4.2.7.3 SubmissionDateTime <SubmissnDtTm>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 37 to 37.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 37

```text
3.4.2.7.3  SubmissionDateTime <SubmissnDtTm>
Presence: [0..1]
Definition: Defines the date and time when this instrument was originally received at the submission
destination.
Datatype: "ISODateTime" on page 449
3.4.2.7.4  RelevantCompetentAuthority <RlvntCmptntAuthrty>
Presence: [0..1]
Definition: Country code of the relevant competent authority of the instrument.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 434
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
3.4.2.7.5  PublicationPeriod <PblctnPrd>
Presence: [0..1]
Definition: Period for which the associated instrument has been publically available.
PublicationPeriod <PblctnPrd> contains one of the following elements (see "Period4Choice" on
page 322 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 322
Or   FromDate <FrDt> [1..1] Date 323
Or   ToDate <ToDt> [1..1] Date 323
Or}   FromDateToDate <FrDtToDt> [1..1] ± 323
3.4.2.7.6  NeverPublished <NvrPblshd>
Presence: [0..1]
Definition: Flag to say if the record has ever been published.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
3.4.2.7.7  RelevantTradingVenue <RlvntTradgVn>
Presence: [0..1]
Definition: Trading venue of the record used by the relevant competent authority to determine the
reference data for the instrument.
Approved by the Securities SEG on 17 July 2025 auth.017.001.02
FinancialInstrumentReportingReferenceDataReport
V02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
37 July 2025
```

