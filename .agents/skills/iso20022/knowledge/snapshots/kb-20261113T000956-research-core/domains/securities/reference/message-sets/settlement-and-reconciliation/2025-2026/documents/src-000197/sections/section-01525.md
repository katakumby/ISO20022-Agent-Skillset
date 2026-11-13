---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.94 PendingCancellationReasons6Choice", "35.1.29.94.1 Code <Cd>"]
file_pages: [2023]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.94.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2023 to 2023.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2023

```text
35.1.29.94.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the cancellation request is pending.
Datatype: "PendingReason34Code" on page 2109
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. It will be
managed as per the bilateral service
agreement between the account servicer
and account owner.
CONF AwaitingConfirmation Awaiting confirmation from the
counterparty.
OTHR Other Other. See Narrative.
DQUA QuantityDisagreement Quantity of financial instruments does
not match.
35.1.29.94.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the cancellation request is pending.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.95  AcknowledgedAcceptedStatus34Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2023
Or}   Reason <Rsn> [1..*] ± 2024
35.1.29.95.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2023 March 2026
```

