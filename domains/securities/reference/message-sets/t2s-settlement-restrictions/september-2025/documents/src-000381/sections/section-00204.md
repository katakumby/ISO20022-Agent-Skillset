---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.14 Miscellaneous", "9.1.14.19 InterestComputationMethodFormat4Choice", "9.1.14.19.2 Proprietary <Prtry>"]
file_pages: [250]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.14.19.2 Proprietary <Prtry>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 250 to 250.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 250

```text
CodeName Name Definition
assumed to be the 30th, even if it is the
last day of the maturity coupon period.
A014 Actual365NL Method whereby interest is calculated
based on the actual number of accrued
days in the interest period, excluding any
leap day from the count, and a 365-day
year.
NARR Narrative Other method than A001-A020. See
Narrative.
9.1.14.19.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the format of interest computation method.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.14.20  UpdateType15Choice
Definition: Choice of format for the update information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 250
Or}   Proprietary <Prtry> [1..1] ± 250
9.1.14.20.1  Code <Cd>
Presence: [1..1]
Definition: Indicates whether the report is complete or contains changes only.
Datatype: "StatementUpdateType1Code" on page 339
CodeName Name Definition
COMP Complete Statement is complete.
DELT Delta Statement contains changes only.
9.1.14.20.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Indicates whether the report is complete or contains changes only.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 250 September 2025
```

