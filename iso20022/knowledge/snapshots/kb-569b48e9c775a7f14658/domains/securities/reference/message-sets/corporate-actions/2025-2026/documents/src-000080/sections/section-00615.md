---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.12 OptionInstructionDetails <OptnInstrDtls>", "14.4.3.5.3.3.7.12.12 InstructionStatus <InstrSts>", "14.4.3.5.3.3.7.12.12.7 Covered <Cvrd>"]
file_pages: [804]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.12.12.7 Covered <Cvrd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 804 to 804.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 804

```text
PendingCancellation <PdgCxl> contains one of the following elements (see
"PendingCancellationStatus21Choice" on page 1148 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1149
Or}   Reason <Rsn> [1..*]  C5 1149
     ReasonCode <RsnCd> [1..1]  1149
{Or       Code <Cd> [1..1] CodeSet 1150
Or}       Proprietary <Prtry> [1..1] ± 1150
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1150
14.4.3.5.3.3.7.12.12.7  Covered <Cvrd>
Presence: [1..1]
Definition: Protect Instruction has been full covered.
Covered <Cvrd> contains the following elements (see "NoSpecifiedReason1" on page 1144 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1144
14.4.3.5.3.3.7.12.12.8  Uncovered <Ucvrd>
Presence: [1..1]
Definition: Cover protect instruction accepted but it has not fully covered the protect instruction.
Uncovered <Ucvrd> contains the following elements (see "NoSpecifiedReason1" on page 1144 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1144
14.4.3.5.3.3.7.12.12.9  Returned <Rtrd>
Presence: [1..1]
Definition: Instructed units are returned or partially returned to the instructing party.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 804 February 2026
```

