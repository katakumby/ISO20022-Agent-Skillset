---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.24 ProcessingStatus67Choice", "17.1.16.24.2 Repair <Rpr>"]
file_pages: [457]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.24.2 Repair <Rpr>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 457 to 457.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 457

```text
17.1.16.24.2  Repair <Rpr>
Presence: [1..1]
Definition: Instruction or request is accepted but in repair.
Repair <Rpr> contains one of the following elements (see "RejectionOrRepairStatus38Choice" on
page 444 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 444
Or}   Reason <Rsn> [1..*]  444
     Code <Cd> [0..*]  445
{Or       Code <Cd> [1..1] CodeSet 445
Or}       Proprietary <Prtry> [1..1] ± 446
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 446
17.1.16.24.3  Cancelled <Canc>
Presence: [1..1]
Definition: Instruction has been cancelled. The status on the processing of a cancellation request must
be provided using a cancellation request report message.
Cancelled <Canc> contains one of the following elements (see "CancellationStatus14Choice" on
page 430 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 430
Or}   Reason <Rsn> [1..*] ± 430
17.1.16.24.4  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus21Choice" on page 472 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 472
Or}   Reason <Rsn> [1..*] ± 472
17.1.16.24.5  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies a choice of status for the processing of an intra-balance movement.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
457 March 2024
```

