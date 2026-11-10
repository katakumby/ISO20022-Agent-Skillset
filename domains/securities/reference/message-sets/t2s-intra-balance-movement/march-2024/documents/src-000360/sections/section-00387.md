---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.22 ProcessingStatus69Choice", "17.1.16.22.1 PendingCancellation <PdgCxl>"]
file_pages: [453]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.22.1 PendingCancellation <PdgCxl>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 453 to 453.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 453

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingCancellation <PdgCxl> [1..1] ± 453
Or   Rejected <Rjctd> [1..1] ± 453
Or   Repair <Rpr> [1..1] ± 453
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 454
Or   Proprietary <Prtry> [1..1] ± 454
Or   Denied <Dnd> [1..1] ± 454
Or}   Cancelled <Canc> [1..1] ± 455
17.1.16.22.1  PendingCancellation <PdgCxl>
Presence: [1..1]
Definition: Cancellation is pending processing.
PendingCancellation <PdgCxl> contains one of the following elements (see
"PendingStatus39Choice" on page 438 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 438
Or}   Reason <Rsn> [1..*]  438
     Code <Cd> [1..1] ± 439
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 439
17.1.16.22.2  Rejected <Rjctd>
Presence: [1..1]
Definition: Instruction or request has been rejected for further processing.
Rejected <Rjctd> contains one of the following elements (see "RejectionOrRepairStatus39Choice" on
page 442 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 442
Or}   Reason <Rsn> [1..*]  443
     Code <Cd> [1..1]  443
{Or       Code <Cd> [1..1] CodeSet 443
Or}       Proprietary <Prtry> [1..1] ± 443
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 444
17.1.16.22.3  Repair <Rpr>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
453 March 2024
```

