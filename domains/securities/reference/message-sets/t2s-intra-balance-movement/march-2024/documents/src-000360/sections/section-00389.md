---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.22 ProcessingStatus69Choice", "17.1.16.22.7 Cancelled <Canc>"]
file_pages: [455]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.22.7 Cancelled <Canc>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 455 to 455.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 455

```text
Denied <Dnd> contains one of the following elements (see "DeniedStatus16Choice" on page 434 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 435
Or}   Reason <Rsn> [1..*]  435
     Code <Cd> [1..1] ± 435
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 435
17.1.16.22.7  Cancelled <Canc>
Presence: [1..1]
Definition: Cancellation requested executed.
Cancelled <Canc> contains one of the following elements (see "CancellationStatus15Choice" on
page 428 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 429
Or}   Reason <Rsn> [1..*]  429
     Code <Cd> [1..1] ± 429
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 429
17.1.16.23  ProcessingStatus68Choice
Definition: Choice of format for the processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 455
Or}   Proprietary <Prtry> [1..1] ± 456
17.1.16.23.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of an instruction.
Datatype: "TransactionProcessingStatus3Code" on page 492
CodeName Name Definition
CAND Cancelled Instruction has been cancelled.
PACK AcknowledgedAccepted Instruction has been acknowledged/
accepted for further processing by the
account servicer.
REJT Rejected Instruction has been rejected for further
processing.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
455 March 2024
```

