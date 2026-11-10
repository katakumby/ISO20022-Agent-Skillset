---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.12 Financial Institution Identification", "82.1.12.3 BranchAndFinancialInstitutionIdentification8", "82.1.12.3.1 FinancialInstitutionIdentification <FinInstnId>", "82.1.12.3.1.4 Name <Nm>"]
file_pages: [2921]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.12.3.1.4 Name <Nm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2921 to 2921.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2921

```text
Datatype: "LEIIdentifier" on page 3322
82.1.12.3.1.4  Name <Nm>
Presence: [0..1]
Definition: Name by which an agent is known and which is usually used to identify that agent.
Datatype: "Max140Text" on page 3326
82.1.12.3.1.5  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
PostalAddress <PstlAdr> contains the following elements (see "PostalAddress27" on page 3087 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  3088
{Or     Code <Cd> [1..1] CodeSet 3088
Or}     Proprietary <Prtry> [1..1] ± 3089
   CareOf <CareOf> [0..1] Text 3089
   Department <Dept> [0..1] Text 3089
   SubDepartment <SubDept> [0..1] Text 3089
   StreetName <StrtNm> [0..1] Text 3089
   BuildingNumber <BldgNb> [0..1] Text 3090
   BuildingName <BldgNm> [0..1] Text 3090
   Floor <Flr> [0..1] Text 3090
   UnitNumber <UnitNb> [0..1] Text 3090
   PostBox <PstBx> [0..1] Text 3090
   Room <Room> [0..1] Text 3090
   PostCode <PstCd> [0..1] Text 3090
   TownName <TwnNm> [0..1] Text 3090
   TownLocationName <TwnLctnNm> [0..1] Text 3091
   DistrictName <DstrctNm> [0..1] Text 3091
   CountrySubDivision <CtrySubDvsn> [0..1] Text 3091
   Country <Ctry> [0..1] CodeSet C3 3091
   AddressLine <AdrLine> [0..7] Text 3091
82.1.12.3.1.6  Other <Othr>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2921 August 2026
```

