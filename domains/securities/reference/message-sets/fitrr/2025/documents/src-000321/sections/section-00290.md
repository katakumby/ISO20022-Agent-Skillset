---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.9 Miscellaneous", "22.1.9.3 CountryCodeAndName3", "22.1.9.3.2 Name <Nm>"]
file_pages: [340]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.9.3.2 Name <Nm>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 340 to 340.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 340

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
22.1.9.3.2  Name <Nm>
Presence: [1..1]
Definition: Country is specified by its name.
Datatype: "Max70Text" on page 456
22.1.9.4  GenericValidationRuleIdentification1
Definition: Information for the identification of a validation rule.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 340
   Description <Desc> [0..1] Text 340
   SchemeName <SchmeNm> [0..1] ± 340
   Issuer <Issr> [0..1] Text 341
22.1.9.4.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of a validation rule.
Datatype: "Max35Text" on page 456
22.1.9.4.2  Description <Desc>
Presence: [0..1]
Definition: Further information on the validation rule as identified in the Identification.
Datatype: "Max350Text" on page 455
22.1.9.4.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following elements (see
"ValidationRuleSchemeName1Choice" on page 339 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 339
Or}   Proprietary <Prtry> [1..1] Text 339
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
340 July 2025
```

