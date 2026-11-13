---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.22 RepurchaseType23Choice", "7.1.18.22.2 Proprietary <Prtry>"]
file_pages: [381]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.22.2 Proprietary <Prtry>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 381 to 381.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 381

```text
CodeName Name Definition
CALL RepurchaseCall Relates to the early closing/maturity date
for a term repo or a termination date of
an open repo with the underlying
collateral.
CADJ Swap Relates to a swap/substitution.
TOPU TopUp Relates to a repo rollover of a position
extending the closing or maturity date.
WTHD Withdrawal Relates to a repo rollover of a position
extending the closing or maturity date.
7.1.18.22.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of securities financing transaction process expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.18.23  BlockTrade4Choice
Definition: Choice of format for the block trade information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 381
Or}   Proprietary <Prtry> [1..1] ± 381
7.1.18.23.1  Code <Cd>
Presence: [1..1]
Definition: Block parent or child information expressed as an ISO 20022 code.
Datatype: "BlockTrade1Code" on page 493
CodeName Name Definition
BLPA Parent Transaction is a block trade parent.
BLCH Child Transaction is a block trade child.
7.1.18.23.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Block parent or child information expressed as a proprietary code.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 381 March 2026
```

