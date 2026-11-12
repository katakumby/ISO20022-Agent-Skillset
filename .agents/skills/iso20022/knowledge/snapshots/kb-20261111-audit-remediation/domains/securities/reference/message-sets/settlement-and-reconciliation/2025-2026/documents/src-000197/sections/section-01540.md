---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.30 Transaction Type", "35.1.30.7 SettlementTransactionCondition44Choice", "35.1.30.7.1 Code <Cd>"]
file_pages: [2039]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.30.7.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2039 to 2039.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2039

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2039
Or}   Proprietary <Prtry> [1..1] ± 2040
35.1.30.7.1  Code <Cd>
Presence: [1..1]
Definition: Settlement conditions expressed as an ISO 20022 code.
Datatype: "SettlementTransactionCondition19Code" on page 2166
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
PENS PendingSale Position to cover the pending sale will be
available by contractual settlement date
(accounting information).
PHYS Physical Securities are to be physically settled.
RHYP Rehypothecation Collateral position is available for other
purposes (for example, onwards
delivery).
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2039 March 2026
```

