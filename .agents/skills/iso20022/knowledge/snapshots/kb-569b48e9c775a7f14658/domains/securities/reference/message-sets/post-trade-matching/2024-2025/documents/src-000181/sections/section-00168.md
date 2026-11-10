---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks", "6.4.12 ReceivingSettlementParties <RcvgSttlmPties>"]
file_pages: [216, 217, 218, 219, 220]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.4.12 ReceivingSettlementParties <RcvgSttlmPties>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 216 to 220.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 216

```text
• Party3PresenceRule
If Party3 is present, then Party2 must be present.
On Condition
    /Party3 is present
Following Must be True
    /Party2 Must be present
• Party4PresenceRule
If Party4 is present, then Party3 must be present.
On Condition
    /Party4 is present
Following Must be True
    /Party3 Must be present
• Party5PresenceRule
If Party5 is present, then Party4 must be present.
On Condition
    /Party5 is present
Following Must be True
    /Party4 Must be present
6.4.12 ReceivingSettlementParties <RcvgSttlmPties>
Presence: [0..1]
Definition: Identifies the chain of receiving settlement parties.
Impacted by: C28 "Party2PresenceRule", C29 "Party3PresenceRule", C30 "Party4PresenceRule", C31
"Party5PresenceRule", C12 "DepositoryGuideline"
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 216 February 2025
```

## File page 217

```text
ReceivingSettlementParties <RcvgSttlmPties> contains the following elements (see
"SettlementParties121" on page 520 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1]  525
     Identification <Id> [1..1]  526
{Or       BIC <BIC> [1..1] IdentifierSet C3 527
Or       NameAndAddress <NmAndAdr> [1..1]  527
         Name <Nm> [1..1] Text 528
         Address <Adr> [0..1]  528
           AddressType <AdrTp> [0..1] CodeSet 528
           AddressLine <AdrLine> [0..5] Text 529
           StreetName <StrtNm> [0..1] Text 529
           BuildingNumber <BldgNb> [0..1] Text 529
           PostCode <PstCd> [0..1] Text 529
           TownName <TwnNm> [0..1] Text 529
           CountrySubDivision <CtrySubDvsn> [0..1] Text 529
           Country <Ctry> [1..1] CodeSet C4 530
Or}       Country <Ctry> [1..1] CodeSet C4 530
     AlternateIdentification <AltrnId> [0..1] ± 530
     AdditionalInformation <AddtlInf> [0..1] ± C2 530
   Party1 <Pty1> [0..1]  C3 531
     Identification <Id> [1..1]  532
{Or       BIC <BIC> [1..1] IdentifierSet C3 532
Or       ProprietaryIdentification <PrtryId> [1..1] ± 533
Or}       NameAndAddress <NmAndAdr> [1..1]  533
         Name <Nm> [1..1] Text 533
         Address <Adr> [0..1]  534
           AddressType <AdrTp> [0..1] CodeSet 534
           AddressLine <AdrLine> [0..5] Text 534
           StreetName <StrtNm> [0..1] Text 534
           BuildingNumber <BldgNb> [0..1] Text 535
           PostCode <PstCd> [0..1] Text 535
           TownName <TwnNm> [0..1] Text 535
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 217 February 2025
```

## File page 218

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           CountrySubDivision <CtrySubDvsn> [0..1] Text 535
           Country <Ctry> [1..1] CodeSet C4 535
     AdditionalInformation <AddtlInf> [0..1] Text 535
     AlternateIdentification <AltrnId> [0..1] ± 535
     SafekeepingAccount <SfkpgAcct> [0..1] Text 536
   Party2 <Pty2> [0..1]  C3 536
     Identification <Id> [1..1]  537
{Or       BIC <BIC> [1..1] IdentifierSet C3 537
Or       ProprietaryIdentification <PrtryId> [1..1] ± 538
Or}       NameAndAddress <NmAndAdr> [1..1]  538
         Name <Nm> [1..1] Text 538
         Address <Adr> [0..1]  539
           AddressType <AdrTp> [0..1] CodeSet 539
           AddressLine <AdrLine> [0..5] Text 539
           StreetName <StrtNm> [0..1] Text 539
           BuildingNumber <BldgNb> [0..1] Text 540
           PostCode <PstCd> [0..1] Text 540
           TownName <TwnNm> [0..1] Text 540
           CountrySubDivision <CtrySubDvsn> [0..1] Text 540
           Country <Ctry> [1..1] CodeSet C4 540
     AdditionalInformation <AddtlInf> [0..1] Text 540
     AlternateIdentification <AltrnId> [0..1] ± 540
     SafekeepingAccount <SfkpgAcct> [0..1] Text 541
   Party3 <Pty3> [0..1]  C3 541
     Identification <Id> [1..1]  542
{Or       BIC <BIC> [1..1] IdentifierSet C3 542
Or       ProprietaryIdentification <PrtryId> [1..1] ± 543
Or}       NameAndAddress <NmAndAdr> [1..1]  543
         Name <Nm> [1..1] Text 543
         Address <Adr> [0..1]  544
           AddressType <AdrTp> [0..1] CodeSet 544
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 218 February 2025
```

## File page 219

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           AddressLine <AdrLine> [0..5] Text 544
           StreetName <StrtNm> [0..1] Text 544
           BuildingNumber <BldgNb> [0..1] Text 545
           PostCode <PstCd> [0..1] Text 545
           TownName <TwnNm> [0..1] Text 545
           CountrySubDivision <CtrySubDvsn> [0..1] Text 545
           Country <Ctry> [1..1] CodeSet C4 545
     AdditionalInformation <AddtlInf> [0..1] Text 545
     AlternateIdentification <AltrnId> [0..1] ± 545
     SafekeepingAccount <SfkpgAcct> [0..1] Text 546
   Party4 <Pty4> [0..1]  C3 546
     Identification <Id> [1..1]  547
{Or       BIC <BIC> [1..1] IdentifierSet C3 547
Or       ProprietaryIdentification <PrtryId> [1..1] ± 548
Or}       NameAndAddress <NmAndAdr> [1..1]  548
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
   Party5 <Pty5> [0..1]  C3 551
     Identification <Id> [1..1]  552
{Or       BIC <BIC> [1..1] IdentifierSet C3 552
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 219 February 2025
```

## File page 220

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       ProprietaryIdentification <PrtryId> [1..1] ± 553
Or}       NameAndAddress <NmAndAdr> [1..1]  553
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
Constraints
• DepositoryGuideline
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD exists in a
particular market, the stock exchange BIC will be used.
Country code should be used for settlement taking place outside of an institution published in the
PSET's BIC list. This includes physical deliveries and investment funds not settling at a CSD.
The format and content of the settlement party sequences will comply with the market practices
published for the counterparty depository included in the message.
For more details, see the relevant market practice document on www.smpg.info.
• Party2PresenceRule
If Party2 is present, then Party1 must be present.
On Condition
    /Party2 is present
Following Must be True
    /Party1 Must be present
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 220 February 2025
```

