---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.29 Organisation Identification", "66.1.29.2 Organisation40", "66.1.29.2.1 Name <Nm>"]
file_pages: [4889]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.29.2.1 Name <Nm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4889 to 4889.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4889

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 4889
   ShortName <ShrtNm> [0..1] Text 4889
   Identification <Id> [0..1]  4889
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4890
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 4890
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 4890
   Purpose <Purp> [0..1] Text 4890
   RegistrationCountry <RegnCtry> [0..1] CodeSet C12 4891
   RegistrationDate <RegnDt> [0..1] Date 4891
   ModifiedPostalAddress <ModfdPstlAdr> [0..*]  4891
     ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4891
     PostalAddress <PstlAdr> [1..1] ± C23 4891
   TypeOfOrganisation <TpOfOrg> [0..1]  4892
{Or     Code <Cd> [1..1] CodeSet 4893
Or}     Proprietary <Prtry> [1..1] ± 4893
   PlaceOfListing <PlcOfListg> [0..*] IdentifierSet 4893
Constraints
• OrganisationElementRule
One of the elements (Name, ShortName, Identification, LegalEntityIdentifier, Purpose,
RegistrationCountry, RegistrationDate, ModifiedPostalAddress, TypeOfOrganisation, PlaceOfListing)
must be present.
66.1.29.2.1  Name <Nm>
Presence: [0..1]
Definition: Name by which the organisation is known and which is usually used to identify that
organisation.
Datatype: "Max350Text" on page 5403
66.1.29.2.2  ShortName <ShrtNm>
Presence: [0..1]
Definition: Name of the organisation in short form.
Datatype: "Max35Text" on page 5403
66.1.29.2.3  Identification <Id>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4889 May 2026
```

