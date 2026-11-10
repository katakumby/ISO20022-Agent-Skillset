---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.26 Settlement Chain", "7.1.26.1 SettlementParties121", "7.1.26.1.1 Depository <Dpstry>", "7.1.26.1.1.1 Identification <Id>", "7.1.26.1.1.1.1 BIC <BIC>"]
file_pages: [527]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.26.1.1.1.1 BIC <BIC>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 527 to 527.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 527

```text
Identification <Id> contains one of the following PartyIdentification244Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet C3 527
Or   NameAndAddress <NmAndAdr> [1..1]  527
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
Or}   Country <Ctry> [1..1] CodeSet C4 530
7.1.26.1.1.1.1  BIC <BIC>
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
7.1.26.1.1.1.2  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Identification of a party with its name and address in free text.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 527 February 2025
```

