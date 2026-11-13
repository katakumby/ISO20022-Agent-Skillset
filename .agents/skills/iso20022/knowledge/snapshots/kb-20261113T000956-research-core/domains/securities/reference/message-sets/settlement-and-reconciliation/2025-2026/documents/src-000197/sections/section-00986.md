---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.4 Balance", "35.1.4.10 OpeningBalance5"]
file_pages: [1422]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.4.10 OpeningBalance5

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1422 to 1422.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1422

```text
UnrealisedGainLoss <UrlsdGnLoss> contains the following elements (see "AmountAndDirection6" on
page 1361 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1362
   Sign <Sgn> [1..1] Indicator 1362
35.1.4.10  OpeningBalance5
Definition: Opening balance for the statement period (first opening balance) or of this page
(intermediary opening balance).
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [1..1] CodeSet 1422
   OpeningBalance <OpngBal> [1..1] ± 1422
Constraints
• ShortLongDefaultRule
If Shortlong is absent, then the default is long, that is, balance is positive.
35.1.4.10.1  ShortLongIndicator <ShrtLngInd>
Presence: [1..1]
Definition: Indication that the position is short or long.
Datatype: "ShortLong1Code" on page 2171
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
LONG Long Position is long, that is, the balance is
positive.
35.1.4.10.2  OpeningBalance <OpngBal>
Presence: [1..1]
Definition: Opening balance for the statement period (first opening balance) or of this page
(intermediary opening balance).
OpeningBalance <OpngBal> contains one of the following elements (see "OpeningBalance6Choice"
on page 1431 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   First <Frst> [1..1] ± 1431
Or}   Intermediary <Intrmy> [1..1] ± 1431
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1422 March 2026
```

