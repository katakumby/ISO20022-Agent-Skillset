---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.10 Party Identification", "22.1.10.4 PersonIdentification12", "22.1.10.4.2 Other <Othr>", "22.1.10.4.2.2 SchemeName <SchmeNm>"]
file_pages: [347]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.10.4.2.2 SchemeName <SchmeNm>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 347 to 347.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 347

```text
22.1.10.4.2.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following
PersonIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 347
Or}   Proprietary <Prtry> [1..1] Text 347
22.1.10.4.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalPersonIdentification1Code" on page 437
22.1.10.4.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 456
22.1.10.4.2.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 456
22.1.10.5  PersonIdentification10
Definition: Unique and unambiguous way to identify a person.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FirstName <FrstNm> [1..1] Text 348
   Name <Nm> [1..1] Text 348
   BirthDate <BirthDt> [1..1] Date 348
   Other <Othr> [1..1]  348
     Identification <Id> [1..1] Text 348
     SchemeName <SchmeNm> [0..1]  348
{Or       Code <Cd> [1..1] CodeSet 349
Or}       Proprietary <Prtry> [1..1] Text 349
     Issuer <Issr> [0..1] Text 349
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
347 July 2025
```

