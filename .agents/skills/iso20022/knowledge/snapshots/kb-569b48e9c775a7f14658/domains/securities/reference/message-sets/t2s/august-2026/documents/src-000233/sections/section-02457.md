---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.105 PenaltyCalculationMethod1Code"]
file_pages: [3268]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.105 PenaltyCalculationMethod1Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3268 to 3268.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3268

```text
82.2.2.105  PenaltyCalculationMethod1Code
Definition: Specifies the calculation method for the penalty.
Type: CodeSet
CodeName Name Definition
BOTH Both Sum of the penalty based on the quantity
of securities
failed to be delivered and penalty rate of
the securities and the penalty based on
the amount of cash failed to be delivered
and the discount rate of the currency.
CASH Cash Penalty is based on the amount of cash
failed to be delivered and the penalty
rate is the discount rate of the relevant
currency.
MIXE Mixed Penalty is based on the quantity of
securities failed to be delivered and
penalty rate is the discount rate of the
relevant currency.
SECU Securities Penalty is based on the quantity of
securities failed to be delivered and
penalty rate of the securities.
82.2.2.106  PenaltyListType1Code
Definition: Specifies the type of report for the penalties.
Type: CodeSet
CodeName Name Definition
CURR Current To report the new penalties and the
modified penalties in one single
message /report.
FWAM ForwardAmend To report a penalty list that has been
amended (that is the penalty list contains
only updated and/or removed penalties
that have already been previously
reported in a FWIS Penalty List).
FWIS ForwardInitialSubmission To report a daily penalty list created for
the first time (that is the penalty list
contains only newly computed penalties)
82.2.2.107  PenaltyStatus2Code
Definition: Specifies the status of the penalty.
Type: CodeSet
CodeName Name Definition
ACTV Active Penalty is active for the party.
NCOM NotComputed Penalty could not be computed.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3268 August 2026
```

