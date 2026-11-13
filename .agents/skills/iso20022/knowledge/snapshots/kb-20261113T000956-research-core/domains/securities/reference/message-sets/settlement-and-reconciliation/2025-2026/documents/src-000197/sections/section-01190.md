---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.92 SettlementTransactionCondition41Choice"]
file_pages: [1641]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.92 SettlementTransactionCondition41Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1641 to 1641.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1641

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.92  SettlementTransactionCondition41Choice
Definition: Choice of format for the settlement transaction conditions.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1641
Or}   Proprietary <Prtry> [1..1] ± 1642
35.1.16.92.1  Code <Cd>
Presence: [1..1]
Definition: Settlement conditions expressed as an ISO 20022 code.
Datatype: "SettlementTransactionCondition16Code" on page 2163
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1641 March 2026
```

