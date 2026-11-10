---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["10 seev.038.001.09 CorporateActionNarrativeV09", "10.4 Message Building Blocks", "10.4.4 AdditionalInformation <AddtlInf>"]
file_pages: [700]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.038.001.09"]
---

# 10.4.4 AdditionalInformation <AddtlInf>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 700 to 700.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 700

```text
10.4.4 AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Provides additional information.
Datatype: "Max8000Text" on page 1252
10.4.5 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C14 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 924 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 924
   Envelope <Envlp> [1..1] (External Schema) 924
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 27 January 2026 seev.038.001.09 CorporateActionNarrativeV09
Corporate Actions - Maintenance 2025 - 2026 700 February 2026
```

