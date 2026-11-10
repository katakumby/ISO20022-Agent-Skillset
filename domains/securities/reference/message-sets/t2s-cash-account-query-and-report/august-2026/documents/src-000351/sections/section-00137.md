---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.8 Party Identification", "7.1.8.1 PartyIdentification274", "7.1.8.1.3 Identification <Id>", "7.1.8.1.3.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>", "7.1.8.1.3.1.4 CountryOfBirth <CtryOfBirth>"]
file_pages: [152]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.8.1.3.1.4 CountryOfBirth <CtryOfBirth>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 152 to 152.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 152

```text
Definition: City where a person was born.
Datatype: "Max35Text" on page 183
7.1.8.1.3.1.4  CountryOfBirth <CtryOfBirth>
Presence: [1..1]
Definition: Country where a person was born.
Impacted by: C7 "Country"
Datatype: "CountryCode" on page 174
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.1.8.1.3.2  Other <Othr>
Presence: [0..*]
Definition: Unique identification of a person, as assigned by an institution, using an identification
scheme.
Other <Othr> contains the following GenericPersonIdentification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 152
   SchemeName <SchmeNm> [0..1]  152
{Or     Code <Cd> [1..1] CodeSet 153
Or}     Proprietary <Prtry> [1..1] Text 153
   Issuer <Issr> [0..1] Text 153
7.1.8.1.3.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of a person.
Datatype: "Max256Text" on page 183
7.1.8.1.3.2.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following
PersonIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 153
Or}   Proprietary <Prtry> [1..1] Text 153
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 152 August 2026
```

