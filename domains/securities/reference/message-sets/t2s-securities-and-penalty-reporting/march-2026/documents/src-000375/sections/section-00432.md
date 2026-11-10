---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.79 TransactionActivity1Code"]
file_pages: [546]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.79 TransactionActivity1Code

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 546 to 546.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 546

```text
CodeName Name Definition
BCBL BoardLot Board lots, not set for odd lots (UK
specific).
BCBN BadName Bad names, not set for good names (UK
specific).
MAPR MarketPrice Trade was executed at market price.
NEGO NegotiatedTrade Trade for which the price is not the one
quoted but an improved one, that is, the
negotiated price.
NMPR NonMarketPrice Trade was executed outside of normal
market conditions, for example, in the
case of an iceberg order.
BCPD DeliverCountryIncorporation Place of delivery, in country of
incorporation when unset (UK specific).
7.2.2.79  TransactionActivity1Code
Definition: Specifies the type of activity to which this transaction relates.
Type: CodeSet
CodeName Name Definition
BOLE BorrowingLendingActivity Transaction relates to lending/borrowing.
CLAI MarketClaim Transaction relates to a market claim
following a corporate action.
COLL CollateralActivity Transaction relates to collateral.
CORP CorporateActionActivity Transaction relates to corporate action.
SETT SettlementandClearingActivity Transaction relates to settlement and
clearing.
7.2.2.80  TransactionProcessingStatus4Code
Definition: Specifies the status of an instruction.
Type: CodeSet
CodeName Name Definition
PACK AcknowledgedAccepted Instruction has been acknowledged/
accepted for further processing by the
account servicer.
PPRC PendingProcessing Processing of the instruction is pending.
REJT Rejected Instruction has been rejected for further
processing.
REPR InRepair Instruction is accepted but in repair.
CAND Cancelled Instruction has been cancelled.
CANP PendingCancellation Cancellation request from yourself for
this instruction is pending waiting for
further processing.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 546 March 2026
```

