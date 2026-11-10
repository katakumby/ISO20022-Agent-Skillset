---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.153 SettlementSystemMethod1Code"]
file_pages: [3301]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.153 SettlementSystemMethod1Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3301 to 3301.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3301

```text
CodeName Name Definition
STPD StatusPeriod Queries settlement instructions based on
criteria that includes statuses during a
period.
82.2.2.153  SettlementSystemMethod1Code
Definition: Specifies whether the settlement instruction is to be settled through the default or the
alternate settlement system.
Type: CodeSet
CodeName Name Definition
NSET Default Settle through the default settlement
system/method. If there is a standing
instruction in place for settlement
through the alternate settlement system/
method, then this standing instruction is
to be ignored.
YSET Alternative Settle through the alternate settlement
system/method. If there is a standing
instruction in place for settlement
through the default settlement system/
method, then this standing instruction is
to be ignored.
82.2.2.154  SettlementTransactionCondition12Code
Definition: Specifies the conditions under which the order/trade is to be settled.
Type: CodeSet
CodeName Name Definition
ADEA AcceptAfterRegularSettlementDeadline Settlement is on a bilaterally accepted
transaction that is to be accepted
beyond the regular settlement deadline.
ASGN Assignement Transfer of ownership of the asset to
another party during the closing of an
option.
BUTC BuytoCover Transaction is a buy to cover.
CLEN Clean Tax-exempt financial instruments are to
be settled.
DLWM DeliveryWithoutMatching Matching receipt instruction not required
(only for concerned international or
national central securities depositories).
DIRT Dirty Taxable financial instruments are to be
settled.
DRAW Drawn Settlement transactions relates to drawn
securities.
EXER Exercised Settlement transaction relates to options,
futures or derivatives that are exercised.
EXPI Expired Settlement transaction relates to options,
futures or derivatives that have expired.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3301 August 2026
```

