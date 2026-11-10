---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.10 Party Identification", "22.1.10.4 PersonIdentification12", "22.1.10.4.1 CountryOfBranch <CtryOfBrnch>"]
file_pages: [346]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.10.4.1 CountryOfBranch <CtryOfBrnch>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 346 to 346.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 346

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CountryOfBranch <CtryOfBrnch> [1..1] CodeSet C4 346
   Other <Othr> [1..1]  346
     Identification <Id> [1..1] Text 346
     SchemeName <SchmeNm> [0..1]  347
{Or       Code <Cd> [1..1] CodeSet 347
Or}       Proprietary <Prtry> [1..1] Text 347
     Issuer <Issr> [0..1] Text 347
22.1.10.4.1  CountryOfBranch <CtryOfBrnch>
Presence: [1..1]
Definition: Branch where the trader is located.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 434
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
22.1.10.4.2  Other <Othr>
Presence: [1..1]
Definition: Unique identification of a person, as assigned by an institution, using an identification
scheme.
Other <Othr> contains the following GenericPersonIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 346
   SchemeName <SchmeNm> [0..1]  347
{Or     Code <Cd> [1..1] CodeSet 347
Or}     Proprietary <Prtry> [1..1] Text 347
   Issuer <Issr> [0..1] Text 347
22.1.10.4.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of a person.
Datatype: "Max35Text" on page 456
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
346 July 2025
```

