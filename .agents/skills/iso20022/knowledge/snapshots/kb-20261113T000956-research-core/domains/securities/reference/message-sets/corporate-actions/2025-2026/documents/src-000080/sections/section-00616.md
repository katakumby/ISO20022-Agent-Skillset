---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.12 OptionInstructionDetails <OptnInstrDtls>", "14.4.3.5.3.3.7.12.12 InstructionStatus <InstrSts>", "14.4.3.5.3.3.7.12.12.9 Returned <Rtrd>", "14.4.3.5.3.3.7.12.12.9.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [805]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.12.12.9.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 805 to 805.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 805

```text
Returned <Rtrd> contains one of the following ReturnedStatus2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 805
Or}   Reason <Rsn> [1..*]  C6 805
     ReasonCode <RsnCd> [1..1]  805
{Or       Code <Cd> [1..1] CodeSet 806
Or}       Proprietary <Prtry> [1..1] ± 806
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 806
14.4.3.5.3.3.7.12.12.9.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Reason not specified.
Datatype: "NoReasonCode" on page 1223
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
14.4.3.5.3.3.7.12.12.9.2  Reason <Rsn>
Presence: [1..*]
Definition: Reason why the meeting instruction message or the individual meeting instruction is
returned.
Impacted by: C6 "AdditionalReasonInforrmationRule"
Reason <Rsn> contains the following ReturnedStatusReason2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReasonCode <RsnCd> [1..1]  805
{Or     Code <Cd> [1..1] CodeSet 806
Or}     Proprietary <Prtry> [1..1] ± 806
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 806
Constraints
• AdditionalReasonInforrmationRule
AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
14.4.3.5.3.3.7.12.12.9.2.1  ReasonCode <RsnCd>
Presence: [1..1]
Definition: Reason for the returned status.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 805 February 2026
```

