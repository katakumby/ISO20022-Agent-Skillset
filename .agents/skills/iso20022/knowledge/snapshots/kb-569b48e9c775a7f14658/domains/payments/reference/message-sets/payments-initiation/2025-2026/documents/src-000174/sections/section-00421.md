---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Person Identification"]
file_pages: [572]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15 Person Identification

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 572 to 572.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 572

```text
Definition: Category purpose, in a proprietary form.
Datatype: "Max35Text" on page 609
6.1.15 Person Identification
6.1.15.1  Contact13
Definition: Specifies the details of the contact person.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 572
   Name <Nm> [0..1] Text 573
   PhoneNumber <PhneNb> [0..1] Text 573
   MobileNumber <MobNb> [0..1] Text 573
   FaxNumber <FaxNb> [0..1] Text 573
   URLAddress <URLAdr> [0..1] Text 573
   EmailAddress <EmailAdr> [0..1] Text 573
   EmailPurpose <EmailPurp> [0..1] Text 573
   JobTitle <JobTitl> [0..1] Text 573
   Responsibility <Rspnsblty> [0..1] Text 574
   Department <Dept> [0..1] Text 574
   Other <Othr> [0..*]  574
     ChannelType <ChanlTp> [1..1] Text 574
     Identification <Id> [0..1] Text 574
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 574
6.1.15.1.1  NamePrefix <NmPrfx>
Presence: [0..1]
Definition: Specifies the terms used to formally address a person.
Datatype: "NamePrefix2Code" on page 598
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MADM Madam Title of the person is Madam.
MISS Miss Title of the person is Miss.
MIST Mister Title of the person is Mister or Mr.
MIKS GenderNeutral Title of the person is gender neutral
(Mx).
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 572 March 2026
```

