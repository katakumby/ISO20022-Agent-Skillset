---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.29 ProcessingStatus69Choice", "9.1.21.29.2 Rejected <Rjctd>"]
file_pages: [299]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.29.2 Rejected <Rjctd>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 299 to 299.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 299

```text
9.1.21.29.2  Rejected <Rjctd>
Presence: [1..1]
Definition: Instruction or request has been rejected for further processing.
Rejected <Rjctd> contains one of the following elements (see "RejectionOrRepairStatus39Choice" on
page 283 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 284
Or}   Reason <Rsn> [1..*]  284
     Code <Cd> [1..1]  284
{Or       Code <Cd> [1..1] CodeSet 284
Or}       Proprietary <Prtry> [1..1] ± 285
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 285
9.1.21.29.3  Repair <Rpr>
Presence: [1..1]
Definition: Instruction or request is accepted but in repair.
Repair <Rpr> contains one of the following elements (see "RejectionOrRepairStatus39Choice" on
page 283 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 284
Or}   Reason <Rsn> [1..*]  284
     Code <Cd> [1..1]  284
{Or       Code <Cd> [1..1] CodeSet 284
Or}       Proprietary <Prtry> [1..1] ± 285
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 285
9.1.21.29.4  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 299 September 2025
```

