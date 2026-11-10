---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.35 DeniedReason4Code"]
file_pages: [3236]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.35 DeniedReason4Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3236 to 3236.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3236

```text
CodeName Name Definition
UNRE UnrecognisedDelivery Original delivery is not recognized.
DQUA WrongQuantity Wrong quantity delivered in the original
instruction.
DMON WrongSettlementAmount Wrong settlement amount settled in the
original delivery.
PART PartialDelivery Only a portion of the original transaction
quantity was delivered by the Central
Securities Depository (CSD).
SAFE AccountMissing Account information is missing in the
original delivery.
DUEB DueBiillMissing Due bill information missing in the
original delivery.
PARD PartialReturn Portion of the original transaction
quantity was returned by the receiver.
82.2.2.35  DeniedReason4Code
Definition: Specifies the denied reason.
Type: CodeSet
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
CDRE ConditionalRealignement Execution is denied due to the execution
of a process of realignment at the issuer
CSD.
82.2.2.36  DistributionPolicy1Code
Definition: Specifies if income is to be paid out (distributed) or retained (accumulated).
Type: CodeSet
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3236 August 2026
```

