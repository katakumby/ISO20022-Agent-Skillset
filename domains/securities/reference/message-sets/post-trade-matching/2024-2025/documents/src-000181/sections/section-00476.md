---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.26 Settlement Chain", "7.1.26.1 SettlementParties121", "7.1.26.1.4 Party3 <Pty3>", "7.1.26.1.4.4 SafekeepingAccount <SfkpgAcct>"]
file_pages: [546]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.26.1.4.4 SafekeepingAccount <SfkpgAcct>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 546 to 546.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 546

```text
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification8"
on page 398 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 398
   Country <Ctry> [1..1] CodeSet C4 398
   AlternateIdentification <AltrnId> [1..1] Text 399
7.1.26.1.4.4  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
Datatype: "Max35Text" on page 669
7.1.26.1.5  Party4 <Pty4>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the party 3.
Impacted by: C3 "AdditionalInforrmationRule"
Party4 <Pty4> contains the following PartyIdentificationAndAccount218 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  547
{Or     BIC <BIC> [1..1] IdentifierSet C3 547
Or     ProprietaryIdentification <PrtryId> [1..1] ± 548
Or}     NameAndAddress <NmAndAdr> [1..1]  548
       Name <Nm> [1..1] Text 548
       Address <Adr> [0..1]  549
         AddressType <AdrTp> [0..1] CodeSet 549
         AddressLine <AdrLine> [0..5] Text 549
         StreetName <StrtNm> [0..1] Text 549
         BuildingNumber <BldgNb> [0..1] Text 550
         PostCode <PstCd> [0..1] Text 550
         TownName <TwnNm> [0..1] Text 550
         CountrySubDivision <CtrySubDvsn> [0..1] Text 550
         Country <Ctry> [1..1] CodeSet C4 550
   AdditionalInformation <AddtlInf> [0..1] Text 550
   AlternateIdentification <AltrnId> [0..1] ± 550
   SafekeepingAccount <SfkpgAcct> [0..1] Text 551
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 546 February 2025
```

