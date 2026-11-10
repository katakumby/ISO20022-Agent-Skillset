---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.18 Person Identification", "16.1.18.2 Contact4", "16.1.18.2.9 Responsibility <Rspnsblty>"]
file_pages: [1057]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.18.2.9 Responsibility <Rspnsblty>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1057 to 1057.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1057

```text
Definition: Title of the function.
Datatype: "Max35Text" on page 1251
16.1.18.2.9  Responsibility <Rspnsblty>
Presence: [0..1]
Definition: Role of a person in an organisation.
Datatype: "Max35Text" on page 1251
16.1.18.2.10  Department <Dept>
Presence: [0..1]
Definition: Identification of a division of a large organisation or building.
Datatype: "Max70Text" on page 1251
16.1.18.2.11  Other <Othr>
Presence: [0..*]
Definition: Contact details in another form.
Other <Othr> contains the following OtherContact1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ChannelType <ChanlTp> [1..1] Text 1057
   Identification <Id> [0..1] Text 1057
16.1.18.2.11.1  ChannelType <ChanlTp>
Presence: [1..1]
Definition: Method used to contact the financial institution's contact for the specific tax region.
Datatype: "Max4Text" on page 1251
16.1.18.2.11.2  Identification <Id>
Presence: [0..1]
Definition: Communication value such as phone number or email address.
Datatype: "Max128Text" on page 1248
16.1.18.2.12  PreferredMethod <PrefrdMtd>
Presence: [0..1]
Definition: Preferred method used to reach the contact.
Datatype: "PreferredContactMethod1Code" on page 1230
CodeName Name Definition
LETT Letter Preferred method used to reach the
contact is per letter.
MAIL Email Preferred method used to reach the
contact is per email.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1057 February 2026
```

