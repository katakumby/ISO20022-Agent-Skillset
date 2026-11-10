---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.21 Person Identification", "82.1.21.2 Contact13", "82.1.21.2.9 JobTitle <JobTitl>"]
file_pages: [3086]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.21.2.9 JobTitle <JobTitl>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3086 to 3086.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3086

```text
82.1.21.2.9  JobTitle <JobTitl>
Presence: [0..1]
Definition: Title of the function.
Datatype: "Max35Text" on page 3328
82.1.21.2.10  Responsibility <Rspnsblty>
Presence: [0..1]
Definition: Role of a person in an organisation.
Datatype: "Max35Text" on page 3328
82.1.21.2.11  Department <Dept>
Presence: [0..1]
Definition: Identification of a division of a large organisation or building.
Datatype: "Max70Text" on page 3329
82.1.21.2.12  Other <Othr>
Presence: [0..*]
Definition: Contact details in another form.
Other <Othr> contains the following OtherContact1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ChannelType <ChanlTp> [1..1] Text 3086
   Identification <Id> [0..1] Text 3086
82.1.21.2.12.1  ChannelType <ChanlTp>
Presence: [1..1]
Definition: Method used to contact the financial institution's contact for the specific tax region.
Datatype: "Max4Text" on page 3329
82.1.21.2.12.2  Identification <Id>
Presence: [0..1]
Definition: Communication value such as phone number or email address.
Datatype: "Max128Text" on page 3326
82.1.21.2.13  PreferredMethod <PrefrdMtd>
Presence: [0..1]
Definition: Preferred method used to reach the contact.
Datatype: "PreferredContactMethod2Code" on page 3280
CodeName Name Definition
MAIL Email Preferred method used to reach the
contact is per email.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3086 August 2026
```

