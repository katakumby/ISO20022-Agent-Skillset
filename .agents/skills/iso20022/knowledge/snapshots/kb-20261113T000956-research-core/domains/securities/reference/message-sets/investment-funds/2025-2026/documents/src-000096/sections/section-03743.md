---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.38 PartyIdentification132"]
file_pages: [5029]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.38 PartyIdentification132

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5029 to 5029.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5029

```text
Definition: Address of the nominee company that holds the assets at the transfer agent or International
Central Securities Depository or Central Securities Depository on behalf of the party.
RegistrationAddress <RegnAdr> contains the following elements (see "PostalAddress1" on
page 5098 for details)
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
66.1.30.38  PartyIdentification132
Definition: Identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 5029
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 5029
   NameAndAddress <NmAndAdr> [0..1] ± 5030
   ProprietaryIdentification <PrtryId> [0..1] ± 5031
   LEI <LEI> [0..1] IdentifierSet 5031
66.1.30.38.1  AnyBIC <AnyBIC>
Presence: [0..1]
Definition: Identification of the party expressed as a BIC.
Impacted by: C4 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 5389
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
66.1.30.38.2  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5029 May 2026
```

