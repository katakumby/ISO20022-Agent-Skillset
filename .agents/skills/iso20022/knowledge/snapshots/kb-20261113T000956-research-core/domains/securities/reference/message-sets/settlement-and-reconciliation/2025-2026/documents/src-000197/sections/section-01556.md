---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.37 DistributionPolicy1Code"]
file_pages: [2061]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.37 DistributionPolicy1Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2061 to 2061.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2061

```text
CodeName Name Definition
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
DPRG DeniedSinceInProgress Request was denied because the
process of settlement is in progress.
DFOR DeniedSinceNotAllowed Repo call request was denied. Call not
allowed on the concerned repo, for
example, out of delay.
DREP DeniedSinceRepoEnded Request was denied because the repo
was cancelled.
DSET DeniedSinceSettled Request was denied because the
instruction was settled.
IPNC InstructionProcessed Instruction has been processed and
cannot be cancelled.
LATE MarketDeadlineMissed Received after market deadline.
OTHR Other Other. See Narrative.
35.2.2.37  DistributionPolicy1Code
Definition: Specifies if income is to be paid out (distributed) or retained (accumulated).
Type: CodeSet
CodeName Name Definition
DIST Distribution Income is distributed to the investors in
the fund.
ACCU Accumulation Income is added to the capital of the
fund.
35.2.2.38  Eligibility1Code
Definition: Identifies the type of investor. The rules that apply to each type of client are different.
Type: CodeSet
CodeName Name Definition
ELIG EligibleCounterparty Eligible customers are the most
sophisticated level of investor, able to
opt out of some the protections afforded
by conduct of business rules.
RETL RetailClient Retail customers are the least
sophisticated level of investor.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2061 March 2026
```

