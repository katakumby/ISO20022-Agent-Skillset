---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["13 auth.043.001.01 FinancialInstrumentReportingReferenceDataIndexReportV01", "13.4 Message Building Blocks", "13.4.2 IndexData <IndxData>", "13.4.2.1 TechnicalRecordIdentification <TechRcrdId>"]
file_pages: [213]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.043.001.01"]
---

# 13.4.2.1 TechnicalRecordIdentification <TechRcrdId>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 213 to 213.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 213

```text
IndexData <IndxData> contains the following SecuritiesIndexReport1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TechnicalRecordIdentification <TechRcrdId> [0..1] Text 213
   RequestingEntity <RqstngNtty> [0..1] CodeSet C1 213
   Index <Indx> [1..1]  C3 213
{Or     ISIN <ISIN> [1..1] IdentifierSet 214
Or}     Index <Indx> [1..1] CodeSet 214
   ValidityPeriod <VldtyPrd> [0..1] ± 216
13.4.2.1  TechnicalRecordIdentification <TechRcrdId>
Presence: [0..1]
Definition: Unique identifier of a record in a message used as part of error management and feedback
messages.
Usage:
This identification will be used in the status advice sent back.
Datatype: "Max35Text" on page 456
13.4.2.2  RequestingEntity <RqstngNtty>
Presence: [0..1]
Definition: Country code of the entity that wishes to express an interest in receiving transaction reports
for the requested indexes.
Impacted by: C1 "Country"
Datatype: "CountryCode" on page 434
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
13.4.2.3  Index <Indx>
Presence: [1..1]
Definition: Details the index that is being requested.
Impacted by: C3 "ValidISINRule"
Approved by the Securities SEG on 17 July 2025 auth.043.001.01
FinancialInstrumentReportingReferenceDataIndexR
eportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
213 July 2025
```

