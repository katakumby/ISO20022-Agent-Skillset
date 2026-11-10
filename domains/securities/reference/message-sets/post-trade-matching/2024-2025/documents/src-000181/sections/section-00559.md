---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.69 SettlementSystemMethod1Code"]
file_pages: [647]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.69 SettlementSystemMethod1Code

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 647 to 647.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 647

```text
CodeName Name Definition
INTE InternalDatabase The settlement standing instruction
database to be used is the receiver's
internal database.
BRKR BrokerDatabase The settlement standing instruction
database to be used is the broker's
database.
VEND VendorDatabase The settlement standing instruction
database to be used is the database of
the vendor.
7.2.2.69  SettlementSystemMethod1Code
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
7.2.2.70  SettlementTransactionCondition7Code
Definition: Specifies the conditions under which the order/trade is to be settled.
Type: CodeSet
CodeName Name Definition
ASGN Assignment Transfer of ownership of the asset to
another party during the closing of an
option.
CLEN Clean Indicates that the trade was executed
clean, ie government tax must not be
paid on the accrued interest on the bond.
DIRT Dirty Indicates that the trade was executed
dirty, ie government tax must be paid on
the accrued interest on the bond.
DLWM DeliveryWithoutMatching Matching receipt instruction not required
(only for concerned international or
national central securities depositories).
DRAW Drawn Settlement transactions relates to drawn
securities.
EXER Exercised Settlement transaction relates to options,
futures or derivatives that are exercised.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 647 February 2025
```

