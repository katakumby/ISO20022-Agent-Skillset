---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.12 Party Identification", "37.1.12.1 PartyIdentification272", "37.1.12.1.3 Identification <Id>", "37.1.12.1.3.1 OrganisationIdentification <OrgId>"]
file_pages: [826]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.12.1.3.1 OrganisationIdentification <OrgId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 826 to 826.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 826

```text
Identification <Id> contains one of the following Party52Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1]  826
     AnyBIC <AnyBIC> [0..1] IdentifierSet C2 827
     LEI <LEI> [0..1] IdentifierSet 827
     Other <Othr> [0..*]  827
       Identification <Id> [1..1] Text 828
       SchemeName <SchmeNm> [0..1]  828
{Or         Code <Cd> [1..1] CodeSet 828
Or}         Proprietary <Prtry> [1..1] Text 828
       Issuer <Issr> [0..1] Text 828
Or}   PrivateIdentification <PrvtId> [1..1]  828
     DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  829
       BirthDate <BirthDt> [1..1] Date 829
       ProvinceOfBirth <PrvcOfBirth> [0..1] Text 829
       CityOfBirth <CityOfBirth> [1..1] Text 830
       CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 830
     Other <Othr> [0..*]  830
       Identification <Id> [1..1] Text 830
       SchemeName <SchmeNm> [0..1]  830
{Or         Code <Cd> [1..1] CodeSet 831
Or}         Proprietary <Prtry> [1..1] Text 831
       Issuer <Issr> [0..1] Text 831
37.1.12.1.3.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 826 February 2025
```

