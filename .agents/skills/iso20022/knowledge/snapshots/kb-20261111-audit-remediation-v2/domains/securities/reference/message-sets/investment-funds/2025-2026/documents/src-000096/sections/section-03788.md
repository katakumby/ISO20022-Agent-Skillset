---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.5 IndividualPerson32", "66.1.32.5.1 Name <Nm>"]
file_pages: [5076]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.5.1 Name <Nm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5076 to 5076.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5076

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 5076
   BirthDate <BirthDt> [0..1] Date 5076
   CountryAndResidentialStatus <CtryAndResdtlSts> [0..1] ± 5076
   OtherIdentification <OthrId> [0..*]  5076
     Identification <Id> [1..1] Text 5077
     IdentificationType <IdTp> [1..1]  5077
{Or       Code <Cd> [1..1] CodeSet 5077
Or}       Proprietary <Prtry> [1..1] ± 5078
     Issuer <Issr> [0..1] Text 5078
Constraints
• PersonElementRule
One of the elements (Name, BirthDate, CountryAndResidentialStatus, OtherIdentification) must be
present.
66.1.32.5.1  Name <Nm>
Presence: [0..1]
Definition: Name by which the party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 5403
66.1.32.5.2  BirthDate <BirthDt>
Presence: [0..1]
Definition: Date on which the person is born.
Datatype: "ISODate" on page 5388
66.1.32.5.3  CountryAndResidentialStatus <CtryAndResdtlSts>
Presence: [0..1]
Definition: Country and residential status of the individual, for example, non-permanent resident.
CountryAndResidentialStatus <CtryAndResdtlSts> contains the following elements (see
"CountryAndResidentialStatusType2" on page 5004 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [1..1] CodeSet C12 5004
   ResidentialStatus <ResdtlSts> [1..1] CodeSet 5004
66.1.32.5.4  OtherIdentification <OthrId>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5076 May 2026
```

