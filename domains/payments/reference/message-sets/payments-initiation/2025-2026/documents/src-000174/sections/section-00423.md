---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Person Identification", "6.1.15.1 Contact13", "6.1.15.1.10 Responsibility <Rspnsblty>"]
file_pages: [574]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15.1.10 Responsibility <Rspnsblty>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 574 to 574.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 574

```text
6.1.15.1.10  Responsibility <Rspnsblty>
Presence: [0..1]
Definition: Role of a person in an organisation.
Datatype: "Max35Text" on page 609
6.1.15.1.11  Department <Dept>
Presence: [0..1]
Definition: Identification of a division of a large organisation or building.
Datatype: "Max70Text" on page 610
6.1.15.1.12  Other <Othr>
Presence: [0..*]
Definition: Contact details in another form.
Other <Othr> contains the following OtherContact1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ChannelType <ChanlTp> [1..1] Text 574
   Identification <Id> [0..1] Text 574
6.1.15.1.12.1  ChannelType <ChanlTp>
Presence: [1..1]
Definition: Method used to contact the financial institution's contact for the specific tax region.
Datatype: "Max4Text" on page 609
6.1.15.1.12.2  Identification <Id>
Presence: [0..1]
Definition: Communication value such as phone number or email address.
Datatype: "Max128Text" on page 608
6.1.15.1.13  PreferredMethod <PrefrdMtd>
Presence: [0..1]
Definition: Preferred method used to reach the contact.
Datatype: "PreferredContactMethod2Code" on page 600
CodeName Name Definition
MAIL Email Preferred method used to reach the
contact is per email.
FAXX Fax Preferred method used to reach the
contact is per fax.
LETT Letter Preferred method used to reach the
contact is per letter.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 574 March 2026
```

