---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.17 Party Identification", "16.1.17.4 PartyIdentification135", "16.1.17.4.5 ContactDetails <CtctDtls>"]
file_pages: [1042]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.17.4.5 ContactDetails <CtctDtls>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1042 to 1042.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1042

```text
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 1205
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
16.1.17.4.5  ContactDetails <CtctDtls>
Presence: [0..1]
Definition: Set of elements used to indicate how to contact the party.
ContactDetails <CtctDtls> contains the following elements (see "Contact4" on page 1055 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 1055
   Name <Nm> [0..1] Text 1056
   PhoneNumber <PhneNb> [0..1] Text 1056
   MobileNumber <MobNb> [0..1] Text 1056
   FaxNumber <FaxNb> [0..1] Text 1056
   EmailAddress <EmailAdr> [0..1] Text 1056
   EmailPurpose <EmailPurp> [0..1] Text 1056
   JobTitle <JobTitl> [0..1] Text 1056
   Responsibility <Rspnsblty> [0..1] Text 1057
   Department <Dept> [0..1] Text 1057
   Other <Othr> [0..*]  1057
     ChannelType <ChanlTp> [1..1] Text 1057
     Identification <Id> [0..1] Text 1057
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 1057
16.1.17.5  PartyIdentification129Choice
Definition: Choice between different formats for the identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1043
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1043
Or   NameAndAddress <NmAndAdr> [1..1] ± 1043
Or}   LEI <LEI> [1..1] IdentifierSet 1043
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1042 February 2026
```

