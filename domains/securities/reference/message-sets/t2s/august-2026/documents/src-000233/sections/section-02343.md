---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.1 SettlementStatus32Choice", "82.1.30.1.2 Failing <Flng>", "82.1.30.1.2.2 Reason <Rsn>", "82.1.30.1.2.2.1 Code <Cd>", "82.1.30.1.2.2.1.2 Proprietary <Prtry>"]
file_pages: [3128]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.1.2.2.1.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3128 to 3128.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3128

```text
CodeName Name Definition
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
PATD PartialDiffer Disagreement on partial indicator
preventing partial settlement.
PREL PartiallyReleased Transaction has been partially released.
82.1.30.1.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a failing settlement status.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3128 August 2026
```

