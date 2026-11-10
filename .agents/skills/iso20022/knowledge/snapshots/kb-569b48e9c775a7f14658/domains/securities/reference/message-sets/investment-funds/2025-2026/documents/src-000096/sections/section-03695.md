---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.15 ExtendedParty13", "66.1.30.15.2 OtherPartyDetails <OthrPtyDtls>"]
file_pages: [4963]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.15.2 OtherPartyDetails <OthrPtyDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4963 to 4963.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4963

```text
66.1.30.15.2  OtherPartyDetails <OthrPtyDtls>
Presence: [1..1]
Definition: Identification and communication information about the party.
OtherPartyDetails <OthrPtyDtls> contains the following elements (see "ContactAttributes5" on
page 5021 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5021
   PostalAddress <PstlAdr> [0..1] ± 5021
   PhoneNumber <PhneNb> [0..1] Text 5022
   FaxNumber <FaxNb> [0..1] Text 5022
   EmailAddress <EmailAdr> [0..1] Text 5022
   URLAddress <URLAdr> [0..1] Text 5022
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 5022
   LEI <LEI> [0..1] IdentifierSet 5023
66.1.30.16  ModificationScope40
Definition: Scope of the modification to be applied on an identified set of information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4963
   Intermediary <Intrmy> [1..1] ± 4963
66.1.30.16.1  ModificationScopeIndication <ModScpIndctn>
Presence: [1..1]
Definition: Type of modification to be applied.
Datatype: "DataModification1Code" on page 5293
CodeName Name Definition
INSE InsertNewDataSet Insert a new set of data.
UPDT UpdateDataSetDetails Update the details of an existing set of
data.
DELT DeleteDataSet Delete an existing set of data.
66.1.30.16.2  Intermediary <Intrmy>
Presence: [1..1]
Definition: Intermediary or other party related to the management of the account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4963 May 2026
```

