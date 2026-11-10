---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.13 Person Identification", "37.1.13.1 Contact13", "37.1.13.1.12 Other <Othr>"]
file_pages: [835]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.13.1.12 Other <Othr>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 835 to 835.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 835

```text
Definition: Identification of a division of a large organisation or building.
Datatype: "Max70Text" on page 890
37.1.13.1.12  Other <Othr>
Presence: [0..*]
Definition: Contact details in another form.
Other <Othr> contains the following OtherContact1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ChannelType <ChanlTp> [1..1] Text 835
   Identification <Id> [0..1] Text 835
37.1.13.1.12.1  ChannelType <ChanlTp>
Presence: [1..1]
Definition: Method used to contact the financial institution's contact for the specific tax region.
Datatype: "Max4Text" on page 890
37.1.13.1.12.2  Identification <Id>
Presence: [0..1]
Definition: Communication value such as phone number or email address.
Datatype: "Max128Text" on page 887
37.1.13.1.13  PreferredMethod <PrefrdMtd>
Presence: [0..1]
Definition: Preferred method used to reach the contact.
Datatype: "PreferredContactMethod2Code" on page 870
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
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 835 February 2025
```

