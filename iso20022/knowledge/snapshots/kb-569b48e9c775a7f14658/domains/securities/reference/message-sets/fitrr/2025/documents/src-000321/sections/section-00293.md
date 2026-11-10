---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.10 Party Identification", "22.1.10.2 PartyIdentification76", "22.1.10.2.1 Identification <Id>", "22.1.10.2.1.1 LEI <LEI>"]
file_pages: [343]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.10.2.1.1 LEI <LEI>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 343 to 343.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 343

```text
Definition: Identifies the owner of the investment account which is used to acquire or sell financial
instruments.
Identification <Id> contains one of the following PersonOrOrganisation1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   LEI <LEI> [1..1] IdentifierSet 343
Or   MIC <MIC> [1..1] IdentifierSet 343
Or   Person <Prsn> [1..1] ± 343
Or}   Internal <Intl> [1..1] CodeSet 343
22.1.10.2.1.1  LEI <LEI>
Presence: [1..1]
Definition: Legal entity identifier of the party.
Datatype: "LEIIdentifier" on page 451
22.1.10.2.1.2  MIC <MIC>
Presence: [1..1]
Definition: Market identifier code of the party.
Datatype: "MICIdentifier" on page 451
22.1.10.2.1.3  Person <Prsn>
Presence: [1..1]
Definition: Identification of a person.
Person <Prsn> contains the following elements (see "PersonIdentification10" on page 347 for details)
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
22.1.10.2.1.4  Internal <Intl>
Presence: [1..1]
Definition: Identifies internal party.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
343 July 2025
```

