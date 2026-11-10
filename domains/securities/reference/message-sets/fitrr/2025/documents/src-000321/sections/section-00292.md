---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.10 Party Identification", "22.1.10.1 DerivativePartyIdentification1Choice", "22.1.10.1.1 Country <Ctry>"]
file_pages: [342]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.10.1.1 Country <Ctry>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 342 to 342.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 342

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Country <Ctry> [1..1] CodeSet C4 342
Or   CountrySubDivision <CtrySubDvsn> [1..1] CodeSet 342
Or}   LEI <LEI> [1..1] IdentifierSet 342
22.1.10.1.1  Country <Ctry>
Presence: [1..1]
Definition: Country of the reference entity.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 434
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
22.1.10.1.2  CountrySubDivision <CtrySubDvsn>
Presence: [1..1]
Definition: Country and country sub-division of the reference entity.
Datatype: "CountrySubDivisionCode" on page 434
22.1.10.1.3  LEI <LEI>
Presence: [1..1]
Definition: Identification of the reference party through Legal entity identifier.
Datatype: "LEIIdentifier" on page 451
22.1.10.2  PartyIdentification76
Definition: Set of elements used to identify a person or an organisation.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  342
{Or     LEI <LEI> [1..1] IdentifierSet 343
Or     MIC <MIC> [1..1] IdentifierSet 343
Or     Person <Prsn> [1..1] ± 343
Or}     Internal <Intl> [1..1] CodeSet 343
   CountryOfBranch <CtryOfBrnch> [0..1] CodeSet C4 344
22.1.10.2.1  Identification <Id>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
342 July 2025
```

