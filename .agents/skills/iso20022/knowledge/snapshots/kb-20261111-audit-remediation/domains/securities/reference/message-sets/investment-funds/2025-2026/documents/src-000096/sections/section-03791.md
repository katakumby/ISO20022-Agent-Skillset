---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.6 IndividualPerson8"]
file_pages: [5079]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.6 IndividualPerson8

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5079 to 5079.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5079

```text
Datatype: "Max35Text" on page 5403
66.1.32.6  IndividualPerson8
Definition: Human entity, as distinguished from a corporate entity (which is sometimes referred to as an
'artificial person').
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5079
   GivenName <GvnNm> [1..1] Text 5079
   NamePrefix <NmPrfx> [0..1] CodeSet 5079
   NameSuffix <NmSfx> [0..1] Text 5080
   Gender <Gndr> [0..1] CodeSet 5080
   BirthDate <BirthDt> [0..1] Date 5080
   SocialSecurityNumber <SclSctyNb> [0..1] Text 5080
   IndividualInvestorAddress <IndvInvstrAdr> [1..1] ± 5080
Constraints
• SocialSecurityNumberGuideline
The UK Insurance Number must be indicated without spaces.
66.1.32.6.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max35Text" on page 5403
66.1.32.6.2  GivenName <GvnNm>
Presence: [1..1]
Definition: First name of a person.
Datatype: "Max35Text" on page 5403
66.1.32.6.3  NamePrefix <NmPrfx>
Presence: [0..1]
Definition: Specifies the terms used to formally address a person.
Datatype: "NamePrefix1Code" on page 5330
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MIST Mister Title of the person is Mister or Mr.
MISS Miss Title of the person is Miss.
MADM Madam Title of the person is Madam.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5079 May 2026
```

