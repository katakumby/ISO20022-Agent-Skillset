---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.143 SettlementStandingInstructionDatabase1Code"]
file_pages: [2161, 2162]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.143 SettlementStandingInstructionDatabase1Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2161 to 2162.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2161

```text
35.2.2.143  SettlementStandingInstructionDatabase1Code
Definition: Indicates what settlement standing instruction database is to be used to derive the settlement
parties involved in the transaction.
Type: CodeSet
CodeName Name Definition
INTE InternalDatabase The settlement standing instruction
database to be used is the receiver's
internal database.
BRKR BrokerDatabase The settlement standing instruction
database to be used is the broker's
database.
VEND VendorDatabase The settlement standing instruction
database to be used is the database of
the vendor.
35.2.2.144  SettlementSystemMethod1Code
Definition: Specifies whether the settlement instruction is to be settled through the default or the
alternate settlement system.
Type: CodeSet
CodeName Name Definition
NSET Default Settle through the default settlement
system/method. If there is a standing
instruction in place for settlement
through the alternate settlement system/
method, then this standing instruction is
to be ignored.
YSET Alternative Settle through the alternate settlement
system/method. If there is a standing
instruction in place for settlement
through the default settlement system/
method, then this standing instruction is
to be ignored.
35.2.2.145  SettlementTransactionCondition15Code
Definition: Specifies the conditions under which the order/trade is to be settled.
Type: CodeSet
CodeName Name Definition
ADEA AcceptAfterRegularSettlementDeadline Settlement is on a bilaterally accepted
transaction that is to be accepted
beyond the regular settlement deadline.
ASGN Assignement Transfer of ownership of the asset to
another party during the closing of an
option.
BUTC BuytoCover Transaction is a buy to cover.
CLEN Clean Tax-exempt financial instruments are to
be settled.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2161 March 2026
```

## File page 2162

```text
CodeName Name Definition
DLWM DeliveryWithoutMatching Matching receipt instruction not required
(only for concerned international or
national central securities depositories).
DIRT Dirty Taxable financial instruments are to be
settled.
DRAW Drawn Settlement transactions relates to drawn
securities.
EXER Exercised Settlement transaction relates to options,
futures or derivatives that are exercised.
EXPI Expired Settlement transaction relates to options,
futures or derivatives that have expired.
FRCL FreeCleanSettlement Delivery will be made free of payment
but a clean payment order will be sent.
GATE GatingEventParticipation Gating event participation. Hold until
event start time.
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2162 March 2026
```

