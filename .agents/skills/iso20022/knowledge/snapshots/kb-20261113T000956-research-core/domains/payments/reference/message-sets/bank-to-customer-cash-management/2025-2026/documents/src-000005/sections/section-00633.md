---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.16 Party Identification", "6.1.16.1 PartyIdentification272", "6.1.16.1.3 Identification <Id>", "6.1.16.1.3.2 PrivateIdentification <PrvtId>", "6.1.16.1.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>", "6.1.16.1.3.2.1.3 CityOfBirth <CityOfBirth>"]
file_pages: [866]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.16.1.3.2.1.3 CityOfBirth <CityOfBirth>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 866 to 866.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 866

```text
6.1.16.1.3.2.1.3  CityOfBirth <CityOfBirth>
Presence: [1..1]
Definition: City where a person was born.
Datatype: "Max35Text" on page 916
6.1.16.1.3.2.1.4  CountryOfBirth <CtryOfBirth>
Presence: [1..1]
Definition: Country where a person was born.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 892
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
6.1.16.1.3.2.2  Other <Othr>
Presence: [0..*]
Definition: Unique identification of a person, as assigned by an institution, using an identification
scheme.
Other <Othr> contains the following GenericPersonIdentification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 866
   SchemeName <SchmeNm> [0..1]  866
{Or     Code <Cd> [1..1] CodeSet 867
Or}     Proprietary <Prtry> [1..1] Text 867
   Issuer <Issr> [0..1] Text 867
6.1.16.1.3.2.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of a person.
Datatype: "Max256Text" on page 916
6.1.16.1.3.2.2.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
866 March 2026
```

