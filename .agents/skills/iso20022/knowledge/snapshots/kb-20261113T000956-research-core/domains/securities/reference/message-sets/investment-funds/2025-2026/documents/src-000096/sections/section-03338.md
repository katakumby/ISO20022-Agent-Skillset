---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.4 InvestmentAccountOwnershipInformation17", "66.1.24.4.1 Party <Pty>", "66.1.24.4.1.2 IndividualPerson <IndvPrsn>"]
file_pages: [4578, 4579]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.4.1.2 IndividualPerson <IndvPrsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4578 to 4579.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4578

```text
Organisation <Org> contains the following elements (see "Organisation40" on page 4888 for details)
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
66.1.24.4.1.2  IndividualPerson <IndvPrsn>
Presence: [1..1]
Definition: Human entity, as distinguished from a corporate entity (which is sometimes referred to as an
'artificial person').
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4578 May 2026
```

## File page 4579

```text
IndividualPerson <IndvPrsn> contains the following elements (see "IndividualPerson38" on
page 5081 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1]  5083
{Or     Code <Cd> [1..1] CodeSet 5083
Or}     Proprietary <Prtry> [1..1] ± 5084
   GivenName <GvnNm> [0..1] Text 5084
   MiddleName <MddlNm> [0..1] Text 5084
   Name <Nm> [1..1] Text 5084
   NameSuffix <NmSfx> [0..1] Text 5084
   Gender <Gndr> [0..1] CodeSet 5084
   BirthDate <BirthDt> [0..1] Date 5085
   CountryOfBirth <CtryOfBirth> [0..1] CodeSet C12 5085
   ProvinceOfBirth <PrvcOfBirth> [0..1] Text 5085
   CityOfBirth <CityOfBirth> [0..1] Text 5085
   Profession <Prfssn> [0..1] Text 5085
   ModifiedPostalAddress <ModfdPstlAdr> [0..*]  5085
     ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 5086
     PostalAddress <PstlAdr> [1..1] ± C23 5086
   ModifiedCitizenship <ModfdCtznsh> [0..3]  5087
     ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 5088
     Citizenship <Ctznsh> [1..1]  5088
       Nationality <Ntlty> [1..1] CodeSet C35 5088
       MinorIndicator <MnrInd> [1..1] Indicator 5088
   EmployingCompany <EmplngCpny> [0..1] Text 5089
   BusinessFunction <BizFctn> [0..1] Text 5089
   PoliticallyExposedPerson <PltclyXpsdPrsn> [0..1]  C29 5089
     PoliticallyExposedPersonType <PltclyXpsdPrsnTp> [1..1]  5089
{Or       Code <Cd> [1..1] CodeSet 5090
Or}       Proprietary <Prtry> [1..1] ± 5090
     PoliticallyExposedPersonStatus <PltclyXpsdPrsnSts> [0..1]  5090
{Or       Code <Cd> [1..1] CodeSet 5090
Or}       Proprietary <Prtry> [1..1] ± 5091
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4579 May 2026
```

