---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.61 Reporting2Code"]
file_pages: [644]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.61 Reporting2Code

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 644 to 644.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 644

```text
CodeName Name Definition
TXST TaxStatus Unrecognised or invalid tax status of the
securities instructed.
ULNK Unknown Message was not recognised. Unknown
linked reference.
VASU VariableRateSupport Unrecognised or invalid variable rate
support (repurchase agreement).
7.2.2.61  Reporting2Code
Definition: Specifies information with regards to reporting.
Type: CodeSet
CodeName Name Definition
STEX StockExchange Trade details are to be reported to a
stock exchange.
REGU RegulatoryOrganisation Trade details are to be reported to a
regulatory organisation.
DEFR DeferredReport Report is deferred, for example, because
the order was executed in partial fills.
7.2.2.62  RepurchaseType9Code
Definition: Specifies the type of repurchase transaction.
Type: CodeSet
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 644 February 2025
```

