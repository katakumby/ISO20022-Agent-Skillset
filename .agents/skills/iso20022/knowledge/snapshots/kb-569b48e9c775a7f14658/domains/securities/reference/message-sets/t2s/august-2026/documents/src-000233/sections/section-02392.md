---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.39 AcknowledgedAcceptedStatus24Choice", "82.1.30.39.2 Reason <Rsn>", "82.1.30.39.2.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [3182]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.39.2.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3182 to 3182.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3182

```text
Code <Cd> contains one of the following elements (see "AcknowledgementReason15Choice" on
page 3173 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3173
Or}   Proprietary <Prtry> [1..1] ± 3173
82.1.30.39.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 3327
82.1.30.40  DeniedReason16Choice
Definition: Choice of format for the denied reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3182
Or}   Proprietary <Prtry> [1..1] ± 3183
82.1.30.40.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the request was denied.
Datatype: "DeniedReason4Code" on page 3236
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
CDRG ConditionalRegistrar Execution is denied due to the execution
of a process at the registrar.
CDCY ConditionalCurrency Execution is denied due to a process
linked to the currency of the transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3182 August 2026
```

