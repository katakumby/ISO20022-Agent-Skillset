---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["48 reda.028.001.01 CollateralDataStatusAdviceV01", "48.4 Message Building Blocks", "48.4.3 StatusReasonAndFinancialInstrument <StsRsnAndFinInstrm>", "48.4.3.1 Status <Sts>"]
file_pages: [2199]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.028.001.01"]
---

# 48.4.3.1 Status <Sts>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2199 to 2199.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2199

```text
StatusReasonAndFinancialInstrument <StsRsnAndFinInstrm> contains the following
CollateralStatusReason2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] CodeSet 2199
   Reason <Rsn> [0..*]  2199
     Reason <Rsn> [1..1]  2200
{Or       Code <Cd> [1..1] CodeSet 2200
Or}       Proprietary <Prtry> [1..1] ± 2200
     FinancialInstrument <FinInstrm> [0..1] ± C1, C2,
C3, C4,
C5
2200
     AdditionalInformation <AddtlInf> [0..1] Text 2201
   EligibilitySetProfile <ElgbltySetPrfl> [0..1] ± 2202
Constraints
• StatusReasonRule
If Status equals 'Rejected' then Reason must be present.
48.4.3.1  Status <Sts>
Presence: [1..1]
Definition: Status of the collateral data maintenance instruction.
Datatype: "Status10Code" on page 3305
CodeName Name Definition
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
REJT Rejected Instruction has been rejected.
PART PartiallyCompleted Processing has been partially
completed.
48.4.3.2  Reason <Rsn>
Presence: [0..*]
Definition: Reason for the status of a collateral data maintenance instruction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.028.001.01 CollateralDataStatusAdviceV01
Target2-Securities 2199 August 2026
```

