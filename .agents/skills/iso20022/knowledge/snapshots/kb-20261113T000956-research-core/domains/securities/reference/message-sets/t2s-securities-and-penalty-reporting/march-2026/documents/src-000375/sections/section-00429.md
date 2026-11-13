---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.72 SettlementTransactionCondition5Code"]
file_pages: [540]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.72 SettlementTransactionCondition5Code

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 540 to 540.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 540

```text
CodeName Name Definition
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
7.2.2.72  SettlementTransactionCondition5Code
Definition: Specifies the conditions under which the order/trade is to be settled.
Type: CodeSet
CodeName Name Definition
PART PartialAllowed Partial settlement is allowed.
NPAR PartialNotAllowed Partial settlement is not allowed.
PARC PartialSettlementCashThresholdAllowed Partial settlement is allowed but must
satisfy a cash value minimum (value
defined in static data).
PARQ PartialSettlementQuantityThresholdAllowed Partial settlement is allowed but must
satisfy a minimum quantity of securities
(quantity defined in static data).
7.2.2.73  SettlingCapacity2Code
Definition: Specifies the role of the party in the settlement of the transaction.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 540 March 2026
```

