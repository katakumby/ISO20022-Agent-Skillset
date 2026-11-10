---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.2 Message Datatypes", "12.2.2 CodeSet", "12.2.2.21 NettingEligible1Code"]
file_pages: [480]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.2.2.21 NettingEligible1Code

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 480 to 480.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 480

```text
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MIST Mister Title of the person is Mister or Mr.
MISS Miss Title of the person is Miss.
MADM Madam Title of the person is Madam.
12.2.2.21  NettingEligible1Code
Definition: Specifies whether the trade is eligible for netting.
Type: CodeSet
CodeName Name Definition
GROS Gross Indicates that the trade is not eligible for
settlement netting.
NETT Nett Indicates that the trade is eligible for
settlement netting.
AGFS AggregationForSettlement Grouping of receipts/purchases to create
one settlement obligation, and the
grouping of deliveries/sales to create
one settlement obligation.
12.2.2.22  ObligationType1Code
Definition: Specifies the type of the obligation.
Type: CodeSet
CodeName Name Definition
FAIL Fails Specifies that the obligation is related to
a failed trade.
NEW1 New Specifies that the obligation is related to
new a trade.
COEV CorporateEvent Specifies that the obligation is related to
a corporate event.
12.2.2.23  PriceValueType7Code
Definition: Specifies a type of value of the price.
Type: CodeSet
CodeName Name Definition
DISC Discount Price expressed as a number of
percentage points below par, for
example, a discount price of 2.0%
equals a price of 98 when par is 100.
PREM Premium Price expressed as a number of
percentage points above par, for
example, a premium price of 2.0%
equals a price of 102 when par is 100.
PARV Par Price is the face amount.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 480
```

