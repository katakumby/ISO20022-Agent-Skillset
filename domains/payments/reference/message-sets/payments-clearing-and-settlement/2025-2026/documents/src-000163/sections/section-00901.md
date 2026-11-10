---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.12 Party Identification", "10.1.12.1 PartyIdentification272", "10.1.12.1.3 Identification <Id>", "10.1.12.1.3.1 OrganisationIdentification <OrgId>"]
file_pages: [1196]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.12.1.3.1 OrganisationIdentification <OrgId>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1196 to 1196.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1196

```text
Identification <Id> contains one of the following Party52Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1]  1196
     AnyBIC <AnyBIC> [0..1] IdentifierSet C4 1197
     LEI <LEI> [0..1] IdentifierSet 1197
     Other <Othr> [0..*]  1197
       Identification <Id> [1..1] Text 1198
       SchemeName <SchmeNm> [0..1]  1198
{Or         Code <Cd> [1..1] CodeSet 1198
Or}         Proprietary <Prtry> [1..1] Text 1198
       Issuer <Issr> [0..1] Text 1198
Or}   PrivateIdentification <PrvtId> [1..1]  1198
     DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  1199
       BirthDate <BirthDt> [1..1] Date 1199
       ProvinceOfBirth <PrvcOfBirth> [0..1] Text 1199
       CityOfBirth <CityOfBirth> [1..1] Text 1200
       CountryOfBirth <CtryOfBirth> [1..1] CodeSet C10 1200
     Other <Othr> [0..*]  1200
       Identification <Id> [1..1] Text 1200
       SchemeName <SchmeNm> [0..1]  1200
{Or         Code <Cd> [1..1] CodeSet 1201
Or}         Proprietary <Prtry> [1..1] Text 1201
       Issuer <Issr> [0..1] Text 1201
10.1.12.1.3.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1196 March 2026
```

