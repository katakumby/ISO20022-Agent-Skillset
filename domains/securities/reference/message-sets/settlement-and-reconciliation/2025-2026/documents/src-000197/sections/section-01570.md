---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.64 OpeningClosing1Code"]
file_pages: [2088]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.64 OpeningClosing1Code

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2088 to 2088.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2088

```text
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.2.2.64  OpeningClosing1Code
Definition: Specifies additional information relative to the processing of the trade.
Type: CodeSet
CodeName Name Definition
CLOP ClosePosition Indicates that the trade is to close a
position.
OPEP OpenPosition Indicates that the trade is to open a
position.
35.2.2.65  OptionStyle2Code
Definition: Defines how an option can be exercised.
Type: CodeSet
CodeName Name Definition
AMER American Option can be exercised before or on
expiry date.
EURO European Option that can be exercised on expiry
date only.
35.2.2.66  OptionType1Code
Definition: Indicates whether it is a Call option (right to purchase a specific underlying asset) or a Put
option (right to sell a specific underlying asset).
Type: CodeSet
CodeName Name Definition
CALL Call Right to buy a quantity of an asset for an
agreed price at exercise date.
PUTO Put Right to sell a quantity of an asset for an
agreed price at exercise date.
35.2.2.67  OriginatorRole2Code
Definition: Specifies the role of the trading party in the transaction.
Type: CodeSet
CodeName Name Definition
SINT SystematicInternaliser Firms which, on an organised, frequent
and systematic basis deal on their own
account by executing client orders
outside a regulated market or a
Multilateral Trading Facility. SI's will have
the obligation to provide, and make
public, a definite bid and offer quote for
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2088 March 2026
```

