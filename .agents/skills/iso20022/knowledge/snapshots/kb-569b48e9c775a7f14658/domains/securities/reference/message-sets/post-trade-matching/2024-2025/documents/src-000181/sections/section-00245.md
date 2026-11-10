---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.13 NettingEligibility4Choice"]
file_pages: [303]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.13 NettingEligibility4Choice

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 303 to 303.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 303

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.13  NettingEligibility4Choice
Definition: Choice of format for the netting eligibility information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 303
Or}   Proprietary <Prtry> [1..1] ± 303
7.1.19.13.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether the settlement transaction is eligible for netting.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.13.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Netting eligibility expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.14  Revaluation3Choice
Definition: Choice between an indicator or a data source scheme to determine the revaluation.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 304
Or}   Proprietary <Prtry> [1..1] ± 304
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 303 February 2025
```

