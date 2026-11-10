---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.14 Postal Address", "37.1.14.2 LongPostalAddress1Choice", "37.1.14.2.1 Unstructured <Ustrd>"]
file_pages: [840]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.14.2.1 Unstructured <Ustrd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 840 to 840.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 840

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unstructured <Ustrd> [1..1] Text 840
Or}   Structured <Strd> [1..1] ± C3 840
37.1.14.2.1  Unstructured <Ustrd>
Presence: [1..1]
Definition: Information that locates and identifies a specific address, as defined by postal services, that
is presented in free format text.
Datatype: "Max140Text" on page 888
37.1.14.2.2  Structured <Strd>
Presence: [1..1]
Definition: Information that locates and identifies a specific address, as defined by postal services, that
is presented in a formal structure.
Impacted by: C3 "StreetNameAndOrPostOfficeBoxRule"
Structured <Strd> contains the following elements (see "StructuredLongPostalAddress1" on
page 844 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BuildingName <BldgNm> [0..1] Text 844
   StreetName <StrtNm> [0..1] Text 844
   StreetBuildingIdentification <StrtBldgId> [0..1] Text 844
   Floor <Flr> [0..1] Text 845
   TownName <TwnNm> [1..1] Text 845
   DistrictName <DstrctNm> [0..1] Text 845
   RegionIdentification <RgnId> [0..1] Text 845
   State <Stat> [0..1] Text 845
   CountyIdentification <CtyId> [0..1] Text 845
   Country <Ctry> [1..1] CodeSet C3 845
   PostCodeIdentification <PstCdId> [1..1] Text 846
   PostOfficeBox <POB> [0..1] Text 846
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 840 February 2025
```

