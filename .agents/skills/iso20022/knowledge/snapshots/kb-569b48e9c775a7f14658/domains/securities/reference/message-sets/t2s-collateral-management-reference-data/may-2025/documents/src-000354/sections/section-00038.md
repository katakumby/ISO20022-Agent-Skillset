---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["6 reda.028.001.01 CollateralDataStatusAdviceV01", "6.4 Message Building Blocks", "6.4.3 StatusReasonAndFinancialInstrument <StsRsnAndFinInstrm>", "6.4.3.1 Status <Sts>"]
file_pages: [42]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.028.001.01"]
---

# 6.4.3.1 Status <Sts>

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 42 to 42.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 42

```text
StatusReasonAndFinancialInstrument <StsRsnAndFinInstrm> contains the following
CollateralStatusReason2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] CodeSet 42
   Reason <Rsn> [0..*]  42
     Reason <Rsn> [1..1]  43
{Or       Code <Cd> [1..1] CodeSet 43
Or}       Proprietary <Prtry> [1..1] ± 43
     FinancialInstrument <FinInstrm> [0..1] ± C1, C2,
C3, C4,
C5
43
     AdditionalInformation <AddtlInf> [0..1] Text 44
   EligibilitySetProfile <ElgbltySetPrfl> [0..1] ± 45
Constraints
• StatusReasonRule
If Status equals 'Rejected' then Reason must be present.
6.4.3.1  Status <Sts>
Presence: [1..1]
Definition: Status of the collateral data maintenance instruction.
Datatype: "Status10Code" on page 80
CodeName Name Definition
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
REJT Rejected Instruction has been rejected.
PART PartiallyCompleted Processing has been partially
completed.
6.4.3.2  Reason <Rsn>
Presence: [0..*]
Definition: Reason for the status of a collateral data maintenance instruction.
Approved by the Securities SEG on 17 April 2025. reda.028.001.01 CollateralDataStatusAdviceV01
Target2-Securities - Collateral Management Reference Data 42 May 2025
```

