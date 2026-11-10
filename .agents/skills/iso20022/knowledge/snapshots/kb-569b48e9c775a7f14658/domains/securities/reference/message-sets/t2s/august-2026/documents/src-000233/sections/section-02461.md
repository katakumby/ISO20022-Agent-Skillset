---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.113 PendingReason31Code"]
file_pages: [3278]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.113 PendingReason31Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3278 to 3278.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3278

```text
CodeName Name Definition
CDLR ConditionalDeliveryAwaitingRelease Instruction is in a hold/frozen/preadvice
mode. Market infrastructure platform is
awaiting release.
INBC IncompleteNumberCount Not all the instructions part of a pool
have been received.
PATD PartialDiffer Disagreement on partial indicator
preventing partial settlement.
PREL PartiallyReleased Transaction has been partially released.
82.2.2.113  PendingReason31Code
Definition: Specifies the reason the transaction/instruction is pending settlement. Settlement on the
instructed settlement date is still possible.
Type: CodeSet
CodeName Name Definition
BLOC AccountBlocked Your account is blocked, no instruction
can settle over the account.
PART TradeSettlesInPartials Trade will settle in partials.
COLL SecuritiesPledgedAsCollateral Financial instruments are not deliverable
as they are pledged as collateral.
LINK PendingLinkedInstruction Your instruction is pending settlement
because the instruction linked to it is
pending.
FUTU AwaitingSettlementDate Awaiting settlement date. No settlement
problems to be reported.
LACK LackOfSecurities Insufficient financial instruments in your
account.
SBLO SecuritiesBlocked Financial instruments are blocked due to
a corporate action event, realignment,
etc.
OTHR Other Other. See Narrative.
PRSY SystemOnHold Transaction was put on hold/frozen by
the system.
INBC IncompleteNumberCount Not all the instructions part of a pool
have been received.
82.2.2.114  PendingReason32Code
Definition: Specifies the reason why a cancellation request sent for the related instruction is pending.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. It will be
managed as per the bilateral service
agreement between the account servicer
and account owner.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3278 August 2026
```

