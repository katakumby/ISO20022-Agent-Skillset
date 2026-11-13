---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types", "3.1 MessageComponents", "3.1.4 Person Identification", "3.1.4.1 Contact13", "3.1.4.1.12 Other <Othr>"]
file_pages: [45]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.1.4.1.12 Other <Othr>

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 45 to 45.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 45

```text
Definition: Identification of a division of a large organisation or building.
Datatype: "Max70Text" on page 57
3.1.4.1.12  Other <Othr>
Presence: [0..*]
Definition: Contact details in another form.
Other <Othr> contains the following OtherContact1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ChannelType <ChanlTp> [1..1] Text 45
   Identification <Id> [0..1] Text 45
3.1.4.1.12.1  ChannelType <ChanlTp>
Presence: [1..1]
Definition: Method used to contact the financial institution's contact for the specific tax region.
Datatype: "Max4Text" on page 57
3.1.4.1.12.2  Identification <Id>
Presence: [0..1]
Definition: Communication value such as phone number or email address.
Datatype: "Max128Text" on page 55
3.1.4.1.13  PreferredMethod <PrefrdMtd>
Presence: [0..1]
Definition: Preferred method used to reach the contact.
Datatype: "PreferredContactMethod2Code" on page 53
CodeName Name Definition
MAIL Email Preferred method used to reach the
contact is per email.
FAXX Fax Preferred method used to reach the
contact is per fax.
LETT Letter Preferred method used to reach the
contact is per letter.
CELL MobileOrCellPhone Preferred method used to reach the
contact is per mobile or cell phone.
ONLI Online Preferred method used to reach the
contact is online.
PHON Phone Preferred method used to reach the
contact is per phone.
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 45 March 2024
```

