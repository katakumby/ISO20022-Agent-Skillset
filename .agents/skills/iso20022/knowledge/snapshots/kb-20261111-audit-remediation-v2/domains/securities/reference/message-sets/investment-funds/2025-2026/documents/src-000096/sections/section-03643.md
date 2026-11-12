---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.29 Organisation Identification", "66.1.29.2 Organisation40", "66.1.29.2.9 TypeOfOrganisation <TpOfOrg>", "66.1.29.2.9.1 Code <Cd>"]
file_pages: [4893]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.29.2.9.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4893 to 4893.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4893

```text
TypeOfOrganisation <TpOfOrg> contains one of the following OrganisationType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4893
Or}   Proprietary <Prtry> [1..1] ± 4893
66.1.29.2.9.1  Code <Cd>
Presence: [1..1]
Definition: Type of organisation expressed as a code.
Datatype: "OrganisationType1Code" on page 5334
CodeName Name Definition
IFUN InvestmentFund Organisation is an investment fund.
PRIV PrivateAssociation Organisation is a private association.
PUBL Public Organisation is a public company.
PFUN PublicFund Organisation is a public fund.
66.1.29.2.9.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of organisation expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.29.2.10  PlaceOfListing <PlcOfListg>
Presence: [0..*]
Definition: Place of listing for shares in the organisation.
Datatype: "MICIdentifier" on page 5396
66.1.29.3  PartyIdentification1Choice
Definition: Identification of a party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4893 May 2026
```

