---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.25 Securities Quantity", "7.1.25.3 QuantityBreakdown76", "7.1.25.3.2 LotQuantity <LotQty>"]
file_pages: [520, 521, 522, 523, 524]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.25.3.2 LotQuantity <LotQty>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 520 to 524.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 520

```text
7.1.25.3.2  LotQuantity <LotQty>
Presence: [0..1]
Definition: Quantity of financial instruments that is part of the lot described.
LotQuantity <LotQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 272 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 273
Or   FaceAmount <FaceAmt> [1..1] Amount 273
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 273
7.1.25.3.3  LotDateTime <LotDtTm>
Presence: [0..1]
Definition: Date/time at which the lot was purchased.
LotDateTime <LotDtTm> contains one of the following elements (see "DateAndDateTime1Choice" on
page 263 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 263
Or}   DateTime <DtTm> [1..1] DateTime 263
7.1.25.3.4  LotPrice <LotPric>
Presence: [0..1]
Definition: Price at which the lot was purchased.
LotPrice <LotPric> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
7.1.26 Settlement Chain
7.1.26.1  SettlementParties121
Definition: Chain of parties involved in the settlement of a transaction, including receipts and deliveries,
book transfers, treasury deals, or other activities, resulting in the movement of a security or amount of
money from one account to another.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 520 February 2025
```

## File page 521

```text
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
           CountrySubDivision <CtrySubDvsn> [0..1] Text 535
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 521 February 2025
```

## File page 522

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
           AddressLine <AdrLine> [0..5] Text 544
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 522 February 2025
```

## File page 523

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Or       ProprietaryIdentification <PrtryId> [1..1] ± 553
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 523 February 2025
```

## File page 524

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 524 February 2025
```

