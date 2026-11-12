---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.55 InterestComputationMethodFormat4Choice", "16.1.15.55.2 Proprietary <Prtry>"]
file_pages: [979]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.55.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 979 to 979.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 979

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
16.1.15.55.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the format of interest computation method.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.56  LotteryTypeFormat4Choice
Definition: Choice between a standard code or proprietary code to specify the type of lottery.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 979
Or}   Proprietary <Prtry> [1..1] ± 979
16.1.15.56.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the type of lottery announced.
Datatype: "LotteryType1Code" on page 1219
CodeName Name Definition
ORIG OriginalLotteryNotification Original lottery that has been announced
for a specific amount and date.
SUPP SupplementalLotteryNotification Supplemental or additional quantity
called on a previously announced
original lottery.
16.1.15.56.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of lottery announced.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 979 February 2026
```

