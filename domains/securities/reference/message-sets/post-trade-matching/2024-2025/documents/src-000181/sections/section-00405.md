---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.23 ConfirmationPartyDetails11", "7.1.20.23.4 AdditionalInformation <AddtlInf>"]
file_pages: [471]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.23.4 AdditionalInformation <AddtlInf>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 471 to 471.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 471

```text
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 669
7.1.20.23.4  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information to a party identification.
Impacted by: C1 "AdditonalDetailsGuideline"
AdditionalInformation <AddtlInf> contains the following elements (see "PartyTextInformation5" on
page 441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 442
   PartyContactDetails <PtyCtctDtls> [0..1] Text 442
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails and
PartyContactDetails must not contain information that can be provided in a structured field.
7.1.20.24  PartyIdentification117
Definition: Choice of identification of a party. The party can be identified by providing a BIC or a
proprietary code.
Optionally, the client account number can also be provided.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 472
   ProprietaryIdentification <PrtryId> [1..1] ± 472
   NameAndAddress <NmAndAdr> [0..1]  472
     Name <Nm> [1..1] Text 473
     Address <Adr> [0..1]  473
       AddressType <AdrTp> [0..1] CodeSet 473
       AddressLine <AdrLine> [0..5] Text 474
       StreetName <StrtNm> [0..1] Text 474
       BuildingNumber <BldgNb> [0..1] Text 474
       PostCode <PstCd> [0..1] Text 474
       TownName <TwnNm> [0..1] Text 474
       CountrySubDivision <CtrySubDvsn> [0..1] Text 474
       Country <Ctry> [1..1] CodeSet C4 475
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 471 February 2025
```

