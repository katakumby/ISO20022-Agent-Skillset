---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types", "3.1 MessageComponents", "3.1.4 Person Identification"]
file_pages: [42]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.1.4 Person Identification

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 42 to 42.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 42

```text
ContactDetails <CtctDtls> contains the following elements (see "Contact13" on page 42 for details)
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
3.1.4 Person Identification
3.1.4.1  Contact13
Definition: Specifies the details of the contact person.
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 42 March 2024
```

