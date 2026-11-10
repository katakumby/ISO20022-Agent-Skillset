---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.43 ProcessingStatus70Choice", "82.1.30.43.1 Code <Cd>"]
file_pages: [3188]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.43.1 Code <Cd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3188 to 3188.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3188

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3188
Or}   Proprietary <Prtry> [1..1] ± 3188
82.1.30.43.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the processing status of the instruction in a coded format.
Datatype: "TransactionProcessingStatus4Code" on page 3312
CodeName Name Definition
PACK AcknowledgedAccepted Instruction has been acknowledged/
accepted for further processing by the
account servicer.
PPRC PendingProcessing Processing of the instruction is pending.
REJT Rejected Instruction has been rejected for further
processing.
REPR InRepair Instruction is accepted but in repair.
CAND Cancelled Instruction has been cancelled.
CANP PendingCancellation Cancellation request from yourself for
this instruction is pending waiting for
further processing.
CPRC CancellationRequested Cancellation request from the
counterparty is awaiting for your
cancellation request or your consent.
MPRC ModificationRequested Modification request from the
counterparty is awaiting for your
modification request or your consent.
82.1.30.43.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the processing status of the instruction in a proprietary format.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.30.44  RepairStatus12Choice
Definition: Specifies whether the status is provided with a reason or not.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3188 August 2026
```

