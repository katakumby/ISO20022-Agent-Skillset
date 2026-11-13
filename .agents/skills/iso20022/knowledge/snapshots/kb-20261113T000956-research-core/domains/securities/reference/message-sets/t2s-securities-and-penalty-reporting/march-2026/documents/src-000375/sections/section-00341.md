---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Party Identification", "7.1.19.8 PartyIdentification272", "7.1.19.8.3 Identification <Id>", "7.1.19.8.3.2 PrivateIdentification <PrvtId>", "7.1.19.8.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>", "7.1.19.8.3.2.1.3 CityOfBirth <CityOfBirth>"]
file_pages: [428]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.8.3.2.1.3 CityOfBirth <CityOfBirth>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 428 to 428.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 428

```text
7.1.19.8.3.2.1.3  CityOfBirth <CityOfBirth>
Presence: [1..1]
Definition: City where a person was born.
Datatype: "Max35Text" on page 557
7.1.19.8.3.2.1.4  CountryOfBirth <CtryOfBirth>
Presence: [1..1]
Definition: Country where a person was born.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 501
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.1.19.8.3.2.2  Other <Othr>
Presence: [0..*]
Definition: Unique identification of a person, as assigned by an institution, using an identification
scheme.
Other <Othr> contains the following GenericPersonIdentification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 428
   SchemeName <SchmeNm> [0..1]  428
{Or     Code <Cd> [1..1] CodeSet 429
Or}     Proprietary <Prtry> [1..1] Text 429
   Issuer <Issr> [0..1] Text 429
7.1.19.8.3.2.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of a person.
Datatype: "Max256Text" on page 557
7.1.19.8.3.2.2.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 428 March 2026
```

