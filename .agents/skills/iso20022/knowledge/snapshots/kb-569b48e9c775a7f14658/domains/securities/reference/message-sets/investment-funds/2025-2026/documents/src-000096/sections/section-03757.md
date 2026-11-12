---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.46 PartyTextInformation1", "66.1.30.46.1 DeclarationDetails <DclrtnDtls>"]
file_pages: [5044]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.46.1 DeclarationDetails <DclrtnDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5044 to 5044.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5044

```text
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails, RegistrationDetails
and PartyContactDetails must not contain information that can be provided in a structured field.
66.1.30.46.1  DeclarationDetails <DclrtnDtls>
Presence: [0..1]
Definition: Provides declaration details narrative relative to the party.
Datatype: "Max350Text" on page 5403
66.1.30.46.2  PartyContactDetails <PtyCtctDtls>
Presence: [0..1]
Definition: Provides additional information regarding the party, for example, the contact unit or person
responsible for the transaction identified in the message.
Datatype: "Max140Text" on page 5402
66.1.30.46.3  RegistrationDetails <RegnDtls>
Presence: [0..1]
Definition: Provides information required for the registration.
Datatype: "Max350Text" on page 5403
66.1.30.47  AlternatePartyIdentification7
Definition: Alternate identification for a party using an identification type, a country code and a text field.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 5044
   Country <Ctry> [1..1] CodeSet C12 5044
   AlternateIdentification <AltrnId> [1..1] Text 5045
66.1.30.47.1  IdentificationType <IdTp>
Presence: [1..1]
Definition: Specifies the type of alternate identification of the party identified.
IdentificationType <IdTp> contains one of the following elements (see "IdentificationType42Choice"
on page 4547 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4547
Or}   Proprietary <Prtry> [1..1] ± 4547
66.1.30.47.2  Country <Ctry>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5044 May 2026
```

