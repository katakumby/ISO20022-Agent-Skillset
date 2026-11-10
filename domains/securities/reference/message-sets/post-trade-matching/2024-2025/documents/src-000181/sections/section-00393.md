---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.20 CashParties33", "7.1.20.20.4 CreditorAgent <CdtrAgt>", "7.1.20.20.4.2 AlternateIdentification <AltrnId>"]
file_pages: [459]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.20.4.2 AlternateIdentification <AltrnId>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 459 to 459.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 459

```text
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
7.1.20.20.4.2  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Alternate identification for a party.
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification8"
on page 398 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 398
   Country <Ctry> [1..1] CodeSet C4 398
   AlternateIdentification <AltrnId> [1..1] Text 399
7.1.20.20.4.3  CashAccount <CshAcct>
Presence: [0..1]
Definition: Account to or from which a cash entry is made.
CashAccount <CshAcct> contains one of the following elements (see
"CashAccountIdentification5Choice" on page 223 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 223
Or}   Proprietary <Prtry> [1..1] Text 223
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 459 February 2025
```

