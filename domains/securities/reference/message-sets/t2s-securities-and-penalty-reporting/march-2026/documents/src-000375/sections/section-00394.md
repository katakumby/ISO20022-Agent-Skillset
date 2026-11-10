---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.29 Transaction Type"]
file_pages: [487]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.29 Transaction Type

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 487 to 487.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 487

```text
7.1.29 Transaction Type
7.1.29.1  TransactionActivity3Choice
Definition: Choice of format for the transaction activity identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 487
Or}   Proprietary <Prtry> [1..1] ± 487
7.1.29.1.1  Code <Cd>
Presence: [1..1]
Definition: Transaction type expressed as an ISO 20022 code.
Datatype: "TransactionActivity1Code" on page 546
CodeName Name Definition
BOLE BorrowingLendingActivity Transaction relates to lending/borrowing.
CLAI MarketClaim Transaction relates to a market claim
following a corporate action.
COLL CollateralActivity Transaction relates to collateral.
CORP CorporateActionActivity Transaction relates to corporate action.
SETT SettlementandClearingActivity Transaction relates to settlement and
clearing.
7.1.29.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Transaction type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.29.2  TradeTransactionCondition5Choice
Definition: Choice of format for the trade transaction condition.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 488
Or}   Proprietary <Prtry> [1..1] ± 489
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 487 March 2026
```

