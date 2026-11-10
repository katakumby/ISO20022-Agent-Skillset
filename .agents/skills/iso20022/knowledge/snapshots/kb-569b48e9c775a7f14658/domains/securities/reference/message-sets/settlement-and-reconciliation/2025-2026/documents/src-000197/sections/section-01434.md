---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.22 Status19Choice", "35.1.29.22.14 SettlementConditionModificationStatus <SttlmCondModSts>", "35.1.29.22.14.2 Proprietary <Prtry>"]
file_pages: [1918]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.22.14.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1918 to 1918.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1918

```text
CodeName Name Definition
DEND Denied Modification Request will not be
executed.
MODC Completed Modification has been completed.
35.1.29.22.14.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the status of the securities settlement condition modification request.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.23  PendingReason30Choice
Definition: Choice of format for the pending reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1918
Or}   Proprietary <Prtry> [1..1] ± 1919
35.1.29.23.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the cancellation request is pending.
Datatype: "PendingReason9Code" on page 2110
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. Processed
on best effort basis.
CONF AwaitingConfirmation Awaiting confirmation from the
counterparty.
OTHR Other Other. See Narrative.
CDRG ConditionalRegistrar Execution is conditional to the execution
of a process at the registrar.
CDCY ConditionalCurrency Execution is conditional to the execution
of a process linked to the currency of the
transaction.
CDRE ConditionalRealignement Execution is conditional to the execution
of a process of realignment at the issuer
CSD.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1918 March 2026
```

