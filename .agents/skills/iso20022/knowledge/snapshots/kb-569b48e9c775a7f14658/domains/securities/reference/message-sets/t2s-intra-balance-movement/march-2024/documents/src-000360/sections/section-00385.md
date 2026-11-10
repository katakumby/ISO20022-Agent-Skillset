---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.21 ProcessingStatus71Choice", "17.1.16.21.3 Rejected <Rjctd>"]
file_pages: [451]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.21.3 Rejected <Rjctd>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 451 to 451.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 451

```text
Pending <Pdg> contains one of the following elements (see "PendingStatus38Choice" on page 439 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 439
Or}   Reason <Rsn> [1..*]  439
     Code <Cd> [1..1] ± 440
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 440
17.1.16.21.3  Rejected <Rjctd>
Presence: [1..1]
Definition: Modification request has been rejected for further processing.
Rejected <Rjctd> contains one of the following elements (see "RejectionOrRepairStatus40Choice" on
page 440 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 440
Or}   Reason <Rsn> [1..*]  441
     Code <Cd> [1..1]  441
{Or       Code <Cd> [1..1] CodeSet 441
Or}       Proprietary <Prtry> [1..1] ± 442
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 442
17.1.16.21.4  Repair <Rpr>
Presence: [1..1]
Definition: Instruction or request is accepted but in repair.
Repair <Rpr> contains one of the following elements (see "RejectionOrRepairStatus39Choice" on
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
451 March 2024
```

