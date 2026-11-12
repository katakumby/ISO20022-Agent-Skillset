---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.8 DeniedStatus16Choice", "17.1.16.8.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [435]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.8.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 435 to 435.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 435

```text
17.1.16.8.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 485
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
17.1.16.8.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the denied status.
Reason <Rsn> contains the following DeniedReason11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 435
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 435
17.1.16.8.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the request has a denied status.
Code <Cd> contains one of the following elements (see "DeniedReason16Choice" on page 433 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 433
Or}   Proprietary <Prtry> [1..1] ± 434
17.1.16.8.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 497
17.1.16.9  AcknowledgementReason15Choice
Definition: Choice of format for the acknowledgement reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 436
Or}   Proprietary <Prtry> [1..1] ± 436
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
435 March 2024
```

