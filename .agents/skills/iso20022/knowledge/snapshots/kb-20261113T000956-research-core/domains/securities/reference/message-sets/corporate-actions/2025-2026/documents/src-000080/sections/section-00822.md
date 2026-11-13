---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.17 Party Identification", "16.1.17.3 PartyIdentificationAndAccount204", "16.1.17.3.4 ProcessingIdentification <PrcgId>"]
file_pages: [1040]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.17.3.4 ProcessingIdentification <PrcgId>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1040 to 1040.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1040

```text
Datatype: "Max140Text" on page 1249
16.1.17.3.4  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Reference meaningful to the party identified.
Datatype: "Max35Text" on page 1251
16.1.17.3.5  AlternateIdentification <AltrnId>
Presence: [0..*]
Definition: Alternate identification for a party.
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification7"
on page 1046 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 1046
   Country <Ctry> [1..1] CodeSet C3 1047
   AlternateIdentification <AltrnId> [1..1] Text 1047
16.1.17.4  PartyIdentification135
Definition: Specifies the identification of a person or an organisation.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 1040
   PostalAddress <PstlAdr> [0..1] ± 1040
   Identification <Id> [0..1] ± 1041
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C3 1041
   ContactDetails <CtctDtls> [0..1] ± 1042
16.1.17.4.1  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 1249
16.1.17.4.2  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1040 February 2026
```

