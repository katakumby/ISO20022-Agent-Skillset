---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.12 SecuritiesRTGS4Choice", "7.1.18.12.2 Proprietary <Prtry>"]
file_pages: [369]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.12.2 Proprietary <Prtry>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 369 to 369.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 369

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
• Meaning When True: Yes
• Meaning When False: No
7.1.18.12.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Securities RTGS information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.18.13  LetterOfGuarantee4Choice
Definition: Choice of format for the letter of guarantee information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 369
Or}   Proprietary <Prtry> [1..1] ± 369
7.1.18.13.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether physical settlement may be executed using a letter of guarantee or if the
physical certificates should be used.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
• Meaning When True: Yes
• Meaning When False: No
7.1.18.13.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Letter of guarantee information expressed as a proprietary code.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 369 March 2026
```

