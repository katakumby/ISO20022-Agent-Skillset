---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.7 IndividualPerson38", "66.1.32.7.21 GDPRData <GDPRData>", "66.1.32.7.21.3 ConsentDate <CnsntDt>"]
file_pages: [5095]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.7.21.3 ConsentDate <CnsntDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5095 to 5095.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5095

```text
Definition: Indicates whether consent has been given.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.32.7.21.3  ConsentDate <CnsntDt>
Presence: [1..1]
Definition: Date of the consent.
Datatype: "ISODate" on page 5388
66.1.32.8  ContactIdentification2
Definition: Information needed to contact a physical person.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 5095
   GivenName <GvnNm> [0..1] Text 5095
   Name <Nm> [1..1] Text 5096
   PhoneNumber <PhneNb> [0..1] Text 5096
   MobileNumber <MobNb> [0..1] Text 5096
   FaxNumber <FaxNb> [0..1] Text 5096
   EmailAddress <EmailAdr> [0..1] Text 5096
66.1.32.8.1  NamePrefix <NmPrfx>
Presence: [0..1]
Definition: Specifies the terms used to formally address a person.
Datatype: "NamePrefix1Code" on page 5330
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MIST Mister Title of the person is Mister or Mr.
MISS Miss Title of the person is Miss.
MADM Madam Title of the person is Madam.
66.1.32.8.2  GivenName <GvnNm>
Presence: [0..1]
Definition: First name of a person.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5095 May 2026
```

