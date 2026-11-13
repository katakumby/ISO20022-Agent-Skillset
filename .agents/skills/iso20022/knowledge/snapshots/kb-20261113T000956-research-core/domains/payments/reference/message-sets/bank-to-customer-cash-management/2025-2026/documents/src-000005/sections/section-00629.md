---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.16 Party Identification", "6.1.16.1 PartyIdentification272", "6.1.16.1.3 Identification <Id>", "6.1.16.1.3.1 OrganisationIdentification <OrgId>"]
file_pages: [862]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.16.1.3.1 OrganisationIdentification <OrgId>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 862 to 862.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 862

```text
Identification <Id> contains one of the following Party52Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1]  862
     AnyBIC <AnyBIC> [0..1] IdentifierSet C2 863
     LEI <LEI> [0..1] IdentifierSet 863
     Other <Othr> [0..*]  863
       Identification <Id> [1..1] Text 864
       SchemeName <SchmeNm> [0..1]  864
{Or         Code <Cd> [1..1] CodeSet 864
Or}         Proprietary <Prtry> [1..1] Text 864
       Issuer <Issr> [0..1] Text 864
Or}   PrivateIdentification <PrvtId> [1..1]  864
     DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  865
       BirthDate <BirthDt> [1..1] Date 865
       ProvinceOfBirth <PrvcOfBirth> [0..1] Text 865
       CityOfBirth <CityOfBirth> [1..1] Text 866
       CountryOfBirth <CtryOfBirth> [1..1] CodeSet C4 866
     Other <Othr> [0..*]  866
       Identification <Id> [1..1] Text 866
       SchemeName <SchmeNm> [0..1]  866
{Or         Code <Cd> [1..1] CodeSet 867
Or}         Proprietary <Prtry> [1..1] Text 867
       Issuer <Issr> [0..1] Text 867
6.1.16.1.3.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
862 March 2026
```

