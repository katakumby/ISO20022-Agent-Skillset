---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.19 ConfirmationPartyDetails7", "7.1.20.19.1 Identification <Id>"]
file_pages: [445]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.19.1 Identification <Id>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 445 to 445.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 445

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 445
   AlternateIdentification <AltrnId> [0..1] ± 445
   ProcessingIdentification <PrcgId> [0..1] Text 446
   AdditionalInformation <AddtlInf> [0..1] ± C1 446
   InvestorCapacity <InvstrCpcty> [0..1] ± 446
   TradingPartyCapacity <TradgPtyCpcty> [0..1] ± 447
7.1.20.19.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Identification <Id> contains one of the following elements (see "PartyIdentification117Choice" on
page 438 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 438
Or   ProprietaryIdentification <PrtryId> [1..1] ± 438
Or}   NameAndAddress <NmAndAdr> [1..1]  439
     Name <Nm> [1..1] Text 439
     Address <Adr> [0..1]  439
       AddressType <AdrTp> [0..1] CodeSet 440
       AddressLine <AdrLine> [0..5] Text 440
       StreetName <StrtNm> [0..1] Text 440
       BuildingNumber <BldgNb> [0..1] Text 440
       PostCode <PstCd> [0..1] Text 441
       TownName <TwnNm> [0..1] Text 441
       CountrySubDivision <CtrySubDvsn> [0..1] Text 441
       Country <Ctry> [1..1] CodeSet C4 441
7.1.20.19.2  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Alternate identification for a party.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 445 February 2025
```

