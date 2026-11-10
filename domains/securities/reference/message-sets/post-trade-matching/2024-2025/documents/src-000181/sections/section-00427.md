---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.32 PartyIdentificationAndAccount219", "7.1.20.32.1 Identification <Id>", "7.1.20.32.1.1 BIC <BIC>"]
file_pages: [493]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.32.1.1 BIC <BIC>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 493 to 493.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 493

```text
Identification <Id> contains one of the following PartyIdentification240Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet C3 493
Or   ProprietaryIdentification <PrtryId> [1..1] ± 493
Or}   NameAndAddress <NmAndAdr> [1..1]  494
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
7.1.20.32.1.1  BIC <BIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C3 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 662
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
7.1.20.32.1.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 493 February 2025
```

