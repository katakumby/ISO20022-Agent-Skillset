---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.22 PartyTextInformation2"]
file_pages: [465]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.22 PartyTextInformation2

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 465 to 465.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 465

```text
Definition: Name and address of a party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 503 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 503
   Address <Adr> [0..1] ± 503
7.1.20.22  PartyTextInformation2
Definition: Provides additional information regarding the party, for example, the contact unit or person
responsible for the transaction identified in the message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 465
   PartyContactDetails <PtyCtctDtls> [0..1] Text 465
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if DeclarationlDetails and/or
PartyContactDetails are present, then they must not contain information that can be provided in a
structured field.
7.1.20.22.1  DeclarationDetails <DclrtnDtls>
Presence: [0..1]
Definition: Provides declaration details narrative relative to the party.
Datatype: "Max350Text" on page 669
7.1.20.22.2  PartyContactDetails <PtyCtctDtls>
Presence: [0..1]
Definition: Provides additional information regarding the party, for example, the contact unit or person
responsible for the transaction identified in the message.
Datatype: "Max140Text" on page 668
7.1.20.23  ConfirmationPartyDetails11
Definition: Parties used for acting parties that apply either to the whole message or to individual sides.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 465 February 2025
```

