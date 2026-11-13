---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.9 PartyIdentification116Choice", "7.1.20.9.1 AnyBIC <AnyBIC>"]
file_pages: [411]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.9.1 AnyBIC <AnyBIC>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 411 to 411.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 411

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 411
Or   NameAndAddress <NmAndAdr> [1..1]  411
     Name <Nm> [1..1] Text 412
     Address <Adr> [0..1]  412
       AddressType <AdrTp> [0..1] CodeSet 412
       AddressLine <AdrLine> [0..5] Text 413
       StreetName <StrtNm> [0..1] Text 413
       BuildingNumber <BldgNb> [0..1] Text 413
       PostCode <PstCd> [0..1] Text 413
       TownName <TwnNm> [0..1] Text 413
       CountrySubDivision <CtrySubDvsn> [0..1] Text 413
       Country <Ctry> [1..1] CodeSet C4 414
Or}   Country <Ctry> [1..1] CodeSet C4 414
7.1.20.9.1  AnyBIC <AnyBIC>
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
7.1.20.9.2  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Identification of a party with its name and address in free text.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 411 February 2025
```

