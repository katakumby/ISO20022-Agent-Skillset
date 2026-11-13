---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.26 AcknowledgedAcceptedStatus24Choice", "9.1.21.26.2 Reason <Rsn>", "9.1.21.26.2.1 Code <Cd>"]
file_pages: [295]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.26.2.1 Code <Cd>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 295 to 295.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 295

```text
9.1.21.26.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason provided for the status.
Code <Cd> contains one of the following elements (see "AcknowledgementReason15Choice" on
page 291 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 291
Or}   Proprietary <Prtry> [1..1] ± 292
9.1.21.26.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 344
9.1.21.27  DeniedReason16Choice
Definition: Choice of format for the denied reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 295
Or}   Proprietary <Prtry> [1..1] ± 296
9.1.21.27.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the request was denied.
Datatype: "DeniedReason4Code" on page 324
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline.
DCAN DeniedSinceAlreadyCancelled Cancellation request was denied since
the instruction has already been
cancelled.
DPRG DeniedSinceInProgress Cancellation request was denied
because the process of settlement is in
progress.
DREP DeniedSinceRepoEnded Cancellation request was denied
because the repo was cancelled.
DSET DeniedSinceAlreadySettled Cancellation request was denied
because the instruction was already
settled.
LATE MarketDeadlineMissed Received after market deadline.
OTHR Other Other. See Narrative.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 295 September 2025
```

