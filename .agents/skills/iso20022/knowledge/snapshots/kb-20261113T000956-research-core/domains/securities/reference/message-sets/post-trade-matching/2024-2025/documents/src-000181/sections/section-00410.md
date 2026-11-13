---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.25 PartyIdentificationAndAccount152", "7.1.20.25.4 AlternateIdentification <AltrnId>"]
file_pages: [476]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.25.4 AlternateIdentification <AltrnId>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 476 to 476.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 476

```text
AdditionalInformation <AddtlInf> contains the following elements (see "PartyTextInformation1" on
page 484 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 484
   PartyContactDetails <PtyCtctDtls> [0..1] Text 484
   RegistrationDetails <RegnDtls> [0..1] Text 484
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails, RegistrationDetails
and PartyContactDetails must not contain information that can be provided in a structured field.
7.1.20.25.4  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Entity involved in an activity.
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification10"
on page 391 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TypeOfIdentification <TpOfId> [1..1] ± 391
   Country <Ctry> [1..1] CodeSet C4 391
   AlternateIdentification <AltrnId> [1..1] Text 392
7.1.20.26  PartyIdentificationAndAccount154
Definition: Entity involved in an activity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 476
   SafekeepingAccount <SfkpgAcct> [0..1] Text 477
   CashAccount <CshAcct> [0..1] ± 477
   ProcessingIdentification <PrcgId> [0..1] Text 477
   AdditionalInformation <AddtlInf> [0..1] ± C2 477
   AlternateIdentification <AltrnId> [0..1] ± 478
7.1.20.26.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 476 February 2025
```

