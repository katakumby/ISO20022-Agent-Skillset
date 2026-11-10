---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.18 MatchingStatus27Choice", "82.1.30.18.1 Code <Cd>"]
file_pages: [3152]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.18.1 Code <Cd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3152 to 3152.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3152

```text
82.1.30.18.1  Code <Cd>
Presence: [1..1]
Definition: Provides the matching status of the instruction.
Datatype: "MatchingStatus1Code" on page 3263
CodeName Name Definition
MACH Matched Instruction has been matched.
NMAT Unmatched Instruction has not been matched.
82.1.30.18.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the matching status of the instruction.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.30.19  ProcessingStatus71Choice
Definition: Choice of format for the processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 3152
Or   Pending <Pdg> [1..1] ± 3153
Or   Rejected <Rjctd> [1..1] ± 3153
Or   Repair <Rpr> [1..1] ± 3153
Or   Denied <Dnd> [1..1] ± 3154
Or   Completed <Cmpltd> [1..1] ± C6 3154
Or}   Proprietary <Prtry> [1..1] ± 3155
82.1.30.19.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Request has been acknowledged by the account servicer.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3152 August 2026
```

