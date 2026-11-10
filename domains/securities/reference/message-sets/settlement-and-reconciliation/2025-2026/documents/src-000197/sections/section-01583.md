---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.86 PledgeeType1Code"]
file_pages: [2111]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.86 PledgeeType1Code

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2111 to 2111.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2111

```text
CodeName Name Definition
CDCY ConditionalCurrency Execution is conditional to the execution
of a process linked to the currency of the
transaction.
CDRE ConditionalRealignement Execution is conditional to the execution
of a process of realignment at the issuer
CSD.
CDAC ConditionalDeliveryAwaitingCancellation Awaiting cancellation of one of the party.
INBC IncompleteNumberCount Not all the instructions part of a pool
have been received.
35.2.2.86  PledgeeType1Code
Definition: Specifies the type of pledgee.
Type: CodeSet
CodeName Name Definition
CPTY Counterparty Financial instruments are pledged to a
counterparty.
REGB RegulatoryBody Financial instruments are pledged to a
regulatory body.
35.2.2.87  PreConfirmation1Code
Definition: Specifies if there is a pre-confirmation of cash or securities.
Type: CodeSet
CodeName Name Definition
PRCA PreConfirmCash Pre-confirmation of the movement of the
cash, pending the movement of
securities.
PRSE PreConfirmSecurities Pre-confirmation of the movement of the
securities, pending the movement of
cash.
35.2.2.88  PriceValueType12Code
Definition: Price will not be paid.
Type: CodeSet
CodeName Name Definition
DISC Discount Price expressed as a number of
percentage points below par, for
example, a discount price of 2.0%
equals a price of 98 when par is 100.
PARV Par Price is the face amount.
PREM Premium Price expressed as a number of
percentage points above par, for
example, a premium price of 2.0%
equals a price of 102 when par is 100.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2111 March 2026
```

