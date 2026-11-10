---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.47 BeneficialOwnership4Choice", "7.1.19.47.1 Indicator <Ind>"]
file_pages: [357]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.47.1 Indicator <Ind>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 357 to 357.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 357

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 357
Or}   Proprietary <Prtry> [1..1] ± 357
7.1.19.47.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether there is change of beneficial ownership.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.47.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Beneficial ownership information expressed a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.48  AutomaticBorrowing6Choice
Definition: Choice of format for the automatic borrowing information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 357
Or}   Proprietary <Prtry> [1..1] ± 358
7.1.19.48.1  Code <Cd>
Presence: [1..1]
Definition: Condition for automatic borrowing expressed as an ISO 20022 code.
Datatype: "AutoBorrowing1Code" on page 615
CodeName Name Definition
LAMI LastResort Only last resort borrowing should be
considered to make settlement occur.
NBOR NoAutomatic No automatic borrowing should take
place.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 357 February 2025
```

