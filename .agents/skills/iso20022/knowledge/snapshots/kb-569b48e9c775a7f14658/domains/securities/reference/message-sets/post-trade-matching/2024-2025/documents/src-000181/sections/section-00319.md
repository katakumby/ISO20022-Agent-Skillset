---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.57 OptionRight2Choice", "7.1.19.57.2 Proprietary <Prtry>"]
file_pages: [383]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.57.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 383 to 383.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 383

```text
CodeName Name Definition
EXER Exercise Exercise option right.
ASGN Assignment Option right assignment.
RENO Renouncement The option right is renounced.
EXPI Expiration Option right expires.
7.1.19.57.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Option rights expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.58  LendingTransactionMethod2Choice
Definition: Choice of format method applied to a lending transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 383
Or}   Proprietary <Prtry> [1..1] ± 383
7.1.19.58.1  Code <Cd>
Presence: [1..1]
Definition: Lending transaction method expressed as a ISO20022 code.
Datatype: "LendingTransactionMethod1Code" on page 634
CodeName Name Definition
ODTR OnDemandTrade Contract applies to a specific security
only.
EXTR ExclusiveTrade Contract applies to a number of different
securities within the same pool/fund.
7.1.19.58.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Lending transaction method expressed as a proprietary code.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 383 February 2025
```

