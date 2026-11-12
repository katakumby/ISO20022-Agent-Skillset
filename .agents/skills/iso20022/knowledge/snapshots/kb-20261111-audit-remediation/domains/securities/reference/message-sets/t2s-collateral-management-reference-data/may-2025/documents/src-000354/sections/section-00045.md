---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["7 reda.044.001.01 EligibleCounterpartCSDStatusAdviceV01", "7.4 Message Building Blocks", "7.4.2 StatusReason <StsRsn>", "7.4.2.1 Status <Sts>"]
file_pages: [49]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.044.001.01"]
---

# 7.4.2.1 Status <Sts>

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 49 to 49.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 49

```text
StatusReason <StsRsn> contains the following CollateralStatusReason1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] CodeSet 49
   Reason <Rsn> [0..*]  49
     Reason <Rsn> [1..1]  49
{Or       Code <Cd> [1..1] CodeSet 50
Or}       Proprietary <Prtry> [1..1] Text 50
     AdditionalInformation <AddtlInf> [0..1] Text 50
Constraints
• StatusReasonRule
If Status equals 'Rejected' then Reason must be present.
7.4.2.1  Status <Sts>
Presence: [1..1]
Definition: Status of the collateral data maintenance instruction.
Datatype: "Status6Code" on page 80
CodeName Name Definition
REJT Rejected Instruction has been rejected.
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
7.4.2.2  Reason <Rsn>
Presence: [0..*]
Definition: Reason for the status of a collateral data maintenance instruction.
Reason <Rsn> contains the following StatusReasonInformation10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  49
{Or     Code <Cd> [1..1] CodeSet 50
Or}     Proprietary <Prtry> [1..1] Text 50
   AdditionalInformation <AddtlInf> [0..1] Text 50
7.4.2.2.1  Reason <Rsn>
Presence: [1..1]
Definition: Specifies the reason for the status report.
Approved by the Securities SEG on 17 April 2025. reda.044.001.01
EligibleCounterpartCSDStatusAdviceV01
Target2-Securities - Collateral Management Reference Data 49 May 2025
```

