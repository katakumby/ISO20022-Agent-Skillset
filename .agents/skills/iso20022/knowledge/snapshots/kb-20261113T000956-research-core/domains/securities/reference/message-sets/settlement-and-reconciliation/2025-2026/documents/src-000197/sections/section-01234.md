---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.20 PartyTextInformation1", "35.1.18.20.3 RegistrationDetails <RegnDtls>"]
file_pages: [1691]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.20.3 RegistrationDetails <RegnDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1691 to 1691.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1691

```text
Definition: Provides additional information regarding the party, for example, the contact unit or person
responsible for the transaction identified in the message.
Datatype: "Max140Text" on page 2191
35.1.18.20.3  RegistrationDetails <RegnDtls>
Presence: [0..1]
Definition: Provides information required for the registration.
Datatype: "Max350Text" on page 2192
35.1.18.21  AlternatePartyIdentification7
Definition: Alternate identification for a party using an identification type, a country code and a text field.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 1691
   Country <Ctry> [1..1] CodeSet C7 1691
   AlternateIdentification <AltrnId> [1..1] Text 1691
35.1.18.21.1  IdentificationType <IdTp>
Presence: [1..1]
Definition: Specifies the type of alternate identification of the party identified.
IdentificationType <IdTp> contains one of the following elements (see "IdentificationType42Choice"
on page 1494 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1494
Or}   Proprietary <Prtry> [1..1] ± 1495
35.1.18.21.2  Country <Ctry>
Presence: [1..1]
Definition: Country in which a person resides (the place of a person's home). In the case of a company,
it is the country from which the affairs of that company are directed.
Impacted by: C7 "Country"
Datatype: "CountryCode" on page 2057
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
35.1.18.21.3  AlternateIdentification <AltrnId>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1691 March 2026
```

