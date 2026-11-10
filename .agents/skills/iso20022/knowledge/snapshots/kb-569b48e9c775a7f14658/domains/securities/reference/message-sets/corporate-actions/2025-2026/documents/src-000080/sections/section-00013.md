---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "2.4 Message Building Blocks", "2.4.14 Related <Rltd>", "2.4.14.1 CharacterSet <CharSet>"]
file_pages: [18]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.02"]
---

# 2.4.14.1 CharacterSet <CharSet>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 18 to 18.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 18

```text
2.4.14.1  CharacterSet <CharSet>
Presence: [0..1]
Definition: Contains the character set of the text-based elements used in the Business Message.
Impacted by: C6 "ValidationByTable"
Datatype: "UnicodeChartsCode" on page 1243
Constraints
• ValidationByTable
2.4.14.2  From <Fr>
Presence: [1..1]
Definition: The sending MessagingEndpoint that has created this Business Message for the receiving
MessagingEndpoint that will process this Business Message.
Note the sending MessagingEndpoint might be different from the sending address potentially contained
in the transport header (as defined in the transport layer).
From <Fr> contains one of the following Party44Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 18
Or}   FinancialInstitutionIdentification <FIId> [1..1] ± 18
2.4.14.2.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Identification of a person or an organisation.
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification135" on
page 1040 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 1040
   PostalAddress <PstlAdr> [0..1] ± 1040
   Identification <Id> [0..1] ± 1041
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C3 1041
   ContactDetails <CtctDtls> [0..1] ± 1042
2.4.14.2.2  FinancialInstitutionIdentification <FIId>
Presence: [1..1]
Definition: Identification of a financial institution.
Approved by the Securities SEG on 27 January 2026 head.001.001.02 BusinessApplicationHeaderV02
Corporate Actions - Maintenance 2025 - 2026 18 February 2026
```

