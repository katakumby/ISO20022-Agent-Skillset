---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.33 PartyIdentificationAndAccount221"]
file_pages: [498]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.33 PartyIdentificationAndAccount221

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 498 to 498.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 498

```text
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails, RegistrationDetails
and PartyContactDetails must not contain information that can be provided in a structured field.
7.1.20.33  PartyIdentificationAndAccount221
Definition: Party and account details.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  498
{Or     BIC <BIC> [1..1] IdentifierSet C3 499
Or     ProprietaryIdentification <PrtryId> [1..1] ± 499
Or}     NameAndAddress <NmAndAdr> [1..1]  500
       Name <Nm> [1..1] Text 500
       Address <Adr> [0..1]  500
         AddressType <AdrTp> [0..1] CodeSet 501
         AddressLine <AdrLine> [0..5] Text 501
         StreetName <StrtNm> [0..1] Text 501
         BuildingNumber <BldgNb> [0..1] Text 501
         PostCode <PstCd> [0..1] Text 502
         TownName <TwnNm> [0..1] Text 502
         CountrySubDivision <CtrySubDvsn> [0..1] Text 502
         Country <Ctry> [1..1] CodeSet C4 502
   AlternateIdentification <AltrnId> [0..1] ± 502
   SafekeepingAccount <SfkpgAcct> [0..1] Text 502
   ProcessingIdentification <PrcgId> [0..1] Text 503
   AdditionalInformation <AddtlInf> [0..1] ± C2 503
7.1.20.33.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 498 February 2025
```

