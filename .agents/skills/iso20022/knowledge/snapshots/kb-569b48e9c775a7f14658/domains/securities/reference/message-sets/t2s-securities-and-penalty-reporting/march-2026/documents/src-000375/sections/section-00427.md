---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.68 SettlementDate4Code"]
file_pages: [538]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.68 SettlementDate4Code

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 538 to 538.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 538

```text
CodeName Name Definition
SWIT SwitchTo Transaction is a change of an
investment from one sub-fund to another
sub-fund (subscription-leg).
ETFT ExchangeTradedFunds Relates to an ETF creation or
redemption.
REBL Rebalancing Relates to a rebalanced transaction.
TRIN TransferIn Transaction is an incoming credit to an
account on the shareholders register,
and is not linked to a shift in investment
(subscription or switch), but to account
management.
TOUT TransferOut Transaction is a debit to an account on
the shareholders register, and is not
linked to a shift in investment
(redemption or switch), but to account
management.
7.2.2.68  SettlementDate4Code
Definition: Specifies the date of settlement, in coded form.
Type: CodeSet
CodeName Name Definition
WISS WhenIssued Settlement is to be done when the
security is issued.
7.2.2.69  SettlementQueryType1Code
Definition: Specifies the type of settlement instruction query to be executed.
Type: CodeSet
CodeName Name Definition
INST Instruction Queries settlement instructions based on
criteria excluding statuses.
STTS Status Queries settlement instructions based on
criteria that includes statuses.
STPD StatusPeriod Queries settlement instructions based on
criteria that includes statuses during a
period.
7.2.2.70  SettlementSystemMethod1Code
Definition: Specifies whether the settlement instruction is to be settled through the default or the
alternate settlement system.
Type: CodeSet
CodeName Name Definition
NSET Default Settle through the default settlement
system/method. If there is a standing
instruction in place for settlement
through the alternate settlement system/
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 538 March 2026
```

