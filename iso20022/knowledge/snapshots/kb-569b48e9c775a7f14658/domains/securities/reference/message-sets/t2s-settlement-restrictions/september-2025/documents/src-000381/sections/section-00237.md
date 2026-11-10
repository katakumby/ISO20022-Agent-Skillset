---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.13 PendingStatus38Choice", "9.1.21.13.2 Reason <Rsn>"]
file_pages: [283]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.13.2 Reason <Rsn>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 283 to 283.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 283

```text
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
9.1.21.13.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending status.
Reason <Rsn> contains the following PendingReason16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 283
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 283
9.1.21.13.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why a cancellation request sent for the related instruction is pending.
Code <Cd> contains one of the following elements (see "PendingReason28Choice" on page 273 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 273
Or}   Proprietary <Prtry> [1..1] ± 274
9.1.21.13.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 344
9.1.21.14  RejectionOrRepairStatus39Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 284
Or}   Reason <Rsn> [1..*]  284
     Code <Cd> [1..1]  284
{Or       Code <Cd> [1..1] CodeSet 284
Or}       Proprietary <Prtry> [1..1] ± 285
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 285
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 283 September 2025
```

