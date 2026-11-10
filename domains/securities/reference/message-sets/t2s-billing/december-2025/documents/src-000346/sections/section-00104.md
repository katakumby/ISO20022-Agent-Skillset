---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.7 Party Identification", "4.1.7.3 PartyIdentification272", "4.1.7.3.3 Identification <Id>", "4.1.7.3.3.2 PrivateIdentification <PrvtId>", "4.1.7.3.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>", "4.1.7.3.3.2.1.3 CityOfBirth <CityOfBirth>"]
file_pages: [130]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.7.3.3.2.1.3 CityOfBirth <CityOfBirth>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 130 to 130.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 130

```text
4.1.7.3.3.2.1.3  CityOfBirth <CityOfBirth>
Presence: [1..1]
Definition: City where a person was born.
Datatype: "Max35Text" on page 153
4.1.7.3.3.2.1.4  CountryOfBirth <CtryOfBirth>
Presence: [1..1]
Definition: Country where a person was born.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 144
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
4.1.7.3.3.2.2  Other <Othr>
Presence: [0..*]
Definition: Unique identification of a person, as assigned by an institution, using an identification
scheme.
Other <Othr> contains the following GenericPersonIdentification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 130
   SchemeName <SchmeNm> [0..1]  130
{Or     Code <Cd> [1..1] CodeSet 131
Or}     Proprietary <Prtry> [1..1] Text 131
   Issuer <Issr> [0..1] Text 131
4.1.7.3.3.2.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of a person.
Datatype: "Max256Text" on page 152
4.1.7.3.3.2.2.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 130 December 2025
```

