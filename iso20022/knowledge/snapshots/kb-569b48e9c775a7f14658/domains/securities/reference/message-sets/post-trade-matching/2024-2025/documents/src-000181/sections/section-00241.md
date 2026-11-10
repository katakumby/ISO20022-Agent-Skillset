---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.10 StandingSettlementInstruction13", "7.1.19.10.3 OtherDeliveringSettlementParties <OthrDlvrgSttlmPties>"]
file_pages: [297, 298]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.10.3 OtherDeliveringSettlementParties <OthrDlvrgSttlmPties>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 297 to 298.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 297

```text
Vendor <Vndr> contains one of the following elements (see "PartyIdentification117Choice" on
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
7.1.19.10.3  OtherDeliveringSettlementParties <OthrDlvrgSttlmPties>
Presence: [0..1]
Definition: Delivering parties, other than the seller, needed for deriving the standing settlement
instruction (for example, depository) or provided for information purposes (for example, instructing party
settlement chain).
Impacted by: C36 "Party2PresenceRule", C37 "Party3PresenceRule", C38 "Party4PresenceRule", C39
"Party5PresenceRule", C18 "DepositoryGuideline"
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 297 February 2025
```

## File page 298

```text
OtherDeliveringSettlementParties <OthrDlvrgSttlmPties> contains the following elements (see
"SettlementParties59" on page 556 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 558
   Party1 <Pty1> [0..1]  C5 559
     Identification <Id> [1..1] ± 559
     AdditionalInformation <AddtlInf> [0..1] Text 560
     AlternateIdentification <AltrnId> [0..1] ± 560
     SafekeepingAccount <SfkpgAcct> [0..1] Text 560
   Party2 <Pty2> [0..1]  C5 561
     Identification <Id> [1..1] ± 561
     AdditionalInformation <AddtlInf> [0..1] Text 562
     AlternateIdentification <AltrnId> [0..1] ± 562
     SafekeepingAccount <SfkpgAcct> [0..1] Text 562
   Party3 <Pty3> [0..1]  C5 563
     Identification <Id> [1..1] ± 563
     AdditionalInformation <AddtlInf> [0..1] Text 564
     AlternateIdentification <AltrnId> [0..1] ± 564
     SafekeepingAccount <SfkpgAcct> [0..1] Text 564
   Party4 <Pty4> [0..1]  C5 565
     Identification <Id> [1..1] ± 565
     AdditionalInformation <AddtlInf> [0..1] Text 566
     AlternateIdentification <AltrnId> [0..1] ± 566
     SafekeepingAccount <SfkpgAcct> [0..1] Text 566
   Party5 <Pty5> [0..1]  C5 567
     Identification <Id> [1..1] ± 567
     AdditionalInformation <AddtlInf> [0..1] Text 568
     AlternateIdentification <AltrnId> [0..1] ± 568
     SafekeepingAccount <SfkpgAcct> [0..1] Text 568
Constraints
• DepositoryGuideline
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 298 February 2025
```

