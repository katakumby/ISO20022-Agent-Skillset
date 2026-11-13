---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.3 AlternatePartyIdentification10", "7.1.20.3.3 AlternateIdentification <AltrnId>"]
file_pages: [392]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.3.3 AlternateIdentification <AltrnId>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 392 to 392.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 392

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.1.20.3.3  AlternateIdentification <AltrnId>
Presence: [1..1]
Definition: Alternate identification for a party.
Datatype: "Max35Text" on page 669
7.1.20.4  ConfirmationPartyDetails14
Definition: Parties used for acting parties that apply either to the whole message or to individual sides.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  392
{Or     BIC <BIC> [1..1] IdentifierSet C3 393
Or     ProprietaryIdentification <PrtryId> [1..1] ± 393
Or}     NameAndAddress <NmAndAdr> [1..1]  394
       Name <Nm> [1..1] Text 394
       Address <Adr> [0..1]  394
         AddressType <AdrTp> [0..1] CodeSet 395
         AddressLine <AdrLine> [0..5] Text 395
         StreetName <StrtNm> [0..1] Text 395
         BuildingNumber <BldgNb> [0..1] Text 395
         PostCode <PstCd> [0..1] Text 396
         TownName <TwnNm> [0..1] Text 396
         CountrySubDivision <CtrySubDvsn> [0..1] Text 396
         Country <Ctry> [1..1] CodeSet C4 396
   SafekeepingAccount <SfkpgAcct> [0..1] ± 396
   CashDetails <CshDtls> [0..1] ± 396
   AlternateIdentification <AltrnId> [0..1] ± 397
   ProcessingIdentification <PrcgId> [0..1] Text 397
   AdditionalInformation <AddtlInf> [0..1] ± C1 397
   PartyCapacity <PtyCpcty> [0..1] ± 398
7.1.20.4.1  Identification <Id>
Presence: [1..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 392 February 2025
```

