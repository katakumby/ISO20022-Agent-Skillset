---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.26 Settlement Chain", "7.1.26.1 SettlementParties121", "7.1.26.1.5 Party4 <Pty4>", "7.1.26.1.5.4 SafekeepingAccount <SfkpgAcct>"]
file_pages: [551]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.26.1.5.4 SafekeepingAccount <SfkpgAcct>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 551 to 551.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 551

```text
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification8"
on page 398 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 398
   Country <Ctry> [1..1] CodeSet C4 398
   AlternateIdentification <AltrnId> [1..1] Text 399
7.1.26.1.5.4  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
Datatype: "Max35Text" on page 669
7.1.26.1.6  Party5 <Pty5>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the party 4.
Impacted by: C3 "AdditionalInforrmationRule"
Party5 <Pty5> contains the following PartyIdentificationAndAccount218 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  552
{Or     BIC <BIC> [1..1] IdentifierSet C3 552
Or     ProprietaryIdentification <PrtryId> [1..1] ± 553
Or}     NameAndAddress <NmAndAdr> [1..1]  553
       Name <Nm> [1..1] Text 553
       Address <Adr> [0..1]  554
         AddressType <AdrTp> [0..1] CodeSet 554
         AddressLine <AdrLine> [0..5] Text 554
         StreetName <StrtNm> [0..1] Text 554
         BuildingNumber <BldgNb> [0..1] Text 555
         PostCode <PstCd> [0..1] Text 555
         TownName <TwnNm> [0..1] Text 555
         CountrySubDivision <CtrySubDvsn> [0..1] Text 555
         Country <Ctry> [1..1] CodeSet C4 555
   AdditionalInformation <AddtlInf> [0..1] Text 555
   AlternateIdentification <AltrnId> [0..1] ± 555
   SafekeepingAccount <SfkpgAcct> [0..1] Text 556
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 551 February 2025
```

