---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.13 PendingReason30Choice", "82.1.30.13.2 Proprietary <Prtry>"]
file_pages: [3145]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.13.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3145 to 3145.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3145

```text
CodeName Name Definition
CDAC ConditionalDeliveryAwaitingCancellation Awaiting cancellation of one of the party.
INBC IncompleteNumberCount Not all the instructions part of a pool
have been received.
82.1.30.13.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the cancellation request is pending.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.30.14  ProcessingStatus68Choice
Definition: Choice of format for the processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3145
Or}   Proprietary <Prtry> [1..1] ± 3145
82.1.30.14.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of an instruction.
Datatype: "TransactionProcessingStatus3Code" on page 3312
CodeName Name Definition
CAND Cancelled Instruction has been cancelled.
PACK AcknowledgedAccepted Instruction has been acknowledged/
accepted for further processing by the
account servicer.
REJT Rejected Instruction has been rejected for further
processing.
REPR InRepair Instruction is accepted but in repair.
82.1.30.14.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies a choice of status for the processing of an intra-balance movement.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3145 August 2026
```

