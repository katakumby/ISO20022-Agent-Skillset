---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.12 Party Identification", "6.1.12.1 PartyIdentification272", "6.1.12.1.3 Identification <Id>", "6.1.12.1.3.1 OrganisationIdentification <OrgId>"]
file_pages: [557]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.12.1.3.1 OrganisationIdentification <OrgId>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 557 to 557.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 557

```text
Identification <Id> contains one of the following Party52Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1]  557
     AnyBIC <AnyBIC> [0..1] IdentifierSet C3 558
     LEI <LEI> [0..1] IdentifierSet 558
     Other <Othr> [0..*]  558
       Identification <Id> [1..1] Text 559
       SchemeName <SchmeNm> [0..1]  559
{Or         Code <Cd> [1..1] CodeSet 559
Or}         Proprietary <Prtry> [1..1] Text 559
       Issuer <Issr> [0..1] Text 559
Or}   PrivateIdentification <PrvtId> [1..1]  559
     DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  560
       BirthDate <BirthDt> [1..1] Date 560
       ProvinceOfBirth <PrvcOfBirth> [0..1] Text 560
       CityOfBirth <CityOfBirth> [1..1] Text 561
       CountryOfBirth <CtryOfBirth> [1..1] CodeSet C18 561
     Other <Othr> [0..*]  561
       Identification <Id> [1..1] Text 561
       SchemeName <SchmeNm> [0..1]  561
{Or         Code <Cd> [1..1] CodeSet 562
Or}         Proprietary <Prtry> [1..1] Text 562
       Issuer <Issr> [0..1] Text 562
6.1.12.1.3.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 557 March 2026
```

