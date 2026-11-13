---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.162 TransactionActivity1Code"]
file_pages: [2173]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.162 TransactionActivity1Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2173 to 2173.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2173

```text
CodeName Name Definition
dividend, that is, selling before the ex
date without the coupon.
GTDL GuaranteedDelivery Indicates whether the delivery of the
financial instrument on settlement date
is guaranteed.
BCRO ResultOption Result of option when set. (UK specific).
BCRP ResultRepo Result of repo when set (UK specific).
BCFD DeliveryForm Form of delivery, not for foreign
registration when unset (UK specific).
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
35.2.2.162  TransactionActivity1Code
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
35.2.2.163  TypeOfIdentification1Code
Definition: Specifies the type of alternate identification which can be used to give an alternate
identification of the party identified.
Type: CodeSet
CodeName Name Definition
ARNU AlienRegistrationNumber Number assigned by a government
agency to identify foreign nationals.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2173 March 2026
```

