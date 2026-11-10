---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.17 Party Identification", "16.1.17.10 PartyIdentification263Choice", "16.1.17.10.5 LEI <LEI>"]
file_pages: [1050]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.17.10.5 LEI <LEI>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1050 to 1050.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1050

```text
IndividualOwnerIdentification <IndvOwnrId> contains the following elements (see
"AlternatePartyIdentification7" on page 1046 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 1046
   Country <Ctry> [1..1] CodeSet C3 1047
   AlternateIdentification <AltrnId> [1..1] Text 1047
16.1.17.10.5  LEI <LEI>
Presence: [1..1]
Definition: Legal entity identification of the party.
Datatype: "LEIIdentifier" on page 1246
16.1.17.11  PartyIdentificationAndAccount226
Definition: Provides information about identification and account of the party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1050
{Or     BICFI <BICFI> [1..1] IdentifierSet C2 1051
Or     NameAndAddress <NmAndAdr> [1..1] ± 1051
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 1051
   CashAccount <CshAcct> [0..1] ± 1052
   ProcessingIdentification <PrcgId> [0..1] Text 1052
   AlternateIdentification <AltrnId> [0..1] ± 1052
Constraints
• AdditionalInforrmationRule
The AdditionalInformation field in all elements must not contain information that can be provided in a
structured field unless bilaterally agreed or advised differently in the element definition as in
NarrativeVersion.
16.1.17.11.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1050 February 2026
```

