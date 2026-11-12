---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.12 Party Identification", "10.1.12.1 PartyIdentification272", "10.1.12.1.3 Identification <Id>", "10.1.12.1.3.2 PrivateIdentification <PrvtId>", "10.1.12.1.3.2.2 Other <Othr>", "10.1.12.1.3.2.2.2 SchemeName <SchmeNm>", "10.1.12.1.3.2.2.2.1 Code <Cd>"]
file_pages: [1201]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.12.1.3.2.2.2.1 Code <Cd>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1201 to 1201.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1201

```text
SchemeName <SchmeNm> contains one of the following
PersonIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1201
Or}   Proprietary <Prtry> [1..1] Text 1201
10.1.12.1.3.2.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalPersonIdentification1Code" on page 1232
10.1.12.1.3.2.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 1246
10.1.12.1.3.2.2.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 1246
10.1.12.1.4  CountryOfResidence <CtryOfRes>
Presence: [0..1]
Definition: Country in which a person resides (the place of a person's home). In the case of a company,
it is the country from which the affairs of that company are directed.
Impacted by: C10 "Country"
Datatype: "CountryCode" on page 1226
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
10.1.12.1.5  ContactDetails <CtctDtls>
Presence: [0..1]
Definition: Set of elements used to indicate how to contact the party.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1201 March 2026
```

