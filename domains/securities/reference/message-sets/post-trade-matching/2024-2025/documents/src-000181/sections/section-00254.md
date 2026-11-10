---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.23 SecuritiesRTGS4Choice", "7.1.19.23.1 Indicator <Ind>"]
file_pages: [312]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.23.1 Indicator <Ind>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 312 to 312.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 312

```text
7.1.19.23.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether the settlement transaction is to be settled through an RTGS or a non
RTGS system.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.23.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Securities RTGS information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.24  LetterOfGuarantee4Choice
Definition: Choice of format for the letter of guarantee information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 312
Or}   Proprietary <Prtry> [1..1] ± 312
7.1.19.24.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether physical settlement may be executed using a letter of guarantee or if the
physical certificates should be used.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.24.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Letter of guarantee information expressed as a proprietary code.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 312 February 2025
```

