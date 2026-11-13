---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.7 InvestmentAccountOwnershipInformation16", "66.1.24.7.1 Party <Pty>", "66.1.24.7.1.2 IndividualPerson <IndvPrsn>"]
file_pages: [4600, 4601]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.7.1.2 IndividualPerson <IndvPrsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4600 to 4601.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4600

```text
Organisation <Org> contains the following elements (see "Organisation39" on page 4895 for details)
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
66.1.24.7.1.2  IndividualPerson <IndvPrsn>
Presence: [1..1]
Definition: Human entity, as distinguished from a corporate entity (which is sometimes referred to as an
'artificial person').
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4600 May 2026
```

## File page 4601

```text
IndividualPerson <IndvPrsn> contains the following elements (see "IndividualPerson37" on
page 5062 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1]  5064
{Or     Code <Cd> [1..1] CodeSet 5064
Or}     Proprietary <Prtry> [1..1] ± 5064
   GivenName <GvnNm> [0..1] Text 5065
   MiddleName <MddlNm> [0..1] Text 5065
   Name <Nm> [1..1] Text 5065
   NameSuffix <NmSfx> [0..1] Text 5065
   Gender <Gndr> [0..1] CodeSet 5065
   BirthDate <BirthDt> [0..1] Date 5065
   CountryOfBirth <CtryOfBirth> [0..1] CodeSet C12 5066
   ProvinceOfBirth <PrvcOfBirth> [0..1] Text 5066
   CityOfBirth <CityOfBirth> [0..1] Text 5066
   Profession <Prfssn> [0..1] Text 5066
   PostalAddress <PstlAdr> [1..10] ± C23 5066
   Citizenship <Ctznsh> [0..3]  5067
     Nationality <Ntlty> [1..1] CodeSet C35 5068
     MinorIndicator <MnrInd> [1..1] Indicator 5068
   EmployingCompany <EmplngCpny> [0..1] Text 5068
   BusinessFunction <BizFctn> [0..1] Text 5068
   PoliticallyExposedPerson <PltclyXpsdPrsn> [0..1]  C29 5068
     PoliticallyExposedPersonType <PltclyXpsdPrsnTp> [1..1]  5069
{Or       Code <Cd> [1..1] CodeSet 5069
Or}       Proprietary <Prtry> [1..1] ± 5070
     PoliticallyExposedPersonStatus <PltclyXpsdPrsnSts> [0..1]  5070
{Or       Code <Cd> [1..1] CodeSet 5070
Or}       Proprietary <Prtry> [1..1] ± 5071
   DeathDate <DthDt> [0..1] Date 5071
   CivilStatus <CvlSts> [0..1]  5071
{Or     Code <Cd> [1..1] CodeSet 5071
Or}     Proprietary <Prtry> [1..1] ± 5072
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4601 May 2026
```

