---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.7 IndividualPerson38", "66.1.32.7.1 NamePrefix <NmPrfx>", "66.1.32.7.1.2 Proprietary <Prtry>"]
file_pages: [5084]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.7.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5084 to 5084.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5084

```text
66.1.32.7.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name prefix expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.32.7.2  GivenName <GvnNm>
Presence: [0..1]
Definition: First name of the person.
Datatype: "Max35Text" on page 5403
66.1.32.7.3  MiddleName <MddlNm>
Presence: [0..1]
Definition: Second name of the person.
Datatype: "Max35Text" on page 5403
66.1.32.7.4  Name <Nm>
Presence: [1..1]
Definition: Name by which the party is known and which is usually used to identify that person.
Datatype: "Max350Text" on page 5403
66.1.32.7.5  NameSuffix <NmSfx>
Presence: [0..1]
Definition: Additional information about the person that follows a person's name, for example,
qualification such as Doctor of Philosophy (PhD).
Datatype: "Max35Text" on page 5403
66.1.32.7.6  Gender <Gndr>
Presence: [0..1]
Definition: Gender of the person.
Datatype: "Gender1Code" on page 5308
CodeName Name Definition
FEMA Female Individual is a female.
MALE Male Individual is a male.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5084 May 2026
```

