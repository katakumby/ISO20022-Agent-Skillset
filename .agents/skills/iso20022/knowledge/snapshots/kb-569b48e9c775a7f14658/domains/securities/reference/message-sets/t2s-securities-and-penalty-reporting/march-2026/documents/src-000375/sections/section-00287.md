---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.5 OptionType6Choice"]
file_pages: [364]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.5 OptionType6Choice

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 364 to 364.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 364

```text
• Meaning When True: Yes
• Meaning When False: No
7.1.18.5  OptionType6Choice
Definition: Choice of format for the option type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 364
Or}   Proprietary <Prtry> [1..1] ± 364
7.1.18.5.1  Code <Cd>
Presence: [1..1]
Definition: Option type expressed as an ISO 20022 code.
Datatype: "OptionType1Code" on page 516
CodeName Name Definition
CALL Call Right to buy a quantity of an asset for an
agreed price at exercise date.
PUTO Put Right to sell a quantity of an asset for an
agreed price at exercise date.
7.1.18.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Option type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.18.6  PriorityNumeric4Choice
Definition: Choice of format for the priority.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 364
Or}   Proprietary <Prtry> [1..1] ± 365
7.1.18.6.1  Numeric <Nmrc>
Presence: [1..1]
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 364 March 2026
```

