---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.20 RepairReason12Choice", "35.1.29.20.2 Proprietary <Prtry>"]
file_pages: [1904]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.20.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1904 to 1904.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1904

```text
CodeName Name Definition
IEXE ReceivingDeliveringParty3 Client of delivering or receiving party 2
mismatch.
ICAG ReceivingDeliveringParty1 Participant of delivering or receiving
depository mismatch.
DEPT ReceivingDeliveringDepository Depository mismatch.
ICUS ReceivingDeliveringParty2 Client of delivering or receiving party 1
mismatch.
REPA TerminationTransactionAmount Unrecognised or invalid termination
transaction amount.
CADE TransactionCallDelay Unrecognised or invalid transaction call
delay.
RERT RepurchaseRateType Unrecognised or invalid repurchase rate
type.
RSPR SpreadRate Unrecognised or invalid spread rate.
VASU VariableRateSupport Unrecognised or invalid variable rate
support (repurchase agreement).
REPO RepurchaseRate Unrecognised or invalid repurchase rate.
REPP PremiumAmount Unrecognised or invalid premium
amount.
TERM ClosingDateTime Unrecognised or invalid closing date/
time.
FORF ForfeitAmount Unrecognised or invalid forfeit amount.
35.1.29.20.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.21  PendingReason28Choice
Definition: Choice of format for the pending reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1905
Or}   Proprietary <Prtry> [1..1] ± 1905
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1904 March 2026
```

