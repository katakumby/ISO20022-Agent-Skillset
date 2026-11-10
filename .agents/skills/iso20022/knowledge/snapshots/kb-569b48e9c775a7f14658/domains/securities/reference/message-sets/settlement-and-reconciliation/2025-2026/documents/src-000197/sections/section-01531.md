---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.100 FailingReason15"]
file_pages: [2029]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.100 FailingReason15

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2029 to 2029.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2029

```text
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on
page 1877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1878
   ProprietaryReason <PrtryRsn> [0..*] ± C1 1878
35.1.29.100  FailingReason15
Definition: Specifies the reason why the instruction or request has a failing settlement status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  2029
{Or     Code <Cd> [1..1] CodeSet 2029
Or}     Proprietary <Prtry> [1..1] ± 2030
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2030
35.1.29.100.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a failing status.
Code <Cd> contains one of the following FailingReason20Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2029
Or}   Proprietary <Prtry> [1..1] ± 2030
35.1.29.100.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a failing settlement status.
Datatype: "FailingReason6Code" on page 2078
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2029 March 2026
```

