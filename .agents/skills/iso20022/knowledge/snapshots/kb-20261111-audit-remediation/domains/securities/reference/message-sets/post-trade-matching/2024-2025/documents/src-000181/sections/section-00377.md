---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.17 PartyTextInformation5", "7.1.20.17.1 DeclarationDetails <DclrtnDtls>"]
file_pages: [442]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.17.1 DeclarationDetails <DclrtnDtls>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 442 to 442.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 442

```text
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails and
PartyContactDetails must not contain information that can be provided in a structured field.
7.1.20.17.1  DeclarationDetails <DclrtnDtls>
Presence: [0..1]
Definition: Provides declaration details narrative relative to the party.
Datatype: "Max350Text" on page 669
7.1.20.17.2  PartyContactDetails <PtyCtctDtls>
Presence: [0..1]
Definition: Provides additional information regarding the party, eg, the contact unit or person
responsible for the transaction identified in the message.
Datatype: "Max140Text" on page 668
7.1.20.18  PartyIdentificationAndAccount149
Definition: Party and account details.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 442
   AlternateIdentification <AltrnId> [0..1] ± 443
   Side <Sd> [0..1] CodeSet 443
   ClearingAccount <ClrAcct> [0..1] ± 444
   ProcessingIdentification <PrcgId> [0..1] Text 444
   AdditionalInformation <AddtlInf> [0..1] ± C2 444
7.1.20.18.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 442 February 2025
```

