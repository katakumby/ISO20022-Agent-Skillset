---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.31 PartyIdentificationAndAccount220", "7.1.20.31.1 Identification <Id>", "7.1.20.31.1.1 BIC <BIC>"]
file_pages: [486]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.31.1.1 BIC <BIC>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 486 to 486.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 486

```text
Identification <Id> contains one of the following PartyIdentification240Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet C3 486
Or   ProprietaryIdentification <PrtryId> [1..1] ± 486
Or}   NameAndAddress <NmAndAdr> [1..1]  487
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
7.1.20.31.1.1  BIC <BIC>
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
7.1.20.31.1.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 486 February 2025
```

