---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.8 Commission", "7.1.8.1 Commission25", "7.1.8.1.3 RecipientIdentification <RcptId>", "7.1.8.1.3.2 ProprietaryIdentification <PrtryId>"]
file_pages: [252]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.8.1.3.2 ProprietaryIdentification <PrtryId>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 252 to 252.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 252

```text
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
7.1.8.1.3.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification36" on
page 279 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 279
   Issuer <Issr> [1..1] Text 279
   SchemeName <SchmeNm> [0..1] Text 279
7.1.8.1.3.3  NameAndAddress <NmAndAdr>
Presence: [0..1]
Definition: Identification of a party with its name and address in free text.
NameAndAddress <NmAndAdr> contains the following NameAndAddress13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 252
   Address <Adr> [0..1]  253
     AddressType <AdrTp> [0..1] CodeSet 253
     AddressLine <AdrLine> [0..5] Text 253
     StreetName <StrtNm> [0..1] Text 253
     BuildingNumber <BldgNb> [0..1] Text 254
     PostCode <PstCd> [0..1] Text 254
     TownName <TwnNm> [0..1] Text 254
     CountrySubDivision <CtrySubDvsn> [0..1] Text 254
     Country <Ctry> [1..1] CodeSet C4 254
7.1.8.1.3.3.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 669
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 252 February 2025
```

