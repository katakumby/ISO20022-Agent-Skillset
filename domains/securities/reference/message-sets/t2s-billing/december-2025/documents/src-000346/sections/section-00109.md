---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.8 Person Identification", "4.1.8.1 Contact13", "4.1.8.1.12 Other <Othr>"]
file_pages: [135]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.8.1.12 Other <Othr>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 135 to 135.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 135

```text
Definition: Identification of a division of a large organisation or building.
Datatype: "Max70Text" on page 154
4.1.8.1.12  Other <Othr>
Presence: [0..*]
Definition: Contact details in another form.
Other <Othr> contains the following OtherContact1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ChannelType <ChanlTp> [1..1] Text 135
   Identification <Id> [0..1] Text 135
4.1.8.1.12.1  ChannelType <ChanlTp>
Presence: [1..1]
Definition: Method used to contact the financial institution's contact for the specific tax region.
Datatype: "Max4Text" on page 153
4.1.8.1.12.2  Identification <Id>
Presence: [0..1]
Definition: Communication value such as phone number or email address.
Datatype: "Max128Text" on page 151
4.1.8.1.13  PreferredMethod <PrefrdMtd>
Presence: [0..1]
Definition: Preferred method used to reach the contact.
Datatype: "PreferredContactMethod2Code" on page 148
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
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 135 December 2025
```

