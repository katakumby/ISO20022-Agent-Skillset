---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.92 SettlementTransactionCondition41Choice", "35.1.16.92.2 Proprietary <Prtry>"]
file_pages: [1642]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.92.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1642 to 1642.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1642

```text
CodeName Name Definition
GATE GatingEventParticipation Gating event participation. Hold until
event start time.
INTS InternalisedSettlement The instruction was settled by the
settlement internaliser/account servicer
(eg custodian) in its own books and not
through a securities settlement system
(e.g. CSD system).
KNOC KnockedOut Settlement transaction relates to options,
futures or derivatives that are expired
worthless.
NOMC NoAutomaticMarketClaim No market claim should be automatically
generated.
NACT NotAccountingRelated Security transaction is not for
accounting.
BPSS PartialSuccessfulBuyIn Identification of settlement instructions
created as a result of a partial successful
buy-in.
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
35.1.16.92.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement conditions expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1642 March 2026
```

