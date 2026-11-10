---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.37 FailingReason15"]
file_pages: [310]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.37 FailingReason15

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 310 to 310.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 310

```text
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on page 270
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 270
   ProprietaryReason <PrtryRsn> [0..*] ± C5 270
9.1.21.37  FailingReason15
Definition: Specifies the reason why the instruction or request has a failing settlement status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  310
{Or     Code <Cd> [1..1] CodeSet 310
Or}     Proprietary <Prtry> [1..1] ± 311
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 311
9.1.21.37.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a failing status.
Code <Cd> contains one of the following FailingReason20Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 310
Or}   Proprietary <Prtry> [1..1] ± 311
9.1.21.37.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a failing settlement status.
Datatype: "FailingReason6Code" on page 326
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
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 310 September 2025
```

