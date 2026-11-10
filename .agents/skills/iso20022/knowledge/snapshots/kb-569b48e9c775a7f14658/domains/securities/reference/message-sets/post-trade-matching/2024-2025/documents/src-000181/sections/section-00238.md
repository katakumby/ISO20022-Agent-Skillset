---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.8 InterestComputationMethod3Choice", "7.1.19.8.2 Proprietary <Prtry>"]
file_pages: [294]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.8.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 294 to 294.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 294

```text
CodeName Name Definition
the 30E/360 (or Eurobond basis) method
where the last day of February is always
assumed to be the 30th, even if it is the
last day of the maturity coupon period.
A014 Actual365NL Method whereby interest is calculated
based on the actual number of accrued
days in the interest period, excluding any
leap day from the count, and a 365-day
year.
7.1.19.8.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Interest computation method is determined using a data source scheme.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.9  Linkages52
Definition: Information related to a linked transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageNumber <MsgNb> [0..1] ± C9 294
   Reference <Ref> [1..1] ± C7 295
7.1.19.9.1  MessageNumber <MsgNb>
Presence: [0..1]
Definition: Message type number/message identifier of the message referenced in the linkage
sequence.
Impacted by: C9 "ShortLongNumberRule"
MessageNumber <MsgNb> contains one of the following elements (see "DocumentNumber17Choice"
on page 269 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 269
Or   LongNumber <LngNb> [1..1] Text 269
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 269
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 294 February 2025
```

