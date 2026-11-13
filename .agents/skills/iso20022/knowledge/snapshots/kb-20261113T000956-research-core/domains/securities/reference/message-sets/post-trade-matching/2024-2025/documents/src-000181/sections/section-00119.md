---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03", "5.4 Message Building Blocks", "5.4.4 ClearingDetails <ClrDtls>", "5.4.4.2 ClearingSegment <ClrSgmt>"]
file_pages: [153]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.030.001.03"]
---

# 5.4.4.2 ClearingSegment <ClrSgmt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 153 to 153.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 153

```text
ClearingMember <ClrMmb> contains the following elements (see "PartyIdentificationAndAccount219"
on page 491 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  492
{Or     BIC <BIC> [1..1] IdentifierSet C3 493
Or     ProprietaryIdentification <PrtryId> [1..1] ± 493
Or}     NameAndAddress <NmAndAdr> [1..1]  494
       Name <Nm> [1..1] Text 494
       Address <Adr> [0..1]  494
         AddressType <AdrTp> [0..1] CodeSet 495
         AddressLine <AdrLine> [0..5] Text 495
         StreetName <StrtNm> [0..1] Text 495
         BuildingNumber <BldgNb> [0..1] Text 495
         PostCode <PstCd> [0..1] Text 496
         TownName <TwnNm> [0..1] Text 496
         CountrySubDivision <CtrySubDvsn> [0..1] Text 496
         Country <Ctry> [1..1] CodeSet C4 496
   AlternateIdentification <AltrnId> [0..1] ± 496
   Side <Sd> [0..1] CodeSet 496
   ClearingAccount <ClrAcct> [0..1] ± 497
   ProcessingIdentification <PrcgId> [0..1] Text 497
   AdditionalInformation <AddtlInf> [0..1] ± C2 497
5.4.4.2  ClearingSegment <ClrSgmt>
Presence: [0..1]
Definition: Clearing organisation that will clear the trade.
Note: This field allows Clearing Member Firm to segregate flows coming from clearing counterparty's
clearing system. Indeed, Clearing Member Firms receive messages from the same system (same
sender) and this field allows them to know if the message is related to equities or derivatives.
ClearingSegment <ClrSgmt> contains one of the following elements (see
"PartyIdentification243Choice" on page 483 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet C3 483
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 483
Approved by the Securities SEG on 13 February 2025 setr.030.001.03
SecuritiesTradeConfirmationResponseV03
Post Trade Matching - Maintenance 2024 - 2025 153 February 2025
```

