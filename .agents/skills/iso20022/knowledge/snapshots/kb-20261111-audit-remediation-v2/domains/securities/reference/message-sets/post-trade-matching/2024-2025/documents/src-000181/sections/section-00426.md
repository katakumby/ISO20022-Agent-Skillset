---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.32 PartyIdentificationAndAccount219", "7.1.20.32.1 Identification <Id>"]
file_pages: [492]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.32.1 Identification <Id>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 492 to 492.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 492

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  492
{Or     BIC <BIC> [1..1] IdentifierSet C3 493
Or     ProprietaryIdentification <PrtryId> [1..1] ± 493
Or}     NameAndAddress <NmAndAdr> [1..1]  494
       Name <Nm> [1..1] Text 494
       Address <Adr> [0..1]  494
         AddressType <AdrTp> [0..1] CodeSet 495
         AddressLine <AdrLine> [0..5] Text 495
         StreetName <StrtNm> [0..1] Text 495
         BuildingNumber <BldgNb> [0..1] Text 495
         PostCode <PstCd> [0..1] Text 496
         TownName <TwnNm> [0..1] Text 496
         CountrySubDivision <CtrySubDvsn> [0..1] Text 496
         Country <Ctry> [1..1] CodeSet C4 496
   AlternateIdentification <AltrnId> [0..1] ± 496
   Side <Sd> [0..1] CodeSet 496
   ClearingAccount <ClrAcct> [0..1] ± 497
   ProcessingIdentification <PrcgId> [0..1] Text 497
   AdditionalInformation <AddtlInf> [0..1] ± C2 497
7.1.20.32.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 492 February 2025
```

