---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.17 Party Identification", "16.1.17.11 PartyIdentificationAndAccount226", "16.1.17.11.1 Identification <Id>", "16.1.17.11.1.1 BICFI <BICFI>"]
file_pages: [1051]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.17.11.1.1 BICFI <BICFI>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1051 to 1051.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1051

```text
Identification <Id> contains one of the following PartyIdentification133Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C2 1051
Or   NameAndAddress <NmAndAdr> [1..1] ± 1051
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 1051
16.1.17.11.1.1  BICFI <BICFI>
Presence: [1..1]
Definition: Code allocated to a financial institution by the ISO 9362 Registration Authority, as described
in ISO 9362 "Banking - Banking telecommunication messages - Business identifier code (BIC)".
Impacted by: C2 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 1244
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
16.1.17.11.1.2  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 1058 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 1058
   Address <Adr> [0..1] ± 1058
16.1.17.11.1.3  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification36" on
page 878 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 878
   Issuer <Issr> [1..1] Text 878
   SchemeName <SchmeNm> [0..1] Text 879
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1051 February 2026
```

