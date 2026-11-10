---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.29 Organisation Identification", "66.1.29.5 Organisation39", "66.1.29.5.1 Name <Nm>"]
file_pages: [4896]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.29.5.1 Name <Nm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4896 to 4896.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4896

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 4896
   ShortName <ShrtNm> [0..1] Text 4896
   Identification <Id> [0..1]  4896
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4897
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 4897
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 4897
   Purpose <Purp> [0..1] Text 4897
   RegistrationCountry <RegnCtry> [0..1] CodeSet C12 4898
   RegistrationDate <RegnDt> [0..1] Date 4898
   PostalAddress <PstlAdr> [0..10] ± C23 4898
   TypeOfOrganisation <TpOfOrg> [0..1]  4899
{Or     Code <Cd> [1..1] CodeSet 4900
Or}     Proprietary <Prtry> [1..1] ± 4900
   PlaceOfListing <PlcOfListg> [0..*] IdentifierSet 4900
Constraints
• OrganisationElementRule
One of the elements (Name, ShortName, Identification, LegalEntityIdentifier, Purpose,
RegistrationCountry, RegistrationDate, PostalAddress, TypeOfOrganisation, PlaceOfListing) must be
present.
66.1.29.5.1  Name <Nm>
Presence: [0..1]
Definition: Name by which the organisation is known and which is usually used to identify that
organisation.
Datatype: "Max350Text" on page 5403
66.1.29.5.2  ShortName <ShrtNm>
Presence: [0..1]
Definition: Name of the organisation in short form.
Datatype: "Max35Text" on page 5403
66.1.29.5.3  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the organisation.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4896 May 2026
```

