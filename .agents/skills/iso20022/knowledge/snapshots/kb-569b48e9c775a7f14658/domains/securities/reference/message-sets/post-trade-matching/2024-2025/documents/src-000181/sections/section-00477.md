---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.26 Settlement Chain", "7.1.26.1 SettlementParties121", "7.1.26.1.5 Party4 <Pty4>", "7.1.26.1.5.1 Identification <Id>"]
file_pages: [547]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.26.1.5.1 Identification <Id>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 547 to 547.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 547

```text
Constraints
• AdditionalInforrmationRule
The AdditionalInformation field in all elements must not contain information that can be provided in a
structured field unless bilaterally agreed or advised differently in the element definition as in
NarrativeVersion.
7.1.26.1.5.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a party.
Identification <Id> contains one of the following PartyIdentification240Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet C3 547
Or   ProprietaryIdentification <PrtryId> [1..1] ± 548
Or}   NameAndAddress <NmAndAdr> [1..1]  548
     Name <Nm> [1..1] Text 548
     Address <Adr> [0..1]  549
       AddressType <AdrTp> [0..1] CodeSet 549
       AddressLine <AdrLine> [0..5] Text 549
       StreetName <StrtNm> [0..1] Text 549
       BuildingNumber <BldgNb> [0..1] Text 550
       PostCode <PstCd> [0..1] Text 550
       TownName <TwnNm> [0..1] Text 550
       CountrySubDivision <CtrySubDvsn> [0..1] Text 550
       Country <Ctry> [1..1] CodeSet C4 550
7.1.26.1.5.1.1  BIC <BIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C3 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 662
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 547 February 2025
```

