---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification"]
file_pages: [3058]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20 Party Identification

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3058 to 3058.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3058

```text
StatementType <StmtTp> contains one of the following elements (see "StatementType7Choice" on
page 3118 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3118
Or}   Proprietary <Prtry> [1..1] ± 3118
82.1.20 Party Identification
82.1.20.1  AlternatePartyIdentification7
Definition: Alternate identification for a party using an identification type, a country code and a text field.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 3058
   Country <Ctry> [1..1] CodeSet C3 3058
   AlternateIdentification <AltrnId> [1..1] Text 3058
82.1.20.1.1  IdentificationType <IdTp>
Presence: [1..1]
Definition: Specifies the type of alternate identification of the party identified.
IdentificationType <IdTp> contains one of the following elements (see "IdentificationType42Choice"
on page 2963 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2964
Or}   Proprietary <Prtry> [1..1] ± 2964
82.1.20.1.2  Country <Ctry>
Presence: [1..1]
Definition: Country in which a person resides (the place of a person's home). In the case of a company,
it is the country from which the affairs of that company are directed.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
82.1.20.1.3  AlternateIdentification <AltrnId>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3058 August 2026
```

