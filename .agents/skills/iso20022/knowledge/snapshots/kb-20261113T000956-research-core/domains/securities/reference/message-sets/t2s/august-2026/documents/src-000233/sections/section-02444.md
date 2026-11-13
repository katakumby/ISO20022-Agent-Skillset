---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.68 FailingReason6Code"]
file_pages: [3253]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.68 FailingReason6Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3253 to 3253.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3253

```text
CodeName Name Definition
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
82.2.2.68  FailingReason6Code
Definition: Specifies the reason the transaction/instruction is failing settlement. Settlement on the
instructed settlement date is no longer possible.
Type: CodeSet
CodeName Name Definition
BLOC AccountBlocked Your account is blocked, no instruction
can settle over the account.
PART TradeSettlesInPartials Trade will settle in partials.
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3253 August 2026
```

