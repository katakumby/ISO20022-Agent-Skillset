---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.30 Transaction Type", "35.1.30.4 SettlementTransactionCondition47Choice"]
file_pages: [2035]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.30.4 SettlementTransactionCondition47Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2035 to 2035.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2035

```text
35.1.30.4  SettlementTransactionCondition47Choice
Definition: Choice of format for the settlement transaction conditions.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2035
Or}   Proprietary <Prtry> [1..1] ± 2036
35.1.30.4.1  Code <Cd>
Presence: [1..1]
Definition: Settlement conditions expressed as an ISO 20022 code.
Datatype: "SettlementTransactionCondition21Code" on page 2169
CodeName Name Definition
ASGN Assignement Transfer of ownership of the asset to
another party during the closing of an
option.
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
GATE GatingEventParticipation Gating event participation. Hold until
event start time.
FRCL FreeCleanSettlement Delivery will be made free of payment
but a clean payment order will be sent.
KNOC KnockedOut Settlement transaction relates to options,
futures or derivatives that are expired
worthless.
PHYS Physical Securities are to be physically settled.
RESI Residual Relates to transaction on a security that
is not eligible at the Central Security
Depository (CSD) but for which the
payment will be enacted by the central
securities depository.
SPDL SpecialDelivery Settlement transactions to be settled
with special delivery.
SPST SplitSettlement Money and financial instruments settle in
different locations.
UNEX Unexposed Delivery cannot be performed until
money is received.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2035 March 2026
```

