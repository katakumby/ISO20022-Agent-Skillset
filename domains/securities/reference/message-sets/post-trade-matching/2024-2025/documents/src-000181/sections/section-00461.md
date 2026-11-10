---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.26 Settlement Chain", "7.1.26.1 SettlementParties121", "7.1.26.1.2 Party1 <Pty1>"]
file_pages: [531]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.26.1.2 Party1 <Pty1>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 531 to 531.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 531

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
7.1.26.1.2  Party1 <Pty1>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the depository.
Impacted by: C3 "AdditionalInforrmationRule"
Party1 <Pty1> contains the following PartyIdentificationAndAccount218 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  532
{Or     BIC <BIC> [1..1] IdentifierSet C3 532
Or     ProprietaryIdentification <PrtryId> [1..1] ± 533
Or}     NameAndAddress <NmAndAdr> [1..1]  533
       Name <Nm> [1..1] Text 533
       Address <Adr> [0..1]  534
         AddressType <AdrTp> [0..1] CodeSet 534
         AddressLine <AdrLine> [0..5] Text 534
         StreetName <StrtNm> [0..1] Text 534
         BuildingNumber <BldgNb> [0..1] Text 535
         PostCode <PstCd> [0..1] Text 535
         TownName <TwnNm> [0..1] Text 535
         CountrySubDivision <CtrySubDvsn> [0..1] Text 535
         Country <Ctry> [1..1] CodeSet C4 535
   AdditionalInformation <AddtlInf> [0..1] Text 535
   AlternateIdentification <AltrnId> [0..1] ± 535
   SafekeepingAccount <SfkpgAcct> [0..1] Text 536
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 531 February 2025
```

