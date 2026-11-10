---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.31 PartyIdentificationAndAccount220", "7.1.20.31.1 Identification <Id>"]
file_pages: [485]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.31.1 Identification <Id>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 485 to 485.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 485

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1]  485
{Or     BIC <BIC> [1..1] IdentifierSet C3 486
Or     ProprietaryIdentification <PrtryId> [1..1] ± 486
Or}     NameAndAddress <NmAndAdr> [1..1]  487
       Name <Nm> [1..1] Text 487
       Address <Adr> [0..1]  487
         AddressType <AdrTp> [0..1] CodeSet 488
         AddressLine <AdrLine> [0..5] Text 488
         StreetName <StrtNm> [0..1] Text 488
         BuildingNumber <BldgNb> [0..1] Text 488
         PostCode <PstCd> [0..1] Text 489
         TownName <TwnNm> [0..1] Text 489
         CountrySubDivision <CtrySubDvsn> [0..1] Text 489
         Country <Ctry> [1..1] CodeSet C4 489
   SafekeepingAccount <SfkpgAcct> [0..1] Text 489
   CashAccount <CshAcct> [0..1] ± 489
   ProcessingIdentification <PrcgId> [0..1] Text 490
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C4 490
   AdditionalInformation <AddtlInf> [0..1] ± C2 490
   AlternateIdentification <AltrnId> [0..1] ± 491
Constraints
• IdentificationUsageRule
The presence of Identification and/or CountryOfResidence is mandatory.
7.1.20.31.1  Identification <Id>
Presence: [0..1]
Definition: Information related to an identification, eg, party identification or account identification.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 485 February 2025
```

