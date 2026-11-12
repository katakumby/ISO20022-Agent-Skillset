---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks"]
file_pages: [283]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4 Message Building Blocks

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 283 to 283.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 283

```text
C31 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
5.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
5.4.1 ChangeInstructionIndicator <ChngInstrInd>
Presence: [0..1]
Definition: Indicates that the current instruction is replacing a previous one that was cancelled earlier.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
5.4.2 CancelledInstructionIdentification <CancInstrId>
Presence: [0..1]
Definition: Identification of a previously sent cancelled instruction document.
CancelledInstructionIdentification <CancInstrId> contains the following elements (see
"DocumentIdentification31" on page 860 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 861
   LinkageType <LkgTp> [0..1] ± C22 861
5.4.3 InstructionCancellationRequestIdentification
<InstrCxlReqId>
Presence: [0..1]
Definition: Identification of a previously sent instruction cancellation request document.
InstructionCancellationRequestIdentification <InstrCxlReqId> contains the following elements (see
"DocumentIdentification31" on page 860 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 861
   LinkageType <LkgTp> [0..1] ± C22 861
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 283 February 2026
```

