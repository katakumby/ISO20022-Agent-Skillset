---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.9 SettlementStatus18Choice", "35.1.29.9.2 Failing <Flng>", "35.1.29.9.2.2 Reason <Rsn>", "35.1.29.9.2.2.1 Code <Cd>", "35.1.29.9.2.2.1.2 Proprietary <Prtry>"]
file_pages: [1887]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.9.2.2.1.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1887 to 1887.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1887

```text
CodeName Name Definition
DENO UnavailableDeliverableDenominatedQuantity Quantity instructed does not match the
denomination available/deliverable.
Physical securities need to be obtained
in deliverable denominated quantities.
DISA NaturalDisaster Exceptional closing of all financial
institutions due to natural disaster, for
example, earthquake.
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
35.1.29.9.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a failing settlement status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1887 March 2026
```

