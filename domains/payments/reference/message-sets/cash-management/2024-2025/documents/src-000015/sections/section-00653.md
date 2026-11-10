---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.12 Party Identification", "37.1.12.1 PartyIdentification272", "37.1.12.1.3 Identification <Id>", "37.1.12.1.3.2 PrivateIdentification <PrvtId>", "37.1.12.1.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>", "37.1.12.1.3.2.1.3 CityOfBirth <CityOfBirth>"]
file_pages: [830]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.12.1.3.2.1.3 CityOfBirth <CityOfBirth>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 830 to 830.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 830

```text
37.1.12.1.3.2.1.3  CityOfBirth <CityOfBirth>
Presence: [1..1]
Definition: City where a person was born.
Datatype: "Max35Text" on page 889
37.1.12.1.3.2.1.4  CountryOfBirth <CtryOfBirth>
Presence: [1..1]
Definition: Country where a person was born.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 851
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
37.1.12.1.3.2.2  Other <Othr>
Presence: [0..*]
Definition: Unique identification of a person, as assigned by an institution, using an identification
scheme.
Other <Othr> contains the following GenericPersonIdentification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 830
   SchemeName <SchmeNm> [0..1]  830
{Or     Code <Cd> [1..1] CodeSet 831
Or}     Proprietary <Prtry> [1..1] Text 831
   Issuer <Issr> [0..1] Text 831
37.1.12.1.3.2.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of a person.
Datatype: "Max256Text" on page 889
37.1.12.1.3.2.2.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 830 February 2025
```

