---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Party Identification", "7.1.19.8 PartyIdentification272", "7.1.19.8.1 Name <Nm>"]
file_pages: [422]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.8.1 Name <Nm>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 422 to 422.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 422

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 422
   PostalAddress <PstlAdr> [0..1] ± 423
   Identification <Id> [0..1]  423
{Or     OrganisationIdentification <OrgId> [1..1]  424
       AnyBIC <AnyBIC> [0..1] IdentifierSet C2 425
       LEI <LEI> [0..1] IdentifierSet 425
       Other <Othr> [0..*]  425
         Identification <Id> [1..1] Text 426
         SchemeName <SchmeNm> [0..1]  426
{Or           Code <Cd> [1..1] CodeSet 426
Or}           Proprietary <Prtry> [1..1] Text 426
         Issuer <Issr> [0..1] Text 426
Or}     PrivateIdentification <PrvtId> [1..1]  426
       DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  427
         BirthDate <BirthDt> [1..1] Date 427
         ProvinceOfBirth <PrvcOfBirth> [0..1] Text 427
         CityOfBirth <CityOfBirth> [1..1] Text 428
         CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 428
       Other <Othr> [0..*]  428
         Identification <Id> [1..1] Text 428
         SchemeName <SchmeNm> [0..1]  428
{Or           Code <Cd> [1..1] CodeSet 429
Or}           Proprietary <Prtry> [1..1] Text 429
         Issuer <Issr> [0..1] Text 429
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C3 429
   ContactDetails <CtctDtls> [0..1] ± 429
7.1.19.8.1  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 556
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 422 March 2026
```

