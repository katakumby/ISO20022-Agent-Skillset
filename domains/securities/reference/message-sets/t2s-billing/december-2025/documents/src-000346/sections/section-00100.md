---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.7 Party Identification", "4.1.7.3 PartyIdentification272", "4.1.7.3.3 Identification <Id>", "4.1.7.3.3.1 OrganisationIdentification <OrgId>"]
file_pages: [126]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.7.3.3.1 OrganisationIdentification <OrgId>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 126 to 126.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 126

```text
Identification <Id> contains one of the following Party52Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1]  126
     AnyBIC <AnyBIC> [0..1] IdentifierSet C2 127
     LEI <LEI> [0..1] IdentifierSet 127
     Other <Othr> [0..*]  127
       Identification <Id> [1..1] Text 128
       SchemeName <SchmeNm> [0..1]  128
{Or         Code <Cd> [1..1] CodeSet 128
Or}         Proprietary <Prtry> [1..1] Text 128
       Issuer <Issr> [0..1] Text 128
Or}   PrivateIdentification <PrvtId> [1..1]  128
     DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  129
       BirthDate <BirthDt> [1..1] Date 129
       ProvinceOfBirth <PrvcOfBirth> [0..1] Text 129
       CityOfBirth <CityOfBirth> [1..1] Text 130
       CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 130
     Other <Othr> [0..*]  130
       Identification <Id> [1..1] Text 130
       SchemeName <SchmeNm> [0..1]  130
{Or         Code <Cd> [1..1] CodeSet 131
Or}         Proprietary <Prtry> [1..1] Text 131
       Issuer <Issr> [0..1] Text 131
4.1.7.3.3.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 126 December 2025
```

