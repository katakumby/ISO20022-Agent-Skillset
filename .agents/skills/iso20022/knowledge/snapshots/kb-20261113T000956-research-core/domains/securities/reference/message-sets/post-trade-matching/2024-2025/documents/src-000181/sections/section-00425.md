---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.31 PartyIdentificationAndAccount220", "7.1.20.31.7 AlternateIdentification <AltrnId>"]
file_pages: [491]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.31.7 AlternateIdentification <AltrnId>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 491 to 491.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 491

```text
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails, RegistrationDetails
and PartyContactDetails must not contain information that can be provided in a structured field.
7.1.20.31.7  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Alternate identification for a party.
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification8"
on page 398 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 398
   Country <Ctry> [1..1] CodeSet C4 398
   AlternateIdentification <AltrnId> [1..1] Text 399
7.1.20.32  PartyIdentificationAndAccount219
Definition: Party and account details.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 491 February 2025
```

