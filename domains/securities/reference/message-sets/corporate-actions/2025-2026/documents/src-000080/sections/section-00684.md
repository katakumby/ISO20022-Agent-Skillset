---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.12 Frequency", "16.1.12.1 Frequency25Choice", "16.1.12.1.2 Proprietary <Prtry>"]
file_pages: [875]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.12.1.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 875 to 875.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 875

```text
16.1.12.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Frequency expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.13 Identification Information
16.1.13.1  IdentificationFormat3Choice
Definition: Choice between either a short, long or a proprietary identification format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortIdentification <ShrtId> [1..1] Text 875
Or   LongIdentification <LngId> [1..1] Text 875
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 875
16.1.13.1.1  ShortIdentification <ShrtId>
Presence: [1..1]
Definition: Format expressed as a short identification.
Datatype: "Exact3UpperCaseAlphaNumericText" on page 1248
16.1.13.1.2  LongIdentification <LngId>
Presence: [1..1]
Definition: Format expressed as a long identification.
Datatype: "Max30Text" on page 1250
16.1.13.1.3  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Format expressed as a proprietary identification.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 875 February 2026
```

