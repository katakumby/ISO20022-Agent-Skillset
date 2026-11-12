---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.34 RepurchaseType23Choice"]
file_pages: [3017]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.34 RepurchaseType23Choice

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3017 to 3017.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3017

```text
Datatype: "Max70Text" on page 3329
82.1.19.34  RepurchaseType23Choice
Definition: Choice of format for the repurchase transaction type information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3017
Or}   Proprietary <Prtry> [1..1] ± 3017
82.1.19.34.1  Code <Cd>
Presence: [1..1]
Definition: Type of securities financing transaction process expressed as an ISO 20022 code.
Datatype: "RepurchaseType10Code" on page 3286
CodeName Name Definition
PAIR Pairoff Relates to a transaction that is paired off
and netted against one or more previous
transactions. A paired off transaction is a
buyback to offset and effectively
liquidate a prior sale of securities or a
sellback to offset and effectively liquidate
a prior buy of securities.
ROLP RepoContractRollover Relates to a repo rollover of a contract
extending the closing or maturity date
without the underlying collateral
impacted.
RATE RepoRate Is part of a pair-off.
CALL RepurchaseCall Relates to the early closing/maturity date
for a term repo or a termination date of
an open repo with the underlying
collateral.
CADJ Swap Relates to a swap/substitution.
TOPU TopUp Relates to a repo rollover of a position
extending the closing or maturity date.
WTHD Withdrawal Relates to a repo rollover of a position
extending the closing or maturity date.
82.1.19.34.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of securities financing transaction process expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3017 August 2026
```

