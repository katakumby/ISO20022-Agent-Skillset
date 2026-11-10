---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.14 ConfirmationPartyDetails12"]
file_pages: [426]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.14 ConfirmationPartyDetails12

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 426 to 426.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 426

```text
AdditionalInformation <AddtlInf> contains the following elements (see "PartyTextInformation1" on
page 484 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 484
   PartyContactDetails <PtyCtctDtls> [0..1] Text 484
   RegistrationDetails <RegnDtls> [0..1] Text 484
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails, RegistrationDetails
and PartyContactDetails must not contain information that can be provided in a structured field.
7.1.20.14  ConfirmationPartyDetails12
Definition: Parties used for acting parties that apply either to the whole message or to individual sides.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  427
{Or     BIC <BIC> [1..1] IdentifierSet C3 427
Or     ProprietaryIdentification <PrtryId> [1..1] ± 427
Or}     NameAndAddress <NmAndAdr> [1..1]  428
       Name <Nm> [1..1] Text 428
       Address <Adr> [0..1]  428
         AddressType <AdrTp> [0..1] CodeSet 429
         AddressLine <AdrLine> [0..5] Text 429
         StreetName <StrtNm> [0..1] Text 429
         BuildingNumber <BldgNb> [0..1] Text 429
         PostCode <PstCd> [0..1] Text 430
         TownName <TwnNm> [0..1] Text 430
         CountrySubDivision <CtrySubDvsn> [0..1] Text 430
         Country <Ctry> [1..1] CodeSet C4 430
   AlternateIdentification <AltrnId> [0..1] ± 430
   ProcessingIdentification <PrcgId> [0..1] Text 430
   AdditionalInformation <AddtlInf> [0..1] ± C1 431
   InvestorCapacity <InvstrCpcty> [0..1] ± 431
   TradingPartyCapacity <TradgPtyCpcty> [0..1] ± 431
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 426 February 2025
```

