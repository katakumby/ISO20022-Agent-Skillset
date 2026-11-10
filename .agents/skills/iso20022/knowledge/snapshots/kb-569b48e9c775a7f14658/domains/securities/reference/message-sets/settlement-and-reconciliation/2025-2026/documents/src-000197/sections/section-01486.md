---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.64 UnmatchedReason23Choice", "35.1.29.64.2 Proprietary <Prtry>"]
file_pages: [1978]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.64.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1978 to 1978.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1978

```text
CodeName Name Definition
DMCT AutomaticGeneration Disagreement on automatic generation
of market claim or transformation.
DCMX CumEx Disagreement if trade was executed cum
or ex.
35.1.29.64.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has an unmatched status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.65  DeniedReason14Choice
Definition: Choice of format for the denied reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1978
Or}   Proprietary <Prtry> [1..1] ± 1979
35.1.29.65.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the request was denied.
Datatype: "DeniedReason7Code" on page 2060
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline.
DCAL CallDeniedSinceAlreadyApplied Repo call request was denied since
another call already applies.
CDCY ConditionalCurrency Execution is denied due to a process
linked to the currency of the transaction.
CDRE ConditionalRealignement Execution is denied due to the execution
of a process of realignment at the issuer
CSD.
CDRG ConditionalRegistrar Execution is denied due to the execution
of a process at the registrar.
DCAN DeniedSinceCancelled Request was denied since the instruction
has been cancelled.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1978 March 2026
```

