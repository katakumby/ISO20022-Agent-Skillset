---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification"]
file_pages: [4906]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30 Party Identification

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4906 to 4906.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4906

```text
Definition: Postal address of the organisation.
CorporateInvestorAddress <CorpInvstrAdr> contains the following elements (see "PostalAddress1"
on page 5098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 5098
   AddressLine <AdrLine> [0..5] Text 5099
   StreetName <StrtNm> [0..1] Text 5099
   BuildingNumber <BldgNb> [0..1] Text 5099
   PostCode <PstCd> [0..1] Text 5099
   TownName <TwnNm> [0..1] Text 5099
   CountrySubDivision <CtrySubDvsn> [0..1] Text 5099
   Country <Ctry> [1..1] CodeSet C12 5100
66.1.30 Party Identification
66.1.30.1  PartyIdentification315
Definition: Identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  4906
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4907
Or     NameAndAddress <NmAndAdr> [1..1] ± 4907
Or     Country <Ctry> [1..1] CodeSet C12 4907
Or}     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 4908
   LEI <LEI> [0..1] IdentifierSet 4908
   AlternateIdentification <AltrnId> [0..1] ± 4908
   ProcessingDate <PrcgDt> [0..1] ± 4908
   ProcessingIdentification <PrcgId> [0..1] Text 4908
   AdditionalInformation <AddtlInf> [0..1] ± C3 4909
66.1.30.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4906 May 2026
```

