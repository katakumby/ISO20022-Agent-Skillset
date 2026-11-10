---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.54 CorporateActionMandatoryVoluntary3Choice"]
file_pages: [975]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.54 CorporateActionMandatoryVoluntary3Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 975 to 975.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 975

```text
16.1.15.54  CorporateActionMandatoryVoluntary3Choice
Definition: Choice between a standard code or a proprietary code to indicate if a corporate action event
is mandatory or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 975
Or}   Proprietary <Prtry> [1..1] ± 975
16.1.15.54.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify whether the event is mandatory, mandatory with options or
voluntary.
Datatype: "CorporateActionMandatoryVoluntary1Code" on page 1195
CodeName Name Definition
MAND Mandatory Participation in CA event is mandatory.
Further instructions from the account
owner are not required.
CHOS MandatoryWithOptions Participation in the corporate action is
mandatory and further instructions from
the account owner are required, unless a
default option has been specified.
VOLU Voluntary Participation in the corporate action is
voluntary. If the owner wishes to take
part in the event, instructions from the
account owner are required.
16.1.15.54.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of an event.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.55  InterestComputationMethodFormat4Choice
Definition: Choice between a standard code or proprietary code to specify the type of interest
computation method.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 975 February 2026
```

