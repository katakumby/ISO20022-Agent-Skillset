---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.8 Party Identification", "7.1.8.1 PartyIdentification274", "7.1.8.1.3 Identification <Id>", "7.1.8.1.3.2 Other <Othr>", "7.1.8.1.3.2.2 SchemeName <SchmeNm>", "7.1.8.1.3.2.2.1 Code <Cd>"]
file_pages: [153]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.8.1.3.2.2.1 Code <Cd>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 153 to 153.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 153

```text
7.1.8.1.3.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalPersonIdentification1Code" on page 177
7.1.8.1.3.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 183
7.1.8.1.3.2.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 183
7.1.8.1.4  CountryOfResidence <CtryOfRes>
Presence: [0..1]
Definition: Country in which a person resides (the place of a person's home). In the case of a company,
it is the country from which the affairs of that company are directed.
Impacted by: C7 "Country"
Datatype: "CountryCode" on page 174
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.1.8.1.5  ContactDetails <CtctDtls>
Presence: [0..1]
Definition: Set of elements used to indicate how to contact the party.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 153 August 2026
```

