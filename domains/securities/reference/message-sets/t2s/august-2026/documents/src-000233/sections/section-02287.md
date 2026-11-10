---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.8 PartyIdentification272"]
file_pages: [3068]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.8 PartyIdentification272

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3068 to 3068.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3068

```text
82.1.20.8  PartyIdentification272
Definition: Specifies the identification of a person or an organisation.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 3068
   PostalAddress <PstlAdr> [0..1] ± 3069
   Identification <Id> [0..1]  3069
{Or     OrganisationIdentification <OrgId> [1..1]  3070
       AnyBIC <AnyBIC> [0..1] IdentifierSet C2 3071
       LEI <LEI> [0..1] IdentifierSet 3071
       Other <Othr> [0..*]  3071
         Identification <Id> [1..1] Text 3072
         SchemeName <SchmeNm> [0..1]  3072
{Or           Code <Cd> [1..1] CodeSet 3072
Or}           Proprietary <Prtry> [1..1] Text 3072
         Issuer <Issr> [0..1] Text 3072
Or}     PrivateIdentification <PrvtId> [1..1]  3072
       DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  3073
         BirthDate <BirthDt> [1..1] Date 3073
         ProvinceOfBirth <PrvcOfBirth> [0..1] Text 3073
         CityOfBirth <CityOfBirth> [1..1] Text 3074
         CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 3074
       Other <Othr> [0..*]  3074
         Identification <Id> [1..1] Text 3074
         SchemeName <SchmeNm> [0..1]  3074
{Or           Code <Cd> [1..1] CodeSet 3075
Or}           Proprietary <Prtry> [1..1] Text 3075
         Issuer <Issr> [0..1] Text 3075
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C3 3075
   ContactDetails <CtctDtls> [0..1] ± 3075
82.1.20.8.1  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 3326
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3068 August 2026
```

