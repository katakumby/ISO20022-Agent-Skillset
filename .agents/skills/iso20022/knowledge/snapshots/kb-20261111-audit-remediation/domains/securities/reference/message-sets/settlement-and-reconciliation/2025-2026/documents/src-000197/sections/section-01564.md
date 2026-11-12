---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.50 FormOfSecurity1Code"]
file_pages: [2079]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.50 FormOfSecurity1Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2079 to 2079.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2079

```text
CodeName Name Definition
LINK PendingLinkedInstruction Your instruction is pending settlement
because the instruction linked to it is
pending.
LACK LackOfSecurities Insufficient financial instruments in your
account.
CYCL AwaitingNextSettlementCycle Your instruction is confirmed in the local
market or is ready for settlement,
awaiting next settlement cycle.
SBLO SecuritiesBlocked Financial instruments are blocked due to
a corporate action event, realignment,
etc.
OTHR Other Other. See Narrative.
LATE MarketDeadlineMissed Instruction was received after market
deadline.
CERT WrongCertificatesNumbers Certificate number error.
PRSY SystemOnHold Transaction was put on hold/frozen by
the system.
INBC IncompleteNumberCount Not all the instructions part of a pool
have been received.
35.2.2.50  FormOfSecurity1Code
Definition: Form of a financial instrument.
Type: CodeSet
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
35.2.2.51  GeneratedReason3Code
Definition: Specifies the reason why the transaction was generated.
Type: CodeSet
CodeName Name Definition
COLL CollateralManagement Transaction has been generated for
collateral management purposes.
CLAI MarketClaim Transaction resulting from a market
claim.
OTHR Other Other. See Narrative.
RODE ReturnRefusedDumps Relates to the return of financial
instruments resulting from a rejected
delivery without matching operation.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2079 March 2026
```

