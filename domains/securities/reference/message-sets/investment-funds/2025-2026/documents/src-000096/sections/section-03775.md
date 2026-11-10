---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.2 IndividualPerson35", "66.1.32.2.1 GivenName <GvnNm>"]
file_pages: [5062, 5063]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.2.1 GivenName <GvnNm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5062 to 5063.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5062

```text
66.1.32.2.1  GivenName <GvnNm>
Presence: [0..1]
Definition: First name of the person.
Datatype: "Max35Text" on page 5403
66.1.32.2.2  MiddleName <MddlNm>
Presence: [0..1]
Definition: Second name of the person.
Datatype: "Max35Text" on page 5403
66.1.32.2.3  Name <Nm>
Presence: [1..1]
Definition: Name by which the party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 5403
66.1.32.2.4  Gender <Gndr>
Presence: [0..1]
Definition: Gender of the person.
Datatype: "Gender1Code" on page 5308
CodeName Name Definition
FEMA Female Individual is a female.
MALE Male Individual is a male.
66.1.32.2.5  BirthDate <BirthDt>
Presence: [0..1]
Definition: Date on which the person is born.
Datatype: "ISODate" on page 5388
66.1.32.3  IndividualPerson37
Definition: Human entity, as distinguished from a corporate entity (which is sometimes referred to as an
'artificial person').
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5062 May 2026
```

## File page 5063

```text
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
   EducationLevel <EdctnLvl> [0..1] Text 5072
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5063 May 2026
```

