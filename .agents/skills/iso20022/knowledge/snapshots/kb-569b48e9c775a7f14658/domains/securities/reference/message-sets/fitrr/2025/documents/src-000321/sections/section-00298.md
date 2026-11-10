---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.10 Party Identification", "22.1.10.5 PersonIdentification10", "22.1.10.5.1 FirstName <FrstNm>"]
file_pages: [348]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.10.5.1 FirstName <FrstNm>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 348 to 348.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 348

```text
22.1.10.5.1  FirstName <FrstNm>
Presence: [1..1]
Definition: First name of a person (also known as given name).
Datatype: "Max140Text" on page 454
22.1.10.5.2  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 454
22.1.10.5.3  BirthDate <BirthDt>
Presence: [1..1]
Definition: Date on which a person is born.
Datatype: "ISODate" on page 449
22.1.10.5.4  Other <Othr>
Presence: [1..1]
Definition: Unique identification of a person, as assigned by an institution, using an identification
scheme.
Other <Othr> contains the following GenericPersonIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 348
   SchemeName <SchmeNm> [0..1]  348
{Or     Code <Cd> [1..1] CodeSet 349
Or}     Proprietary <Prtry> [1..1] Text 349
   Issuer <Issr> [0..1] Text 349
22.1.10.5.4.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of a person.
Datatype: "Max35Text" on page 456
22.1.10.5.4.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
348 July 2025
```

