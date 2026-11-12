---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.26 Settlement Chain", "7.1.26.1 SettlementParties121", "7.1.26.1.5 Party4 <Pty4>", "7.1.26.1.5.1 Identification <Id>", "7.1.26.1.5.1.2 ProprietaryIdentification <PrtryId>"]
file_pages: [548]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.26.1.5.1.2 ProprietaryIdentification <PrtryId>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 548 to 548.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 548

```text
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
7.1.26.1.5.1.2  ProprietaryIdentification <PrtryId>
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
7.1.26.1.5.1.3  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Identification of a party with its name and address in free text.
NameAndAddress <NmAndAdr> contains the following NameAndAddress13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
7.1.26.1.5.1.3.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 669
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 548 February 2025
```

