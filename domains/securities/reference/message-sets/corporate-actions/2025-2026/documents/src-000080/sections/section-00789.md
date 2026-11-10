---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.61 CertificationTypeFormat3Choice"]
file_pages: [984]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.61 CertificationTypeFormat3Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 984 to 984.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 984

```text
Definition: Proprietary identification of the narrative type of the message.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.61  CertificationTypeFormat3Choice
Definition: Choice between a standard code or proprietary code to specify the certification format
required.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 984
Or}   Proprietary <Prtry> [1..1] ± 984
16.1.15.61.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the certification format required, that is, physical or electronic
format.
Datatype: "CertificationFormatType1Code" on page 1166
CodeName Name Definition
ELEC Electronic Certification must be provided in
electronic format.
PHYS Physical Certification must be provided in physical
format.
16.1.15.61.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the certification format.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 984 February 2026
```

