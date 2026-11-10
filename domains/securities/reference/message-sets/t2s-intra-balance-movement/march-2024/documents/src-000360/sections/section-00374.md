---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.13 PendingStatus38Choice", "17.1.16.13.2 Reason <Rsn>", "17.1.16.13.2.1 Code <Cd>"]
file_pages: [440]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.13.2.1 Code <Cd>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 440 to 440.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 440

```text
Definition: Specifies the reason of the pending status.
Reason <Rsn> contains the following PendingReason16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 440
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 440
17.1.16.13.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why a cancellation request sent for the related instruction is pending.
Code <Cd> contains one of the following elements (see "PendingReason28Choice" on page 430 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 430
Or}   Proprietary <Prtry> [1..1] ± 431
17.1.16.13.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 497
17.1.16.14  RejectionOrRepairStatus40Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 440
Or}   Reason <Rsn> [1..*]  441
     Code <Cd> [1..1]  441
{Or       Code <Cd> [1..1] CodeSet 441
Or}       Proprietary <Prtry> [1..1] ± 442
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 442
17.1.16.14.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 485
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
440 March 2024
```

