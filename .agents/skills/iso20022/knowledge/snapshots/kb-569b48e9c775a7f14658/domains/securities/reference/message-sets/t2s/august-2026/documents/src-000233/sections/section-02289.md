---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.8 PartyIdentification272", "82.1.20.8.3 Identification <Id>", "82.1.20.8.3.1 OrganisationIdentification <OrgId>"]
file_pages: [3070]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.8.3.1 OrganisationIdentification <OrgId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3070 to 3070.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3070

```text
Identification <Id> contains one of the following Party52Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1]  3070
     AnyBIC <AnyBIC> [0..1] IdentifierSet C2 3071
     LEI <LEI> [0..1] IdentifierSet 3071
     Other <Othr> [0..*]  3071
       Identification <Id> [1..1] Text 3072
       SchemeName <SchmeNm> [0..1]  3072
{Or         Code <Cd> [1..1] CodeSet 3072
Or}         Proprietary <Prtry> [1..1] Text 3072
       Issuer <Issr> [0..1] Text 3072
Or}   PrivateIdentification <PrvtId> [1..1]  3072
     DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  3073
       BirthDate <BirthDt> [1..1] Date 3073
       ProvinceOfBirth <PrvcOfBirth> [0..1] Text 3073
       CityOfBirth <CityOfBirth> [1..1] Text 3074
       CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 3074
     Other <Othr> [0..*]  3074
       Identification <Id> [1..1] Text 3074
       SchemeName <SchmeNm> [0..1]  3074
{Or         Code <Cd> [1..1] CodeSet 3075
Or}         Proprietary <Prtry> [1..1] Text 3075
       Issuer <Issr> [0..1] Text 3075
82.1.20.8.3.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3070 August 2026
```

