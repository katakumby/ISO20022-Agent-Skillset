---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.23 ConfirmationPartyDetails11", "7.1.20.23.1 Identification <Id>"]
file_pages: [466]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.23.1 Identification <Id>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 466 to 466.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 466

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  466
{Or     BIC <BIC> [1..1] IdentifierSet C3 467
Or     ProprietaryIdentification <PrtryId> [1..1] ± 467
Or}     NameAndAddress <NmAndAdr> [1..1]  468
       Name <Nm> [1..1] Text 468
       Address <Adr> [0..1]  468
         AddressType <AdrTp> [0..1] CodeSet 469
         AddressLine <AdrLine> [0..5] Text 469
         StreetName <StrtNm> [0..1] Text 469
         BuildingNumber <BldgNb> [0..1] Text 469
         PostCode <PstCd> [0..1] Text 470
         TownName <TwnNm> [0..1] Text 470
         CountrySubDivision <CtrySubDvsn> [0..1] Text 470
         Country <Ctry> [1..1] CodeSet C4 470
   AlternateIdentification <AltrnId> [0..1] ± 470
   ProcessingIdentification <PrcgId> [0..1] Text 470
   AdditionalInformation <AddtlInf> [0..1] ± C1 471
7.1.20.23.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 466 February 2025
```

