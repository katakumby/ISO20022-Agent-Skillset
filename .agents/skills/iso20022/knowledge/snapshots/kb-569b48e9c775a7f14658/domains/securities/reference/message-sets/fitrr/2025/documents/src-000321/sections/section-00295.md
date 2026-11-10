---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.10 Party Identification", "22.1.10.3 PartyIdentification79", "22.1.10.3.2 DecisionMaker <DcsnMakr>"]
file_pages: [345]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.10.3.2 DecisionMaker <DcsnMakr>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 345 to 345.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 345

```text
22.1.10.3.2  DecisionMaker <DcsnMakr>
Presence: [0..*]
Definition: Identifies the person who makes the decision on the financial instrument, acquire in case the
of a buyer or to sell in case of the seller.
DecisionMaker <DcsnMakr> contains one of the following PersonOrOrganisation2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   LEI <LEI> [1..1] IdentifierSet 345
Or}   Person <Prsn> [1..1] ± 345
22.1.10.3.2.1  LEI <LEI>
Presence: [1..1]
Definition: Legal entity identifier of the party.
Datatype: "LEIIdentifier" on page 451
22.1.10.3.2.2  Person <Prsn>
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
22.1.10.4  PersonIdentification12
Definition: Specifies the identification of a person.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
345 July 2025
```

