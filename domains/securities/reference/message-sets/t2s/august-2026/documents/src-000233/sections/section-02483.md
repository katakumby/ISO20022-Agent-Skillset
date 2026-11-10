---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.163 Status10Code"]
file_pages: [3305]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.163 Status10Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3305 to 3305.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3305

```text
CodeName Name Definition
DELT Delta Statement contains changes only.
82.2.2.163  Status10Code
Definition: Specifies the status of an instruction.
Type: CodeSet
CodeName Name Definition
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
REJT Rejected Instruction has been rejected.
PART PartiallyCompleted Processing has been partially
completed.
82.2.2.164  Status6Code
Definition: Specifies the status of an instruction.
Type: CodeSet
CodeName Name Definition
REJT Rejected Instruction has been rejected.
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
82.2.2.165  SystemSecuritiesAccountType1Code
Definition: Lists the type of the securities account specific for a system.
Type: CodeSet
CodeName Name Definition
CSDP CSDParticipantAccount Account owned by a CSD Participant
.
CSDM CSDMirrorAccount Account operated by CSD for mirroring
positions
.
ICSA InterCSDAccount Account operated by CSD for settlement
of securities legs for instructions
involving internal CSD s.
TOFF TechnicalOffsetAccount Account operated by CSDs in a direct
holding market context.
CSDO CSDOmnibusAccount Account operated by CSD in cross-CSD
settlement context.
ISSA IssuanceAccount Account reflecting the holdings of the
participants of the issuer CSD for a given
financial instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3305 August 2026
```

