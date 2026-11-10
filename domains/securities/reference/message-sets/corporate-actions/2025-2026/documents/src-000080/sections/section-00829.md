---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.17 Party Identification", "16.1.17.8 AlternatePartyIdentification7", "16.1.17.8.2 Country <Ctry>"]
file_pages: [1047]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.17.8.2 Country <Ctry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1047 to 1047.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1047

```text
IdentificationType <IdTp> contains one of the following elements (see "IdentificationType42Choice"
on page 877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 877
Or}   Proprietary <Prtry> [1..1] ± 878
16.1.17.8.2  Country <Ctry>
Presence: [1..1]
Definition: Country in which a person resides (the place of a person's home). In the case of a company,
it is the country from which the affairs of that company are directed.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 1205
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
16.1.17.8.3  AlternateIdentification <AltrnId>
Presence: [1..1]
Definition: Alternate identification for a party.
Datatype: "Max35Text" on page 1251
16.1.17.9  AlternatePartyIdentification12
Definition: Alternate identification for a party using an identification type, a country code and a text field.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 1047
   Country <Ctry> [1..1] CodeSet C3 1048
   AlternateIdentification <AltrnId> [1..1] Text 1048
   LEI <LEI> [0..1] IdentifierSet 1048
16.1.17.9.1  IdentificationType <IdTp>
Presence: [1..1]
Definition: Specifies the type of alternate identification of the party identified.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1047 February 2026
```

