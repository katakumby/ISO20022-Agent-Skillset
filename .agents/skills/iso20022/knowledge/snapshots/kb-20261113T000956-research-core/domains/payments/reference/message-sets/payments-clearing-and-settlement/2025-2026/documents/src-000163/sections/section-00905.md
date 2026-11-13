---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.12 Party Identification", "10.1.12.1 PartyIdentification272", "10.1.12.1.3 Identification <Id>", "10.1.12.1.3.2 PrivateIdentification <PrvtId>", "10.1.12.1.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>", "10.1.12.1.3.2.1.3 CityOfBirth <CityOfBirth>"]
file_pages: [1200]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.12.1.3.2.1.3 CityOfBirth <CityOfBirth>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1200 to 1200.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1200

```text
10.1.12.1.3.2.1.3  CityOfBirth <CityOfBirth>
Presence: [1..1]
Definition: City where a person was born.
Datatype: "Max35Text" on page 1246
10.1.12.1.3.2.1.4  CountryOfBirth <CtryOfBirth>
Presence: [1..1]
Definition: Country where a person was born.
Impacted by: C10 "Country"
Datatype: "CountryCode" on page 1226
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
10.1.12.1.3.2.2  Other <Othr>
Presence: [0..*]
Definition: Unique identification of a person, as assigned by an institution, using an identification
scheme.
Other <Othr> contains the following GenericPersonIdentification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1200
   SchemeName <SchmeNm> [0..1]  1200
{Or     Code <Cd> [1..1] CodeSet 1201
Or}     Proprietary <Prtry> [1..1] Text 1201
   Issuer <Issr> [0..1] Text 1201
10.1.12.1.3.2.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of a person.
Datatype: "Max256Text" on page 1245
10.1.12.1.3.2.2.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1200 March 2026
```

