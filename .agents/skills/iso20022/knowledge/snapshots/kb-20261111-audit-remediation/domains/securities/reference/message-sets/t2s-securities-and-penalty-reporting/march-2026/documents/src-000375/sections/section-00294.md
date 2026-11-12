---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.14 SettlementTransactionCondition34Choice", "7.1.18.14.2 Proprietary <Prtry>"]
file_pages: [371]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.14.2 Proprietary <Prtry>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 371 to 371.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 371

```text
CodeName Name Definition
KNOC KnockedOut Settlement transaction relates to options,
futures or derivatives that are expired
worthless.
NOMC NoAutomaticMarketClaim No market claim should be automatically
generated.
NACT NotAccountingRelated Security transaction is not for
accounting.
PENS PendingSale Position to cover the pending sale will be
available by contractual settlement date
(accounting information).
PHYS Physical Securities are to be physically settled.
RHYP Rehypothecation Collateral position is available for other
purposes (for example, onwards
delivery).
RPTO Reporting Relates to a transaction that is for
reporting purposes only.
RESI Residual Relates to transaction on a security that
is not eligible at the Central Security
Depository (CSD) but for which the
payment will be enacted by the central
securities depository.
SHOR ShortSell Account is used for short sale orders.
SPDL SpecialDelivery Settlement transactions to be settled
with special delivery.
SPST SplitSettlement Money and financial instruments settle in
different locations.
TRAN Transformation Transaction resulting from a
transformation.
TRIP TripartySegregation Securities are not be delivered but
segregated following triparty collateral
transaction.
UNEX Unexposed Delivery cannot be performed until
money is received.
INTS InternalisedSettlement The instruction was settled by the
settlement internaliser/account servicer
(eg custodian) in its own books and not
through a securities settlement system
(e.g. CSD system).
BPSS PartialSuccessfulBuyIn Identification of settlement instructions
created as a result of a partial successful
buy-in.
7.1.18.14.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement conditions expressed as a proprietary code.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 371 March 2026
```

