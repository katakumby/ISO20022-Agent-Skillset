---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types", "3.1 MessageComponents", "3.1.3 Party Identification", "3.1.3.1 PartyIdentification272", "3.1.3.1.3 Identification <Id>", "3.1.3.1.3.1 OrganisationIdentification <OrgId>"]
file_pages: [36]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.1.3.1.3.1 OrganisationIdentification <OrgId>

Source: [src-000011](../../../../../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf). Locator: one-based file pages 36 to 36.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 36

```text
Identification <Id> contains one of the following Party52Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1]  36
     AnyBIC <AnyBIC> [0..1] IdentifierSet C1 37
     LEI <LEI> [0..1] IdentifierSet 37
     Other <Othr> [0..*]  37
       Identification <Id> [1..1] Text 38
       SchemeName <SchmeNm> [0..1]  38
{Or         Code <Cd> [1..1] CodeSet 38
Or}         Proprietary <Prtry> [1..1] Text 38
       Issuer <Issr> [0..1] Text 38
Or}   PrivateIdentification <PrvtId> [1..1]  38
     DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  39
       BirthDate <BirthDt> [1..1] Date 39
       ProvinceOfBirth <PrvcOfBirth> [0..1] Text 39
       CityOfBirth <CityOfBirth> [1..1] Text 40
       CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 40
     Other <Othr> [0..*]  40
       Identification <Id> [1..1] Text 40
       SchemeName <SchmeNm> [0..1]  40
{Or         Code <Cd> [1..1] CodeSet 41
Or}         Proprietary <Prtry> [1..1] Text 41
       Issuer <Issr> [0..1] Text 41
3.1.3.1.3.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 36 March 2024
```

