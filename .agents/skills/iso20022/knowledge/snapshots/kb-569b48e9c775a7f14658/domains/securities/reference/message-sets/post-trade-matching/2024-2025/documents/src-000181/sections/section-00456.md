---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.26 Settlement Chain", "7.1.26.1 SettlementParties121", "7.1.26.1.1 Depository <Dpstry>", "7.1.26.1.1.1 Identification <Id>"]
file_pages: [526]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.26.1.1.1 Identification <Id>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 526 to 526.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 526

```text
Depository <Dpstry> contains the following PartyIdentification268 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  526
{Or     BIC <BIC> [1..1] IdentifierSet C3 527
Or     NameAndAddress <NmAndAdr> [1..1]  527
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
Or}     Country <Ctry> [1..1] CodeSet C4 530
   AlternateIdentification <AltrnId> [0..1] ± 530
   AdditionalInformation <AddtlInf> [0..1] ± C2 530
7.1.26.1.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 526 February 2025
```

