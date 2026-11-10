---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.10 ConfirmationPartyDetails13", "7.1.20.10.1 Identification <Id>"]
file_pages: [415]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.10.1 Identification <Id>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 415 to 415.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 415

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  415
{Or     BIC <BIC> [1..1] IdentifierSet C3 416
Or     ProprietaryIdentification <PrtryId> [1..1] ± 416
Or}     NameAndAddress <NmAndAdr> [1..1]  417
       Name <Nm> [1..1] Text 417
       Address <Adr> [0..1]  417
         AddressType <AdrTp> [0..1] CodeSet 418
         AddressLine <AdrLine> [0..5] Text 418
         StreetName <StrtNm> [0..1] Text 418
         BuildingNumber <BldgNb> [0..1] Text 418
         PostCode <PstCd> [0..1] Text 419
         TownName <TwnNm> [0..1] Text 419
         CountrySubDivision <CtrySubDvsn> [0..1] Text 419
         Country <Ctry> [1..1] CodeSet C4 419
   AlternateIdentification <AltrnId> [0..1] ± 419
   ProcessingIdentification <PrcgId> [0..1] Text 419
   AdditionalInformation <AddtlInf> [0..1] ± C1 420
   InvestorProtectionAssociationMembership
<InvstrPrtcnAssoctnMmbsh>
[0..1] Indicator 420
7.1.20.10.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 415 February 2025
```

