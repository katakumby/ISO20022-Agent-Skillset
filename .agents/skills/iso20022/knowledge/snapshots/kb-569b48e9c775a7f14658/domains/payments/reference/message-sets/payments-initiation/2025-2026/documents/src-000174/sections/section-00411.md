---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.12 Party Identification", "6.1.12.1 PartyIdentification272", "6.1.12.1.3 Identification <Id>", "6.1.12.1.3.2 PrivateIdentification <PrvtId>", "6.1.12.1.3.2.2 Other <Othr>", "6.1.12.1.3.2.2.2 SchemeName <SchmeNm>", "6.1.12.1.3.2.2.2.1 Code <Cd>"]
file_pages: [562]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.12.1.3.2.2.2.1 Code <Cd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 562 to 562.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 562

```text
SchemeName <SchmeNm> contains one of the following
PersonIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 562
Or}   Proprietary <Prtry> [1..1] Text 562
6.1.12.1.3.2.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalPersonIdentification1Code" on page 596
6.1.12.1.3.2.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 609
6.1.12.1.3.2.2.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 609
6.1.12.1.4  CountryOfResidence <CtryOfRes>
Presence: [0..1]
Definition: Country in which a person resides (the place of a person's home). In the case of a company,
it is the country from which the affairs of that company are directed.
Impacted by: C18 "Country"
Datatype: "CountryCode" on page 590
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
6.1.12.1.5  ContactDetails <CtctDtls>
Presence: [0..1]
Definition: Set of elements used to indicate how to contact the party.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 562 March 2026
```

