---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types", "3.1 MessageComponents", "3.1.4 Person Identification", "3.1.4.1 Contact13", "3.1.4.1.1 NamePrefix <NmPrfx>"]
file_pages: [43]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.1.4.1.1 NamePrefix <NmPrfx>

Source: [src-000011](../../../../../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf). Locator: one-based file pages 43 to 43.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 43

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 43
   Name <Nm> [0..1] Text 43
   PhoneNumber <PhneNb> [0..1] Text 43
   MobileNumber <MobNb> [0..1] Text 44
   FaxNumber <FaxNb> [0..1] Text 44
   URLAddress <URLAdr> [0..1] Text 44
   EmailAddress <EmailAdr> [0..1] Text 44
   EmailPurpose <EmailPurp> [0..1] Text 44
   JobTitle <JobTitl> [0..1] Text 44
   Responsibility <Rspnsblty> [0..1] Text 44
   Department <Dept> [0..1] Text 44
   Other <Othr> [0..*]  45
     ChannelType <ChanlTp> [1..1] Text 45
     Identification <Id> [0..1] Text 45
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 45
3.1.4.1.1  NamePrefix <NmPrfx>
Presence: [0..1]
Definition: Specifies the terms used to formally address a person.
Datatype: "NamePrefix2Code" on page 52
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MADM Madam Title of the person is Madam.
MISS Miss Title of the person is Miss.
MIST Mister Title of the person is Mister or Mr.
MIKS GenderNeutral Title of the person is gender neutral
(Mx).
3.1.4.1.2  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 56
3.1.4.1.3  PhoneNumber <PhneNb>
Presence: [0..1]
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 43 March 2024
```

