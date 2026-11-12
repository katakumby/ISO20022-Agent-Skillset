---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.15 ConfirmationPartyDetails15"]
file_pages: [432]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.15 ConfirmationPartyDetails15

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 432 to 432.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 432

```text
TradingPartyCapacity <TradgPtyCpcty> contains one of the following elements (see
"TradingPartyCapacity4Choice" on page 420 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 420
Or}   Proprietary <Prtry> [1..1] ± 422
7.1.20.15  ConfirmationPartyDetails15
Definition: Parties used for acting parties that apply either to the whole message or to individual sides.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  432
{Or     BIC <BIC> [1..1] IdentifierSet C3 433
Or     ProprietaryIdentification <PrtryId> [1..1] ± 433
Or}     NameAndAddress <NmAndAdr> [1..1]  434
       Name <Nm> [1..1] Text 434
       Address <Adr> [0..1]  434
         AddressType <AdrTp> [0..1] CodeSet 435
         AddressLine <AdrLine> [0..5] Text 435
         StreetName <StrtNm> [0..1] Text 435
         BuildingNumber <BldgNb> [0..1] Text 435
         PostCode <PstCd> [0..1] Text 436
         TownName <TwnNm> [0..1] Text 436
         CountrySubDivision <CtrySubDvsn> [0..1] Text 436
         Country <Ctry> [1..1] CodeSet C4 436
   SafekeepingAccount <SfkpgAcct> [0..1] ± 436
   CashDetails <CshDtls> [0..1] ± 436
   AlternateIdentification <AltrnId> [0..1] ± 437
   ProcessingIdentification <PrcgId> [0..1] Text 437
   AdditionalInformation <AddtlInf> [0..1] ± C1 437
7.1.20.15.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 432 February 2025
```

