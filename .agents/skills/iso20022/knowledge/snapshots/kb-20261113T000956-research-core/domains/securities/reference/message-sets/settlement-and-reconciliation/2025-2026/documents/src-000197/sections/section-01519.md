---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.90 PendingReason80Choice"]
file_pages: [2017]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.90 PendingReason80Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2017 to 2017.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2017

```text
35.1.29.90  PendingReason80Choice
Definition: Choice of format for the pending reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2017
Or}   Proprietary <Prtry> [1..1] ± 2017
35.1.29.90.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason code why the instruction or request is pending.
Datatype: "PendingReason32Code" on page 2105
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. It will be
managed as per the bilateral service
agreement between the account servicer
and account owner.
CONF AwaitingConfirmation Awaiting confirmation from the
counterparty.
CDCY ConditionalCurrency Execution is conditional to the execution
of a process linked to the currency of the
transaction.
CDRE ConditionalRealignement Execution is conditional to the execution
of a process of realignment at the issuer
CSD.
CDRG ConditionalRegistrar Execution is conditional to the execution
of a process at the registrar.
OTHR Other Other. See Narrative.
35.1.29.90.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason code why the instruction or request is pending, using a proprietary
format.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.91  PendingStatus82Choice
Definition: Specifies whether the status is provided with a reason or not.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2017 March 2026
```

