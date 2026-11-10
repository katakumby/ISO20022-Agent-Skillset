---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.7 RegisteredShareholderName1Choice", "66.1.30.7.1 IndividualPerson <IndvPrsn>"]
file_pages: [4918]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.7.1 IndividualPerson <IndvPrsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4918 to 4918.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4918

```text
66.1.30.7.1  IndividualPerson <IndvPrsn>
Presence: [1..1]
Definition: Human entity, as distinguished from a corporate entity (which is sometimes referred to as an
'artificial person').
IndividualPerson <IndvPrsn> contains the following IndividualPerson29 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1]  4918
{Or     Code <Cd> [1..1] CodeSet 4918
Or}     Proprietary <Prtry> [1..1] ± 4918
   GivenName <GvnNm> [0..1] Text 4919
   MiddleName <MddlNm> [0..1] Text 4919
   Name <Nm> [1..1] Text 4919
   PostalAddress <PstlAdr> [1..5] ± C23 4919
66.1.30.7.1.1  NamePrefix <NmPrfx>
Presence: [0..1]
Definition: Term used to address the person.
NamePrefix <NmPrfx> contains one of the following NamePrefix1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4918
Or}   Proprietary <Prtry> [1..1] ± 4918
66.1.30.7.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Name prefix expressed as a code.
Datatype: "NamePrefix1Code" on page 5330
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MIST Mister Title of the person is Mister or Mr.
MISS Miss Title of the person is Miss.
MADM Madam Title of the person is Madam.
66.1.30.7.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name prefix expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4918 May 2026
```

