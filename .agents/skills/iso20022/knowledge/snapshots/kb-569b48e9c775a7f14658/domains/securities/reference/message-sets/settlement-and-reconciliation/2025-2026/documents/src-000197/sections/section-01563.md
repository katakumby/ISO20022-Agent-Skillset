---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.49 FailingReason6Code"]
file_pages: [2078]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.49 FailingReason6Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2078 to 2078.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2078

```text
CodeName Name Definition
DKNY CounterpartyReturnedShares Counterparty has returned or refuses the
securities.
FROZ SecuritiesFrozenAtCSD Financial instruments are blocked at the
Central Security Depository (CSD)
following a corporate event.
LAAW AwaitingOtherTransaction Awaiting settlement of a purchase to
cover failing positions.
LATE MarketDeadlineMissed Instruction was received after market
deadline.
LIQU InsufficientCentralBankLiquidity Central bank liquidity is insufficient.
PRCY CounterpartyInstructionOnHold Counterparty's instruction is a preadvice,
that is, for matching only.
REGT CertificatesRejected Certificates have been lodged with the
registrar but rejected due to incomplete
documentation or foreign ownership
limitation reached.
SETS SettlementSystemMethodModified Settlement system/method has been
modified at central securities depository
to allow settlement.
CERT WrongCertificatesNumbers Certificate number error.
PRSY SystemOnHold Transaction was put on hold/frozen by
the system.
CDLR ConditionalDeliveryAwaitingRelease Instruction is in a hold/frozen/preadvice
mode. Market infrastructure platform is
awaiting release.
CSDH CSDHold Central securities depository sets the
instruction in a hold/frozen/preadvice
mode.
CVAL CSDValidation Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditions of
a restriction processing type in the
market infrastructure platform.
INBC IncompleteNumberCount Not all the instructions part of a pool
have been received.
PATD PartialDiffer Disagreement on partial indicator
preventing partial settlement.
PREL PartiallyReleased Transaction has been partially released.
35.2.2.49  FailingReason6Code
Definition: Specifies the reason the transaction/instruction is failing settlement. Settlement on the
instructed settlement date is no longer possible.
Type: CodeSet
CodeName Name Definition
BLOC AccountBlocked Your account is blocked, no instruction
can settle over the account.
PART TradeSettlesInPartials Trade will settle in partials.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2078 March 2026
```

