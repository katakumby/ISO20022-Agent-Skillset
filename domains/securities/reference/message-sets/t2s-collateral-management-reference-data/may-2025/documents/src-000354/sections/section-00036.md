---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["6 reda.028.001.01 CollateralDataStatusAdviceV01", "6.4 Message Building Blocks", "6.4.2 StatusReason <StsRsn>", "6.4.2.1 Status <Sts>"]
file_pages: [40]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.028.001.01"]
---

# 6.4.2.1 Status <Sts>

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 40 to 40.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 40

```text
StatusReason <StsRsn> contains the following CollateralStatusReason1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] CodeSet 40
   Reason <Rsn> [0..*]  40
     Reason <Rsn> [1..1]  40
{Or       Code <Cd> [1..1] CodeSet 41
Or}       Proprietary <Prtry> [1..1] Text 41
     AdditionalInformation <AddtlInf> [0..1] Text 41
Constraints
• StatusReasonRule
If Status equals 'Rejected' then Reason must be present.
6.4.2.1  Status <Sts>
Presence: [1..1]
Definition: Status of the collateral data maintenance instruction.
Datatype: "Status6Code" on page 80
CodeName Name Definition
REJT Rejected Instruction has been rejected.
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
6.4.2.2  Reason <Rsn>
Presence: [0..*]
Definition: Reason for the status of a collateral data maintenance instruction.
Reason <Rsn> contains the following StatusReasonInformation10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  40
{Or     Code <Cd> [1..1] CodeSet 41
Or}     Proprietary <Prtry> [1..1] Text 41
   AdditionalInformation <AddtlInf> [0..1] Text 41
6.4.2.2.1  Reason <Rsn>
Presence: [1..1]
Definition: Specifies the reason for the status report.
Approved by the Securities SEG on 17 April 2025. reda.028.001.01 CollateralDataStatusAdviceV01
Target2-Securities - Collateral Management Reference Data 40 May 2025
```

