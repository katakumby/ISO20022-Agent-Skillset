---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.39 RepurchaseType22Choice", "7.1.19.39.2 Proprietary <Prtry>"]
file_pages: [333]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.39.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 333 to 333.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 333

```text
CodeName Name Definition
PAIR Pairoff Relates to a transaction that is paired off
and netted against one or more previous
transactions. A paired off transaction is a
buyback to offset and effectively
liquidate a prior sale of securities or a
sellback to offset and effectively liquidate
a prior buy of securities.
PADJ PrincipalExposureAdjustment Relates to a principal adjustment.
RATE RepoRate Is part of a pair-off.
CALL RepurchaseCall Relates to the early closing/maturity date
for a term repo or a termination date of
an open repo with the underlying
collateral.
ROLP RepoContractRollover Relates to a repo rollover of a contract
extending the closing or maturity date
without the underlying collateral
impacted.
CADJ Swap Relates to a swap/substitution.
TOPU TopUp Relates to a repo rollover of a position
extending the closing or maturity date.
WTHD Withdrawal Relates to a repo rollover of a position
extending the closing or maturity date.
7.1.19.39.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of securities financing transaction process expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.40  SecuritiesLendingType2Choice
Definition: Choice of format for the securities lending type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 333
Or}   Proprietary <Prtry> [1..1] ± 334
7.1.19.40.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 333 February 2025
```

