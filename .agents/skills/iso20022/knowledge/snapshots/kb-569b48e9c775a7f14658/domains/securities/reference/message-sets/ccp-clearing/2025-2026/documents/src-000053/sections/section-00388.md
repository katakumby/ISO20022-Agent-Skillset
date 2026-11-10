---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.2 Message Datatypes", "12.2.2 CodeSet", "12.2.2.24 ReceiveDelivery1Code"]
file_pages: [481]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.2.2.24 ReceiveDelivery1Code

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 481 to 481.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 481

```text
CodeName Name Definition
YIEL Yield Price expressed as a yield.
SPRE Spread Difference between a market maker's bid
and asked price.
PEUN PerUnit Price expressed per unit.
ABSO Absolute Price is expressed as absolute.
TEDP TEDPrice Price is expressed as Treasury Euro
Dollar price.
TEDY TEDYield Price is expressed as Treasury Euro
Dollar yield.
FICT FixedCabinetTrade Cabinet trades are used to indicate
prices that trade at a price lower than
that available on an exchange and they
can be fixed or variable (primarily used
for listed futures and options).
VACT VariableCabinetTrade Cabinet trades are used to indicate
prices that trade at a price lower than
that available on an exchange and they
can be fixed or variable (primarily used
for listed futures and options).
PRCT Percentage Price expressed as a percentage of par.
ACTU ActualAmount Price expressed as a currency and
amount per unit or per share.
12.2.2.24  ReceiveDelivery1Code
Definition: Specifies whether the settlement transaction is a delivery or receipt.
Type: CodeSet
CodeName Name Definition
DELI Delivery Financial instruments will be debited
from the safekeeping account.
RECE Receive Financial instruments will be credited to
the safekeeping account.
12.2.2.25  SafekeepingPlace1Code
Definition: Specifies the type of place of safekeeping.
Type: CodeSet
CodeName Name Definition
CUST SharesHeldAtLocalCustodian Financial instruments held at a local
custodian.
ICSD SharesHeldAtICSD Financial instruments held at an
International Central Securities
Depository.
NCSD SharesHeldAtNCSD Financial instruments held at a National
Central Securities Depository.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 481
```

