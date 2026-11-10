---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.33 AutomaticBorrowing6Choice"]
file_pages: [390]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.33 AutomaticBorrowing6Choice

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 390 to 390.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 390

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.18.33  AutomaticBorrowing6Choice
Definition: Choice of format for the automatic borrowing information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 390
Or}   Proprietary <Prtry> [1..1] ± 390
7.1.18.33.1  Code <Cd>
Presence: [1..1]
Definition: Condition for automatic borrowing expressed as an ISO 20022 code.
Datatype: "AutoBorrowing1Code" on page 493
CodeName Name Definition
LAMI LastResort Only last resort borrowing should be
considered to make settlement occur.
NBOR NoAutomatic No automatic borrowing should take
place.
YBOR Automatic Automatic borrowing should take place.
7.1.18.33.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Condition for automatic borrowing expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.18.34  Number22Choice
Definition: Choice number format.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 390 March 2026
```

