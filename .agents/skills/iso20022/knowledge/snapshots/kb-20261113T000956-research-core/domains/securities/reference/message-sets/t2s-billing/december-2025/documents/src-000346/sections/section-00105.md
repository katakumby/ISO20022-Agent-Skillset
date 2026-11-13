---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.7 Party Identification", "4.1.7.3 PartyIdentification272", "4.1.7.3.3 Identification <Id>", "4.1.7.3.3.2 PrivateIdentification <PrvtId>", "4.1.7.3.3.2.2 Other <Othr>", "4.1.7.3.3.2.2.2 SchemeName <SchmeNm>", "4.1.7.3.3.2.2.2.1 Code <Cd>"]
file_pages: [131]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.7.3.3.2.2.2.1 Code <Cd>

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 131 to 131.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 131

```text
SchemeName <SchmeNm> contains one of the following
PersonIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 131
Or}   Proprietary <Prtry> [1..1] Text 131
4.1.7.3.3.2.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalPersonIdentification1Code" on page 147
4.1.7.3.3.2.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 153
4.1.7.3.3.2.2.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 153
4.1.7.3.4  CountryOfResidence <CtryOfRes>
Presence: [0..1]
Definition: Country in which a person resides (the place of a person's home). In the case of a company,
it is the country from which the affairs of that company are directed.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 144
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
4.1.7.3.5  ContactDetails <CtctDtls>
Presence: [0..1]
Definition: Set of elements used to indicate how to contact the party.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 131 December 2025
```

