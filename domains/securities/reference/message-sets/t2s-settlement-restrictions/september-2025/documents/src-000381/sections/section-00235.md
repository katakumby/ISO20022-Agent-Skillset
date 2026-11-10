---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.12 ProcessingStatus71Choice", "9.1.21.12.4 Repair <Rpr>"]
file_pages: [281]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.12.4 Repair <Rpr>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 281 to 281.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 281

```text
Rejected <Rjctd> contains one of the following elements (see "RejectionOrRepairStatus40Choice" on
page 296 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 296
Or}   Reason <Rsn> [1..*]  297
     Code <Cd> [1..1]  297
{Or       Code <Cd> [1..1] CodeSet 297
Or}       Proprietary <Prtry> [1..1] ± 297
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 298
9.1.21.12.4  Repair <Rpr>
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
9.1.21.12.5  Denied <Dnd>
Presence: [1..1]
Definition: Modification request will not be executed.
Denied <Dnd> contains one of the following elements (see "DeniedStatus16Choice" on page 287 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 288
Or}   Reason <Rsn> [1..*]  288
     Code <Cd> [1..1] ± 288
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 288
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 281 September 2025
```

