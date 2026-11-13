---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.30 ProcessingStatus99Choice", "9.1.21.30.3 Repair <Rpr>"]
file_pages: [302]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.30.3 Repair <Rpr>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 302 to 302.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 302

```text
Rejected <Rjctd> contains one of the following elements (see "RejectionOrRepairStatus38Choice" on
page 277 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 277
Or}   Reason <Rsn> [1..*]  277
     Code <Cd> [0..*]  278
{Or       Code <Cd> [1..1] CodeSet 278
Or}       Proprietary <Prtry> [1..1] ± 279
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 279
9.1.21.30.3  Repair <Rpr>
Presence: [1..1]
Definition: Instruction or request is accepted but in repair.
Repair <Rpr> contains one of the following elements (see "RejectionOrRepairStatus38Choice" on
page 277 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 277
Or}   Reason <Rsn> [1..*]  277
     Code <Cd> [0..*]  278
{Or       Code <Cd> [1..1] CodeSet 278
Or}       Proprietary <Prtry> [1..1] ± 279
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 279
9.1.21.30.4  Cancelled <Canc>
Presence: [1..1]
Definition: Instruction has been cancelled. The status on the processing of a cancellation request must
be provided using a cancellation request report message.
Cancelled <Canc> contains one of the following elements (see "CancellationStatus14Choice" on
page 290 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 290
Or}   Reason <Rsn> [1..*] ± 290
9.1.21.30.5  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies a choice of status for the processing of an intra-balance movement.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 302 September 2025
```

