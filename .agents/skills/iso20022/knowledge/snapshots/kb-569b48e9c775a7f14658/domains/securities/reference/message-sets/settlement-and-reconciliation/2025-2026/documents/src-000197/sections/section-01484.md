---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.63 DeniedReason15Choice"]
file_pages: [1975]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.63 DeniedReason15Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1975 to 1975.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1975

```text
35.1.29.63  DeniedReason15Choice
Definition: Choice of format for the denied reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1975
Or}   Proprietary <Prtry> [1..1] ± 1975
35.1.29.63.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the request was denied.
Datatype: "DeniedReason6Code" on page 2060
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline.
CDCY ConditionalCurrency Execution is denied due to a process
linked to the currency of the transaction.
CDRE ConditionalRealignement Execution is denied due to the execution
of a process of realignment at the issuer
CSD.
DCAN DeniedSinceCancelled Request was denied since the instruction
has been cancelled.
DSET DeniedSinceSettled Request was denied because the
instruction was settled.
DPRG DeniedSinceInProgress Request was denied because the
process of settlement is in progress.
DREP DeniedSinceRepoEnded Request was denied because the repo
was cancelled.
LATE MarketDeadlineMissed Received after market deadline.
OTHR Other Other. See Narrative.
CDRG ConditionalRegistrar Execution is denied due to the execution
of a process at the registrar.
35.1.29.63.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the request was denied.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1975 March 2026
```

