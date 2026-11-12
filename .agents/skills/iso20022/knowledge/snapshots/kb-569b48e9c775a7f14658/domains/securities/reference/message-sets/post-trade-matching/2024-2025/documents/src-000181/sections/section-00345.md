---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.8 ConfirmationPartyDetails16", "7.1.20.8.4 AlternateIdentification <AltrnId>"]
file_pages: [409]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.8.4 AlternateIdentification <AltrnId>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 409 to 409.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 409

```text
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
CashDetails <CshDtls> contains one of the following elements (see "AccountIdentification55Choice"
on page 224 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 224
Or   BBAN <BBAN> [1..1] IdentifierSet 224
Or   UPIC <UPIC> [1..1] IdentifierSet 225
Or}   ProprietaryAccount <PrtryAcct> [1..1] ± 225
7.1.20.8.4  AlternateIdentification <AltrnId>
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
7.1.20.8.5  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 669
7.1.20.8.6  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information to a party identification.
Impacted by: C1 "AdditonalDetailsGuideline"
AdditionalInformation <AddtlInf> contains the following elements (see "PartyTextInformation5" on
page 441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 442
   PartyContactDetails <PtyCtctDtls> [0..1] Text 442
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 409 February 2025
```

