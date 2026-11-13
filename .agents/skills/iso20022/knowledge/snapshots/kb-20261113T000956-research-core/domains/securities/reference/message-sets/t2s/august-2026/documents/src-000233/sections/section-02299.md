---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.13 PartyTextInformation1"]
file_pages: [3080]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.13 PartyTextInformation1

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3080 to 3080.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3080

```text
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 3098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 3098
   Address <Adr> [0..1] ± 3098
82.1.20.13  PartyTextInformation1
Definition: Provides additional information regarding the party, for example, the contact unit or person
responsible for the transaction identified in the message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 3080
   PartyContactDetails <PtyCtctDtls> [0..1] Text 3080
   RegistrationDetails <RegnDtls> [0..1] Text 3080
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails, RegistrationDetails
and PartyContactDetails must not contain information that can be provided in a structured field.
82.1.20.13.1  DeclarationDetails <DclrtnDtls>
Presence: [0..1]
Definition: Provides declaration details narrative relative to the party.
Datatype: "Max350Text" on page 3328
82.1.20.13.2  PartyContactDetails <PtyCtctDtls>
Presence: [0..1]
Definition: Provides additional information regarding the party, for example, the contact unit or person
responsible for the transaction identified in the message.
Datatype: "Max140Text" on page 3326
82.1.20.13.3  RegistrationDetails <RegnDtls>
Presence: [0..1]
Definition: Provides information required for the registration.
Datatype: "Max350Text" on page 3328
82.1.21 Person Identification
82.1.21.1  Contact14
Definition: Specifies the details of the contact person.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3080 August 2026
```

